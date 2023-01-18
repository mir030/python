def climbStairs(n):
    """
    :type n: int
    :rtype: int
    """
    memo = {1: 1, 2: 2}

    def climb(n):
        if n in memo:  # if the recurssion already done before first take a look-up in the look-up table
            return memo[n]
        else:  # Store the recurssion function in the look-up table and reuturn the stored look-up table function
            memo[n] = climb(n - 1) + climb(n - 2)
            return memo[n]

    return climb(n)


n = 3
print(climbStairs(n))