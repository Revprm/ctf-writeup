# Nowruz 1404

|       Name      |   Category   | Solved? |
| :-------------: | :----------: | :-----: |
|      VLESS      |   Forensics  |    ✅    |
|       KaB       |   Forensics  |    ✅    |
| Robin’s Mystery | Cryptography |    ✅    |

## Forensics

### VLESS

> What do you know about VLESS?
>
> Flag format: `FMCTF{DestinationIP_UUID}`

We're given a couple TCP packets where there's only one stream of TCP packets

```
..Z....C.......%m...k..
%.Hi

..Hello

Please give me flag format

oh ok
this is flag format
FMCTF{DestinationIP_UUID4}
for example: FMCTF{1.1.1.1_34cdbd88-7466-45c2-9287-364a9f02ecd6}

Thanks <3

bye
```

Okay so it's just a flag format that doesn't give us much information.

We can try to find out what VLESS is in this [website](https://xtls.github.io/en/development/protocols/vless.html)

Based on the website, VLESS has the following request and response

<figure><img src="https://260992468-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FeX7f2pvLxkrgE7gSlDCX%2Fuploads%2FumJ84fTHNukDjRR0P2m1%2Fimage.png?alt=media&#x26;token=fad55913-7740-42a0-91d7-67c91e7255fc" alt=""><figcaption></figcaption></figure>

<figure><img src="https://260992468-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FeX7f2pvLxkrgE7gSlDCX%2Fuploads%2FpzqpyjnxGCyi0hqCgiMA%2Fimage.png?alt=media&#x26;token=bb41a06a-a943-47a4-8f5f-cff72cebadba" alt=""></figure>

To extract the data, we'll use the hex stream from the previous TCP stream.&#x20;

```
00875aa716c9aa43eebea09dbcbe87256d0001046b017f0d2501

48690a

000048656c6c6f0a

506c656173652067697665206d6520666c616720666f726d61740a

6f68206f6b0a

7468697320697320666c616720666f726d61740a464d4354467b44657374696e6174696f6e49505f55554944347d0a

666f72206578616d706c653a20464d4354467b312e312e312e315f33346364626438382d373436362d343563322d393238372d3336346139663032656364367d0a

5468616e6b73203c330a

6279650a
```

Based on the VLESS format for requests and responses, we can simply take the first hex stream

```python
import uuid
import socket

hex_payload = "00875aa716c9aa43eebea09dbcbe87256d0001046b017f0d2501"
data = bytes.fromhex(hex_payload)

offset = 0

protocol_version = data[offset]
offset += 1

uuid_bytes = data[offset:offset+16]
equivalent_uuid = str(uuid.UUID(bytes=uuid_bytes))
offset += 16

add_info_length = data[offset]
offset += 1

additional_info = data[offset:offset+add_info_length]
offset += add_info_length

instruction = data[offset]
offset += 1

port = int.from_bytes(data[offset:offset+2], byteorder='big')
offset += 2

address_type = data[offset]
offset += 1

if address_type == 0x01:
    address = socket.inet_ntoa(data[offset:offset+4])
    offset += 4
elif address_type == 0x04:
    address = socket.inet_ntop(socket.AF_INET6, data[offset:offset+16])
    offset += 16
elif address_type == 0x03:
    domain_length = data[offset]
    offset += 1
    address = data[offset:offset+domain_length].decode('utf-8', errors='ignore')
    offset += domain_length
else:
    address = None

request_data = data[offset:]

print("Protocol Version:", protocol_version)
print("Equivalent UUID:", equivalent_uuid)
print("Additional Info Length (M):", add_info_length)
print("Additional Info (ProtoBuf):", additional_info)
print("Instruction:", instruction)
print("Port:", port)
print("Address Type:", address_type)
print("Address:", address)
print("Request Data:", request_data)
```

```
Protocol Version: 0
Equivalent UUID: 875aa716-c9aa-43ee-bea0-9dbcbe87256d
Additional Info Length (M): 0
Additional Info (ProtoBuf): b''
Instruction: 1
Port: 1131
Address Type: 1
Address: 127.13.37.1
Request Data: b''
```

Flag: `FMCTF{127.13.37.1_875aa716-c9aa-43ee-bea0-9dbcbe87256d}`

### KaB

> i would've given you the challenge, but that would've been too easy
>
> Hint: the image is your carrier
>
> Hint2: Pixel order is left to right, Up to down, In red channel

Given a Pcapng file containing a couple HTTP and TCP Requests.

The main highlight of this challenge is that we have a couple interesting endpoints.

The endpoints are:

1. `/key` -> `Im_THE_kyE`&#x20;
2. `/KaB_Doc.pdf` -> PDF File
3. `/steg.png` -> Normal Image

Based on the hint given from the author, we have to make a script to extract the pixels data from the image using the given key and pdf files as a guidance.

```python
from PIL import Image

img = Image.open("download.png")
r, g, b = img.split()
red_channel = list(r.getdata())

key_str = "Im_THE_kyE"
key_bytes = [ord(c) for c in key_str]  
key_bitmaps = [
    f"{byte:08b}" for byte in key_bytes
]

secret_bits = []
key_len = len(key_bitmaps)
for i, carrier_byte in enumerate(red_channel):
    key_bitmap = key_bitmaps[i % key_len]
    
    carrier_bin = f"{carrier_byte:08b}"
    
    for bit_pos, kbit in enumerate(key_bitmap):
        if kbit == "1":
            secret_bits.append(carrier_bin[bit_pos])
            
def bits_to_bytes(bits):
    return [
        int("".join(bits[i : i + 8]), 2) for i in range(0, len(bits) - len(bits) % 8, 8)
    ]
secret_bytes = bits_to_bytes(secret_bits)
try:
    secret_message = bytes(secret_bytes).decode("utf-8", errors="replace")
except Exception as e:
    secret_message = f"Decoding error: {str(e)}"
print(secret_message[:200])
```

Flag: `FMCTF{haha_ypu_unlocked_bitmap}`

## Cryptography

### Robin's Mystery

> Robin’s friend used an unusual RSA setup, and now he can’t decrypt his own message! Can you step in and use a special technique to recover the plaintext?

The challenge is quite straight forward. we can get the n and the e from the public key and solve it using fermat theorem

```python
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from Crypto.Util.number import *

pub_key_pem = b"""
-----BEGIN PUBLIC KEY-----
MIGcMA0GCSqGSIb3DQEBAQUAA4GKADCBhgKBgGjpRi/Hr5oN5NS219dZrq6nW7AC
Y7fUItXAvbgy0TtagVKO2goQiOssL331b7zRjMvdHkEBR4bTd+hHblmynO+2//fz
4DmVgdgMnrP54+2RSzguEGS1ONX4MpJonBsEGGc1IOiKECiwIbl4DkyTxl6AnFsz
ZI2E+lLDZnX5P44FAgEQ
-----END PUBLIC KEY-----
"""

from cryptography.hazmat.primitives.asymmetric import rsa

# Load public key
pub_key = serialization.load_pem_public_key(pub_key_pem, backend=default_backend())

# Extract n and e
n = pub_key.public_numbers().n
e = pub_key.public_numbers().e

print(f"n = {n}\ne = {e}")
```

```
n = 73671169113692412161518091695991074472499960503340036931063401833844789007180020715886458582760614423768286510200921468682879797651585778343666370976746242033960964171883195866661042323420463092656546940842903827382288624493399406855771112920858499309807681038473688274738183488216155275283711673441904987653
e = 16
```

```python
from Crypto.Util.number import *
from math import isqrt

n = 73671169113692412161518091695991074472499960503340036931063401833844789007180020715886458582760614423768286510200921468682879797651585778343666370976746242033960964171883195866661042323420463092656546940842903827382288624493399406855771112920858499309807681038473688274738183488216155275283711673441904987653
e = 16
cipher_bytes = b'\x10\xc4\xbf\xfapg\xee\x00\xe4\xcd\x00\xb4i\xf5\x801\xdd\xafm\xb1\xad\x8dy\x01\xaa\x14\xd1\xa3\x14[\xdf\xc8c\xb1\xf4\xcb\xcf\xf0\xf9\x83\x85%\x19\xd2d>N\x9aR\xa4\xba\xc9\xda\xd8\xe4\xa2\x9cg%.\xac\xd7\xb5\x95\x7f\x87\x04?\xf7\xe4\x06(\xe7l\x1c"c\x95\x90z\xd4\x8b\x9f\x1b\x00\xc67\xe4\x82g\xc4b\x10\x8c\xe7s[\x95-TB+Z;\xe4\x00\x11<\xc51K\xec\x94ZL\xb2\xf9\x7fp<\xe6C\xf8\x7f\x90\x0bG\xcf'
c = bytes_to_long(cipher_bytes)

def isSquare(n):
    return isqrt(n) ** 2 == n

def fermat_factor(n):
    a = isqrt(n)
    if a * a < n:
        a += 1
    b2 = a * a - n
    while not isSquare(b2):
        a += 1
        b2 = a * a - n
    b = isqrt(b2)
    return a - b, a + b

p, q = fermat_factor(n)
print("p =", p)
print("q =", q)

def get_16th_root(a, p):
    T = (p - 1) // 2
    d = inverse(16, T)
    r = pow(a, d, p)
    if pow(r, 16, p) != a % p:
        raise ValueError("No valid 16th root found modulo p")
    return r

c_mod_p = c % p
c_mod_q = c % q

r_p = get_16th_root(c_mod_p, p)
r_q = get_16th_root(c_mod_q, q)

solutions_mod_p = [r_p, (-r_p) % p]
solutions_mod_q = [r_q, (-r_q) % q]

def crt(moduli, residues):
    p, q = moduli
    r1, r2 = residues
    inv_q = inverse(q, p)
    inv_p = inverse(p, q)
    x = (r1 * q * inv_q + r2 * p * inv_p) % (p * q)
    return x

solutions = []
for sol_p in solutions_mod_p:
    for sol_q in solutions_mod_q:
        candidate = crt([p, q], [sol_p, sol_q])
        solutions.append(candidate)

for i, cand in enumerate(solutions):
    cand_bytes = long_to_bytes(cand)
    print(f"Candidate {i}:")
    print("Hex:", cand_bytes.hex())
    try:
        decoded = cand_bytes.decode('utf-8', errors='replace')
        print("Decoded:", decoded)
    except Exception as ex:
        print("Decoding error:", ex)
    print("------")
```

Flag: `FMCTF{S0lv3d_w1th_R4b1n_fx777}`