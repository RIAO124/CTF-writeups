# PW Crack, Levels 1-5

**Platform:** picoCTF / CyLab Academy · **Category:** Cryptography · **Challenge:** PW Crack 1-5  
**Skills:** dictionary attacks, hashing (MD5), Bash, Python

## The challenge
A five-level series. Each level protects a flag file with a password, checked either directly in the code or against an MD5 hash. The levels get harder as the checks get less obvious.

## How I approached it
1. **Levels 1-2:** downloaded the program with `wget`, browsed with `ls`, read it with `cat`, and found how the password is checked. I used a regex one-liner (written with AI assistance, then reviewed by me) to pull out the compared string.
2. **Level 3:** tried a short list of candidate passwords in a Bash loop, filtering out failures with `grep -v "incorrect"`.
3. **Levels 4-5:** computed the MD5 digest of each candidate and compared it with the target hash from the `.hash.bin` file, first on a list of 100 passwords, then on a dictionary file with tens of thousands of entries.

## Tools
`wget`, `ls`, `cat`, `grep`, Bash loops, Python `hashlib`.

## Where I got stuck
With the dictionary file, no hash ever matched. Each line carried an invisible trailing newline, and adding `.strip()` before `.encode()` fixed it. I also learned to compare raw bytes (`.digest()`) rather than a hex string.

## Takeaways
Offline dictionary attacks against unsalted hashes are fast. Small details like whitespace, and the difference between hex and binary hash formats, decide whether a script works.

## Why it matters in the real world
Hardcoded credentials (CWE-798) and weak, unsalted hashes are common findings. Password cracking is a core skill in investigations involving stolen credentials.
