def edit_distance_matrix(s1, s2):
    m = len(s1)
    n = len(s2)

    # Create matrix
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Initialize first row and column
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    # Fill matrix using DP logic
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            cost = 0 if s1[i - 1] == s2[j - 1] else 1

            dp[i][j] = min(
                dp[i - 1][j] + 1,       # Delete
                dp[i][j - 1] + 1,       # Insert
                dp[i - 1][j - 1] + cost # Substitute
            )
    return dp


def edit_distance(s1, s2):
    dp = edit_distance_matrix(s1, s2)
    return dp[-1][-1]


def print_matrix(word1, word2, matrix):
    print("\nMatrix:")
    print("     ", "  ".join(list("#" + word2)))
    for i, row in enumerate(matrix):
        label = "#" if i == 0 else word1[i - 1]
        print(label, row)

#PREDEFINED EXAMPLES
examples = {
    "write": "right",
    "delete": "replace",
    "yellow": "pillow"
}

print("\n--- Predefined Dictionary Edit Distances with Matrices ---")
for word1, word2 in examples.items():
    matrix = edit_distance_matrix(word1, word2)
    dist = edit_distance(word1, word2)

    print(f"\nWords: '{word1}' → '{word2}'")
    print(f"Edit Distance: {dist}")
    print_matrix(word1, word2, matrix)
