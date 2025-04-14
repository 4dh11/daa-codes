import math
def bellman_ford(nodes, edges, source_index=0):
    # Initialize distances with infinity
    path_length = {v: float('inf') for v in nodes}
    path_length[source_index] = 0

    # Initialize paths
    path = {v: [] for v in nodes}
    path[source_index] = [source_index]

    # Relax all edges |V|-1 times
    for _ in range(len(nodes) - 1):
        for (u, v), weight in edges.items():
            if path_length[u] + weight < path_length[v]:
                path_length[v] = path_length[u] + weight
                path[v] = path[u] + [v]

    # Check for negative-weight cycles
    for (u, v), weight in edges.items():
        if path_length[u] != math.inf and path_length[u] + weight < path_length[v]:
            raise ValueError("Graph contains a negative-weight cycle")

    return path_length, path

if __name__ == "__main__":
    nodes = [0, 1, 2, 3, 4]
    edges = {
        (0, 1): 1,
        (0, 2): 4,
        (1, 2): -3,
        (1, 3): 2,
        (2, 4): 3,
        (3, 4): -1
    }

    path_length, path = bellman_ford(nodes, edges)
    print("Shortest path length from source node:", path_length)
    print("Shortest paths from source node:", path)