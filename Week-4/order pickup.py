import heapq

# -----------------------------
# Node class
# -----------------------------
class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.g = 0
        self.h = 0

    def __lt__(self, other):
        return (self.g + self.h) < (other.g + other.h)

    def __eq__(self, other):
        return self.position == other.position

    def __hash__(self):
        return hash(self.position)


# -----------------------------
# Manhattan Heuristic
# -----------------------------
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


# -----------------------------
# A* Search
# -----------------------------
def a_star(grid, start, goal):
    open_list = []
    closed_set = set()

    start_node = Node(start)
    start_node.h = heuristic(start, goal)
    heapq.heappush(open_list, start_node)

    moves = [(-1,0),(1,0),(0,-1),(0,1)]

    while open_list:
        current = heapq.heappop(open_list)

        if current.position == goal:
            path = []
            while current:
                path.append(current.position)
                current = current.parent
            return path[::-1]

        closed_set.add(current)

        for move in moves:
            r = current.position[0] + move[0]
            c = current.position[1] + move[1]

            if (0 <= r < len(grid) and
                0 <= c < len(grid[0]) and
                grid[r][c] != 1):

                child = Node((r, c), current)
                child.g = current.g + 1
                child.h = heuristic(child.position, goal)

                if child in closed_set:
                    continue

                heapq.heappush(open_list, child)

    return None


# -----------------------------
# Order Picking Logic
# -----------------------------
def order_picking(grid, start, pick_locations, goal):
    current_pos = start
    full_path = []

    remaining_picks = pick_locations[:]

    while remaining_picks:
        # Pick nearest order
        nearest = min(remaining_picks,
                      key=lambda p: heuristic(current_pos, p))

        path = a_star(grid, current_pos, nearest)
        full_path.extend(path[:-1])

        current_pos = nearest
        remaining_picks.remove(nearest)

    # Go to final goal
    path = a_star(grid, current_pos, goal)
    full_path.extend(path)

    return full_path


# -----------------------------
# Display Grid
# -----------------------------
def print_grid(grid, path, start, picks, goal):
    display = [row[:] for row in grid]

    for r, c in path:
        display[r][c] = "*"

    sr, sc = start
    display[sr][sc] = "S"

    for p in picks:
        display[p[0]][p[1]] = "P"

    gr, gc = goal
    display[gr][gc] = "G"

    for row in display:
        print(" ".join(str(x) for x in row))


# -----------------------------
# Main
# -----------------------------
def main():
    grid = [
        [0, 0, 0, 0, 0],
        [1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 0, 1],
        [0, 0, 0, 0, 0]
    ]

    start = (0, 0)
    pick_locations = [(2, 2), (4, 1)]
    goal = (4, 4)

    path = order_picking(grid, start, pick_locations, goal)

    print("Order Picking Path:\n", path)
    print("\nWarehouse Layout:")
    print_grid(grid, path, start, pick_locations, goal)


if __name__ == "__main__":
    main()
