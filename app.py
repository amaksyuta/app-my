#!/usr/bin/env python


import sys
import os
import pickle
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


    def check_obj_exist(self, obj):
        """ Check if object exist """
        if os.path.exists(obj):
            try:
                os.remove(obj)
            except OSError as e:
                print(f"[ERROR]: {e.obj} - {e.strerror}.")
        else:
            print(f"[WARNING]: Looks like {obj} object has been removed or doesn't exist")


def main():
    args = create_parser()
    print(f"Current parameters: {args}")
    App(input=args.input, output=args.output)
    personal_data = {
        "name": ["Cristiano Ronaldo", "Lionel Messi", "Eden Hazard", "Neymar"],
        "address": ["Manchester United", "PSG", "Real Madrid", "Atletico Madrid", "PSG"],
        "phone": ["234", "54545", "6666", "2234", "33334"]
    }
    print(personal_data)
    personal_data_file = open('persons.txt', 'wb')
    pickle.dump(personal_data, personal_data_file)
    personal_data_file.close()
    sys.stderr.close


if __name__ == "__main__":
    main()
