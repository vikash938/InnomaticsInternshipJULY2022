# validating UID



# Enter your code here. Read input from STDIN. Print output to STDOUT

import re
n = int(input())
for _ in range(n):
    d = ''.join(sorted(input()))
    try:
        assert re.search(r'[A-z]{2}',d)
        assert re.search(r'\d\d\d', d)
        assert not re.search(r'[^a-zA-Z0-9]', d)
        assert not re.search(r'(.)\1', d)
        assert len(d) == 10
    except:
        print('Invalid')
    else:
        print('Valid')
