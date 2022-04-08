"""
The first module to do something
"""

import sys


def echo(phrase: str) -> None:
    """wrapper around the print function"""
    print(phrase)


def main(text: str) -> int:
    """Echo the text to standard out"""
    echo(text)
    return 0


if __name__ == "__main__":
    sys.exit(main("Kevin is actually butts"))
