import string


# s= string, k = no. of shifts
def caesarCipher(s, k):
    if k > 26:
        k = k % 26
    lowercase_alphabets = list(string.ascii_lowercase)*2
    uppercase_alphabets = list(string.ascii_uppercase)*2

    cipher_string = []
    for letter in s:
        if letter in lowercase_alphabets:
            index = lowercase_alphabets.index(letter)
            cipher_index = index + k
            cipher_string.append(lowercase_alphabets[cipher_index])
        elif letter in uppercase_alphabets:
            index = uppercase_alphabets.index(letter)
            cipher_index = index + k
            cipher_string.append(uppercase_alphabets[cipher_index])
        else:
            cipher_string.append(letter)
    cipher_string = "".join(cipher_string)
    return cipher_string


s = "1X7T4VrCs23k4vv08D6yQ3S19G4rVP188M9ahuxB6j1tMG" \
    "Zs1m10ey7eUj62WV2exLT4C83zl7Q80M"
k = 27
print(caesarCipher(s, k))

