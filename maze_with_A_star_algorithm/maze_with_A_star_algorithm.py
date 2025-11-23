import json
import time
import os
from queue import Queue, PriorityQueue

# Colors for terminal output (works in most terminals)
RED = "\033[91m"
GREEN = "\033[92m"
BRIGHT_BLUE = "\033[94m"
BRIGHT_YELLOW  = "\033[93m"
RESET = "\033[0m"


def find_position(maze, target):
    """Find (row, col) of target character (e.g. 'S' or 'F') in the maze."""
    index = (-1, -1)
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == target:
                index = (i, j)
                break
    return index


def check_overflow(maze, row, column):
    """Check if (row, column) is inside the maze bounds."""
    result = False
    if row >= 0 and row < len(maze) and column >= 0 and column < len(maze[0]):
        result = True
    return result


def possible_path(maze, row, column):
    """Return all valid neighbor cells (up, down, left, right)."""
    path = []
    moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    for point in moves:
        new_row = row + point[0]
        new_column = column + point[1]
        if check_overflow(maze, new_row, new_column):
            path.append((new_row, new_column))
    return path


def print_maze(maze):
    """Pretty-print the maze with colors."""
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            cell = maze[i][j]
            if cell == 'X':
                print(f'{RED}{cell:>4}{RESET}', end="")
            elif cell == 'S' or cell == 'F':
                print(f'{BRIGHT_YELLOW}{cell:>4}{RESET}', end="")
            elif cell == '.':
                print(f'{BRIGHT_BLUE}{cell:>4}{RESET}', end="")
            else:
                print(f'{GREEN}{cell:>4}{RESET}', end="")
        print()
    print()


def set_distance(maze, target):
    """
    BFS distance from target (S or F) to all reachable cells.
    Walls 'X' are treated as blocked.
    """
    zero = [0] * len(maze[0])
    distance = [zero[:] for _ in range(len(maze))]

    position = find_position(maze, target)
    QUEUE = Queue()
    QUEUE.put(position)

    while not QUEUE.empty():
        current = QUEUE.get()
        row = current[0]
        column = current[1]
        current_distance = distance[row][column]

        if row == position[0] and column == position[1]:
            current_distance = 0
            distance[row][column] = -1  # mark source specially

        path = possible_path(maze, row, column)
        for point in path:
            new_row = point[0]
            new_column = point[1]

            # skip walls
            if maze[new_row][new_column] == 'X':
                continue

            if distance[new_row][new_column] == 0:
                distance[new_row][new_column] = current_distance + 1
                QUEUE.put((new_row, new_column))

    return distance


def A_Star(maze, dist_start, dist_finish):
    """A*–like search using precomputed distances from start and finish."""
    start = find_position(maze, "S")
    finish = find_position(maze, "F")

    QUEUE = PriorityQueue()
    QUEUE.put((0, (start[0], start[1])))

    zero = [0] * len(maze[0])
    visited = [zero[:] for _ in range(len(maze))]
    visited[start[0]][start[1]] = 1

    while not QUEUE.empty():
        current = QUEUE.get()
        row = current[1][0]
        column = current[1][1]

        if maze[row][column] == "F":
            print(f'{RED}{"Reached The Finish Point\n"}{RESET}')
            break

        # Avoid overwriting the start cell with a number (priority 0 is the start)
        if current[0] != 0 and maze[row][column] not in ("S", "F"):
            maze[row][column] = str(dist_start[row][column] + dist_finish[row][column])

            # Clear screen (Windows='cls', Linux/Mac='clear')
            os.system("cls" if os.name == "nt" else "clear")
            print("Maze:")
            print_maze(maze)

            print("Distance From Start:")
            print_maze(dist_start)

            print("Distance From Finish:")
            print_maze(dist_finish)

            time.sleep(0.3)

        path = possible_path(maze, row, column)
        for point in path:
            new_row = point[0]
            new_column = point[1]

            if visited[new_row][new_column] != 1:
                visited[new_row][new_column] = 1
                new_distance = dist_start[new_row][new_column] + dist_finish[new_row][new_column]
                if maze[new_row][new_column] != "X":
                    QUEUE.put((new_distance, (new_row, new_column)))


# --------- MAIN EXECUTION ---------
if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(script_dir, 'maze.json')
    try:
        with open(json_path, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        print(f"Error: 'maze.json' not found at expected path: {json_path}")
        print(f"Current working directory: {os.getcwd()}")
        print("Place 'maze.json' next to this script or run the script from its directory.")
        raise

    Maze = data["Maze"]

    Distance_From_Finish = set_distance(Maze, "F")
    Distance_From_Start = set_distance(Maze, "S")

    print("Initial Maze:")
    print_maze(Maze)
    time.sleep(2)

    A_Star(Maze, Distance_From_Start, Distance_From_Finish)
