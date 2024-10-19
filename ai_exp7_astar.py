import heapq

class Node:
    def __init__(self, position, g=0, h=0, f=0, parent=None):
        self.position = position
        self.g = g
        self.h = h
        self.f = f
        self.parent = parent

    def __lt__(self, other):
        return self.f < other.f

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star_search(grid, start, goal):
    open_list = []
    closed_set = set()
    
    start_node = Node(start, g=0, h=heuristic(start, goal))
    start_node.f = start_node.g + start_node.h
    heapq.heappush(open_list, start_node)
    
    while open_list:
        current_node = heapq.heappop(open_list)
        
        if current_node.position == goal:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]
        
        closed_set.add(current_node.position)
        
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor_pos = (current_node.position[0] + dx, current_node.position[1] + dy)
            
            if (0 <= neighbor_pos[0] < len(grid) and 0 <= neighbor_pos[1] < len(grid[0])
                and grid[neighbor_pos[0]][neighbor_pos[1]] == 0 and neighbor_pos not in closed_set):
                
                neighbor_g = current_node.g + 1
                neighbor_h = heuristic(neighbor_pos, goal)
                neighbor_f = neighbor_g + neighbor_h
                
                neighbor_node = Node(neighbor_pos, g=neighbor_g, h=neighbor_h, f=neighbor_f, parent=current_node)
                
                if any(neighbor_node.position == node.position and neighbor_node.f >= node.f for node in open_list):
                    continue
                
                heapq.heappush(open_list, neighbor_node)
    
    return None

grid = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)
goal = (4, 4)

path = a_star_search(grid, start, goal)
print("Path found:", path)




















# Sample Output
# Path found: [(0, 0), (1, 0), (2, 0), (2, 1),
# (2, 2), (3, 2), (4, 2), (4, 3), (4, 4)]