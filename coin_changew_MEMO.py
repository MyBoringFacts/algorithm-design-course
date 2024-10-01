def coin_change_memoization(coins, amount):
    # Create a memo dictionary to store already computed results
    memo = {}

    def helper(rem):
        # Base case: if rem < 0, return infinity (no solution)
        if rem < 0:
            return float('inf')
        
        # If rem is 0, no coins are needed
        if rem == 0:
            return 0
        
        # If we already computed this subproblem, return the stored result
        if rem in memo:
            return memo[rem]

        # Initialize the result for this subproblem
        min_coins = float('inf')

        # Try using each coin and take the minimum
        for coin in coins:
            res = helper(rem - coin)
            if res != float('inf'):
                min_coins = min(min_coins, res + 1)

        # Store the result in the memo table
        memo[rem] = min_coins
        
        return memo[rem]

    # Call the helper function
    result = helper(amount)
    
    # If the result is infinity, return -1 (no solution)
    return result if result != float('inf') else -1

# Example usage
coins = [1, 2, 5]
amount = 11
print(coin_change_memoization(coins, amount))  # Output: 3
