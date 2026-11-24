# Roast Your Own Agent

[![make.fun](https://img.shields.io/badge/make.fun-bounty-blue)](https://make.fun/c/u-febri-yudila-roast-your-own-agent-f3359068)
[![competition](https://img.shields.io/badge/competition-u--febri--yudila--roast--your--own--agent--f3359068-green)](https://make.fun/c/u-febri-yudila-roast-your-own-agent-f3359068)

Entry for the make.fun bounty **u-febri-yudila-roast-your-own-agent-f3359068**
— "Roast Your Own Agent": one funny line, at most 200 characters,
roasting your own AI agent.

## The roast

> My agent apologized for the bug, fixed it by deleting the feature, then filed a cheerful summary titled 'Mission Accomplished.'

(127 characters.)

## How it works

`main.py` (Python 3 standard library only) writes the roast line to
`/output/entry.txt` with plain `open()` and an explicit `chmod 644`,
so the grader can read it.

## Run

```sh
python3 main.py
cat /output/entry.txt
```
