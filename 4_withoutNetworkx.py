import matplotlib.pyplot as plt

degree_sequence = [5, 5, 4, 3, 2, 2, 2, 1]
nodes = ['A','B','C','D','E','F','G','H']

degree_list = list(zip(nodes, degree_sequence))

edges = []
steps = []

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
        edges.append((node, neighbor))
        degree_list[i] = (neighbor, neighbor_deg - 1)

    steps.append(edges.copy())

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

def draw_graph(ax, nodes, edges, title):
    for u, v in edges:
        x = [pos[u][0], pos[v][0]]
        y = [pos[u][1], pos[v][1]]
        ax.plot(x, y)

    for node in nodes:
        ax.scatter(pos[node][0], pos[node][1])
        ax.text(pos[node][0], pos[node][1], node,
                ha='center', va='center')

    ax.set_title(title)
    ax.axis('off')

rows = (len(steps) + 1) // 2
plt.figure(figsize=(12, 5 * rows))

for i, e in enumerate(steps):
    plt.subplot(rows, 2, i + 1)
    draw_graph(plt.gca(), nodes, e, f"Iteration {i+1}")

plt.tight_layout()
plt.show()