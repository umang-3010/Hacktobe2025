import heapq  # for priority queue
import networkx as nx
import matplotlib.pyplot as plt

def best_first_search(graph, heuristic, start, goal):
    pq = [(heuristic[start], [start])]   # heap stores (heuristic, path)
    visited = set()
    while pq:
        h, path = heapq.heappop(pq)   # pop node with lowest heuristic
        node = path[-1]              # current node is the last in path
        print(f"Visiting: {node} (h={h})")

        if node == goal:   # goal found
            print(" Goal Reached!")
            print("Path:", " -> ".join(path))
            return path
        if node in visited:
            continue
        visited.add(node)
        # push neighbors into heap with their heuristic
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                new_path = path + [neighbor]   # extend the path
                heapq.heappush(pq, (heuristic[neighbor], new_path))
    print(" No path found!")
    return None
def visualize_graph(graph, heuristic, start, goal, path=None):
    G = nx.DiGraph()
    # Add nodes and edges
    for node in graph:
        G.add_node(node, h=heuristic[node])
        for nbr in graph[node]:
            G.add_edge(node, nbr)
    pos = nx.spring_layout(G, seed=42)
    # Node colors
    node_colors = []
    for node in G.nodes():
        if path and node in path:
            node_colors.append("lightgreen")
        elif node == goal:
            node_colors.append("orange")
        elif node == start:
            node_colors.append("yellow")
        else:
            node_colors.append("lightblue")
    # Draw nodes with only names
    nx.draw(G, pos, with_labels=True, node_size=1500,
            node_color=node_colors, font_weight="bold", arrows=True)
    # Draw heuristic separately (slightly below node)
    heuristic_labels = {n: f"h={heuristic[n]}" for n in G.nodes()}
    nx.draw_networkx_labels(
        G, {k: (v[0], v[1]-0.08) for k, v in pos.items()},  # shift downward
        labels=heuristic_labels, font_size=8, font_color="black"
    )
    # Highlight path edges
    if path:
        edges_in_path = [(path[i], path[i+1]) for i in range(len(path)-1)]
        nx.draw_networkx_edges(G, pos, edgelist=edges_in_path, edge_color="red", width=2)

    plt.title("Best First Search Graph Visualization")
    plt.show()
graph = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': [],
    'D': ['G'],
    'E': [],
    'F': ['H', 'I'],
    'G': [],
    'H': [],
    'I': []
}
heuristic = {
    'A': 7,
    'B': 6,
    'C': 9,
    'D': 5,
    'E': 8,
    'F': 4,
    'G': 6,
    'H': 3,
    'I': 0
}
# Run the search
start = input("Enter Start Node: ").strip().upper()
goal = input("Enter Goal Node: ").strip().upper()
result_path = best_first_search(graph, heuristic, start, goal)
visualize_graph(graph, heuristic, start, goal, result_path)
