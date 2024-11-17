# T.E.G. 1: Hide and Seek [100 Pts]

**Category:** Beginner, stego

**Solves:** -

## Description
> T.E.G. level 1
> 
> Everything is right in front of you, but you need the right words to see it. Will you be able to decipher the message?

## Solution

---
![chall](lipgloss.jpg)

Use Stegseek: 
`stegseek lipgloss.jpg`

Output:
```
┌──(rev㉿Prm)-[/mnt/c/Users/Indop/OneDrive/Documents/CTF/ctf-writeup/2024/Metared-Argentina/Beginner/TEG1]
└─$ stegseek lipgloss.jpg 
StegSeek 0.6 - https://github.com/RickdeJager/StegSeek

[i] Found passphrase: "lipgloss"
[i] Original filename: "flagTeg.txt".
[i] Extracting to "lipgloss.jpg.out".
```
### Flag

`flag{5t3g0_1s_fun_wh3n_y0u_f1nd_1t}`