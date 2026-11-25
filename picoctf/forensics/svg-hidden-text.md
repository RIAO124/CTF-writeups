# Hidden Data in an SVG File

**Platform:** picoCTF / CyLab Academy · **Category:** Forensics · **Challenge:** drawing.flag.svg  
**Skills:** file-format awareness, metadata, XML

## The challenge
Find information hidden inside a vector image.

## How I approached it
1. Ran `file`, `exiftool`, `strings` and `binwalk`, treating it like a normal image. No result.
2. Realised that SVG is XML text and opened it with `cat`.
3. Used `grep -E "<tspan|<text|<!--" drawing.flag.svg` to list text elements and comments, and found the hidden text.

## Tools
`file`, `exiftool`, `strings`, `binwalk`, `cat`, `grep`.

## Where I got stuck
I assumed a raster image (PNG or JPEG) and went straight to binary tools. Text can be hidden visually (same colour as the background, or placed off-canvas) while staying fully readable in the source.

## Takeaways
Match the method to the real file format: byte-level tools for binaries, structure inspection for XML-based formats.

## Why it matters in the real world
The same approach applies when inspecting suspicious documents and web content in phishing and DFIR cases.
