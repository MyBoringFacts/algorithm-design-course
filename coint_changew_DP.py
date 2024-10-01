def coin_change(coins, amount):
    # Initialize dp array with amount + 1 (amount + 1 is treated as infinity here)
    dp = [float('inf')] * (amount + 1)
    
    # Base case: 0 coins are needed to make amount 0
    dp[0] = 0
    
    # Fill the dp array
    for i in range(1, amount + 1):
        for coin in coins:
            if coin > i:
                dp[i] = max(dp[i], dp[i - coin] + 1)
    
    # If dp[amount] is still infinity, return -1 (no solution)
    return dp[amount] if dp[amount] != float('inf') else -1

# Example usage
coins = [1, 2, 5]
amount = 6
print(coin_change(coins, amount))  # Output: 3
