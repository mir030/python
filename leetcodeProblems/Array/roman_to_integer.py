def romanToInt(s):
    roman = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10,
             'V': 5, 'I': 1}
    z = 0
    for i in range(0, len(s) - 1):
        print(s[i], s[i + 1])
        if roman[s[i]] < roman[s[i + 1]]:
            # brain fart - what would happen for a case like "IV"
            # The first value would be negative but that's okay
            # since the next value will add to it ad become positive
            z -= roman[s[i]]
        else:
            z += roman[s[i]]
    return z + roman[s[-1]]


print(romanToInt("III"))
print(romanToInt("LVIII"))
print(romanToInt("MCMXCIV"))
