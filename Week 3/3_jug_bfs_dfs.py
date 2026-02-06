from collections import deque

# Goal state
goal_state = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 0]]

# Find blank tile position
def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

# Generate possible moves
def generate_neighbors(state):
    neighbors = []
    x, y = find_blank(state)
    moves = [(1,0), (-1,0), (0,1), (0,-1)]

    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(new_state)

    return neighbors
def bfs(start_state):
    queue = deque()
    visited = set()

    queue.append((start_state, []))
    visited.add(str(start_state))

    while queue:
        state, path = queue.popleft()

        if state == goal_state:
            return path + [state]

        for neighbor in generate_neighbors(state):
            if str(neighbor) not in visited:
                visited.add(str(neighbor))
                queue.append((neighbor, path + [state]))
    return None
def dfs(state, visited, path, depth, max_depth):
    if state == goal_state:
        return path + [state]

    if depth >= max_depth:
        return None

    visited.add(str(state))

    for neighbor in generate_neighbors(state):
        if str(neighbor) not in visited:
            result = dfs(neighbor, visited, path + [state], depth + 1, max_depth)
            if result:
                return result
    return None
start_state = [[1, 2, 3],
               [4, 0, 6],
               [7, 5, 8]]

print("BFS Solution:")
bfs_solution = bfs(start_state)
for step in bfs_solution:
    for row in step:
        print(row)
    print()

print("DFS Solution:")
dfs_solution = dfs(start_state, set(), [], 0, 20)
for step in dfs_solution:
    for row in step:
        print(row)
    print()

