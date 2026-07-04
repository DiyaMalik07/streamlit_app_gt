import networkx as nx
import matplotlib.pyplot as plt


def edges_to_nodes(edge_list):

    if not edge_list:
        return []

    nodes = [edge[0] for edge in edge_list]
    nodes.append(edge_list[-1][1])

    return nodes


def plot_graph_row(fig, row_idx, G, pos, title, results):

    titles = [title, "Path", "Trail", "Closed Walk"]
    elements = [None, results['path'], results['trail'], results['walk']]

    for col_idx in range(4):

        ax = fig.add_subplot(2, 4, row_idx * 4 + col_idx + 1)
        ax.set_title(titles[col_idx], fontsize=10)

        nx.draw_networkx_nodes(
            G,
            pos,
            ax=ax,
            node_color='lightblue',
            edgecolors='black',
            node_size=500
        )

        nx.draw_networkx_labels(G, pos, ax=ax)

        nx.draw_networkx_edges(
            G,
            pos,
            ax=ax,
            edge_color='gray'
        )

        if elements[col_idx]:

            seq = elements[col_idx]

            edges_in_seq = [
                (seq[i], seq[i + 1])
                for i in range(len(seq) - 1)
            ]

            nx.draw_networkx_nodes(
                G,
                pos,
                ax=ax,
                nodelist=seq,
                node_color='orange',
                edgecolors='black',
                node_size=500
            )

            nx.draw_networkx_edges(
                G,
                pos,
                ax=ax,
                edgelist=edges_in_seq,
                edge_color='red',
                width=3
            )

        ax.axis('off')


def main_visual():

    fig = plt.figure(figsize=(18, 10))

    # ---------------- GRAPH 1 ----------------

    G1 = nx.Graph()

    G1.add_edges_from([
        ('A', 'B'),   # e1
        ('B', 'C'),   # e2
        ('C', 'D'),   # e3
        ('F', 'D'),   # e4
        ('A', 'F'),   # e5
        ('A', 'D'),   # e6
        ('F', 'C'),   # e7
        ('A', 'C')    # e8
    ])

    pos1 = {
        'A': (0, 1),
        'B': (1, 2),
        'C': (2, 1),
        'F': (0, 0),
        'D': (2, 0)
    }

    path1 = nx.shortest_path(G1, source='B', target='D')

    all_paths1 = list(nx.all_simple_paths(G1, source='B', target='D'))
    trail1 = max(all_paths1, key=len)

    cycle_edges1 = nx.find_cycle(G1, source='A')
    walk1 = edges_to_nodes(cycle_edges1)

    res1 = {
        'path': path1,
        'trail': trail1,
        'walk': walk1
    }

    print("\n--- Graph 1 Results ---")
    print(f"Path: {res1['path']}")
    print(f"Trail: {res1['trail']}")
    print(f"Walk: {res1['walk']}")

    # ---------------- GRAPH 2 ----------------

    G2 = nx.Graph()

    G2.add_edges_from([
        ('A', 'B'),   # e1
        ('B', 'C'),   # e2
        ('C', 'E'),   # e3
        ('D', 'E'),   # e4
        ('A', 'D'),   # e5
        ('A', 'C'),
        ('A', 'E'),
        ('B', 'D'),
        ('B', 'E'),
        ('C', 'D')
    ])

    pos2 = {
        'A': (0, 1),
        'B': (1, 2),
        'C': (2, 1),
        'D': (0.5, 0),
        'E': (1.8, 0)
    }

    path2 = nx.shortest_path(G2, source='A', target='E')

    all_paths2 = list(nx.all_simple_paths(G2, source='A', target='E'))
    trail2 = max(all_paths2, key=len)

    cycle_edges2 = nx.find_cycle(G2, source='A')
    walk2 = edges_to_nodes(cycle_edges2)

    res2 = {
        'path': path2,
        'trail': trail2,
        'walk': walk2
    }

    print("\n--- Graph 2 Results ---")
    print(f"Path: {res2['path']}")
    print(f"Trail: {res2['trail']}")
    print(f"Walk: {res2['walk']}")

    # ---------------- PLOTS ----------------

    plot_graph_row(
        fig,
        0,
        G1,
        pos1,
        "Graph 1",
        res1
    )

    plot_graph_row(
        fig,
        1,
        G2,
        pos2,
        "Graph 2",
        res2
    )

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main_visual()