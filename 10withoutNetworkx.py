import matplotlib.pyplot as plt

plt.figure(figsize=(12,5))

plt.subplot(1,2,1)

pos1 = {
    'A': (0,1),
    'B': (1,2),
    'C': (2,1),
    'D': (2,0),
    'E': (0,0)
}

edges1 = [
    ('A','B'), ('B','C'),
    ('A','E'), ('C','D'),
    ('E','D'),
    ('A','C'),
    ('A','D'), ('C','E')
]

ham1 = [
    ('B','A'), ('A','E'),
    ('E','D'), ('D','C'),
    ('C','B')
]

for (u,v) in edges1:
    x = [pos1[u][0], pos1[v][0]]
    y = [pos1[u][1], pos1[v][1]]
    plt.plot(x, y, 'black')

for (u,v) in ham1:
    x = [pos1[u][0], pos1[v][0]]
    y = [pos1[u][1], pos1[v][1]]
    plt.plot(x, y, 'red', linewidth=2)

for node, (x,y) in pos1.items():
    plt.scatter(x, y, s=500)
    plt.text(x, y, node, ha='center', va='center', color='white')

plt.title("Graph 1 (House) - Hamiltonian Circuit")
plt.axis('off')


plt.subplot(1,2,2)

import math
nodes = ['A','B','C','D','E']
pos2 = {}

n = len(nodes)
for i, node in enumerate(nodes):
    angle = 2 * math.pi * i / n
    pos2[node] = (math.cos(angle), math.sin(angle))

edges2 = []
for i in range(n):
    for j in range(i+1, n):
        edges2.append((nodes[i], nodes[j]))

ham2 = [
    ('A','B'), ('B','C'),
    ('C','D'), ('D','E'),
    ('E','A')
]

for (u,v) in edges2:
    x = [pos2[u][0], pos2[v][0]]
    y = [pos2[u][1], pos2[v][1]]
    plt.plot(x, y, 'black')

for (u,v) in ham2:
    x = [pos2[u][0], pos2[v][0]]
    y = [pos2[u][1], pos2[v][1]]
    plt.plot(x, y, 'red', linewidth=2)

for node, (x,y) in pos2.items():
    plt.scatter(x, y, s=500)
    plt.text(x, y, node, ha='center', va='center', color='white')

plt.title("Graph 2 (K5) - Hamiltonian Circuit")
plt.axis('off')

plt.show()