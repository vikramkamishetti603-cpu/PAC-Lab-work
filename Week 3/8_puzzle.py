# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
from collections import deque

# Goal state
goal_state = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 0]]

# Function to find position of 0 (blank tile)
def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

# Generate all possible moves
def generate_neighbors(state):
    neighbors = []
    x, y = find_blank(state)
    directions = [(1,0), (-1,0), (0,1), (0,-1)]  # down, up, right, left

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(new_state)

    return neighbors

# BFS algorithm
def bfs(start_state):
    queue = deque()
    visited = set()

    queue.append((start_state, []))
    visited.add(str(start_state))

    while queue:
        current_state, path = queue.popleft()

        if current_state == goal_state:
            return path + [current_state]

        for neighbor in generate_neighbors(current_state):
            if str(neighbor) not in visited:
                visited.add(str(neighbor))
                queue.append((neighbor, path + [current_state]))

    return None

# Initial state
start_state = [[1, 2, 3],
               [4, 5, 6],
               [7, 0, 8]]

# Solve the puzzle
solution = bfs(start_state)

# Print solution
if solution:
    print("Solution steps:")
    for step in solution:
        for row in step:
            print(row)
        print()
else:
    print("No solution found")

