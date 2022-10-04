# HexColorCode





# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

in_css = False

# get the number of lines and loop through

n = int(input())
for i in range(n):
    # get the line and check the color code
    line = input()
    if '{' in line:
        in_css = True
    elif '}' in line:
        in_css = False
    elif in_css:
        for i in re.findall('#[0-9a-fA-F]{3,6}', line):
            print(i)