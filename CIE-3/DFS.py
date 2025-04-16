class graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_edge(self, u, v):
        if u not in self.adjacency_list:
            self.adjacency_list[u].append(v)

    def dfs(self, start_vertex):
        visited = set()
        travsersal_order = []

        def dfs_recursive(vertex):
            if vertex not in visited:
                visited.add(vertex)
                travsersal_order.append(vertex)
                for neighbor in self.adjacency_list.get(vertex, []):
                    dfs_recursive(neighbor)

# Example usage
    g = graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)



    
