import networkx as nx
import matplotlib.pyplot as plt


def draw_graph_iterations(G, pos, is_multigraph=False):

    circuit = list(nx.eulerian_path(G))

    num_steps = len(circuit) + 1

    cols = 4
    rows = (num_steps + cols - 1) // cols

    fig, axes = plt.subplots(rows, cols, figsize=(20, 5 * rows))

    if rows == 1:
        axes = list(axes)

    axes = axes.flatten()

    current_G = G.copy()

    start_node = circuit[0][0]
    current_path = [start_node]

    for i in range(num_steps):

        ax = axes[i]

        if i > 0:

            u, v = circuit[i - 1]

            if is_multigraph:
                keys = list(current_G[u][v].keys())
                current_G.remove_edge(u, v, key=keys[0])
            else:
                current_G.remove_edge(u, v)

            current_path.append(v)

            ax.set_title(
                f"Step {i}: ({u}-{v})\n"
                f"{'->'.join(map(str, current_path))}",
                fontsize=9
            )

        else:
            ax.set_title("Start", fontsize=10)

        # Draw nodes
        nx.draw_networkx_nodes(
            current_G,
            pos,
            ax=ax,
            node_color='lightblue',
            edgecolors='black',
            node_size=500
        )

        nx.draw_networkx_labels(
            current_G,
            pos,
            ax=ax,
            font_size=10
        )

        if is_multigraph:

            straight_all = [
                (e[0], e[1])
                for e in G.edges(data=True)
                if e[2].get('curve') is None
            ]

            up_all = [
                (e[0], e[1])
                for e in G.edges(data=True)
                if e[2].get('curve') == 'up'
            ]

            down_all = [
                (e[0], e[1])
                for e in G.edges(data=True)
                if e[2].get('curve') == 'down'
            ]

            nx.draw_networkx_edges(
                G,
                pos,
                ax=ax,
                edgelist=straight_all,
                edge_color='lightgray',
                style='dashed'
            )

            nx.draw_networkx_edges(
                G,
                pos,
                ax=ax,
                edgelist=up_all,
                edge_color='lightgray',
                style='dashed',
                connectionstyle="arc3,rad=0.3"
            )

            nx.draw_networkx_edges(
                G,
                pos,
                ax=ax,
                edgelist=down_all,
                edge_color='lightgray',
                style='dashed',
                connectionstyle="arc3,rad=-0.3"
            )

            straight_cur = [
                (e[0], e[1])
                for e in current_G.edges(data=True)
                if e[2].get('curve') is None
            ]

            up_cur = [
                (e[0], e[1])
                for e in current_G.edges(data=True)
                if e[2].get('curve') == 'up'
            ]

            down_cur = [
                (e[0], e[1])
                for e in current_G.edges(data=True)
                if e[2].get('curve') == 'down'
            ]

            nx.draw_networkx_edges(
                current_G,
                pos,
                ax=ax,
                edgelist=straight_cur,
                width=2
            )

            nx.draw_networkx_edges(
                current_G,
                pos,
                ax=ax,
                edgelist=up_cur,
                width=2,
                connectionstyle="arc3,rad=0.3"
            )

            nx.draw_networkx_edges(
                current_G,
                pos,
                ax=ax,
                edgelist=down_cur,
                width=2,
                connectionstyle="arc3,rad=-0.3"
            )

        else:

            removed_edges = [
                edge for edge in G.edges()
                if not current_G.has_edge(*edge)
            ]

            nx.draw_networkx_edges(
                G,
                pos,
                ax=ax,
                edgelist=removed_edges,
                edge_color='lightgray',
                style='dashed'
            )

            nx.draw_networkx_edges(
                current_G,
                pos,
                ax=ax,
                width=2
            )

        ax.axis('off')

    for j in range(num_steps, len(axes)):
        axes[j].axis('off')

    plt.tight_layout()
    plt.show()


def main():

    G1 = nx.Graph()

    G1.add_edges_from([
        (1, 2),
        (2, 3),
        (3, 4),
        (4, 5),
        (5, 1),
        (1, 4),
        (5, 3),
        (1, 3)
    ])

    pos1 = {
        1: (0, 1),
        2: (1, 2),
        3: (2, 1),
        4: (2, 0),
        5: (0, 0)
    }

    draw_graph_iterations(G1, pos1)

    G2 = nx.Graph()

    # Outer pentagon
    G2.add_edges_from([
        (1, 2),
        (2, 3),
        (3, 4),
        (4, 5),
        (5, 1)
    ])

    # Star edges
    G2.add_edges_from([
        (1, 3),
        (1, 4),
        (2, 4),
        (2, 5),
        (3, 5)
    ])

    pos2 = {
        1: (0, 2),
        2: (2, 3),
        3: (4, 2),
        4: (3, 0),
        5: (1, 0)
    }

    draw_graph_iterations(G2, pos2)


if __name__ == "__main__":
    main()