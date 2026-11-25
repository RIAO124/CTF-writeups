#!/usr/bin/env python3
"""Recover an RSA plaintext when e is tiny and the message was not padded (m^e < n).

In that case c = m^e exactly (no modular reduction), so m is the exact integer e-th root of c.
Floating point loses precision on large numbers, so the root is computed with integer binary search.

Origin: written with AI assistance, reviewed and annotated by the repository owner.
Usage:  python3 rsa_small_exponent.py --e 3 --c <ciphertext>
"""
import argparse
import sys


def integer_root(value: int, k: int) -> int:
    low, high = 0, 1 << (value.bit_length() // k + 1)
    while low < high:
        mid = (low + high) // 2
        if mid ** k < value:
            low = mid + 1
        else:
            high = mid
    return low


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--e", type=int, default=3, help="public exponent")
    parser.add_argument("--c", type=int, required=True, help="ciphertext as integer")
    args = parser.parse_args()
    m = integer_root(args.c, args.e)
    if m ** args.e != args.c:
        sys.exit("Not an exact root: m^e >= n, so this attack does not apply directly.")
    print("Plaintext:", m.to_bytes((m.bit_length() + 7) // 8, "big").decode(errors="replace"))


if __name__ == "__main__":
    main()
