import argparse
import os
import re

parser = argparse.ArgumentParser()

parser.add_argument('-p', '--path', help='Path to dir for scaning')
parser.add_argument('-f', '--filter', help='Filter for scan')

args = parser.parse_args()

if args.filter:
    pattern = r'.*\.{}'.format(args.filter)
else:
    pattern = r'.*'

l = []

if args.path:
    folder_list = os.listdir(args.path)
    for item in folder_list:
        mathes = re.findall(pattern, item)
        for match in mathes:
            l.append(match)
    if l:
        print(l)
    else:
        print('Empty')
else:
    print('Nothing to scan')