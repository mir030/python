# Function to find the total number of ways to represent N
# as the sum of integers over the range [1, K]
def NumberOfWays(N, K):
    # Initialize a list
    dp = [0] * (N + 1)
    # Update dp[0] to 1
    dp[0] = 1

    # Iterate over the range [1, K + 1]
    for row in range(1, K + 1):
        # Iterate over the range [1, N + 1]
        for col in range(1, N + 1):
            # If col is greater than or equal to row
            if col >= row:
                # Update current dp[col] state
                dp[col] = dp[col] + dp[col - row]

    # Return the total number of ways
    return dp[N]


N = 5
K = 2

print(NumberOfWays(N, K))
