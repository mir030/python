def reverseBits(n):
    bit_str = '{0:032b}'.format(n)
    reverser_str = bit_str[::-1]
    return int(reverser_str, 2)

print(reverseBits(0b00000010100101000001111010011100))