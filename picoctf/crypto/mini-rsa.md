# RSA with a Small Public Exponent

**Platform:** picoCTF / CyLab Academy · **Category:** Cryptography · **Challenge:** Mini RSA  
**Skills:** RSA, number theory, Python

## The challenge
This time the modulus `N` was huge and impossible to factor, but the public exponent was tiny (`e = 3`) and the message was not padded.

## How I approached it
1. Realised that with `e = 3` and no padding, the message can be small enough that `m^3 < N`. The modular reduction then never happens, so `c = m^3` exactly.
2. Computed the exact integer cube root of `c` with a binary search on Python integers.
3. Converted the result to text with `to_bytes(..., "big")`.

## Tools
Python. A reusable version is in [`scripts/rsa_small_exponent.py`](../../scripts/rsa_small_exponent.py).

## Where I got stuck
My first idea, `c ** (1/3)`, gave a wrong result. Floating point loses precision on numbers with hundreds of digits and corrupts the last bytes. Switching to integer arithmetic fixed it.

## Takeaways
A small exponent without padding removes RSA's protection, so no private key or factoring is needed. Padding schemes such as OAEP exist to prevent this.

## Why it matters in the real world
Unpadded ("textbook") RSA is a known flaw that reviewers look for in custom cryptographic code.
