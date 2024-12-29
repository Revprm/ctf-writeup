# Wargamesmy CTF 2024

I participated as **Revvv** with **HCS** in this CTF event and achieved **Rank 4**.

|       Name       | Category | Solved? |
|:----------------:|:--------:|:-------:|
| **Christmast GIFt** |   Misc   |   ✅    |
| **Invisible Ink**  |   Misc   |   ✅    |

## Miscellaneous Challenges

### Christmast GIFt [94 Points]

> "Here is your Christmas GIFt from Santa! Just open and wait for it."
>
> **Author:** SKR

#### Solution

To solve this challenge, simply open the provided GIF file using **GIMP**. Locate the frame where the "gift" opens to reveal the flag.

![image](https://hackmd.io/_uploads/rkwxRfRSyx.png)

#### Flag

`wgmy{1eaa6da7b7f5df6f7c0381c8f23af4d3}`

---

### Invisible Ink [388 Points]

> "The flag is hidden somewhere in this GIF. Can’t see it? It must be written in transparent ink."
>
> **Author:** Yes

#### Solution

Similar to the previous challenge, open the GIF file using **GIMP** and analyze it.

In this case, I noticed two frames appeared transparent, and neither of them was located at the default (0, 0) coordinates for X and Y. To investigate further:

1. Move these transparent frames to the (0, 0) position.
2. Make only these two frames visible.

![image](https://hackmd.io/_uploads/B1RgxX0r1x.png)

After making this adjustment, the frames resembled a static noise pattern, similar to a TV signal. By equalizing the colors, the output revealed a white screen.

![image](https://hackmd.io/_uploads/Hky_gmAB1g.png)

Upon closer inspection, equalizing just one frame initially showed faint text. To make the text more readable, I adjusted the transparency settings.

![image](https://hackmd.io/_uploads/HkEWW7CByx.png)

This revealed the flag hidden within the GIF.

#### Flag

`wgmy{d41d8cd98f00b204e9800998ecf8427e}`

