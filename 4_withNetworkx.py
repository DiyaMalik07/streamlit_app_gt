import networkx as nx
import matplotlib.pyplot as plt

degree_sequence = [5, 5, 4, 3, 2, 2, 2, 1]
nodes = ['A','B','C','D','E','F','G','H']

degree_list = list(zip(nodes, degree_sequence))

G = nx.Graph()
G.add_nodes_from(nodes)

graphs = []
labels = []

realistic = True

while True:
    degree_list.sort(key=lambda x: x[1], reverse=True)
    degree_list = [x for x in degree_list if x[1] > 0]

    if not degree_list:
        break

    node, deg = degree_list.pop(0)

    if deg > len(degree_list):
        realistic = False
        break

    for i in range(deg):
        neighbor, neighbor_deg = degree_list[i]
        G.add_edge(node, neighbor)
        degree_list[i] = (neighbor, neighbor_deg - 1)

    graphs.append(G.copy())
    labels.append(sorted([d for _, d in degree_list], reverse=True))

if realistic:
    print("The given degree sequence is REALISTIC (graphical).")
else:
    print("The given degree sequence is NOT REALISTIC (not graphical).")

pos = {
    'A': (0, 2),
    'B': (2, 2),
    'C': (3, 1),
    'D': (3, 0),
    'E': (2, -1),
    'F': (0, -1),
    'G': (-1, 0),
    'H': (-1, 1)
}

rows = (len(graphs) + 1) // 2
plt.figure(figsize=(12, 5 * rows))

for i, graph in enumerate(graphs):
    plt.subplot(rows, 2, i + 1)
    nx.draw(
        graph, pos,
        with_labels=True,
        node_color='lightblue',
        node_size=900,
        font_size=11,
        edge_color='black'
    )
    seq_text = " ".join(map(str, labels[i]))
    plt.title(f"Iteration {i+1}\nRemaining degrees (desc): {seq_text}")

plt.tight_layout()
plt.show()