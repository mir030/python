def happyNumber(n):
    mapping = []

    while n != 1:
        sum = 0
        for digit in str(n):
            sum += int(digit) ** 2
        n = sum
        if n in mapping:
            return False
        else:
            mapping.append(n)
    return True

print(happyNumber(19))