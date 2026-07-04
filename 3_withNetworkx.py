import networkx as nx
import matplotlib.pyplot as plt
import math

G = nx.Graph()
G.add_nodes_from(range(1, 9))

edges = [
    (1,3),(1,7),(1,5),
    (2,8),(2,4),(2,6),
    (3,5),(3,7),
    (4,6),(4,8),
    (5,7),
    (6,8),
    (3,2),(2,1),(1,8),(8,7),(7,6),(6,5),(5,4),(4,3)
]
G.add_edges_from(edges)

radius = 3
pos = {}
rotation = math.pi / 8

for i in range(8):
    angle = 2 * math.pi * i / 8 + rotation
    pos[i + 1] = (radius * math.cos(angle), radius * math.sin(angle))

# Subgraphs
G_induced = G.subgraph([1, 2, 3, 4])
G_spanning = nx.minimum_spanning_tree(G) 
G_edge_deleted = nx.edge_subgraph(
    G,
    [(u, v) for u, v in G.edges() 
     if (u, v) not in [(1,3), (4,5)] and (v, u) not in [(1,3), (4,5)]]
)

# Plot
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

nx.draw(G, pos, ax=axes[0,0], with_labels=True, node_color='lightblue', node_size=700)
axes[0,0].set_title("Original Graph")
axes[0,0].axis('off')

nx.draw(G_induced, pos, ax=axes[0,1], with_labels=True, node_color='lightgreen', node_size=700)
axes[0,1].set_title("Induced Subgraph")
axes[0,1].axis('off')

nx.draw(G_spanning, pos, ax=axes[1,0], with_labels=True, node_color='orange', node_size=700)
axes[1,0].set_title("Minimum Spanning Tree")  
axes[1,0].axis('off')

nx.draw(G_edge_deleted, pos, ax=axes[1,1], with_labels=True, node_color='pink', node_size=700)
axes[1,1].set_title("Edge-Deleted Subgraph")
axes[1,1].axis('off')

plt.show()

# Output
print("Original Graph:")
print("Vertices:", G.number_of_nodes())
print("Edges:", G.number_of_edges())

print("\nInduced Subgraph:")
print("Vertices:", G_induced.number_of_nodes())
print("Edges:", G_induced.number_of_edges())

print("\nSpanning Tree:")
print("Vertices:", G_spanning.number_of_nodes())
print("Edges:", G_spanning.number_of_edges())

print("\nEdge-Deleted Subgraph:")
print("Vertices:", G_edge_deleted.number_of_nodes())
print("Edges:", G_edge_deleted.number_of_edges())