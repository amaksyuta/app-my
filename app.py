#!/usr/bin/env python


import argparse
from __version import __version__


def create_parser():
    """ Function for parsing commandline parameters """
    parser = argparse.ArgumentParser(
        description="Command line tool for serialise/deserialise data",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,)
    parser.add_argument ("-i","--input", 
        help="Input file with personal data(name, address, phone)",
        default="test.txt", 
        required=True)
    parser.add_argument ("-o", "--output", 
        help="Output file in supported format csv/json only)", 
        default="test.json",
        required=True)
    parser.add_argument ("-v", "--version", 
        action="version", 
        version=__version__)
    args = parser.parse_args()
    return args


def fib(num: int) -> int:
    return num if num < 2 else fib(num-1)+fib(num-2)


def summ(one, two):
    return one + two


def main():
    args = create_parser()
    print(f"Current parameters: {args}")


if __name__ == "__main__":
    main()
