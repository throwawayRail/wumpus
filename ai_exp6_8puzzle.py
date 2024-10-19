import heapq

def manhattan_distance(board):
    distance = 0
    goal_positions = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 0: (2, 2)
    }

    for i in range(3):
        for j in range(3):
            num = board[i][j]
            if num != 0:
                goal_x, goal_y = goal_positions[num]
                distance += abs(i - goal_x) + abs(j - goal_y)
    
    return distance

def find_blank(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                return i, j
    return None

def is_goal(board):
    goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    return board == goal

def get_neighbors(board):
    neighbors = []
    x, y = find_blank(board)

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < 3 and 0 <= new_y < 3:
            new_board = [row[:] for row in board]
            new_board[x][y], new_board[new_x][new_y] = new_board[new_x][new_y], new_board[x][y]
            neighbors.append(new_board)
    
    return neighbors

def solve_8_puzzle(start_board):
    priority_queue = []
    heapq.heappush(priority_queue, (manhattan_distance(start_board), 0, start_board, None))
    visited = set()

    while priority_queue:
        heuristic, move_count, current_board, prev_board = heapq.heappop(priority_queue)

        if is_goal(current_board):
            return current_board, move_count
        
        visited.add(tuple(map(tuple, current_board)))

        for neighbor_board in get_neighbors(current_board):
            if tuple(map(tuple, neighbor_board)) not in visited:
                heapq.heappush(priority_queue, (
                    move_count + 1 + manhattan_distance(neighbor_board),
                    move_count + 1,
                    neighbor_board,
                    current_board
                ))
    
    return None, None

def print_solution(solution_board):
    for row in solution_board:
        print(" ".join(str(x) for x in row))
    print("\n")

# Starting board
start_board = [
    [1, 2, 3],
    [4, 0, 5],
    [7, 8, 6]
]

solution_board, move_count = solve_8_puzzle(start_board)

if solution_board:
    print(f"Solution found in {move_count} moves!")
    print_solution(solution_board)
else:
    print("No solution exists.")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# Sample Output
# Solution found in 2 moves!
# 1 2 3
# 4 5 6
# 7 8 0

