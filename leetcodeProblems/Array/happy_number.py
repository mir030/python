def isHappy(n):
    mem = set()
    while n != 1:
        sum = 0
        for i in str(n):
            sum += int(i) ** 2
        n = sum
        print(n)
        if n in mem:
            return False
        else:
            mem.add(n)
        print(mem)
    else:
        return True

print(isHappy(19))