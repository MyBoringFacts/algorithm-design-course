# Step 1: Read the maze and input values
def read_maze():
    M, N = map(int, input().split())  # Dimensions of the maze
    entrance = tuple(map(int, input().split()))  # Entrance position (r, c)
    exit_pos = tuple(map(int, input().split()))  # Exit position (R, C)
    
    # Create the maze as a 2D list
    maze = [list(map(int, input().split())) for _ in range(M)]
    
    return M, N, entrance, exit_pos, maze

# Step 2: Valid function to check if a position is a valid move
def valid(y, x, M, N, maze):
    # Check if the position is within bounds and is a runnable ground (value 0)
    return 0 <= y < M and 0 <= x < N and maze[y][x] == 0

# Step 3: Define the state class
class State:
    def __init__(self, y, x, step):
        self.y = y  # Row position
        self.x = x  # Column position
        self.step = step  # Number of steps taken to reach this position

# Step 4: BFS algorithm to find the shortest path without deque
def bfs(M, N, entrance, exit_pos, maze):
    # Initialize BFS queue using a list
    queue = [State(entrance[0], entrance[1], 0)]
    
    # Set of visited positions to avoid re-processing
    visited = set()
    visited.add((entrance[0], entrance[1]))
    
    # Directions for movement: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while queue:
        current_state = queue.pop(0)  # Use pop(0) to simulate a queue (FIFO)
        
        # If we reached the exit, return the step count
        if (current_state.y, current_state.x) == exit_pos:
            return current_state.step
        
        # Expand to neighboring positions
        for dy, dx in directions:
            new_y, new_x = current_state.y + dy, current_state.x + dx
            
            if valid(new_y, new_x, M, N, maze) and (new_y, new_x) not in visited:
                visited.add((new_y, new_x))
                queue.append(State(new_y, new_x, current_state.step + 1))
    
    # If there's no valid path, return -1 (or any indicator of failure)
    return -1

# Main function to tie everything together
def main():
    M, N, entrance, exit_pos, maze = read_maze()
    shortest_path_length = bfs(M, N, entrance, exit_pos, maze)
    print(shortest_path_length)

if __name__ == "__main__":
    main()
