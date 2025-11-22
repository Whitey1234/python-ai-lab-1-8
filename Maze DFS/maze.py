import json

with open('maze.json','r') as file:
    data = json.load(file)

Maze = data["Maze"]

def DFS_On_Maze(Graph, Path, vertices, root, target):
    visited = [0] * (vertices + 1)
    Stack = []

    Stack.append(root)
    visited[root] = 1

    while Stack:
        vertex = Stack.pop()

        for current in Graph[vertex]:
            if visited[current] != 1:
                Path[current] = vertex
                visited[current] = 1
                Stack.append(current)

            if current == target:
                return

Maze_Row = len(data['Maze'])
Maze_Column = len(data['Maze'][0])
Vertices = Maze_Row*Maze_Column

RED = "\033[91m"
GREEN = "\033[92m"
BRIGHT_BLUE = "\033[94m"
BRIGHT_YELLOW  = "\033[93m"
RESET = "\033[0m"

print('\nThe Maze\n')
for i in range(1, Maze_Row + 1):
    for j in range(1, Maze_Column + 1):
        cell = Maze[i - 1][j - 1]
        if cell == 'O':
            print(f'{GREEN}{cell}{RESET}   ', end="")
        elif cell == 'S' or cell == 'F':
            print(f'{BRIGHT_YELLOW}{cell}{RESET}   ', end="")
        elif cell == 'X':
            print(f'{RED}{cell}{RESET}   ', end="")
        else:
            print(f'{BRIGHT_BLUE}{cell}{RESET}   ', end="")
    print()

Graph = [[]for _ in range(Vertices+1)]

start = -1
finish = -1
current = 0

Matrix_Position = [(-1,-1)] * (Vertices+1)

for i in range(1,Maze_Row+1):
    for j in range(1,Maze_Column+1):
        current += 1
        Matrix_Position[current] = (i,j)

        bottom_vertex = current + Maze_Column
        right_vertex = current + 1

        if Maze[i - 1][j - 1] == 'X':
            continue
        elif Maze[i - 1][j - 1] == 'S':
            start = current
        elif Maze[i - 1][j - 1] == 'F':
            finish = current

        if i + 1 <= Maze_Row:
            if Maze[i][j - 1] != 'X':
                Graph[current].append(bottom_vertex)
                Graph[bottom_vertex].append(current)

        if j + 1 <= Maze_Column:
            if Maze[i - 1][j] != 'X':
                Graph[current].append(right_vertex)
                Graph[right_vertex].append(current)

Path = list(range(Vertices + 1))
DFS_On_Maze(Graph, Path, Vertices, start, finish)

Maze_Path = []
traverse = finish
Maze_Path.append(traverse)

while traverse != start:
    traverse = Path[traverse]
    Maze_Path.append(traverse)

for point in Maze_Path:
    if point == start or point == finish:
        continue

    value = Matrix_Position[point]
    i, j = value
    Maze[i - 1][j - 1] = 'O'

print('\nSolved Maze\n')

for i in range(1, Maze_Row + 1):
    for j in range(1, Maze_Column + 1):
        cell = Maze[i - 1][j - 1]
        if cell == 'O':
            print(f'{GREEN}{cell}{RESET}   ', end="")
        elif cell == 'S' or cell == 'F':
            print(f'{BRIGHT_YELLOW}{cell}{RESET}   ', end="")
        elif cell == 'X':
            print(f'{RED}{cell}{RESET}   ', end="")
        else:
            print(f'{BRIGHT_BLUE}{cell}{RESET}   ', end="")
    print()