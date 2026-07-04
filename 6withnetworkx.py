import networkx as nx
import matplotlib.pyplot as plt

def mst_networkx_steps():

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

    G = nx.Graph()
    G.add_weighted_edges_from(edges)

    mst = nx.minimum_spanning_tree(G, algorithm='kruskal')

    mst_edges = list(mst.edges(data=True))
    mst_edges = sorted(mst_edges, key=lambda x: x[2]['weight'])

    pos = nx.spring_layout(G, seed=42)

    steps = []
    current = []
    total = 0

    for u, v, data in mst_edges:
        w = data['weight']
        prev = total
        total += w
        current.append((u, v, w))
        steps.append((u, v, w, list(current), prev, total))

    fig, axes = plt.subplots(2, 4, figsize=(18, 8))

    for i, ax in enumerate(axes.flatten()):
        u, v, w, curr, prev, total_now = steps[i]

        temp = nx.Graph()
        temp.add_weighted_edges_from(curr)

        nx.draw(temp, pos, with_labels=True, ax=ax)
        labels = nx.get_edge_attributes(temp, 'weight')
        nx.draw_networkx_edge_labels(temp, pos, edge_labels=labels, ax=ax)

        if i == 0:
            sum_text = f"{w}"
        else:
            sum_text = f"{prev} + {w} = {total_now}"

        ax.set_title(f"Step {i+1}: ({u}-{v}) w={w}\nTotal: {sum_text}")

        print(f"Step {i+1}: {sum_text}")

    plt.tight_layout()
    plt.show()

mst_networkx_steps()