def levenshtein_distance(str1, str2):
    # Get the length of the two strings
    len1, len2 = len(str1), len(str2)
    
    # Create a dp matrix initialized with zeros
    dp = [[0 for _ in range(len2 + 1)] for _ in range(len1 + 1)]
    
    # Initialize the base cases
    for i in range(len1 + 1):
        dp[i][0] = i  # Cost of converting to an empty string (all deletions)
    
    for j in range(len2 + 1):
        dp[0][j] = j  # Cost of converting from an empty string (all insertions)
    
    # Fill the dp matrix
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]  # No change needed
            else:
                dp[i][j] = min(
                    dp[i-1][j] + 1,    # Deletion
                    dp[i][j-1] + 1,    # Insertion
                    dp[i-1][j-1] + 1   # Substitution
                )
    
    return dp[len1][len2]

# Example Usage
str1 = "kitten"
str2 = "sitting"
print(levenshtein_distance(str1, str2))  # Output: 3
