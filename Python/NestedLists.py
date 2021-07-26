if __name__ == '__main__':
    arr = []
    sA = sB = 1e9*1.0
    for _ in range(int(input())):
        name = input()
        score = float(input())
        if score < sB:
            tmp = sB
            sB = score
            sA = tmp
        elif score < sA and score != sB:
            sA = score
        arr.append([name,score])
    listName = []
    for x in arr:
        if x[1] == sA:
            listName.append(x[0])
    listName.sort()
    for x in listName:
        print(x)



    
    
