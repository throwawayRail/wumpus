from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    
    visited.add(start)
    
    while queue:
        node = queue.popleft()
        print(node, end=" ")
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

def input_graph():
    graph = {}
    num_nodes = int(input("Enter the number of nodes: "))
    
    for _ in range(num_nodes):
        node = input("Enter the node: ")
        neighbors = input(f"Enter the neighbors of {node} separated by spaces: ").split()
        graph[node] = neighbors
    
    return graph

graph = input_graph()
start_node = input("Enter the starting node for BFS: ")
print("BFS Traversal starting from node", start_node, ":")
bfs(graph, start_node)































# Sample Output
# Enter the number of nodes: 6
# Enter the node: A 
# Enter the neighbors of A separated by spaces: B C 
# Enter the node: B 
# Enter the neighbors of B separated by spaces: A D E 
# Enter the node: C 
# Enter the neighbors of C separated by spaces: A F 
# Enter the node: D 
# Enter the neighbors of D separated by spaces: B 
# Enter the node: E 
# Enter the neighbors of E separated by spaces: B F 
# Enter the node: F 
# Enter the neighbors of F separated by spaces: C E 
# Enter the starting node for BFS: A 
# BFS Traversal starting from node A : 
# A B C D E F 


