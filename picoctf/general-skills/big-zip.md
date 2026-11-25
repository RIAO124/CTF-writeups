# Searching a Huge Archive from the Command Line

**Platform:** picoCTF / CyLab Academy · **Category:** General Skills · **Challenge:** Big Zip  
**Skills:** Linux CLI, grep, file triage

## The challenge
A large archive with hundreds of nested folders and files. The target text had to be found without opening files by hand.

## How I approached it
1. Extracted the archive with `unzip`.
2. Searched every file's content recursively with `grep -rnw . -e "<pattern>"`. An alternative is `find . -type f -exec grep -H "..." {} +`.

## Tools
`unzip`, `grep`, `find`.

## Where I got stuck
I started by browsing folders with `ls` and `cd`, which is hopeless in a deep tree. Recursive `grep` (`-r` to recurse, `-n` for line numbers) solved it instantly.

## Takeaways
Search tools beat manual browsing. Recursive grep is the fastest way to triage large amounts of data.

## Why it matters in the real world
The same habit applies directly to log analysis and file-system triage in DFIR.
