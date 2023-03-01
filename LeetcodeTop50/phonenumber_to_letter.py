def letterCombinations(digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    if not digits:
        return []
    mapper = {"2": ["a", "b", "c"], "3": ["d", "e", "f"], "4": ["g", "h", "i"],
              "5": ["j", "k", "l"], "6": ["m", "n", "o"], "7": ["p", "q", "r", "s"],
              "8": ["t", "u", "v"], "9": ["w", "x", "y", "z"]}
    result = mapper[digits[0]]
    i = 1
    while i < len(digits):
        result = [x+y for x in result for y in mapper[digits[i]]]
        i += 1
    return result

print(letterCombinations("233"))


