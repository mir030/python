def validPalindrome(s):
    new_str = ""
    for char in s:
        if char.isalnum():
            new_str += char.lower()
    if new_str == new_str[::-1]:
        return True
    return False

s = "A man, a plan, a canal: Panama"
s2 = "race a car"
print(validPalindrome(" "))