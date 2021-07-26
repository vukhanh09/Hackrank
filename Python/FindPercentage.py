if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    X = student_marks[query_name]
    avg = 0.0
    for x in X:
        avg += x
    print(format(avg/3, '.2f'))