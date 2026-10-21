import re
n = int(input())
pattern = r'^[789]\d{9}$'
for _ in range(n):
    num = input().strip()
    if re.match(pattern, num):
        print("YES")
    else:
        print("NO")