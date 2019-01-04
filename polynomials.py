import numpy

ls = []
ls1 = []
coeffs = ls.append(raw_input())
x = raw_input()

arr = ls[0].split(" ")
for i in range(len(arr)):
    ls1.append(float(arr[i]))

res = numpy.polyval(ls1, float(x))
print res