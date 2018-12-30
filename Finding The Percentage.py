# Python 2

if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = raw_input()

arr = student_marks[query_name]
res = float((arr[0]+arr[1]+arr[2])/3)
print format(res, '.2f')
