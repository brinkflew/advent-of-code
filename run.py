#!/usr/bin/env python

import sys
from importlib import import_module
from pprint import pprint


try:
    year = sys.argv[1]
    day = sys.argv[2].rjust(2, "0")
except IndexError:
    print("Usage: run.py <year> <day>")
    sys.exit(1)

try:
    challenge_module = import_module(f"{year}.day-{day}.challenge", package=None)
except ModuleNotFoundError:
    print(f"Could not find challenge for {year}/day-{day}/challenge.py")
    sys.exit(1)

print(f"===[ Advent of Code {year}: Day {day} ]===\n")

for id_ in range(1, 3):
    challenge = getattr(challenge_module, f"challenge_{str(id_).rjust(2, '0')}", None)

    if challenge is not None:
        print(f"--- Part {id_} ---")
        print()
        pprint(challenge())
        print()

print("===[ Done ]===")
