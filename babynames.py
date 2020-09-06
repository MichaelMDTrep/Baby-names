#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# BabyNames python coding exercise.

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0
__author__ = 'Michael Trepanier'

"""
Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration. Here's what the HTML looks like in the
baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 - Extract all the text from the file and print it
 - Find and extract the year and print it
 - Extract the names and rank numbers and print them
 - Get the names data into a dict and print it
 - Build the [year, 'name rank', ... ] list and print it
 - Fix main() to use the extracted_names list
"""

import sys
import argparse


def extract_names(filename):
    """
    Given a single file name for babyXXXX.html, returns a
    single list starting with the year string followed by
    the name-rank strings in alphabetical order.
    ['2006', 'Aaliyah 91', 'Aaron 57', 'Abagail 895', ...]
    """
    names = []
    names_only = []
    # +++your code here+++

    with open(filename, 'r') as file:
        html = file.read().replace('\n', "")
    # print(html)

    # first get the year
    parts = html.split('Popularity in ')
    # print(parts)
    parts = parts[1].split('</h')
    year = parts[0]
    # print(year)
    names.append(year)

    str_list = html.split('<tr align="right">')
    # print(str_list)
    for str in str_list:
        # print(str)
        if (str.startswith('<td>')):
            # this is ignore the first part of the file before the names

            # this is to handle the stuff
            # at the end of the file after the names
            if (not str.endswith('</td>')):
                parts = str.split('<tr>')
                str = parts[0]

            # print(str)
            if (str.endswith('</td>')):
                str = str[4:-5]
            else:
                str = str[4:-10]
            # print(str)
            fields = str.split('</td><td>')
            rank = fields[0]
            boy_name = fields[1]
            girl_name = fields[2]
            # check to make sure the name hasn't already appeared in the file
            if (boy_name not in names_only):
                names.append(boy_name+' '+rank)
                names_only.append(boy_name)

            # check to make sure the name hasn't already appeared in the file
            if (girl_name not in names_only):
                names.append(girl_name+' '+rank)
                names_only.append(girl_name)

    names.sort()
    # print(names)
    return names


def create_parser():
    """Create a command line parser object with 2 argument definitions."""
    parser = argparse.ArgumentParser(
        description="Extracts and alphabetizes baby names from html.")
    parser.add_argument(
        '--summaryfile', help='creates a summary file', action='store_true')
    # The nargs option instructs the parser to expect 1 or more
    # filenames. It will also expand wildcards just like the shell.
    # e.g. 'baby*.html' will work.
    parser.add_argument('files', help='filename(s) to parse', nargs='+')
    return parser


def main(args):
    # Create a command line parser object with parsing rules
    parser = create_parser()
    # Run the parser to collect command line arguments into a
    # NAMESPACE called 'ns'
    ns = parser.parse_args(args)
    # print(ns)

    if not ns:
        parser.print_usage()
        sys.exit(1)

    file_list = ns.files

    # option flag
    create_summary = ns.summaryfile

    # For each filename, call `extract_names()` with that single file.
    # Format the resulting list as a vertical list (separated by newline \n).
    # Use the create_summary flag to decide whether to print the list
    # or to write the list to a summary file (e.g. `baby1990.html.summary`).

    # +++your code here+++
    for file in file_list:
        name_list = extract_names(file)
        names_str = "\n".join(name_list)
        if (create_summary):
            f = open(file+".summary", "w")
            f.write(names_str)
            f.close()
        else:
            print(names_str)


if __name__ == '__main__':
    main(sys.argv[1:])
