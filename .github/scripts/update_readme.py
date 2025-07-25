#!/usr/bin/env python3
"""
Script to automatically update README.md with new CTF writeups
"""

import os
import re
from pathlib import Path
from typing import Dict, List, Tuple

def get_year_directories() -> List[str]:
    """Get all year directories (e.g., 2024, 2025)"""
    years = []
    for item in os.listdir('.'):
        if os.path.isdir(item) and item.isdigit() and len(item) == 4:
            years.append(item)
    return sorted(years)

def get_ctf_events(year: str) -> List[str]:
    """Get all CTF event directories for a given year"""
    year_path = Path(year)
    if not year_path.exists():
        return []
    
    events = []
    for item in year_path.iterdir():
        if item.is_dir():
            events.append(item.name)
    return sorted(events)

def parse_existing_readme() -> Dict[str, List[Dict[str, str]]]:
    """Parse existing README to extract current entries"""
    readme_path = Path('README.md')
    if not readme_path.exists():
        return {}
    
    content = readme_path.read_text()
    
    # Parse existing entries by year
    year_sections = {}
    current_year = None
    current_entries = []
    
    lines = content.split('\n')
    in_table = False
    
    for line in lines:
        # Check for year headers
        year_match = re.match(r'^## (\d{4})$', line)
        if year_match:
            if current_year:
                year_sections[current_year] = current_entries
            current_year = year_match.group(1)
            current_entries = []
            in_table = False
            continue
        
        # Check for table headers (skip them)
        if line.startswith('| Event') or line.startswith('|---'):
            in_table = True
            continue
        
        # Parse table rows
        if in_table and line.startswith('|') and current_year:
            parts = [part.strip() for part in line.split('|')[1:-1]]  # Remove empty first/last
            if len(parts) >= 4:
                entry = {
                    'event': parts[0],
                    'team': parts[1],
                    'rank': parts[2],
                    'link': parts[3]
                }
                current_entries.append(entry)
        
        # End of table
        if in_table and not line.startswith('|') and line.strip():
            in_table = False
    
    # Don't forget the last year
    if current_year:
        year_sections[current_year] = current_entries
    
    return year_sections

def extract_link_from_markdown(link_text: str) -> str:
    """Extract the actual link from markdown format [Text](link)"""
    match = re.search(r'\[.*?\]\((.*?)\)', link_text)
    if match:
        return match.group(1)
    return link_text

def get_existing_events_by_year(existing_data: Dict[str, List[Dict[str, str]]]) -> Dict[str, set]:
    """Get set of existing event names by year"""
    events_by_year = {}
    for year, entries in existing_data.items():
        events_by_year[year] = set()
        for entry in entries:
            # Extract event name and normalize it
            event_name = entry['event'].strip()
            events_by_year[year].add(event_name)
    return events_by_year

def generate_readme_content(existing_data: Dict[str, List[Dict[str, str]]]) -> str:
    """Generate the complete README content"""
    content = []
    content.append("# ctf-writeup")
    content.append("Repository for all of my CTF Writeups. Playing as Rev or Revvv")
    content.append("")
    
    # Get all years (both existing and new)
    all_years = set(get_year_directories())
    all_years.update(existing_data.keys())
    
    # Get existing events to avoid duplicates
    existing_events_by_year = get_existing_events_by_year(existing_data)
    
    for year in sorted(all_years):
        content.append(f"## {year}")
        
        # Start table
        content.append("| Event              | Team     | Rank | Link                                                |")
        content.append("|--------------------|----------|------|-----------------------------------------------------|")
        
        # Add existing entries
        if year in existing_data:
            for entry in existing_data[year]:
                content.append(f"| {entry['event']:<18} |{entry['team']:<10}|{entry['rank']:<6}|{entry['link']:<53}|")
        
        # Add new entries (directories that don't have existing entries)
        year_events = get_ctf_events(year)
        existing_events = existing_events_by_year.get(year, set())
        
        for event in year_events:
            # Try to match existing event (case-insensitive, flexible matching)
            event_exists = False
            for existing_event in existing_events:
                if (event.lower().replace('-', '').replace('_', '') == 
                    existing_event.lower().replace('-', '').replace('_', '').replace(' ', '')):
                    event_exists = True
                    break
            
            if not event_exists:
                # Add new event with placeholder values
                event_name = event.replace('-', ' ').replace('_', ' ')
                link = f"[Link]({year}/{event})"
                content.append(f"| {event_name:<18} |{'TBD':<10}|{'-':<6}|{link:<53}|")
        
        content.append("")
    
    return '\n'.join(content)

def main():
    """Main function to update README"""
    print("🔍 Scanning for CTF writeups...")
    
    # Parse existing README
    existing_data = parse_existing_readme()
    print(f"📖 Found existing data for years: {list(existing_data.keys())}")
    
    # Get current directory structure
    years = get_year_directories()
    print(f"📁 Found year directories: {years}")
    
    total_events = 0
    for year in years:
        events = get_ctf_events(year)
        total_events += len(events)
        print(f"  {year}: {len(events)} events - {events}")
    
    # Generate new README content
    new_content = generate_readme_content(existing_data)
    
    # Write updated README
    readme_path = Path('README.md')
    if readme_path.exists():
        old_content = readme_path.read_text()
        if old_content != new_content:
            readme_path.write_text(new_content)
            print("✅ README.md updated successfully!")
        else:
            print("ℹ️  README.md is already up to date.")
    else:
        readme_path.write_text(new_content)
        print("✅ README.md created successfully!")

if __name__ == "__main__":
    main()
