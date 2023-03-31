def int_to_string(x): 
    negative = False
    if x < 0: 
        negative = True
        x *= -1

    s = []
    while True: 
        s.append(chr(ord('0') + x % 10))
        x = x // 10
        if x == 0: 
            break

    return ('-' if negative else '') + ''.join(s[::-1])



def string_to_int(y):
    negative = False
    start = 0
    res = 0
    if y[0] == '-':
        negative = True
        start = 1

    for i in range(start, len(y)):
        digit = ord(y[i]) - ord('0')
        if 0 <= digit <= 9: 
            res = res * 10 + digit

        else: 
            raise ValueError("non numeric character found")

    return (-1 * res) if negative else (res)

print(int_to_string(10))
print(string_to_int("432143"))
