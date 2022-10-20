s = [4, 1]
d = 4
m = 1


def birthday(s, d, m):
    count = 0
    for i in range(0, len(s)-m+1):
        sum = 0
        for _ in range(0, m):
            sum += s[i]
            i = i+1
        if sum == d:
            count += 1
    return count


result = birthday(s, d, m)