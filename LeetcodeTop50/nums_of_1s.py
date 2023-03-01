def numOf1Bits(n):
    str = '{0:032b}'.format(n)
    return str.count("1")

print(numOf1Bits(0b00000000000000000000000000001011))