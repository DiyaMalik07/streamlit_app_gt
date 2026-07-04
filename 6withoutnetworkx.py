import matplotlib.pyplot as plt

edges = [
    (1, 2, 10), (1, 3, 9), (1, 4, 6), (1, 5, 12),
    (2, 5, 8),
    (3, 4, 7), (3, 6, 5),
    (4, 5, 8), (4, 6, 8), (4, 7, 7),
    (5, 7, 4), (5, 9, 13),
    (6, 7, 14), (6, 8, 6),
    (7, 8, 8), (7, 9, 8),
    (8, 9, 10)
]

parent = {}
rank = {}

def find(u):
    if parent[u] != u:
        parent[u] = find(parent[u])
    return parent[u]

def union(u, v):
    ru = find(u)
    rv = find(v)
    if ru != rv:
        if rank[ru] > rank[rv]:
            parent[rv] = ru
        elif rank[ru] < rank[rv]:
            parent[ru] = rv
        else:
            parent[rv] = ru
            rank[ru] += 1
        return True
    return False

nodes = set()
for u, v, w in edges:
    nodes.add(u)
    nodes.add(v)

for node in nodes:
    parent[node] = node
    rank[node] = 0

edges.sort(key=lambda x: x[2])

steps = []
current = []
total = 0

for u, v, w in edges:
    if union(u, v):
        prev = total
        total += w
        current.append((u, v, w))
        steps.append((u, v, w, list(current), prev, total))

pos = {
    1: (0, 2),
    2: (2, 2),
    3: (3, 1.5),
    4: (1, 1),
    5: (2.5, 0.8),
    6: (3.2, 0),
    7: (1.5, -0.5),
    8: (2.8, -1),
    9: (3.8, -0.5)
}

rows, cols = 2, 4
plt.figure(figsize=(16, 8))

for i, (u, v, w, curr, prev, total_now) in enumerate(steps):
    plt.subplot(rows, cols, i + 1)

    # Draw nodes
    for node, (x, y) in pos.items():
        plt.scatter(x, y, s=300)
        plt.text(x, y, str(node), ha='center', va='center', color='white', fontsize=10)

    # Draw edges
    for a, b, weight in curr:
        x1, y1 = pos[a]
        x2, y2 = pos[b]
        plt.plot([x1, x2], [y1, y2])

        mx = (x1 + x2) / 2
        my = (y1 + y2) / 2
        plt.text(mx, my, str(weight), fontsize=9)

    if i == 0:
        sum_text = f"{w}"
    else:
        sum_text = f"{prev} + {w} = {total_now}"

    plt.title(f"Step {i+1}: ({u}-{v}) w={w}\nTotal: {sum_text}", fontsize=10)
    plt.axis('off')

plt.tight_layout()
plt.show()