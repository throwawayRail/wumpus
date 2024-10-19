def dfs(graph, start, goal, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []

    visited.add(start)
    path.append(start)
    print(start, end=' ')
    
    if start == goal:
        return True, path

    for neighbor in graph[start]:
        if neighbor not in visited:
            found, path = dfs(graph, neighbor, goal, visited, path)
            if found:
                return True, path

    path.pop()
    return False, path

def input_graph():
    graph = {}
    num_nodes = int(input("Enter the number of nodes: "))

    for _ in range(num_nodes):
        node = input("Enter the node: ")
        neighbors = input(f"Enter the neighbors of {node} separated by spaces:").split()
        graph[node] = neighbors

    return graph

graph = input_graph()
start_node = input("Enter the starting node for DFS: ")
goal_node = input("Enter the goal node to search for: ")
print("DFS Traversal starting from node", start_node + ":")
found, path = dfs(graph, start_node, goal_node)
if found:
    print(f"\nGoal node '{goal_node}' is reachable from node '{start_node}'.")
    print("Path:", ' -> '.join(path))
else:
    print(f"\nGoal node '{goal_node}' is not reachable from node '{start_node}'.")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    



# Sample Output

# Enter the number of nodes: 4
# Enter the node: A
# Enter the neighbors of A separated by spaces:B C
# Enter the node: B
# Enter the neighbors of B separated by spaces:D A
# Enter the node: C
# Enter the neighbors of C separated by spaces:D B
# Enter the node: D
# Enter the neighbors of D separated by spaces:A
# Enter the starting node for DFS: A
# Enter the goal node to search for: D
# DFS Traversal starting from node A:
# A B D
# Goal node 'D' is reachable from node 'A'.
# Path: A -> B -> D