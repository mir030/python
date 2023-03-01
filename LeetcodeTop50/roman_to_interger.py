def romanToInteger(s):
    dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    integer = dic[s[-1]]
    for i in range(len(s)-1):
        if dic[s[i]] < dic[s[i+1]]:
            integer -= dic[s[i]]
        else:
            integer += dic[s[i]]
    return integer

s = "MCMXCIV"
print(romanToInteger(s))