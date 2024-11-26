def bellman_ford(graph, start):
    nodes = set()
    for source, dest, _ in graph:
        nodes.add(source)
        nodes.add(dest)

    # Initialize distances and paths
    distances = {node: float('infinity') for node in nodes}
    distances[start] = 0
    paths = {node: [] for node in nodes}
    paths[start] = [start]

    # Relax all edges |V| - 1 times
    n = len(nodes)
    for _ in range(n - 1):
        for source, dest, weight in graph:
            if distances[source] != float('infinity') and distances[source] + weight < distances[dest]:
                distances[dest] = distances[source] + weight
                paths[dest] = paths[source] + [dest]


    has_negative_cycle = False
    for source, dest, weight in graph:
        if distances[source] != float('infinity') and distances[source] + weight < distances[dest]:
            has_negative_cycle = True
            break

    return distances, paths, has_negative_cycle

# Example usage
if __name__ == "__main__":
    # Example graph with no negative cycles
    graph1 = [
        ('A', 'B', 4),
        ('A', 'C', 2),
        ('B', 'C', 1),
        ('B', 'D', 5),
        ('C', 'D', 8),
        ('C', 'B', 1)
    ]

    # Find shortest paths from node 'A'
    distances, paths, has_cycle = bellman_ford(graph1, 'A')

    # Print results
    print("Results for graph without negative cycles:")
    print("Negative cycle exists:", has_cycle)
    print("\nShortest distances from A:")
    for node, distance in distances.items():
        print(f"To {node}: {distance}")

    print("\nShortest paths from A:")
    for node, path in paths.items():
        print(f"To {node}: {' -> '.join(path)}")

    # Example graph with negative cycle
    graph2 = [
        ('A', 'B', 1),
        ('B', 'C', 2),
        ('C', 'D', -6),
        ('D', 'B', 2)
    ]

    distances2, paths2, has_cycle2 = bellman_ford(graph2, 'A')
    print("\nResults for graph with negative cycles:")
    print("Negative cycle exists:", has_cycle2)