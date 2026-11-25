# Client-Side License Validation

**Platform:** picoCTF / CyLab Academy · **Category:** Reverse Engineering · **Challenge:** keygenme-py  
**Skills:** static analysis, hashing (SHA-256), Python

## The challenge
A Python program checked a license key on the client side. The goal was to understand the check and produce a valid key.

## How I approached it
1. Read the script and located the key-check function and the constants it uses.
2. Saw that the key is derived from the SHA-256 digest of a hardcoded username, with specific characters compared at specific positions.
3. Reproduced the derivation with `hashlib`, keeping only the checked positions, in the order the code expects.

## Tools
`cat`, `grep -A 15 "def check_key"`, Python `hashlib`.

## Where I got stuck
My instance used a different username from the usual examples, and at first I used the whole hash instead of only the characters the function actually compares. Reading each comparison carefully fixed it.

## Takeaways
Client-side validation is weak by design: the user can read the algorithm and its inputs.

## Why it matters in the real world
Licensing and anti-tamper checks are analysed by reverse engineers every day, and the same static-analysis habits apply to malware triage.
