class Graph:
    def __init__(self, directed=False, weighted=False):
        # Initialize an empty dictionary to store the adjacency list
        # directed=False means the graph is undirected by default
        # weighted=False means the graph is unweighted by default
        self.adj_list = {}
        self.directed = directed
        self.weighted = weighted

    # Add a vertex to the graph
    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []
        else:
            print(f"Vertex {vertex} already exists.")

    # Add an edge between two vertices (u, v) with an optional weight
    def add_edge(self, u, v, weight=1):
        if u not in self.adj_list:
            self.add_vertex(u)
        if v not in self.adj_list:
            self.add_vertex(v)

        # If the graph is weighted, store the edge as (vertex, weight)
        if self.weighted:
            self.adj_list[u].append((v, weight))
            if not self.directed:
                self.adj_list[v].append((u, weight))
        else:
            # If the graph is unweighted, store only the vertex
            self.adj_list[u].append(v)
            if not self.directed:
                self.adj_list[v].append(u)

    # Remove an edge between two vertices (u, v)
    def remove_edge(self, u, v):
        # Remove v from u's adjacency list
        if u in self.adj_list:
            if self.weighted:
                self.adj_list[u] = [adj for adj in self.adj_list[u] if adj[0] != v]
            else:
                self.adj_list[u].remove(v)

        # For undirected graphs, remove u from v's adjacency list
        if not self.directed and v in self.adj_list:
            if self.weighted:
                self.adj_list[v] = [adj for adj in self.adj_list[v] if adj[0] != u]
            else:
                self.adj_list[v].remove(u)

    # Remove a vertex and all its connected edges
    def remove_vertex(self, vertex):
        if vertex in self.adj_list:
            # Remove all edges to this vertex from other vertices' lists
            for adjacent in list(self.adj_list[vertex]):
                # Check if the graph is weighted and remove accordingly
                if self.weighted:
                    adj_vertex = adjacent[0]  # Extract vertex from tuple (vertex, weight)
                else:
                    adj_vertex = adjacent

                # For directed graphs, just remove edges pointing to this vertex
                if self.directed:
                    self.adj_list[adj_vertex] = [
                        adj for adj in self.adj_list[adj_vertex]
                        if (adj[0] if self.weighted else adj) != vertex
                    ]
                else:
                    # For undirected graphs, remove both directions
                    self.remove_edge(adj_vertex, vertex)

            # Remove the vertex itself
            del self.adj_list[vertex]
        else:
            print(f"Vertex {vertex} does not exist.")

    # Print the adjacency list representation of the graph
    def print_graph(self):
        for vertex, edges in self.adj_list.items():
            if self.weighted:
                formatted_edges = ', '.join([f"{v} (weight {w})" for v, w in edges])
            else:
                formatted_edges = ', '.join([str(v) for v in edges])
            print(f"{vertex} -> {formatted_edges}")


# Example usage:
g = Graph(directed=True, weighted=True)  # Set directed=True for directed graph, weighted=True for weighted graph

# Add vertices
g.add_vertex('A')
g.add_vertex('B')
g.add_vertex('C')
g.add_vertex('D')

# Add edges (with weights for weighted graph)
g.add_edge('A', 'B', 2)
g.add_edge('A', 'C', 3)
g.add_edge('B', 'D', 4)
g.add_edge('C', 'D', 5)

# Print the graph
print("Graph (Directed, Weighted):")
g.print_graph()

# Remove an edge
g.remove_edge('A', 'B')
print("\nGraph after removing edge A-B:")
g.print_graph()

# Remove a vertex
g.remove_vertex('D')
print("\nGraph after removing vertex D:")
g.print_graph()

# Example for Unweighted Graph:
g_unweighted = Graph(directed=False, weighted=False)  # Unweighted and undirected graph

# Add edges (no weights)
g_unweighted.add_edge('A', 'B')
g_unweighted.add_edge('A', 'C')
g_unweighted.add_edge('B', 'D')
g_unweighted.add_edge('C', 'D')

# Print the unweighted graph
print("\nGraph (Undirected, Unweighted):")
g_unweighted.print_graph()
