# Re.start() & Re.end()





import re

S, n = input(), input()
matches = re.finditer(r'(?=(' + n + '))', S)

match = False
for match in matches:
    match = True
    print((match.start(1), match.end(1) - 1))

if match == False:
    print((-1, -1))
    