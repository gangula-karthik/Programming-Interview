def is_palindrome(s):
    left, right = 0, len(s) - 1
    while right >=  left:
        if s[left] == s[right] and left == right: 
            return True
        if s[left] == s[right]:
            left += 1
            right -= 1
        if s[left] != s[right]: 
            return False

    return True

print(is_palindrome('racecar'))
print(is_palindrome('karthik'))
print(is_palindrome('anna'))

