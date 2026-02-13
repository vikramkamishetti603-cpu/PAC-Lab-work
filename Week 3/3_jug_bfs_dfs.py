from collections import deque

# Jug capacities
JUG_A = 8
JUG_B = 5
JUG_C = 3
GOAL = 4

# Generate all possible next states
def get_neighbors(state):
    a, b, c = state
    neighbors = []

    # Fill jugs
    neighbors.append((JUG_A, b, c))
    neighbors.append((a, JUG_B, c))
    neighbors.append((a, b, JUG_C))

    # Empty jugs
    neighbors.append((0, b, c))
    neighbors.append((a, 0, c))
    neighbors.append((a, b, 0))

    # Pour operations
    def pour(x, y, cap_y):
        t = min(x, cap_y - y)
        return x - t, y + t

    # A -> B, A -> C
    na, nb = pour(a, b, JUG_B)
    neighbors.append((na, nb, c))
    na, nc = pour(a, c, JUG_C)
    neighbors.append((na, b, nc))

    # B -> A, B -> C
    nb, na = pour(b, a, JUG_A)
    neighbors.append((na, nb, c))
    nb, nc = pour(b, c, JUG_C)
    neighbors.append((a, nb, nc))

    # C -> A, C -> B
    nc, na = pour(c, a, JUG_A)
    neighbors.append((na, b, nc))
    nc, nb = pour(c, b, JUG_B)
    neighbors.append((a, nb, nc))

    return neighbors


# Goal test
def is_goal(state):
    return GOAL in state


# ---------------- BFS ----------------
def bfs():
    start = (0, 0, 0)
    queue = deque([(start, [])])
    visited = set()

    while queue:
        current, path = queue.popleft()

        if current in visited:
            continue

        visited.add(current)
        path = path + [current]

        if is_goal(current):
            return path

        for neighbor in get_neighbors(current):
            if neighbor not in visited:
                queue.append((neighbor, path))

    return None


# ---------------- DFS ----------------
def dfs():
    start = (0, 0, 0)
    stack = [(start, [])]
    visited = set()

    while stack:
        current, path = stack.pop()

        if current in visited:
            continue

        visited.add(current)
        path = path + [current]

        if is_goal(current):
            return path

        for neighbor in get_neighbors(current):
            if neighbor not in visited:
                stack.append((neighbor, path))

    return None


# Run both algorithms
bfs_solution = bfs()
dfs_solution = dfs()

print("BFS Solution Path:")
for step in bfs_solution:
    print(step)

print("\nDFS Solution Path:")
for step in dfs_solution:
    print(step)
