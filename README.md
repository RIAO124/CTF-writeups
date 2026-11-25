# CTF Write-ups & Cybersecurity Learning Log

Documented methodology, notes and tooling from my hands-on cybersecurity training, with a focus on **DFIR / SOC fundamentals**.

> **Note on content:** I do not publish flags or full solutions. Each write-up documents *approach, tools and lessons learned*, in line with platform rules.

## About
Final-year Applied Mathematics & Informatics student (Politehnica Bucharest, graduating 2027), working toward an entry-level cybersecurity / SOC role. Bachelor's thesis topic: digital forensics in computer and communication systems.

## Profiles
| Platform | Profile |
|---|---|
| picoCTF / CMU CyLab Academy | `RIAO124` |
| TryHackMe | [pradu124](https://tryhackme.com/p/pradu124) |

## Progress snapshot (CyLab Academy, Nov 2026)
**38 challenges completed.**

| Learning path | Progress |
|---|---|
| General Skills in CTFs | 20/20 ✅ |
| Python in CTFs | 6/6 ✅ |
| The Beginner's Guide | 28/28 ✅ |
| Cryptography & Challenge Library | 8/15 🔄 |
| Forensics in CTFs | 2/17 🔄 |
| Low Level Binary Intro | 3/46 🔄 |
| Vault Door Series (reverse engineering) | 1/8 🔄 |

## Certifications & courses
| Title | Issuer | Date |
|---|---|---|
| Cyber Security 101 (learning path, 45h) | TryHackMe | Sep 2026 |
| Pre Security (learning path, 19h) | TryHackMe | Mar 2026 |
| Getting Started with Cybersecurity | IBM SkillsBuild ([verify](https://www.credly.com/badges/e67270a7-92d2-453c-bef1-f359b6f14cc4)) | Nov 2026 |
| Microsoft Azure AI Essentials Professional Certificate | Microsoft & LinkedIn Learning | Nov 2026 |
| Cybersecurity Job Simulation (phishing simulation design & analysis) | Mastercard via Forage | Jun 2026 |

## Repository structure
```
picoctf/         write-ups by category (general-skills, crypto, forensics, web, reverse-engineering, binary-exploitation)
tryhackme/       room notes and takeaways
scripts/         small helper scripts (see disclosure below)
notes/           cheat sheets
templates/       write-up template
```

## Method
1. Identify the artifact (`file`, `strings`, metadata, source).
2. Form a hypothesis, test the cheapest option first.
3. Document the reasoning, not only the result.
4. Map the technique to a real-world scenario (incident response, log analysis, forensics).

## Disclosure
Some scripts were written with AI assistance. I review and annotate them, and I am progressively writing my own. Each script states its origin in its header.

## Write-ups
| Challenge | Topic | Category |
|---|---|---|
| [caesar](picoctf/crypto/caesar.md) | Caesar brute force | Crypto |
| [interencdec](picoctf/crypto/interencdec.md) | Layered Base64 + ROT | Crypto |
| [New Caesar](picoctf/crypto/new-caesar.md) | Custom cipher cryptanalysis | Crypto |
| [Mind your Ps and Qs](picoctf/crypto/mind-your-ps-and-qs.md) | RSA, small modulus | Crypto |
| [Mini RSA](picoctf/crypto/mini-rsa.md) | RSA, small exponent | Crypto |
| [PW Crack 1-5](picoctf/crypto/pw-crack-1-5.md) | Dictionary attacks on MD5 | Crypto |
| [what's a net cat?](picoctf/general-skills/whats-a-netcat.md) | Netcat | General Skills |
| [Big Zip](picoctf/general-skills/big-zip.md) | Recursive search | General Skills |
| [buffer overflow 0](picoctf/binary-exploitation/buffer-overflow-0.md) | Stack overflow | Binary Exploitation |
| [keygenme-py](picoctf/reverse-engineering/keygenme-py.md) | Client-side validation | Reverse Engineering |
| [drawing.flag.svg](picoctf/forensics/svg-hidden-text.md) | Hidden data in SVG | Forensics |

## Roadmap
- [ ] Complete picoCTF Cryptography and Forensics paths
- [ ] TryHackMe SOC Level 1 and DFIR modules
- [ ] Write-ups for every completed category
- [x] RSA helpers (`scripts/rsa_small_modulus.py`, `scripts/rsa_small_exponent.py`)
- [ ] Own Python tooling for forensics triage
