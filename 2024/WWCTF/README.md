# World Wide CTF 2024

I participated as Revvv with HCS in this CTF Event and Achieved Rank 8

|       Name       |   Category    | Solved? |
|:----------------:|:-------------:|:-------:|
|   Simpler RSA    |   Beginners   |   ✅    |
|    Bongcloud     | Miscellaneous |   ✅    |
| World Wide Flags | Miscellaneous |   ✅    |

# Beginners

## Simpler RSA [50 Pts]

### Description
> Author: yun
>
> RSA is so complicated! I made it simpler.

### Solution

We are given a python file

```python
from secret import flag
from Crypto.Util.number import bytes_to_long, getPrime

flag = bytes_to_long(flag)
p = getPrime(2048)
q = getPrime(2048)
c = pow(flag, p, q)  # i believe this is the fancy rsa encryption?
print(f'{p=}')
print(f'{q=}')
print(f'{c=}')
```

This code calculates using $c$ $=$ $flag^p$ $mod$ $q$. We can retrieve the flag by inversing it to $flag$ = $𝑐^{inverse_p}$ $mod$ $𝑞$

Solver:
```python
from Crypto.Util.number import inverse, long_to_bytes

p = 20322136122026329892580404875086132520732558134579258531781672192065024437324055172065343417524169304918928056147680414370351055409439818026607876517460045945556933456319117456860928521423787112252544266864178773974904640732880445449138842965327995838722222110164109025916914430044528254715080648900354468118393295346137198518513075775514617222780524163798065365970392865107270392212968677531885628998155305428785133820145555740608026626724539584106018453003156159305252013173659975815845286802275956807162426425721298560633326719023970391963404981189820163950120529861779878077006530640930032570206978446007206971761
q = 19097560527100693557502945814016176943507375936656621847599300620729196257594977906326233653252987169303598004653720974045696589437233399711658994040877123702369987961301047714594623670674571987772814959679153558360152976652255742578324469478560556855210734037861198243000935281050776548747455717266013266531885744852759548255091579407464355390341944708706006878618904548103612995804547530724085856234186750409404880456083750984829553552127853848824218180459231650990529456828407224866655873224370892839628814748212142246752082561042142636866939231370987974125358875253454199574864895153300338298982667319003886687691
c = 4281681357519343869235268029657832985104802601857889851833662824770073601279722389949102805423012693423900316266993146428480448851806951090530135683459342224839031144425810971344588481297094697047852347659595441639804230546879345999083627138617034295731725402645279785129174304818023129638779656619113578465655082808462489379872294929944719545647280271454196700396004152529288987570497804498041888697213294509916951489315431831556860863264254674452235360890586742441263188663158067860877772336480637257856658858967478284817730555629113613134338975168062044831796369552664256963808360408525644200922627703094455580032

p_inv = inverse(p, q - 1)

flag = pow(c, p_inv, q)

decoded_flag = long_to_bytes(flag)
print(decoded_flag)
```

#### Flag

`wwf{ju57_u53_l1br4r135}`

# Miscellaneous

## Bongcloud [153 Pts]

### Description
> Author: yun
> 
> Are you a true chess master?
> 
> nc chess.chal.wwctf.com 1337

### Solution

When I connect to the netcat connection, it says that we need to win 3 games of chess to get the flag. Since it has no timelimit to the connection, let's just spam the best move for each condition of the board with the help of [Chess Bot](https://chess-bot.com/online_calculator/next_best_move.html)

![image](https://hackmd.io/_uploads/BkqubK5QJl.png)

#### Flag

`wwf{y0u_4r3_4_7ru3_ch355_m4573r}`

## World Wide Flags [150 Pts]

### Description
> "Oh, you are a WWCTF player? Name every flag."
> Identify flags with increasing difficulty!
> 
> http://flags.chal.wwctf.com:1337/

### Solution

From the Website, we need to guess 100 flags that appeared. But somethig interesting when I solve a couple of them, the answer is not entirely correct, for example the flag France will be incorrect if we submit France as the answer.

> Note: We can refresh the page and our progress will still be there but the flag changes

From this understanding, I don't want to think too much for the automation so I decided to manually answer all 100 flags.

![image](https://hackmd.io/_uploads/SJpAGt9mJe.png)

#### Flag
`wwf{d1d_y0u_u53_41_70_r34d_f1465}`
