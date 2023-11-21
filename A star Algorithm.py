import heapq

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, name, heuristic):
        self.vertices[name] = (heuristic, {})

    def add_edge(self, from_vertex, to_vertex, weight):
        if from_vertex not in self.vertices:
            raise ValueError(f"Vertex {from_vertex} not found in the graph.")
        if to_vertex not in self.vertices:
            raise ValueError(f"Vertex {to_vertex} not found in the graph.")

        self.vertices[from_vertex][1][to_vertex] = weight

def astar(graph, start, goal):
    priority_queue = [(0, start)]
    visited = set()
    g_values = {vertex: float('inf') for vertex in graph.vertices}
    g_values[start] = 0

    while priority_queue:
        _, current_vertex = heapq.heappop(priority_queue)
        if current_vertex == goal:
            return g_values[goal]

        if current_vertex in visited:
            continue

        visited.add(current_vertex)
        for neighbor, weight in graph.vertices[current_vertex][1].items():
            tentative_g = g_values[current_vertex] + weight
            if tentative_g < g_values[neighbor]:
                g_values[neighbor] = tentative_g
                f_value = tentative_g + graph.vertices[neighbor][0]
                heapq.heappush(priority_queue, (f_value, neighbor))

    return float('inf')  # No path found

# Example usage:
# Create a graph and add vertices with heuristic values
g = Graph()
g.add_vertex('A', 5)
g.add_vertex('B', 3)
g.add_vertex('C', 2)
g.add_vertex('D', 7)
g.add_vertex('E', 8)

# Add edges between vertices with weights
g.add_edge('A', 'B', 4)
g.add_edge('A', 'C', 1)
g.add_edge('B', 'C', 2)
g.add_edge('B', 'D', 5)
g.add_edge('C', 'D', 8)
g.add_edge('C', 'E', 10)
g.add_edge('D', 'E', 2)

# Find the shortest path from 'A' to 'E' using A* algorithm
start_vertex = 'A'
goal_vertex = 'E'
shortest_path_cost = astar(g, start_vertex, goal_vertex)
print(f"Shortest path cost from {start_vertex} to {goal_vertex}: {shortest_path_cost}")
