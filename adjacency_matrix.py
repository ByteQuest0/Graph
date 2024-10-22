import numpy as np

class GraphMatrix:
    def __init__(self, num_nodes, directed=False, weighted=False):
        self.num_nodes = num_nodes
        self.directed = directed
        self.weighted = weighted
        if weighted:
            self.adj_matrix = np.full((num_nodes, num_nodes), '*', dtype=object)
        else:
            self.adj_matrix = np.zeros((num_nodes, num_nodes), dtype=int)

    def add_edge(self, node1, node2, weight=1):
        if self.weighted:
            if not isinstance(weight, (int, float)):
                raise ValueError("Weight must be a number.")
            self.adj_matrix[node1][node2] = weight
            if not self.directed:
                self.adj_matrix[node2][node1] = weight
        else:
            self.adj_matrix[node1][node2] = 1
            if not self.directed:
                self.adj_matrix[node2][node1] = 1

    def remove_edge(self, node1, node2):
        if self.weighted:
            self.adj_matrix[node1][node2] = '*'
            if not self.directed:
                self.adj_matrix[node2][node1] = '*'
        else:
            self.adj_matrix[node1][node2] = 0
            if not self.directed:
                self.adj_matrix[node2][node1] = 0

    def remove_vertex(self, vertex):
        # Create a new matrix with one less row and column
        new_size = self.num_nodes - 1
        if self.weighted:
            new_matrix = np.full((new_size, new_size), '*', dtype=object)
        else:
            new_matrix = np.zeros((new_size, new_size), dtype=int)

        # Copy data excluding the row and column of the vertex to be removed
        i_new = 0
        for i_old in range(self.num_nodes):
            if i_old == vertex:
                continue
            j_new = 0
            for j_old in range(self.num_nodes):
                if j_old == vertex:
                    continue
                new_matrix[i_new][j_new] = self.adj_matrix[i_old][j_old]
                j_new += 1
            i_new += 1

        # Update the adjacency matrix and the number of nodes
        self.adj_matrix = new_matrix
        self.num_nodes = new_size

    def display_matrix(self):
        print("Adjacency Matrix:")
        if self.weighted:
            for row in self.adj_matrix:
                print(' '.join(map(str, row)))
        else:
            print(self.adj_matrix)


# Example usage:
# Directed and weighted graph with 4 nodes
g = GraphMatrix(4, directed=True, weighted=True)

# Add edges
g.add_edge(0, 1, 3)
g.add_edge(0, 2, 2)
g.add_edge(1, 3, 4)

# Display adjacency matrix
g.display_matrix()

# Remove vertex (1)
g.remove_vertex(1)
print("\nAfter removing vertex (1):")
g.display_matrix()

# Undirected and unweighted graph with 4 nodes
g2 = GraphMatrix(4, directed=False, weighted=False)

# Add edges
g2.add_edge(0, 1)
g2.add_edge(0, 2)
g2.add_edge(1, 3)

# Display adjacency matrix
g2.display_matrix()

# Remove vertex (1)
g2.remove_vertex(1)
print("\nAfter removing vertex (1):")
g2.display_matrix()
