#!/usr/bin/env python


import argparse
import sys
import os
import json
import pickle
import pandas as pd
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


class Person:
    def __init__(self, ifile, ofile):
        self.ifile = ifile
        self.ofile = ofile
        print(f"Input file name: {self.ifile}, Output file name: {self.ofile}")


    def check_extention(self):
        """ Check file extensions """
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
    input_file = args.input
    output_file = args.output
    Person(ifile=input_file, ofile=output_file)
    name = []
    address = []
    phone = []
    with open(input_file, encoding='utf8') as f:
        for line in f:
            l = line.strip().split(",")
            name.append(l[0])
            address.append(l[1])
            phone.append(int(l[2]))       
        keys = ["name", "address", "phone"]
        values = [name, address, phone]
        data = dict(zip(keys, values))    
    # Serealize data 
    print("Serialize data to the object")
    ser = pickle.dumps(data)
    print(ser)
    # Deserialise data
    print("Deserialize data from the object")
    deser = pickle.loads(ser)
    print(deser)
    # Convert object-data to the proper format
    df = pd.DataFrame(deser)
    print("Print data from DataFrame objeckt")
    print(df)
    print("Convert data to csv format")
    df.to_csv(output_file, index=False)
    print("Convert data to json format")
    df.to_json('test.json', orient='records', lines=True)
    sys.stderr.close


if __name__ == "__main__":
    main()
