import networkx as nx
import matplotlib.pyplot as plt

plt.figure(figsize=(12,5))

G1 = nx.Graph()

edges1 = [
    ('A','B'), ('B','C'),  
    ('A','E'), ('C','D'),  
    ('E','D'),             
    ('A','C'),             
    ('A','D'), ('C','E')   
]

G1.add_edges_from(edges1)

pos1 = {
    'A': (0,1),
    'B': (1,2),
    'C': (2,1),
    'D': (2,0),
    'E': (0,0)
}

plt.subplot(1,2,1)
nx.draw(G1, pos1, with_labels=True,
        node_color='lightblue', node_size=2000)

ham1 = [
    ('B','A'), ('A','E'),
    ('E','D'), ('D','C'),
    ('C','B')
]

nx.draw_networkx_edges(G1, pos1,
                       edgelist=ham1,
                       edge_color='red', width=2)

plt.title("Graph 1 (House) - Hamiltonian Circuit")

G2 = nx.complete_graph(['A','B','C','D','E'])

pos2 = nx.circular_layout(G2)

plt.subplot(1,2,2)
nx.draw(G2, pos2, with_labels=True,
        node_color='lightgreen', node_size=2000)

ham2 = [
    ('A','B'), ('B','C'),
    ('C','D'), ('D','E'),
    ('E','A')
]

nx.draw_networkx_edges(G2, pos2,
                       edgelist=ham2,
                       edge_color='red', width=2)

plt.title("Graph 2 (K5) - Hamiltonian Circuit")

plt.show()