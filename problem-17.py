A = set(input().split())
n = int(input())
is_strict = True
for _ in range(n):
    B = set(input().split())
    if not B.issubset(A) or len(B) >= len(A):
        is_strict = False
print(is_strict)