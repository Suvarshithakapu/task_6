from collections import Counter
s = sorted(input().strip())
cnt = Counter(s)
for k, v in cnt.most_common(3):
    print(k, v)