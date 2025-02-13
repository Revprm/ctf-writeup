# nine solves
Category: Reverse Engineering

Given a Binary file named `nine-solves` let's open it using ida.

```c
int __cdecl main(int argc, const char **argv, const char **envp)
{
  __int64 i; // rsi
  unsigned int v4; // eax
  int v5; // ecx
  int v6; // edx
  char v8[6]; // [rsp+0h] [rbp-18h] BYREF
  char v9; // [rsp+6h] [rbp-12h]

  puts("Welcome to the Tianhuo Research Center.");
  printf("Please enter your access code: ");
  fflush(stdout);
  fgets(v8, 16, stdin);
  for ( i = 0LL; i != 6; ++i )
  {
    v4 = v8[i];
    if ( (unsigned __int8)(v8[i] - 32) > 0x5Eu )
      goto LABEL_14;
    v5 = yi[i];
    if ( !v5 )
      goto LABEL_14;
    v6 = 0;
    while ( (v4 & 1) == 0 )
    {
      ++v6;
      v4 >>= 1;
      if ( v5 == v6 )
        goto LABEL_9;
LABEL_6:
      if ( v4 == 1 )
        goto LABEL_14;
    }
    ++v6;
    v4 = 3 * v4 + 1;
    if ( v5 != v6 )
      goto LABEL_6;
LABEL_9:
    if ( v4 != 1 )
      goto LABEL_14;
  }
  if ( !v9 || v9 == 10 )
  {
    eigong(yi);
    return 0;
  }
LABEL_14:
  puts("ACCESS DENIED");
  return 1;
}
```

Simply this is a [Collatz transformation](https://en.wikipedia.org/wiki/Collatz_conjecture) code just by looking at `v4 = 3 * v4 + 1;`. So the first step is we need to reverse the method and then we need to find out what the `yi` value is.

![image](https://hackmd.io/_uploads/H13kQ-2Yye.png)

From the binary, the yi is an array of value `{0x1B, 0x26, 0x57, 0x5F, 0x76, 0x9}` that can be converted to `{27, 38, 87, 95, 118, 9}`

From that, we can make the script to generate the access code to get the flag

`Solve.py`

```python
yi = [27, 38, 87, 95, 118, 9]

def collatz_steps(n, steps):
    for _ in range(steps):
        if n == 1:
            return False
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    return n == 1

access_code = []
for steps in yi:
    for c in range(32, 127):  
        if collatz_steps(c, steps):
            access_code.append(chr(c))
            break

access_code = ''.join(access_code)
print(f"Access Code: {access_code}")
```
`Output`
`Access Code: AigyaP`

## Flag
`lactf{REDACTED}`