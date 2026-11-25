# RSA with a Small Modulus

**Platform:** picoCTF / CyLab Academy · **Category:** Cryptography · **Challenge:** Mind your Ps and Qs  
**Skills:** RSA, factoring, Python, SymPy

## The challenge
An RSA-encrypted message came with its public key: a modulus `n` of about 81 digits (roughly 270 bits) and `e = 65537`. The title hints at the two primes, `p` and `q`, that make up `n`.

## How I approached it
1. Saw that the modulus is small enough to factor.
2. Solved it first with dCode's RSA tool, using the public values.
3. Then rebuilt the attack in Python to understand it: factor `n` with SymPy, compute `phi = (p-1)(q-1)`, get the private exponent `d` as the modular inverse of `e`, and decrypt with `pow(c, d, n)`.
4. Converted the resulting integer to text with `to_bytes(..., "big")`.

## Tools
dCode RSA tool; Python with SymPy. A cleaned-up, reusable version is in [`scripts/rsa_small_modulus.py`](../../scripts/rsa_small_modulus.py), with no challenge values included.

## Where I got stuck
No major blockers. The real work was understanding the maths behind the tool well enough to reproduce it.

## Takeaways
RSA is only secure if `n` cannot be factored. A short modulus falls in seconds and hands over the private key. This is why modern guidance asks for at least 2048-bit keys.

## Why it matters in the real world
Weak key sizes and poor key generation are genuine findings in security audits.
