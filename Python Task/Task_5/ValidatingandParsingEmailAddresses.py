# Validating and Parsing Email Addresses



# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
# number of email addresses
n = int(input())

for i in range(n):
    # get the name and email address line
    line = input()
    # separate the name and email
    name, email = line.split(' ')
    regex_pattern = "<[a-z][a-zA-Z0-9\-\.\_]+@[a-zA-Z]+\.[]a-zA-Z]{1,3}>"
    if bool(re.match(regex_pattern, email)):
        print(name, email)