#!/usr/bin/env python3
"""Decrypt an RSA ciphertext when the modulus is small enough to factor.

Math: n = p*q, phi = (p-1)(q-1), d = e^-1 mod phi, m = c^d mod n.
This only works for weak (small) moduli, which is the point of the exercise.

Origin: written with AI assistance, reviewed and annotated by the repository owner.
Usage:  python3 rsa_small_modulus.py --n <modulus> --e <exponent> --c <ciphertext>
"""
import argparse
import sys

from sympy import factorint


def decrypt(n: int, e: int, c: int) -> tuple[int, int, int, bytes]:
    factors = factorint(n)
    if len(factors) != 2 or any(exp != 1 for exp in factors.values()):
        raise ValueError(f"Expected n = p*q with distinct primes, got {factors}")
    p, q = factors
    phi = (p - 1) * (q - 1)
    d = pow(e, -1, phi)
    m = pow(c, d, n)
    return p, q, d, m.to_bytes((m.bit_length() + 7) // 8, "big")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--n", type=int, required=True, help="modulus")
    parser.add_argument("--e", type=int, default=65537, help="public exponent")
    parser.add_argument("--c", type=int, required=True, help="ciphertext as integer")
    args = parser.parse_args()
    try:
        p, q, d, plain = decrypt(args.n, args.e, args.c)
    except ValueError as err:
        sys.exit(f"Error: {err}")
    print(f"p = {p}\nq = {q}\nd = {d}")
    print("Plaintext:", plain.decode(errors="replace"))


if __name__ == "__main__":
    main()
