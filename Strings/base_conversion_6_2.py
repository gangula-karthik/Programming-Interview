import string

def findTotalNum(num, b1): 
    numDigits = len(num) - 1
    res = 0
    for i in num:
        res += (int(i) * (b1 ** numDigits))
        numDigits -= 1
    return res

def baseConvertor(num, b1, b2): 
    total = findTotalNum(num, b1)
    negative = False
    if int(num) < 0: 
        negative = True
    lst = []
    while True:
        x = total % b2
        if x == 0: 
            break
        lst.append(x)
        total = total // 13
    return ('-' if negative else '') + ''.join([str(i) if i < 10 else string.hexdigits[i].upper() for i in lst[::-1]])

print(baseConvertor("615",7,13))

