if __name__ == '__main__':
    n = int(input())
    ls = []
    for i in range(n):
        ls.append(map(str,raw_input().split()))
result = []
i = 0
for i in range(len(ls)):
    if ls[i][0] == 'insert':
        result.insert(int(ls[i][1]), int(ls[i][2]))
    elif ls[i][0] == 'remove':
        result.remove(int(ls[i][1]))
    elif ls[i][0] == 'append':
        result.append(int(ls[i][1]))
    elif ls[i][0] == 'sort':
        result.sort()
    elif ls[i][0] == 'pop':
        result.pop()
    elif ls[i][0] == 'reverse':
        result.reverse()
    elif ls[i][0] == 'print':
        print(result)
