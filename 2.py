import networkx as nx
import matplotlib.pyplot as plt

#  Graph 1 
G1 = nx.Graph()
G1.add_nodes_from([0, 1, 2, 3])
G1.add_edges_from([
    (0, 1), (1, 2), (2, 3), (3, 0)
])

#  Graph 2 
G2 = nx.Graph()
G2.add_nodes_from([10, 11, 12, 13])
G2.add_edges_from([
    (10, 12), (12, 11), (11, 13), (13, 10)
])

#  Draw Graphs 
fig, axes = plt.subplots(1, 2, figsize=(8, 4))

nx.draw(G1, ax=axes[0], with_labels=True,
        node_color='red', node_size=800)
axes[0].set_title("Graph 1")
axes[0].axis('off')

nx.draw(G2, ax=axes[1], with_labels=True,
        node_color='green', node_size=800)
axes[1].set_title("Graph 2")
axes[1].axis('off')

plt.show()

#  Graph Information 
print("\nGraph 1:")
print("Vertices :", G1.number_of_nodes())
print("Edges    :", G1.number_of_edges())
print("Cycles   :", nx.cycle_basis(G1))

print("\nGraph 2:")
print("Vertices :", G2.number_of_nodes())
print("Edges    :", G2.number_of_edges())
print("Cycles   :", nx.cycle_basis(G2))

#  Isomorphism Check 
matcher = nx.algorithms.isomorphism.GraphMatcher(G1, G2)

if matcher.is_isomorphic():
    print("\nThe given graphs are ISOMORPHIC")
    print("Node Mapping:")
    for k, v in matcher.mapping.items():
        print(f"{k} → {v}")
else:
    print("\nThe given graphs are NOT ISOMORPHIC")
