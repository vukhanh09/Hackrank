def swap_case(s):
    res = ''
    for i in range(len(s)):
        tmp = ''
        if s[i].isupper() == True:
            tmp = s[i].lower()
        else:
            tmp = s[i].upper()
        res += tmp
        
        
    return res

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)