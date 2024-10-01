def levenshtein_memoization(str1, str2):
    # Create a memoization table
    memo = {}

    def edit_distance(i, j):
        # Base cases
        if i == 0:
            return j  # Need j insertions
        if j == 0:
            return i  # Need i deletions

        # Check if the result is already in the memo
        if (i, j) in memo:
            return memo[(i, j)]

        # If characters are the same, no operation is required
        if str1[i - 1] == str2[j - 1]:
            memo[(i, j)] = edit_distance(i - 1, j - 1)
        else:
            # Calculate the minimum of the three possible operations
            memo[(i, j)] = min(
                edit_distance(i - 1, j) + 1,    # Deletion
                edit_distance(i, j - 1) + 1,    # Insertion
                edit_distance(i - 1, j - 1) + 1 # Substitution
            )

        return memo[(i, j)]

    # Start the recursion from the full lengths of str1 and str2
    return edit_distance(len(str1), len(str2))

# Example usage
str1 = "kitten"
str2 = "sitting"
print(levenshtein_memoization(str1, str2))  # Output: 3
