import heapq

# Goal state
GOAL = [[1,2,3],
        [4,5,6],
        [7,8,0]]

# Actions: left, right, up, down
MOVES = [(0,-1),(0,1),(-1,0),(1,0)]

# Check if a cell is within bounds
def is_valid(r, c):
    return 0 <= r < 3 and 0 <= c < 3

# Heuristic: number of tiles in correct position
def heuristic(state):
    count = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] == GOAL[i][j]:
                count += 1
    return count

# Print puzzle nicely
def print_puzzle(state):
    for row in state:
        print(" ".join(map(str,row)))
    print()

# Find position of 0 (empty space)
def find_zero(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return (i,j)

# Solve puzzle using priority queue (like A*)
def solve_puzzle(start):
    pq = []
    visited = set()
    backtrack = {}
    
    start_tuple = tuple(tuple(row) for row in start)
    heapq.heappush(pq, (-heuristic(start), start_tuple))
    backtrack[start_tuple] = None
    
    while pq:
        _, current = heapq.heappop(pq)
        
        if current == tuple(tuple(row) for row in GOAL):
            # Reconstruct path
            path = []
            while current:
                path.append([list(row) for row in current])
                current = backtrack[current]
            return path[::-1]
        
        visited.add(current)
        zero_r, zero_c = find_zero([list(row) for row in current])
        
        for dr, dc in MOVES:
            nr, nc = zero_r + dr, zero_c + dc
            if is_valid(nr, nc):
                next_state = [list(row) for row in current]
                next_state[zero_r][zero_c], next_state[nr][nc] = next_state[nr][nc], next_state[zero_r][zero_c]
                next_tuple = tuple(tuple(row) for row in next_state)
                if next_tuple not in visited:
                    heapq.heappush(pq, (-heuristic(next_state), next_tuple))
                    if next_tuple not in backtrack:
                        backtrack[next_tuple] = current

# Example start state
start_state = [
    [1,3,6],
    [4,2,0],
    [7,5,8]
]

solution = solve_puzzle(start_state)

for step in solution:
    print_puzzle(step)
