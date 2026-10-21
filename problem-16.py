t = int(input())
for _ in range(t):
    n = int(input())
    A = set(input().split())
    m = int(input())
    B = set(input().split())
    print(A.issubset(B))