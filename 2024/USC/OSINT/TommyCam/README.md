# TommyCam [300 Pts]

**Category:** OSINT

**Solves:** -

## Description
> In May of 1995, university staff members completed what would become a quirky, well-enjoyed campus feature - TommyCam! The 24/7 live video feed of our unofficial mascot's statue, Tommy Trojan, is still going strong almost 30 years later.
>
> The site usc.edu was first archived by the Internet Archive in December 1996. At that time, the site included the technical specs for TommyCam. What PC was initially used to run TommyCam?
>
> Answers should be formatted like this, for example: CYBORG{ThinkPad T480}
>
> Note: this challenge is limited to 10 attempts to prevent brute-forcing

## Solution

We can use [web.archive.org](https://web.archive.org) to get the webpage in December 1996

![alt text](image.png)

The device PC is `Toshiba 5200 80386`

### Flag

`CYBORG{Toshiba 5200 80386}`
