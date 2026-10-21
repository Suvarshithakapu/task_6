if __name__ == '__main__':
    n = int(input())
    t = tuple(map(int, input().split()))
    
    # Correct hash calculation for HackerRank
    x = 0x345678
    mult = 1000003
    for i in range(len(t)):
        # l = remaining length
        l = len(t) - i
        x = (x ^ t[i]) * mult
        mult += 82520 + l
    x += 97531
    print(x)