# Layered Encoding: Base64 and ROT

**Platform:** picoCTF / CyLab Academy · **Category:** Cryptography · **Challenge:** interencdec  
**Skills:** decoding, CyberChef, Linux CLI

## The challenge
A downloaded file hid its content behind several layers of encoding. Each layer had to be identified and removed in order.

## How I approached it
1. Downloaded the file with `wget` and read it with `cat`.
2. Recognised Base64 from its character set and `=` padding.
3. In CyberChef, applied *From Base64* twice, then *ROT13* with the amount set to 19.
4. Read the resulting plaintext.

## Tools
`wget`, `cat`, CyberChef.

## Where I got stuck
Working out how many layers there were took some trial and error; CyberChef makes it easy to add and remove steps.

## Takeaways
Encoding is not encryption. The method is to identify the format, decode it, look at the result, and repeat.

## Why it matters in the real world
Attackers often stack encodings to hide payloads, for example Base64-encoded PowerShell commands in phishing campaigns. Peeling layers is routine work in malware triage and DFIR.
