GOAL = ((1, 2, 3), (4, 5, 6), (7, 8, 0))

def manhattan_distance(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                x, y = divmod(state[i][j] - 1, 3)
                distance += abs(x - i) + abs(y - j)
    return distance

def get_neighbors(state):
    neighbors = []
    zero_row, zero_col = next((i, j) for i, row in enumerate(state) for j, val in enumerate(row) if val == 0)
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for move in moves:
        new_row, new_col = zero_row + move[0], zero_col + move[1]
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_state = [list(row) for row in state]
            new_state[zero_row][zero_col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[zero_row][zero_col]
            neighbors.append(tuple(tuple(row) for row in new_state))
    
    return neighbors

def ida_star(initial_state):
    def search(path, g, threshold):
        node = path[-1]
        f = g + manhattan_distance(node)
        if f > threshold:
            return f
        if node == GOAL:
            return True
        
        min_cost = float('inf')
        for neighbor in get_neighbors(node):
            if neighbor not in path:
                path.append(neighbor)
                t = search(path, g + 1, threshold)
                if t == True:
                    return True
                if t < min_cost:
                    min_cost = t
                path.pop()
        
        return min_cost

    threshold = manhattan_distance(initial_state)
    path = [initial_state]
    while True:
        t = search(path, 0, threshold)
        if t == True:
            return len(path) - 1
        if t == float('inf'):
            return -1
        threshold = t

# Read input
initial_state = tuple(tuple(map(int, input().split())) for _ in range(3))

# Solve the puzzle and print the result
print(ida_star(initial_state))