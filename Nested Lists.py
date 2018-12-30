# Python 2

n = []
e = []
s = []
t = []

for _ in range(int(raw_input())):
    name = raw_input()
    score = float(raw_input())
    n.append((score, name))
    s.append(score)

res = sorted(n)
sc = sorted(s)

for i in sc:
    if i not in e:
        e.append(i)
second_lowest = e[1]

for j in range(len(n)):
    if n[j][0] == second_lowest:
        t.append(n[j][1])

t.sort()

for k in range(len(t)):
    print t[k]