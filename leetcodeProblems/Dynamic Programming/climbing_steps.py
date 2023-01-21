def climbingSteps(n):
    mapping = {0: 0, 1: 1, 2: 2}
    i = 0
    def climb(n,):
        if n in mapping:
            return mapping[n]
        else:
            i += 1
            print(f"iteration number {i}")
            mapping[n] = climb(n-1) + climb(n-2)
            return mapping[n]

    return climb(n)


print(climbingSteps(10))