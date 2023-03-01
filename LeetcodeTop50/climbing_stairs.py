def climbing_stairs(n):
    mapping = {0: 0, 1: 1, 2: 2}

    def climb(n):
        if n in mapping:
            return mapping[n]
        else:
            mapping[n] = climb(n - 1) + climb(n - 2)
            return mapping[n]

    return climb(n)


print(climbing_stairs(5))
