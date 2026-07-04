import networkx as nx
import matplotlib.pyplot as plt

# -------- Graph 1 (Cycle with chords) --------
G1 = nx.Graph()

# Nodes
G1.add_nodes_from([1, 2, 3, 4, 5, 6])

# Cycle edges
G1.add_edges_from([
    (1, 2), (2, 3), (3, 4),
    (4, 5), (5, 6), (6, 1)
])

# Chords (inside edges as shown)
G1.add_edges_from([
    (6, 3), (5, 2), (4, 1)
])

pos1 = nx.circular_layout(G1)

# -------- Graph 2 (Complete Bipartite Graph K3,3) --------
G2 = nx.Graph()

left_nodes  = ['a', 'b', 'c']
right_nodes = ['d', 'e', 'f']

G2.add_nodes_from(left_nodes, bipartite=0)
G2.add_nodes_from(right_nodes, bipartite=1)

# Complete bipartite edges
for u in left_nodes:
    for v in right_nodes:
        G2.add_edge(u, v)

pos2 = {
    'a': (0, 2), 'b': (0, 1), 'c': (0, 0),
    'd': (2, 2), 'e': (2, 1), 'f': (2, 0)
}

# -------- Draw Graphs --------
fig, axes = plt.subplots(1, 2, figsize=(10, 4))

nx.draw(G1, pos1, ax=axes[0],
        with_labels=True, node_color='lightblue',
        node_size=800)
axes[0].set_title("Graph 1")
axes[0].axis('off')

nx.draw(G2, pos2, ax=axes[1],
        with_labels=True, node_color='lightgreen',
        node_size=800)
axes[1].set_title("Graph 2 (K₃,₃)")
axes[1].axis('off')

plt.show()
