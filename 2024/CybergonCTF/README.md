# Cybergon CTF 2024

I participated as Revvv with HCS in this CTF Event and Achieved Rank 3

|           Name           | Category | Solved? |
|:------------------------:|:--------:|:-------:|
|        Invisible         | Stegano  |   ✅    |
|        Truesight         | Stegano  |   ✅    |
| What's behind the wall ? | Stegano  |   ✅    |
|       Triple Quiz        |   Misc   |   ✅    |

# Stegano

## Invisible [50 Pts]

### Description
> Sometimes it's a relief to be invisible. 
> CYBERGON_CTF2024{xxxx_xxxx_xxxxx}
>
> Author - iamkfromburma

### Solution

Given an image file `challenge1.jpg`, let's try find something using [Aperisolve](https://www.aperisolve.com).

There's something interesting in the `Red` section.

![image](https://hackmd.io/_uploads/HkrJTaYmke.png)

We can see that there's `getyourflag` on the bottom left of the picture.

let's try using `steghide extract -sf challenge1.jpg` and `getyourflag` as the passphrase

and we got a `flag.txt` file

#### Flag

`CYBERGON_CTF2024{n07h1ng_5t4ys_h1dd3n}`


## Truesight [50 Pts]

### Description
> If you are waiting for a sign, this is it. 
> CYBERGON_CTF2024{xxx_xxxx_xxxxx}
>
> Author - iamkfromburma

### Solution

We are given a png file but is corrupted.

let's try checking it using a hexeditor

![image](https://hackmd.io/_uploads/r1YmCatmye.png)

As expected, we're missing the first 8 bytes of the png header. let's try adding it

![image](https://hackmd.io/_uploads/r1Z_CpFQJx.png)

Save it and we can now view the png file

![image](https://hackmd.io/_uploads/SyZ5ATFmkl.png)

#### Flag

`CYBERGON_CTF2024{y0u_g07_7h3_r!gh7_s1gn5}`

## What's behind the wall ? [50 Pts]

### Description
> Find the secret behind the wall ? 
> CYBERGON_CTF2024{xxxx_xxxxx_xxxxx}
>
> Author - iamkfromburma

### Solution

We are given an image `challenge4.jpg` and a `JS.txt` file from the challenge.

Let's try check the image metadata first using `exiftool`

```
ExifTool Version Number         : 13.00
File Name                       : challenge4.jpg
Directory                       : .
File Size                       : 180 kB
File Modification Date/Time     : 2024:09:28 01:28:53+07:00
File Access Date/Time           : 2024:11:30 18:33:47+07:00
File Inode Change Date/Time     : 2024:11:30 18:33:49+07:00
File Permissions                : -rwxrwxrwx
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.01
X Resolution                    : 72
Y Resolution                    : 72
Exif Byte Order                 : Big-endian (Motorola, MM)
Resolution Unit                 : inches
Y Cb Cr Positioning             : Centered
Exif Version                    : 0232
Components Configuration        : Y, Cb, Cr, -
User Comment                    : winteriscoming
Flashpix Version                : 0100
Image Width                     : 1920
Image Height                    : 1080
Encoding Process                : Progressive DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 1920x1080
Megapixels                      : 2.1
```

I saw `winteriscoming` on user comment, maybe we can use it for something related to txt files. since there is nothing else we can do by using jpg files. let's try to find some steganography tools related to Text.

After some research, I found a tool called `Snow` and it's for a text-based steganography. let's try using it

Command:
`./SNOW.EXE -C -p "winteriscoming" JS.txt`

Output:
`3X1f_w1th_5n0w5`

#### Flag

`CYBERGON_CTF2024{3X1f_w1th_5n0w5}`

# Misc

## Triple Quiz [50 Pts]

### Description
> You’ll recognize it when you see it, it’s something you’ve already done before.
> 
> CYBERGON_CTF2024{XXXXXXXXXXXXXXXXXXXXX}
> Author - iamkfromburma

### Solution

We are given a password protected rar file. we can try to crack it using john the ripper.

```
rar2john Triple_Quiz.rar > cek.hash -> Extracting the hash of the rar file

john --wordlist=/usr/share/wordlists/rockyou.txt cek.hash -> cracking using rockyou
```

and we get the password `ICEMAN`

After extracting the `rar` file, we got a `.wav` file. By hearing it, I suspect that this audio is a morse code.

Let's try decode it using [Morse Code Decoder](https://morsecode.world/international/decoder/audio-decoder-adaptive.html) and we got this
`6 666 777 7777 33 9 444 8 44 8 66 444 66 33`

let's try using cipher identifier in dcode

![image](https://hackmd.io/_uploads/S1UISAF7Jx.png)

#### Flag

`CYBERGON_CTF2024{MORSEWITHTNINE}`
