def floyd_warshall(graph):

    # Convert graph to list of nodes
    nodes = list(graph.keys())

    # Initialize distances and paths matrices
    distances = {}
    paths = {}

    # Initialize with direct edges from the graph
    for start in nodes:
        distances[start] = {}
        paths[start] = {}
        for end in nodes:
            if start == end:
                distances[start][end] = 0
                paths[start][end] = [start]
            elif end in graph[start]:
                distances[start][end] = graph[start][end]
                paths[start][end] = [start, end]
            else:
                distances[start][end] = float('infinity')
                paths[start][end] = []

    # Main Floyd-Warshall algorithm
    for k in nodes:  # intermediate node
        for i in nodes:  # start node
            for j in nodes:  # end node
                # If path through k is shorter than current path
                if distances[i][k] != float('infinity') and distances[k][j] != float('infinity'):
                    new_distance = distances[i][k] + distances[k][j]
                    if new_distance < distances[i][j]:
                        distances[i][j] = new_distance
                        # Update path
                        paths[i][j] = paths[i][k][:-1] + paths[k][j]

    return distances, paths

# Example usage
if __name__ == "__main__":
    # Example graph
    graph = {
        'A': {'B': 4, 'C': 2},
        'B': {'C': 1, 'D': 5},
        'C': {'D': 8},
        'D': {}
    }

    # Find all shortest paths
    distances, paths = floyd_warshall(graph)

    # Print results
    print("Shortest distances between all pairs:")
    for start in graph:
        for end in graph:
            if distances[start][end] == float('infinity'):
                print(f"{start} to {end}: No path exists")
            else:
                path_str = ' -> '.join(paths[start][end])
                print(f"{start} to {end}: Distance = {distances[start][end]}, Path = {path_str}")

def pretty_print_matrix(matrix, nodes):
    # Print header
    print("\nDistance Matrix:")
    print("    " + "   ".join(nodes))

    # Print rows
    for i in nodes:
        row = [str(matrix[i][j]).rjust(3) if matrix[i][j] != float('infinity') else 'INF'
               for j in nodes]
        print(f"{i}: {' '.join(row)}")

# Example with pretty printing
if __name__ == "__main__":
    # Create a more interesting example graph
    example_graph = {
        'A': {'B': 3, 'C': 6},
        'B': {'C': 2, 'D': 4},
        'C': {'D': 1},
        'D': {'A': 5}
    }

    distances, paths = floyd_warshall(example_graph)
    pretty_print_matrix(distances, list(example_graph.keys()))