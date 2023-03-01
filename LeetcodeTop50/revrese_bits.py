def reverseBits(binary):
    bits_str = '{0:032b}'.format(binary)
    reversed_str = bits_str[::-1]
    output = int(reversed_str, 2)
    return output

print(reverseBits(0b00000010100101000001111010011100))