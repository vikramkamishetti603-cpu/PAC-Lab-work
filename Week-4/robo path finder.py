import heapq

# -----------------------------
# Node class for robot state
# -----------------------------
class Node:
    def __init__(self, position, parent=None):
        self.position = position    # (row, col)
        self.parent = parent        # parent node
        self.g = 0                  # cost from start
        self.h = 0                  # heuristic cost

    def __lt__(self, other):
        return (self.g + self.h) < (other.g + other.h)

    def __eq__(self, other):
        return self.position == other.position

    def __hash__(self):
        return hash(self.position)


# -----------------------------
# Manhattan Distance Heuristic
# -----------------------------
def heuristic(current, goal):
    return abs(current[0] - goal[0]) + abs(current[1] - goal[1])


# -----------------------------
# A* Robot Path Planning
# -----------------------------
def a_star_robot(grid, start, goal):
    open_list = []
    closed_set = set()

    start_node = Node(start)
    start_node.h = heuristic(start, goal)

    heapq.heappush(open_list, start_node)

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

    while open_list:
        current_node = heapq.heappop(open_list)

        # Goal reached
        if current_node.position == goal:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]

        closed_set.add(current_node)

        for move in moves:
            new_row = current_node.position[0] + move[0]
            new_col = current_node.position[1] + move[1]
            new_pos = (new_row, new_col)

            # Check boundaries
            if (0 <= new_row < len(grid) and
                0 <= new_col < len(grid[0]) and
                grid[new_row][new_col] == 0):

                new_node = Node(new_pos, current_node)
                new_node.g = current_node.g + 1
                new_node.h = heuristic(new_pos, goal)

                if new_node in closed_set:
                    continue

                heapq.heappush(open_list, new_node)

    return None


# -----------------------------
# Display Path on Grid
# -----------------------------
def print_grid_with_path(grid, path):
    grid_copy = [row[:] for row in grid]

    for r, c in path:
        grid_copy[r][c] = "*"

    for row in grid_copy:
        print(" ".join(str(x) for x in row))


# -----------------------------
# Main Function
# -----------------------------
def main():
    grid = [
        [0, 0, 0, 0],
        [1, 1, 0, 1],
        [0, 0, 0, 0]
        
    ]

    start = (1, 1)   # Robot start position
    goal = (2, 3)    # Goal position

    path = a_star_robot(grid, start, goal)

    if path:
        print("Robot Path Found:\n")
        print("Path:", path)
        print("\nGrid with path (*):")
        print_grid_with_path(grid, path)
    else:
        print("No path found!")


if __name__ == "__main__":
    main()
