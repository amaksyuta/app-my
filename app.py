#!/usr/bin/env python


import sys
import os
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


class App:
    def __init__(self, input, output):
        self.input = input
        self.output = output
        print(f"Input file name: {self.input}, Output file name: {self.output}")


    def check_extention(self):
        """ Check file extensions"""
        pass

    def check_file_exist(self):
        """ Check if file exist """
        pass


def main():
    args = create_parser()
    print(f"Current parameters: {args}")
    result = App(input=args.input, output=args.output)
    sys.stderr.close


if __name__ == "__main__":
    main()
