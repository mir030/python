def isPalindrome(s):
    s_parsed = []
    for i in range(len(s)):
        if s[i].isalnum():
            s_parsed.append(s[i])
    s_parsed_str = "".join(s_parsed)
    s_lower = s_parsed_str.lower()
    s_reverse = s_lower[::-1]

    if s_lower == s_reverse:
        return True
    return False


s = "A man, a plan, a canal: Panama"
s2 = "0P"
print(isPalindrome(s2))