# !/usr/bin/env python
# coding:utf-8
"""
Name : ${HW08_Akshay_Prasanna}.py
CWID: 10469775
Author : Akshay Prasanna
Contact : akshayprasanna4@gmail.com
Time    : ${07-04-2021} ${21:01}
Desc: Creating various functions to check if dates are right and to scan and file directory.
"""
import datetime
from typing import Dict, Tuple, Iterator, List



def date_arithmetic() -> [datetime, datetime, int]:
    # the date three days after Feb 27, 2020.
    Date = datetime.date(2020, 2, 27)
    three_days_after_02272020 = Date + datetime.timedelta(days=3)

    # the date three days after Feb 27, 2019.
    Date = datetime.date(2019, 2, 27)
    three_days_after_02272019 = Date + datetime.timedelta(days=3)

    # the number of days between Feb 1, 2019 and Sept 30, 2019
    days_passed_02012019_09302019 = datetime.date(2019, 9, 30) - datetime.date(2019, 2, 1)

    return three_days_after_02272020, three_days_after_02272019, days_passed_02012019_09302019


x, y, z = date_arithmetic()
print(x, " ::: ", y, " ::: ", z)

# Part 2

def file_reader(path: str, fields: int, sep=',', header=False)->Iterator[Tuple[str]]:
    """file reader function implementation"""
    try:    #if unable to open file raising filenotfound error
        f = open(path, "r")
    except:
        raise FileNotFoundError(f'the path {path} do not exist')

    line_no = 0

    for line in f:

        line = line.strip("\n")
        line_no += 1

        if header:
            header = False
            continue

        tup = line.split(sep)

        if len(tup)<fields:
            raise ValueError("(file: {}, line number: {}, Fields found: {}, Fields expected: {}".format(path, line_no, len(tup), fields))

        yield tuple(tup)


if __name__=='__main__':
    for cwid, name, major in file_reader('foo.txt', 3, sep='|', header=True):
        print("cwid: {}  name: {}  major: {}".format(cwid, name, major))



# Part - 3
import os
import re
from prettytable import PrettyTable

class FileAnalyzer:
        """Given a directory name, searches that directory for Python files"""
        def __init__(self,directory: str = os.curdir):
                if type(directory) != str:
                    raise TypeError('directory must be a str')

                if not os.path.exists(directory):
                    raise FileNotFoundError(f'path {directory} do not exist')

                self.files_summary = {}
                self.directory = "/home/akshay/analyzer"
                self.analyze_files()

        def analyze_files(self):
            """Analyzing file to get directoru"""
            for root, dir, files in os.walk(self.directory):
                     for file in files:
                            if file.endswith(".py"):
                                myfile = root + "/" + file
                                characters = 0
                                lines = 0
                                classes = 0
                                definition = 0

                                try:
                                    with open(myfile, 'r') as frb:
                                        for line in frb:
                                            lines = lines + 1
                                            characters = characters + len(line)
                                            if line.startswith("class"):
                                                classes = classes + 1
                                            if re.match('\s.*def|def', line):
                                                definition = definition + 1
                                        self.files_summary[file] = {}

                                    self.files_summary[file]['class'] = classes
                                    self.files_summary[file]['function'] = definition
                                    self.files_summary[file]['line'] = lines
                                    self.files_summary[file]['char'] = characters

                                except (FileNotFoundError):
                                    print("Wrong file or file path: %s" %myfile)
                                except PermissionError:
                                        print("Cannot open file : %s" %myfile)

            self.pretty_print()

        def pretty_print(self):
                # Declaring a pretty table object
                x = PrettyTable()
                x.field_names = ["Filename", "classes", "definition", "lines", "characters"]
                for key,value in self.files_summary.items():
                     data = []
                     data.extend([key,value["class"],value["function"],value["line"],value["char"]])
                     x.add_row(data)
                print(x)

if __name__ == "__main__":
    obj = FileAnalyzer()