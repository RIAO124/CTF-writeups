# Caesar Cipher: Brute Force

**Platform:** picoCTF / CyLab Academy · **Category:** Cryptography · **Challenge:** caesar  
**Skills:** classical ciphers, brute force

## The challenge
A message was encrypted with a Caesar cipher, where every letter is shifted by a fixed amount. The goal was to read it.

## How I approached it
1. Recognised the pattern of a simple shift cipher.
2. Pasted the ciphertext into dCode's Caesar tool.
3. Used its brute-force option, which lists all 25 possible shifts, and picked the one that read as English.

## Tools
dCode Caesar tool. To understand what the site does, I added an offline version: [`scripts/caesar_bruteforce.py`](../../scripts/caesar_bruteforce.py).

## Where I got stuck
Nothing here. This was a warm-up.

## Takeaways
With only 25 possible keys, an attacker simply tries them all. A cipher is only as strong as its key space, however clever the algorithm looks.

## Why it matters in the real world
Simple shift or ROT obfuscation still shows up in malware strings and scripts, and analysts decode it exactly this way.
