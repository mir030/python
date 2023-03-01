def countOnes(n):
    bit_to_str = '{0:032b}'.format(n)
    return bit_to_str.count("1")

print(countOnes(0b10110100))

def hammingWeight(n):
    result = 0
    while n:
        n = n & (n-1)
        result += 1
    return result

print(hammingWeight(0b11010001))