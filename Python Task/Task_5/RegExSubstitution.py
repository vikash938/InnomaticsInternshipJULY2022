
# RegEx Substitution



import re
n = int(input())
for i in range(n):
    text = input()
    matches = re.sub(r"=?( && )", " and ", text)
    matches = re.sub(r"=?( \|\| )", " or ", matches)
    matches = re.sub(r"=?( && )", " and ", matches)
    matches = re.sub(r"=?( \|\| )", " or ", matches)
    
    print(matches)