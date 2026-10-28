def get_user_inputs():
    # Take heuristic values
    heuristic = {}

    num_nodes = int(input("Enter the total number of nodes: "))

    print("\nEnter heuristic value h(n) for each node:")

    for _ in range(num_nodes):
        node = input("Node name: ").strip().upper()
        h_val = float(input(f"Heuristic h({node}): "))
        heuristic[node] = h_val

    # Take graph edges
    graph = {node: [] for node in heuristic}

    num_edges = int(input("\nEnter total number of directed edges: "))

    print("\nEnter edges in format: from_node to_node weight")

    for i in range(num_edges):
        u, v, w = input(f"Edge {i + 1}: ").strip().split()
        u, v = u.upper(), v.upper()
        weight = float(w)

        if u not in graph or v not in graph:
            print("Error: Both nodes must have heuristic values.")
            return None, None

        graph[u].append((v, weight))

    return graph, heuristic


def astar(graph, heuristic, start, goal):
    open_list = [(start, 0)]
    came_from = {}
    g_cost = {start: 0}
    closed_list = set()

    while open_list:
        # Select node with minimum f(n) = g(n) + h(n)
        current = min(
            open_list,
            key=lambda x: x[1] + heuristic[x[0]]
        )

        open_list.remove(current)
        current_node = current[0]

        if current_node in closed_list:
            continue

        # Goal check and path reconstruction
        if current_node == goal:
            path = [goal]

            while current_node in came_from:
                current_node = came_from[current_node]
                path.append(current_node)

            path.reverse()
            return path, g_cost[goal]

        closed_list.add(current_node)

        # Explore neighbors
        for neighbor, cost in graph.get(current_node, []):
            new_cost = g_cost[current_node] + cost

            if new_cost < g_cost.get(neighbor, float('inf')):
                g_cost[neighbor] = new_cost
                came_from[neighbor] = current_node

                if neighbor in closed_list:
                    closed_list.remove(neighbor)

                open_list.append((neighbor, new_cost))

    return None, float('inf')


# Main program
graph, heuristic = get_user_inputs()

if graph is not None:
    start = input("\nEnter the starting node: ").strip().upper()
    goal = input("Enter the goal node: ").strip().upper()

    if start in graph and goal in graph:
        path, cost = astar(graph, heuristic, start, goal)

        if path:
            print("\nShortest path:", " -> ".join(path))
            print("Total path cost:", cost)
        else:
            print("\nNo path found.")
    else:
        print("Starting node or goal node not found")




