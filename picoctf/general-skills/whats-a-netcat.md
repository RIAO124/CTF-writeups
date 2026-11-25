# Talking to a Remote Service with Netcat

**Platform:** picoCTF / CyLab Academy · **Category:** General Skills · **Challenge:** what's a net cat?  
**Skills:** networking basics, Linux CLI

## The challenge
The challenge exposed a service on a given host and port, and the answer was in what it sent back.

## How I approached it
1. Took the host and port from the challenge.
2. Connected with `nc <host> <port>`.
3. Read the response.

## Tools
`nc` (netcat).

## Where I got stuck
Nothing significant.

## Takeaways
Many services, in CTFs and in real life, are just plain TCP. Netcat is the quickest way to talk to one and see what it returns.

## Why it matters in the real world
Banner grabbing, service enumeration and quick connectivity checks all rely on this during incident response.
