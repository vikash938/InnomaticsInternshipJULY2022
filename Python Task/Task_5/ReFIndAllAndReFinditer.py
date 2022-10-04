#Re.findall() & Re.finditer()





import re

n = input()
m = re.findall(r"(?<=[qwrtypsdfghjklzxcvbnm])([aeiou]{2,})[qwrtypsdfghjklzxcvbnm]", n,flags=re.IGNORECASE)
if len(m) > 0:
    print("\n".join(m))
else:
    print(-1)