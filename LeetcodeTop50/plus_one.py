def plusOne(digits):
    s = ""
    for x in digits:
        s += str(x)
    plus_one = int(s) + 1
    result = []
    for ch in str(plus_one):
        result.append(int(ch))

    return result
digits = [1, 9, 9]
print(plusOne(digits))

def plusOnev2(digits):
    for i in range(len(digits)-1, -1, -1):
        if digits[i] == 9:
            digits[i] = 1
        else:
            digits[i] += 1
            return digits

    digits.append(0)
    digits[0] = 1
    return digits

print(plusOnev2(digits))
