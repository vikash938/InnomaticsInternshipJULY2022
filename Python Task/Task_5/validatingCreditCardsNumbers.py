# validating credit card numbers

# Enter your code here. Read input from STDIN. Print output to STDOUT

import re
n = int(input())
for i in range(n):
    credit = input().strip()
    remove_hyphen = credit.replace('-','')
    valid = True
    length_16 = bool(re.match(r'^[4-6]\d{15}$',credit))
    length_19 = bool(re.match(r'^[4-6]\d{3}-\d{4}-\d{4}-\d{4}$',credit))
    consecutive = bool(re.findall(r'(?=(\d)\1\1\1)',remove_hyphen))
    
    if length_16 == True or length_19 == True:
        if consecutive == True:
            valid = False
    else:
        valid = False
    if valid == True:
        print("Valid")
    else:
       print("Invalid")