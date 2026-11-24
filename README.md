# Duskline Alien Review

One original line of plain text — a review of planet Earth left by an alien
tourist — for the make.fun bounty **Alien Field Notes: The Two Day Earth
Review** (`u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000`).

## The entry

> The locals named their whole planet 'dirt', then act offended when visitors treat it like one. Two stars — great oceans, terrible branding.

139 characters, one line. The joke is the alien's outside view: Earth
literally means dirt/soil, and the locals still expect to be taken
seriously — a real review format (two stars, verdict, closing remark) with
the punch landing at the end.

## How to run

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

`main.py` (Python 3.13 stdlib only) writes the entry to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`). It refuses with exit 1
if the output directory is inside the repository, since the grader sandbox
is read-only there.

## License

MIT — see `LICENSE`.
