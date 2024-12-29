# Wargamesmy CTF 2024

I participated as Revvv with HCS in this CTF Event and Achieved Rank 4

|      Name       | Category | Solved? |
|:---------------:|:--------:|:-------:|
| Christmast GIFt |   Misc   |   ✅    |
|  Invisible Ink  |   Misc   |   ✅    |

# Misc

## Christmast GIFt [94 Pts]

> Here is your christmas GIFt from santa! Just open and wait for it..
> 
> Author: SKR

### Solution:

Simply we can just open the `gif` file using GIMP and find the frame where the gift is opened and shows the flag

![image](https://hackmd.io/_uploads/rkwxRfRSyx.png)

### Flag

`wgmy{1eaa6da7b7f5df6f7c0381c8f23af4d3}`

## Invisible Ink [388 Pts]

> The flag is hidden somewhere in this GIF. You can't see it? Must be written in transparent ink.
> 
> Author: Yes

### Solution

Same as the previous challenge, we open the `gif` file using GIMP and analyze it.

Noticed that there are two frames that are appeared transparent and both of them are not on the (0, 0) X and Y

Let's change it and to (0, 0) and make the only visible frame is only that two frames

![image](https://hackmd.io/_uploads/B1RgxX0r1x.png)

Now we have a some sort of noise like in a Television, let's try to make the color equal.

![image](https://hackmd.io/_uploads/Hky_gmAB1g.png)

Now it's only showing white but noticed when you equalized one frame at first, it shows some kind of text. let's try to make it transparent.

![image](https://hackmd.io/_uploads/HkEWW7CByx.png)

And we got the flag

### Flag
`wgmy{d41d8cd98f00b204e9800998ecf8427e}`