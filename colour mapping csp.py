class MapColoring:
    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges
        self.colors = {}

    def is_safe(self, vertex, color):
        for neighbor in self.edges[vertex]:
            if self.colors.get(neighbor) == color:
                return False
        return True

    def color_map(self):
        for vertex in self.vertices:
            available_colors = set(["Red", "Green", "Blue", "Yellow"])  # Available colors for coloring
            for neighbor in self.edges[vertex]:
                if self.colors.get(neighbor) in available_colors:
                    available_colors.remove(self.colors[neighbor])

            if available_colors:
                self.colors[vertex] = available_colors.pop()

    def print_colors(self):
        for vertex, color in self.colors.items():
            print(f"{vertex} -> {color}")

# Example usage:
# Define vertices and edges
vertices = ["A", "B", "C", "D", "E"]
edges = {
    "A": ["B", "C", "D"],
    "B": ["A", "C"],
    "C": ["A", "B", "D", "E"],
    "D": ["A", "C", "E"],
    "E": ["C", "D"]
}

map_coloring = MapColoring(vertices, edges)
map_coloring.color_map()
map_coloring.print_colors()
