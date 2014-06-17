#!/bin/python3

"""
E-mail Parser
@author Arun George, 2014
Python
"""

# import regex lib
import re


def main():
    """Parses headers from an email file using regular expressions."""

    # set input file
    file = "email.txt"
    global email_file

    # try to open the file
    try:
        email_file = open(file, "r")
    except:
        print("File can't be opened to read! - ", file)
        exit()

    print("-" * 50)  # line dash

    # read sequence of lines and print output
    for line in email_file:
        line = line.rstrip()

        if re.search('^From:', line) or \
                re.search('^To:', line) or \
                re.search('^Subject:', line) or \
                re.search('^Date:', line) or \
                re.search('^Reply-To:', line) or \
                re.search('^Content-Type:', line):

            print(line)  # display the final output

    email_file.close()


main()
