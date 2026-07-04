import networkx as nx
import matplotlib.pyplot as plt
import heapq
import math

G = nx.Graph()

edges = [
    ('A','B',2), ('A','F',3),
    ('B','F',1),
    ('A','D',5),
    ('F','G',1),
    ('D','G',5),
    ('D','E',3),
    ('G','H',9),
    ('F','C',7)
]

G.add_weighted_edges_from(edges)

pos = {
    'A': (0,2), 'B': (-1,1), 'C': (1,1),
    'D': (1,2), 'E': (2,2),
    'F': (0,1), 'G': (0,0), 'H': (1,0)
}

def dijkstra(G, source):
    dist = {node: float('inf') for node in G.nodes()}
    parent = {node: None for node in G.nodes()}

    dist[source] = 0
    pq = [(0, source)]

    while pq:
        d, node = heapq.heappop(pq)

        for neigh in G.neighbors(node):
            weight = G[node][neigh]['weight']
            new_dist = d + weight

            if new_dist < dist[neigh]:
                dist[neigh] = new_dist
                parent[neigh] = node
                heapq.heappush(pq, (new_dist, neigh))

    return dist, parent

def get_path(parent, target):
    path = []
    while target:
        path.append(target)
        target = parent[target]
    return path[::-1]

def print_paths(G, source, dist, parent):
    print(f"\nStep-by-Step Shortest Paths from {source}:")
    print("-" * 45)

    for node in G.nodes():
        if node == source:
            continue

        path = get_path(parent, node)
        path_str = " -> ".join(path)

        print(f"To {node}: {path_str} | Total Weight: {dist[node]}")

def draw_all_paths(G, pos, source):
    dist, parent = dijkstra(G, source)

    print_paths(G, source, dist, parent)   

    nodes = list(G.nodes())
    cols = 3
    rows = math.ceil(len(nodes) / cols)

    fig, axes = plt.subplots(rows, cols, figsize=(15, 5*rows))
    axes = axes.flatten()

    for i, target in enumerate(nodes):
        ax = axes[i]

        path = get_path(parent, target)
        path_edges = list(zip(path, path[1:]))

        nx.draw(G, pos, ax=ax,
                with_labels=True,
                node_color="lightblue",
                node_size=800,
                edge_color="lightgray")

        nx.draw_networkx_nodes(G, pos, nodelist=path,
                               node_color="skyblue", ax=ax)

        nx.draw_networkx_edges(G, pos, edgelist=path_edges,
                               edge_color="green", width=3, ax=ax)

        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, ax=ax)

        ax.set_title(f"{source} → {target} (Dist: {dist[target]})")

    for j in range(i+1, len(axes)):
        fig.delaxes(axes[j])

    plt.tight_layout()
    plt.show()

draw_all_paths(G, pos, 'A')