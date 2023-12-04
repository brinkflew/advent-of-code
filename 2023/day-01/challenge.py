import re
from pathlib import Path


input_file = Path(__file__).parent / "input.txt"

# --- Part 1 -------------------------------------------------------------------


def challenge_01():
    with input_file.open() as f:
        total = 0

        for line in f:
            line = re.sub(r"[^\d]+", "", line)
            total += int(line[0] + line[-1])

        return total


# --- Part 2 -------------------------------------------------------------------

digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


def convert(number):
    return str(digits.index(number) + 1) if not number.isdigit() else number


def challenge_02():
    with input_file.open() as f:
        total = 0

        for line in f:
            numbers = re.findall(rf"(?=({'|'.join(digits)}|\d))", line)
            total += int(convert(numbers[0]) + convert(numbers[-1]))

        return total
