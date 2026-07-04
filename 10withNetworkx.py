import networkx as nx
import matplotlib.pyplot as plt

steps1 = []
steps2 = []

def hamiltonian_circuit(G, steps):
    n = len(G.nodes())

    def solve(path):
        if len(path) == n:
            if G.has_edge(path[-1], path[0]):
                return path + [path[0]]
            return None

        for neighbor in sorted(G.neighbors(path[-1])):
            if neighbor not in path:
                new_path = path + [neighbor]

                if new_path not in steps:
                    steps.append(new_path)

                result = solve(new_path)
                if result:
                    return result
        return None

    for start in G.nodes():
        steps.append([start])
        result = solve([start])

        if result:
            if result not in steps:
                steps.append(result)
            return result

    return None


# -------- Graph 1 (Notebook Graph) --------
G1 = nx.Graph()

edges1 = [
    ('A','B'), ('B','C'),
    ('A','C'),
    ('A','E'),
    ('C','D'),
    ('E','D'),
    ('A','D'),
    ('E','C')
]

G1.add_edges_from(edges1)

pos1 = {
    'A': (0, 1),
    'B': (1, 2),
    'C': (2, 1),
    'D': (2, 0),
    'E': (0, 0)
}

cycle1 = hamiltonian_circuit(G1, steps1)

print("Graph (a) Hamiltonian Circuit:")
print(" -> ".join(cycle1))


# Draw steps
cols = 3
rows = (len(steps1) + cols - 1) // cols

fig1, axes1 = plt.subplots(rows, cols, figsize=(18, rows * 5))

if rows == 1:
    axes1 = axes1.reshape(1, -1)

for i in range(rows):
    for j in range(cols):
        index = i * cols + j
        ax = axes1[i][j]

        if index < len(steps1):
            step = steps1[index]

            nx.draw(G1, pos1, with_labels=True, node_size=900,
                    node_color="white", edgecolors="black", ax=ax)

            step_edges = list(zip(step, step[1:]))

            nx.draw_networkx_edges(G1, pos1, edgelist=step_edges,
                                   edge_color="red", width=3, ax=ax)

            ax.set_title(f"Step {index+1}: {' -> '.join(step)}")

        ax.axis("off")

plt.tight_layout()
plt.show()


# -------- Graph 2 (Complete-like Graph) --------
G2 = nx.Graph()

edges2 = [
    ('A','B'), ('A','C'), ('A','D'), ('A','E'),
    ('B','C'), ('B','D'), ('B','E'),
    ('C','D'), ('C','E'),
    ('D','E')
]

G2.add_edges_from(edges2)

pos2 = {
    'A': (1, 2),
    'B': (2, 1),
    'C': (1.5, 0),
    'D': (0.5, 0),
    'E': (0, 1)
}

cycle2 = hamiltonian_circuit(G2, steps2)

print("\nGraph (b) Hamiltonian Circuit:")
print(" -> ".join(cycle2))


# Draw steps
rows = (len(steps2) + cols - 1) // cols

fig2, axes2 = plt.subplots(rows, cols, figsize=(18, rows * 5))

if rows == 1:
    axes2 = axes2.reshape(1, -1)

for i in range(rows):
    for j in range(cols):
        index = i * cols + j
        ax = axes2[i][j]

        if index < len(steps2):
            step = steps2[index]

            nx.draw(G2, pos2, with_labels=True, node_size=900,
                    node_color="white", edgecolors="black", ax=ax)

            step_edges = list(zip(step, step[1:]))

            nx.draw_networkx_edges(G2, pos2, edgelist=step_edges,
                                   edge_color="red", width=3, ax=ax)

            ax.set_title(f"Step {index+1}: {' -> '.join(step)}")

        ax.axis("off")

plt.tight_layout()
plt.show()