def plusOne(digit):
    for i in range(len(digit) - 1, -1, -1):
        if digit[i] == 9:
            digit[i] = 0
        else:
            digit[i] += 1
            return digit

    digit.append(0)
    digit[0] = 1
    return digit


digits = [9]
print(plusOne(digits))

