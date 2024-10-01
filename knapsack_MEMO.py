def knapsack_dp(values, weights, W):
    n = len(values)
    # Create dp table with dimensions (n+1) x (W+1)
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    # Fill dp table
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            # Exclude the item
            dp[i][w] = dp[i - 1][w]
            
            # Include the item if its weight is less than or equal to capacity
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i][w], values[i - 1] + dp[i - 1][w - weights[i - 1]])

    return dp[n][W]

# Example usage
values = [60, 100, 120]
weights = [10, 20, 30]
W = 50
print(knapsack_dp(values, weights, W))  # Output: 220
