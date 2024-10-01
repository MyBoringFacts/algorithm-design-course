def knapsack_recursive(values, weights, W, n):
    # Base case: no items or capacity is 0
    if n == 0 or W == 0:
        return 0
    
    # If the current item's weight is more than the remaining capacity, skip it
    if weights[n - 1] > W:
        return knapsack_recursive(values, weights, W, n - 1)
    
    # Return the maximum of including or excluding the current item
    else:
        return max(
            knapsack_recursive(values, weights, W, n - 1),  # Exclude the item
            values[n - 1] + knapsack_recursive(values, weights, W - weights[n - 1], n - 1)  # Include the item
        )

# Example usage
values = [60, 100, 120]
weights = [10, 20, 30]
W = 500
n = len(values)
print(knapsack_recursive(values, weights, W, n))  # Output: 220
