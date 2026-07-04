import networkx as nx
import matplotlib.pyplot as plt

fig, axes = plt.subplots(2, 2, figsize=(10, 10))

# 
G1 = nx.Graph()
G1.add_nodes_from([0, 1, 2, 3])
G1.add_edges_from([
    (0,1), (0,2), (0,3),
    (1,2), (1,3),
    (2,3)
])

nx.draw(G1, ax=axes[0,0], with_labels=True)
axes[0,0].set_title("Complete Graph K4")
axes[0,0].axis('off')

G2 = nx.Graph()
G2.add_nodes_from(range(5))
G2.add_edges_from([
    (0,1), (1,2), (2,3), (3,4), (4,0)
])

nx.draw(G2, ax=axes[0,1], with_labels=True)
axes[0,1].set_title("Cycle Graph C5")
axes[0,1].axis('off')

G3 = nx.Graph()
G3.add_nodes_from(range(5))
G3.add_edges_from([
    (0,1), (1,2), (2,3), (3,4)
])

nx.draw(G3, ax=axes[1,0], with_labels=True)
axes[1,0].set_title("Path Graph P5")
axes[1,0].axis('off')

# Bip
G4 = nx.Graph()
G4.add_nodes_from([0, 1])          
G4.add_nodes_from([2, 3, 4])      

G4.add_edges_from([
    (0,2), (0,3), (0,4),
    (1,2), (1,3), (1,4)
])

pos = {
    0: (-1, 1),  1: (1, 1),    
    2: (-1,-1), 3: (0,-1), 4: (1,-1)  
}

nx.draw(G4, pos, ax=axes[1,1], with_labels=True)
axes[1,1].set_title("Bipartite Graph K2,3")
axes[1,1].axis('off')

plt.tight_layout()
plt.show()
