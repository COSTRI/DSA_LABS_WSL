#1815522

# Graph Implementation using Adjacency List
class Graph:
    def __init__(self):
        # Initialize an empty graph
        self.graph = {}
    
    def add_edge(self, u, v):
        # Add an edge from vertex u to vertex v
        if u not in self.graph:
            self.graph[u] = []  # Create a new list for the new vertex u
        if v not in self.graph:
            self.graph[v] = []  # Create a new list for the new vertex v
        self.graph[u].append(v)  # Add vertex v to the adjacency list of u
        self.graph[v].append(u)  # Add vertex u to the adjacency list of v (for undirected graph)
    
    def get_edges(self):
        # Return the edges of the graph
        return self.graph


# BFS Implementation to find the shortest path in an unweighted graph
def bfs_shortest_path(graph, start, goal):
    # Initialize a queue for BFS, starting with the start vertex and its path
    queue = [(start, [start])]  # Queue contains tuples of (current_vertex, path_to_vertex)
    
    # Set to keep track of visited vertices
    visited = set()  
    
    while queue:
        # Dequeue an element from the front of the queue
        current_vertex, path = queue.pop(0)
        
        # Check if the current vertex is the goal
        if current_vertex == goal:
            return path  # Return the path if the goal is reached
        
        # Mark the current vertex as visited
        visited.add(current_vertex)  

        # Iterate over all adjacent vertices of the current vertex
        for neighbor in graph.graph.get(current_vertex, []):
            if neighbor not in visited:
                # Add the neighbor to the queue with the updated path
                queue.append((neighbor, path + [neighbor]))  

    return None  # Return None if no path is found


# Example Usage
if __name__ == "__main__":
    # Create a graph
    g = Graph()
    g.add_edge('A', 'B')
    g.add_edge('A', 'C')
    g.add_edge('B', 'D')
    g.add_edge('C', 'D')
    g.add_edge('D', 'E')
    
    # Find the shortest path from A to E using BFS
    start_vertex = 'A'
    goal_vertex = 'E'
    shortest_path = bfs_shortest_path(g, start_vertex, goal_vertex)
    
    # Output the shortest path found
    if shortest_path:
        print(f"Shortest path from {start_vertex} to {goal_vertex}: {shortest_path}")
    else:
        print(f"No path found from {start_vertex} to {goal_vertex}.")