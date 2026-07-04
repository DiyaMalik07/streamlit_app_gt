import matplotlib.pyplot as plt
import math
from collections import deque

nodes = list(range(1, 9))

edges = [
    (1,3),(1,7),(1,5),
    (2,8),(2,4),(2,6),
    (3,5),(3,7),
    (4,6),(4,8),
    (5,7),
    (6,8),
    (3,2),(2,1),(1,8),(8,7),(7,6),(6,5),(5,4),(4,3)
]

adj = {node: [] for node in nodes}
for u, v in edges:
    adj[u].append(v)
    adj[v].append(u)

radius = 3
pos = {}
rotation = math.pi / 8

for i in range(8):
    angle = 2 * math.pi * i / 8 + rotation
    pos[i + 1] = (radius * math.cos(angle), radius * math.sin(angle))

def draw_graph(ax, nodes, edges, title, color):
    for u, v in edges:
        x = [pos[u][0], pos[v][0]]
        y = [pos[u][1], pos[v][1]]
        ax.plot(x, y)

    for node in nodes:
        ax.scatter(pos[node][0], pos[node][1])
        ax.text(pos[node][0], pos[node][1], str(node),
                ha='center', va='center', color='black')

    ax.set_title(title)
    ax.axis('off')

induced_nodes = [1,2,3,4]
induced_edges = [(u,v) for u,v in edges if u in induced_nodes and v in induced_nodes]

visited = set()
spanning_edges = []

queue = deque([1])
visited.add(1)

while queue:
    u = queue.popleft()
    for v in adj[u]:
        if v not in visited:
            visited.add(v)
            queue.append(v)
            spanning_edges.append((u, v))

remove_edges = [(1,3),(4,5)]
edge_deleted = [(u,v) for u,v in edges if (u,v) not in remove_edges and (v,u) not in remove_edges]

fig, axes = plt.subplots(2, 2, figsize=(10, 8))

draw_graph(axes[0,0], nodes, edges, "Original Graph", 'lightblue')
draw_graph(axes[0,1], induced_nodes, induced_edges, "Induced Subgraph", 'lightgreen')
draw_graph(axes[1,0], nodes, spanning_edges, "Spanning Tree (BFS)", 'orange')
draw_graph(axes[1,1], nodes, edge_deleted, "Edge Deleted Subgraph", 'pink')

plt.show()

print("Original Graph:")
print("Vertices:", len(nodes))
print("Edges:", len(edges))

print("\nInduced Subgraph:")
print("Vertices:", len(induced_nodes))
print("Edges:", len(induced_edges))

print("\nSpanning Tree:")
print("Vertices:", len(nodes))
print("Edges:", len(spanning_edges))

print("\nEdge Deleted Subgraph:")
print("Vertices:", len(nodes))
print("Edges:", len(edge_deleted))