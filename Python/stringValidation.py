if __name__ == '__main__':
    s = input()
    arrVal = [0,0,0,0,0]
    for i in s:
        if(i.isalnum()):
            arrVal[0] = 1
        if (i.isalpha()):
            arrVal[1] = 1
        if i.isdigit():
            arrVal[2] = 1
        if i.islower():
            arrVal[3] =1
        if i.isupper():
            arrVal[4] = 1
    for x in arrVal:
        if x :
            print('True')
        else:
            print('False')
