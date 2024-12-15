from collections import deque


def shortest_path(maze, start, exit):
    rows, cols = len(maze), len(maze[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
    queue = deque([start])
    visited = set([start])
    parent = {start: None}  # To reconstruct the path

    # Perform BFS
    while queue:
        current = queue.popleft()

        if current == exit:  # Found the exit
            path = []
            while current is not None:  # Backtrack using the parent map
                path.append(current)
                current = parent[current]
            return path[::-1]  # Reverse to get the path from start to exit

        # Explore neighbors
        for direction in directions:
            r, c = current[0] + direction[0], current[1] + direction[1]

            if 0 <= r < rows and 0 <= c < cols and maze[r][c] == 0 and (r, c) not in visited:
                queue.append((r, c))
                visited.add((r, c))
                parent[(r, c)] = current  # Track the parent node

    return None  # No path found


# Input 1
maze1 = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0]
]
start1, exit1 = (0, 0), (4, 4)
print(shortest_path(maze1, start1, exit1))

# Input 2
maze2 = [
    [0, 1, 0, 0, 0, 1, 0],
    [0, 1, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 1, 0]
]
start2, exit2 = (0, 0), (0, 6)
print(shortest_path(maze2, start2, exit2))