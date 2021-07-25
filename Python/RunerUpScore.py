if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(arr)
    a = b = -101
    for x in arr:
        if x > b:
            tmp = b
            b = x
            a = tmp
        elif x > a and x != a:
            a = x

    print(a)