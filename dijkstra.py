def dijkstra(graph, start):
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    paths = {node: [] for node in graph}
    paths[start] = [start]

    # Keep track of unvisited nodes
    unvisited = list(graph.keys())

    while unvisited:
        # Find the unvisited node with minimum distance
        current = min(unvisited, key=lambda node: distances[node])

        # Remove the current node from unvisited
        unvisited.remove(current)

        # Check all neighbors of current node
        for neighbor, weight in graph[current].items():
            distance = distances[current] + weight

            # If we found a shorter path, update it
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                paths[neighbor] = paths[current] + [neighbor]

    return distances, paths

# Example usage
if __name__ == "__main__":
    # Example graph
    graph = {
        'A': {'B': 4, 'C': 2},
        'B': {'A': 4, 'C': 1, 'D': 5},
        'C': {'A': 2, 'B': 1, 'D': 8},
        'D': {'B': 5, 'C': 8}
    }

    # Find shortest paths from node 'A'
    distances, paths = dijkstra(graph, 'A')

    # Print results
    print("Shortest distances from A:")
    for node, distance in distances.items():
        print(f"To {node}: {distance}")

    print("\nShortest paths from A:")
    for node, path in paths.items():
        print(f"To {node}: {' -> '.join(path)}")