def isValid(s):
    if len(s) % 2 != 0:
        return False
    stack = [0]
    mapping = {0: None, '(': ')', '[': ']', '{': '}'}
    for c in s:
        if c in mapping:
            stack.append(c)
        else:
            if mapping[stack.pop()] != c:
                return False
    return stack == [0]


print(isValid("()"))