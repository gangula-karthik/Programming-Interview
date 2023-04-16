def phone_mnemonic(phone_number): 
    if phone_number == "":
        return None
    mapping = ["0", "1", "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
    def helper_func(digit):
        if digit == len(phone_number): 
            mnemonics.append(''.join(fillerNum))
            return mnemonics
        else: 
            for i in mapping[int(phone_number[digit])]: 
                fillerNum[digit] = i
                helper_func(digit + 1)
    mnemonics, fillerNum = [], [0] * len(phone_number)
    helper_func(0)
    return mnemonics


print(phone_mnemonic("227"))
print(phone_mnemonic("4314125"))
