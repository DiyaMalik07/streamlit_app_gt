import networkx as nx
import matplotlib.pyplot as plt

# ----------- GIRTH FUNCTION -----------
def find_girth(G):
    cycles = nx.cycle_basis(G)
    if not cycles:
        return float('inf')
    return min(len(c) for c in cycles)

# ----------- GRAPH 1 (CIRCLE EXACT) -----------
G1 = nx.Graph()

G1.add_nodes_from([1,2,3,4,5,6])

G1.add_edges_from([
    (1,2), (2,3), (3,4),
    (4,5), (5,6), (6,1),  # outer circle
    (2,5), (1,4), (3,6)   # inner edges
])

# ----------- GRAPH 2 (MATCHED FOR ISOMORPHISM) -----------
G2 = nx.Graph()

G2.add_nodes_from(['a','b','c','d','e','f'])

# Carefully mapped edges so graphs become ISOMORPHIC
G2.add_edges_from([
    ('a','d'), ('d','b'), ('b','e'),
    ('e','c'), ('c','f'), ('f','a'),
    ('d','c'), ('a','e'), ('b','f')
])

# ----------- GRAPH 1 DETAILS -----------
print("Graph 1")
print("Vertices       :", G1.number_of_nodes())
print("Edges          :", G1.number_of_edges())
print("Degree Sequence:", sorted([d for n,d in G1.degree()]))
print("Cycle Girth    :", find_girth(G1))

# ----------- GRAPH 2 DETAILS -----------
print("\nGraph 2")
print("Vertices       :", G2.number_of_nodes())
print("Edges          :", G2.number_of_edges())
print("Degree Sequence:", sorted([d for n,d in G2.degree()]))
print("Cycle Girth    :", find_girth(G2))

# ----------- ISOMORPHISM CHECK -----------
GM = nx.isomorphism.GraphMatcher(G1, G2)

print("\nIsomorphism Check:")
if GM.is_isomorphic():
    print("Result: Both graphs are mathematically ISOMORPHIC!\n")
    print("Bijection Mapping (Graph 1 node ---> Graph 2 node):")
    
    for k,v in GM.mapping.items():
        print(f"{k} ---> {v}")
else:
    print("Result: Graphs are NOT isomorphic")

# ----------- DRAW EXACT LIKE IMAGE -----------

plt.figure(figsize=(10,5))

# GRAPH 1 (CIRCLE EXACT POSITION)
plt.subplot(121)
pos1 = {
    1:(-1,0),
    2:(-0.5,-1),
    3:(0.5,-1),
    4:(1,0),
    5:(0.5,1),
    6:(-0.5,1)
}
nx.draw(G1, pos1, with_labels=True, node_size=800)
plt.title("Graph 1")

# GRAPH 2 (VERTICAL TWO COLUMN EXACT)
plt.subplot(122)
pos2 = {
    'a':(-1,1), 'b':(-1,0), 'c':(-1,-1),
    'd':(1,1),  'e':(1,0),  'f':(1,-1)
}
nx.draw(G2, pos2, with_labels=True, node_size=800)
plt.title("Graph 2")

plt.show()