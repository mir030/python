def strStr(haystack, needle):
    if needle == haystack:
        return 0
    if needle in haystack:
        for i in range(0, len(haystack) - len(needle) + 1):
            if needle == haystack[i:i+len(needle)]:
                return i
    return -1


haystack = "mississipi"
needle = "issip"

index = strStr(haystack, needle)

print(index)
