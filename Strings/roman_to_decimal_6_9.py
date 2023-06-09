def roman_to_int(s):
    lookup = {"I": 1, "V": 5, "X": 10, "L": 50, "C":100, 'D': 500, 'M': 1000}
    N = len(s)
    i = N - 1
    res = 0
    while i >= 0: 
        if i < N - 1 and lookup[s[i]] < lookup[s[i + 1]]:
            res -= lookup[s[i]]
        else: 
            res += lookup[s[i]]
        i -= 1
    return res


print(roman_to_int("III"))
print(roman_to_int("IX"))
print(roman_to_int("LIX"))
