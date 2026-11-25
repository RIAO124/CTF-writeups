#!/usr/bin/env python3
"""Caesar cipher brute-force: prints all 25 shifts.
Origin: written with AI assistance, reviewed and annotated by the repository owner.
Usage: python3 caesar_bruteforce.py "Ciphertext here"
"""
import sys

def shift(text: str, k: int) -> str:
    out = []
    for ch in text:
        if ch.isalpha():
            base = ord("A") if ch.isupper() else ord("a")
            out.append(chr((ord(ch) - base - k) % 26 + base))
        else:
            out.append(ch)
    return "".join(out)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit('Usage: python3 caesar_bruteforce.py "ciphertext"')
    for k in range(1, 26):
        print(f"[{k:2}] {shift(sys.argv[1], k)}")
