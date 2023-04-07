def reverse_words(s):
    encoded = s.encode('utf-8')
    s = bytearray(encoded)
    s.reverse()

    def rev_range(s, start, finish):
        while finish > start:
            s[start], s[finish] = s[finish], s[start]
            start, finish = start + 1, finish - 1

    start = 0
    while True: 
        finish = s.find(b' ', start)
        if finish < 0:
            break
        rev_range(s, start, finish - 1)
        start = finish + 1

    rev_range(s, start, len(s) - 1) # to reverse the last word
    return s.decode('utf-8')

print(reverse_words("car is red"))
print(reverse_words("is this good"))
