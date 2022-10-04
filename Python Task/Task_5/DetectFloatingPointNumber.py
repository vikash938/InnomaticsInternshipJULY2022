#Detect Floating Point Number

import re

n = int(input())
for i in range(n):
    s = input()
    pattern = re.compile('^[+-]?[0-9]*[.][0-9]+$')
    print(bool(pattern.match(s)))