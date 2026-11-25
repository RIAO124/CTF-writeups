# Breaking a Custom Cipher: New Caesar

**Platform:** picoCTF / CyLab Academy · **Category:** Cryptography · **Challenge:** New Caesar  
**Skills:** cryptanalysis, Python, modular arithmetic

## The challenge
`new_caesar.py` implemented a custom cipher: the text is first encoded with a 4-bit scheme over a 16-letter alphabet (`a` to `p`), then shifted with a modular Caesar step. The goal was to recover the original message.

## How I approached it
1. Started with dCode's Caesar tool, as in the earlier challenge. It could not solve this one, because the cipher is more than a plain shift.
2. Read the source and identified the two stages: the 16-letter encoding and the modular shift.
3. Wrote the inverse of each stage: an `unshift` modulo 16, and a decoder that rebuilds each character from a pair of 4-bit symbols.
4. Tried every possible key. There are only 16, since the alphabet has 16 letters. Kept the readable output.

## Tools
`cat`, Python.

## Where I got stuck
I first tried to reuse the original encryption script with my ciphertext dropped in, and it failed with an `AssertionError` because of its placeholder key. The fix was to write the decryption logic myself instead of bending their script.

## Takeaways
When facing a custom cipher, read the code, reverse it step by step, and check how big the key space is. Here it was tiny.

## Why it matters in the real world
Home-made cryptography is a classic red flag in code reviews: small key spaces and reversible steps make it easy to break.
