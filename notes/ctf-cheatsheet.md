# CTF Beginner Cheat Sheet

## 1. Linux navigation & files
| Command | Purpose |
|---|---|
| `pwd` | Print current directory |
| `ls -la` | List files incl. hidden ones and permissions |
| `cd <dir>` / `cd ..` / `cd ~` | Change directory |
| `cat <file>` | Print file content (quote names with special chars: `cat "name"` or `./name`) |
| `file <file>` | Identify the real file type |
| `chmod +x script.sh` | Make a script executable |
| `unzip -q a.zip` | Extract archive quietly |

## 2. Networking & remote access
| Command | Purpose |
|---|---|
| `wget <URL>` | Download a file |
| `curl <URL>` | Print raw page content (HTML, `/robots.txt`) |
| `ssh user@host -p <port>` | Encrypted remote shell on a non-default port |
| `nc <host> <port>` | Raw TCP connection to a service |

## 3. Search, filter, redirect
| Command | Purpose |
|---|---|
| `grep "text" file` | Show matching lines (`-i` ignore case, `-rn` recursive with line numbers) |
| `find . -name "name"` | Find a file by name |
| `strings binary` | Extract printable strings without running it |
| `cmd1 \| cmd2` | Pipe output into the next command |
| `cmd > out.txt` | Save output to a file |

## 4. Decoding & Python one-liners
```bash
echo "<base64>" | base64 -d                  # Base64 -> text
echo "<hex>" | xxd -r -p                     # Hex -> text
echo "text" | tr 'A-Za-z' 'N-ZA-Mn-za-m'     # ROT13
python3 -c 'print("".join(chr(n) for n in [97,98,99]))'   # ASCII decimals -> text
python3 -c 'print(chr(0x64))'                              # Hex value -> char
python3 script.py -h                                       # Show script options
```

## 5. Cryptography basics
- **Caesar / ROT-N:** shift each letter by N. Only 25 keys, so try all (`scripts/caesar_bruteforce.py`).
- **Base64:** alphabet A-Z a-z 0-9 + /, often ends with `=`. Encoding, not encryption.
- **Hex:** pairs of 0-9 a-f. Two hex digits = one byte.
- **Substitution / Vigenère:** use frequency analysis; determine key length first.
- Quick experiments: CyberChef (browser).

## 6. Forensics basics
```bash
file artifact           # real type, ignore extension
exiftool image.jpg      # metadata
strings -n 8 artifact | grep -i "flag\|ctf"
binwalk artifact        # embedded files
xxd artifact | head     # inspect magic bytes / header
sha256sum artifact      # record integrity hash
```
Always work on a **copy** of the evidence.

## 7. Web basics (browser)
- `Ctrl+U` view source (comments, hints)
- `F12` DevTools: Sources, Network, Application (cookies, storage)
- `/robots.txt` for hidden paths

## 8. Brute-forcing a small keyspace (pattern)
When a program checks a short PIN/password and the candidate set is small, loop over candidates and filter failures:
```bash
for pw in <candidates>; do echo "$pw" | python3 checker.py; done | grep -v "incorrect"
```

## 9. Workflow for any new challenge
1. **File given?** `wget` -> `file` -> unzip / `strings` / `cat` the script.
2. **Host + port?** `nc host port` or `ssh user@host -p port`.
3. **URL?** Browser -> view source -> `/robots.txt` -> DevTools.
4. Document what worked **and** what didn't.
