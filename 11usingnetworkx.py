import networkx as nx
import matplotlib.pyplot as plt

G=nx.Graph()

edges=[
(1,2),(1,4),(1,5),(1,3),
(2,3),(2,4),
(3,5),(3,7),(3,6),
(4,5),
(5,6),(5,7),
(6,7),(6,9),(6,10),
(7,8),(7,9),
(8,9),
(9,10)
]

G.add_edges_from(edges)

def my_strategy(G,colors):
    return sorted(G.nodes())

colors1=nx.coloring.greedy_color(G,strategy=my_strategy)

color_names=['green','orange','blue','red','yellow']

print("Colors used:",len(set(colors1.values())))
print("Node coloring assignment:")

for node in sorted(colors1):
    print(f"V{node}: color {color_names[colors1[node]]}")

print("\nValid coloring - no adjacent nodes share a color")

color_map=['green','orange','blue','red','yellow']
node_colors=[color_map[colors1[node]] for node in G.nodes()]

pos={
1:(0.5,2),
2:(0,1),
4:(0,0),
3:(1,1),
5:(1,0),
7:(2,1),
6:(2,0),
8:(2.5,2),
9:(3,1),
10:(3,0)
}

plt.figure(figsize=(12,5))

nx.draw(
G,
pos,
with_labels=True,
node_color=node_colors,
node_size=1000,
font_size=12,
font_weight='bold',
edge_color='gray'
)

plt.show()