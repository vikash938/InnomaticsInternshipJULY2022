#Group(), Groups() & Groupdict()


import re
regex_pattern = r"([a-zA-Z0-9])\1+"
m = re.search(regex_pattern, input())
if m:
    print(m.group(1))
else:
    print(-1)

