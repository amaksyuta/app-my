#!/usr/bin/env python


import argparse
import sys
import os
import pathlib
import json
from version import __version__


def create_parser():
    """ Function for parsing command line parameters """
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


class Person:
    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone
    

    def encode(self):
        """ For corect encode object """
        return self.__dict__
    

def pp_json_file(path, file):
    """ Pretty print JSON file to console """
    print(json.dumps(json.load(open(os.path.join(path, file), "r")), indent = 4))


def get_file_extension(f):
    """ Function return file extention """
    file_extension = pathlib.Path(f).suffix
    exten = file_extension.split(".")[1]
    return exten


def get_file_name(f):
    """ Function return file name """
    file_name = pathlib.Path(f).stem
    return file_name


def csv_ser(items, f):
    """ CVS format desserialization function """
    print("Serialize csv data to the object")
    file = open(f, 'w')
    file.write(f'name,address,phone')
    for i in range(len(items)):
        file.write(f'\n{items[i].name},{items[i].address},{items[i].phone}')
    file.close()


def txt_ser(items, f):
    """ TXT serialization function """
    print("Serialize txt data to the object")
    file = open(f, 'w')
    for i in range(len(items)):
        if i == 0:
            file.write(f'{items[i].name},{items[i].address},{items[i].phone}')
        else:
            file.write(f'\n{items[i].name},{items[i].address},{items[i].phone}')
    file.close()
    

def json_ser(items, f):
    """ JSON serialization function """
    print("Serialize Json data to the object")
    with open(f, 'w') as file:
        json.dump(items, fp=file, default=lambda o: o.encode(), indent=4)
    #print(json.dump(items, fp=file, default=lambda o: o.encode(), indent=4))
    file.close()


def csv_des(f):
    """ CVS format desserialization function """
    result = []
    with open(f, encoding='utf8') as f:
        # Skip firs line header in CSV
        lines = f.readlines()[1:]
        for line in lines:
            l = line.strip().split(",")
            result.append(Person(l[0], l[1], l[2]))     
    return result


def txt_des(f):
    """ TXT deserialization function """
    print("Deserialize data from the object")
    result = []
    with open(f, encoding='utf8') as f:
        for line in f:
            l = line.strip().split(",")
            result.append(Person(l[0], l[1], l[2]))     
    return result


def json_des(f):
    """ JSON deserialization function """
    print("Serialize data to the object")
    # opening the JSON file
    fp = open(f,'r')
    items = json.load(fp)
    result = []
    for item in items:
        result.append(Person(item['name'], item['address'], item['phone']))
    return result


def main():
    """ Main function parsiong and serialise/deserialize files """
    # Create parser object for handling application command line parameters by keys
    args = create_parser()
    print(f"[INFO]: Current parameters: {args}")
    # Set variables for input/out files
    in_file = args.input
    out_file = args.output
    # Create a dictionary with supported file formats for serialisation and deserialization
    serializers = {"csv":csv_ser, "txt":txt_ser, "json":json_ser}
    deserializers = {"csv":csv_des, "txt":txt_des, "json":json_des}
    # Print supported formats for serialization and deserialization
    print(f"Supported serializers: {[key for key in serializers.keys()]}")
    print(f"Supported deserializers: {[key for key in deserializers.keys()]}")
    # Check input/output files extentions - make sys.exit() in case unsupported format
    if get_file_extension(in_file) not in deserializers.keys():
        in_extention = get_file_extension(in_file)
        in_file_name = get_file_name(in_file)
        print(f"[ERROR]: *.{in_extention} unsupported input file - {in_file_name}.{in_extention}  format")
        sys.exit(1)
    if get_file_extension(out_file) not in serializers.keys():
        out_extention = get_file_extension(out_file)
        out_file_name = get_file_name(out_file)
        print(f"[ERROR]: *.{out_extention} unsupported output file - {out_file_name}.{out_extention}  format")
        sys.exit(1)
    # Set items for deserialize objects from input file
    items = deserializers[get_file_extension(in_file)](in_file)
    #print([x.toJson() for x in items])
    serializers[get_file_extension(out_file)](items, out_file)
    print(f"\n[INFO]: Display content serialized file: {out_file}\n")
    f = open(out_file, "r")
    print(f.read())
    f.close()
    
if __name__ == "__main__":
    main()
