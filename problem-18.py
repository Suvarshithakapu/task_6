n = int(input())
A = set(map(int, input().split()))
m = int(input())
for _ in range(m):
    cmd = input().split()[0]
    B = set(map(int, input().split()))
    if cmd == 'intersection_update':
        A.intersection_update(B)
    elif cmd == 'update':
        A.update(B)
    elif cmd == 'symmetric_difference_update':
        A.symmetric_difference_update(B)
    elif cmd == 'difference_update':
        A.difference_update(B)
print(sum(A))