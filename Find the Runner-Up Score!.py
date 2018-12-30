# Python 2

if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    a = [int(i) for i in arr]
    b = sorted(a)
    c = []
    for j in b:
        if j not in c:
            c.append(j)

    print(c[len(c) - 2])