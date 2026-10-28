def minimax(depth, node_index, maximizing_player, values, max_depth):
    # Base case: leaf node
    if depth == max_depth:
        return values[node_index]

    if maximizing_player:
        best = float('-inf')

        # Explore child nodes
        for i in range(2):
            val = minimax(depth + 1, node_index * 2 + i,
                          False, values, max_depth)
            best = max(best, val)

        return best

    else:
        best = float('inf')

        # Explore child nodes
        for i in range(2):
            val = minimax(depth + 1, node_index * 2 + i,
                          True, values, max_depth)
            best = min(best, val)

        return best


# Main program
values = list(map(int, input(
    "Enter the leaf node values separated by spaces: "
).split()))

max_depth = int(input("Enter the depth of the tree: "))

if len(values) != 2 ** max_depth:
    print("Error: Number of leaf values must be 2^depth.")
else:
    result = minimax(0, 0, True, values, max_depth)
    print("Optimal value:", result)



