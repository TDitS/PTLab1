# -*- coding: utf-8 -*-
import argparse
from decimal import Clamped
import sys

from CalcRating import CalcRating
from TextDataReader import TextDataReader
from XmlDataReader import XmlDataReader
from PrintStudents100 import PrintStudents100


def get_path_from_arguments(args) -> str:
    parser = argparse.ArgumentParser(description="Path to datafile")
    parser.add_argument("-p", dest="path", type=str, required=True,
                        help="Path to datafile")
    args = parser.parse_args(args)
    return args.path


def main():
    path = get_path_from_arguments(sys.argv[1:])

    if (path[-3:] == 'txt'):
        reader = TextDataReader()
    else:
        reader = XmlDataReader()

    students = reader.read(path)
    print("Students: ", students, "\n")

    rating = CalcRating(students).calc()
    print("Rating: ", rating, "\n")

    students100 = PrintStudents100(students).calc()
    print(students100)


if __name__ == "__main__":
    main()
