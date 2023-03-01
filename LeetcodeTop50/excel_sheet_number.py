def excelSheetNumber(column_title):
    key = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    value = [i for i in range(1, 27)]
    mapping = dict(zip(key, value))
    output = 0
    for i, char in enumerate(reversed(column_title)):
        output += mapping[char] * 26 ** i

    return output

print(excelSheetNumber("FXSHRXW"))