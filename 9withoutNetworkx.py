import matplotlib.pyplot as plt


class FleuryAlgorithmGraph:

    def __init__(self, vertices):
        self.V = vertices
        self.adj = {i: [] for i in vertices}

    def add_edge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)

    def remove_edge(self, u, v):
        self.adj[u].remove(v)
        self.adj[v].remove(u)

    def dfs_count(self, v, visited):

        count = 1
        visited.add(v)

        for neighbor in self.adj[v]:
            if neighbor not in visited:
                count += self.dfs_count(neighbor, visited)

        return count

    def is_cut_edge(self, u, v):

        if len(self.adj[u]) == 1:
            return False

        visited = set()
        count_before = self.dfs_count(u, visited)

        self.remove_edge(u, v)

        visited = set()
        count_after = self.dfs_count(u, visited)

        self.add_edge(u, v)

        return count_before > count_after

    def get_euler_path(self, start_vertex):

        circuit = [start_vertex]

        curr = start_vertex

        edges_remaining = sum(len(neighbors)
                              for neighbors in self.adj.values()) // 2

        while edges_remaining > 0:

            edge_chosen = False

            for v in list(self.adj[curr]):

                if not self.is_cut_edge(curr, v):

                    self.remove_edge(curr, v)

                    circuit.append(v)

                    curr = v

                    edges_remaining -= 1

                    edge_chosen = True

                    break

            if not edge_chosen:

                v = self.adj[curr][0]

                self.remove_edge(curr, v)

                circuit.append(v)

                curr = v

                edges_remaining -= 1

        return circuit


def remove_edge(edges, u, v):

    if (u, v) in edges:
        edges.remove((u, v))

    else:
        edges.remove((v, u))


def draw_graph_iterations(edges, pos, path):

    current_edges = edges.copy()

    num_steps = len(path)

    cols = 4
    rows = (num_steps + cols - 1) // cols

    fig, axes = plt.subplots(rows, cols, figsize=(20, 5 * rows))

    if rows == 1:
        axes = [axes]

    axes = axes.flatten()

    current_path = [path[0]]

    for i in range(num_steps):

        ax = axes[i]

        if i > 0:

            u = path[i - 1]
            v = path[i]

            remove_edge(current_edges, u, v)

            current_path.append(v)

            ax.set_title(
                f"Step {i}: ({u}-{v})\n"
                f"{'->'.join(map(str, current_path))}",
                fontsize=9
            )

        else:
            ax.set_title("Start", fontsize=10)

        for edge in edges:

            x1, y1 = pos[edge[0]]
            x2, y2 = pos[edge[1]]

            if edge in current_edges or (edge[1], edge[0]) in current_edges:

                ax.plot(
                    [x1, x2],
                    [y1, y2],
                    'k-',
                    linewidth=2
                )

            else:

                ax.plot(
                    [x1, x2],
                    [y1, y2],
                    linestyle='dashed',
                    color='lightgray'
                )

        for node in pos:

            x, y = pos[node]

            circle = plt.Circle(
                (x, y),
                0.08,
                color='lightblue',
                ec='black'
            )

            ax.add_patch(circle)

            ax.text(
                x,
                y,
                str(node),
                ha='center',
                va='center'
            )

        ax.set_xlim(-1, 5)
        ax.set_ylim(-1, 4)

        ax.set_aspect('equal')

        ax.axis('off')

    for j in range(num_steps, len(axes)):
        axes[j].axis('off')

    plt.tight_layout()

    plt.show()


def main_manual():

    g1 = FleuryAlgorithmGraph([1, 2, 3, 4, 5])

    edges1 = [
        (1, 2),
        (2, 3),
        (3, 4),
        (4, 5),
        (5, 1),
        (1, 4),
        (5, 3),
        (1, 3)
    ]

    for u, v in edges1:
        g1.add_edge(u, v)

    print("--- Graph 1 Euler Path ---")

    path1 = g1.get_euler_path(4)

    print(path1)

    pos1 = {
        1: (0, 1),
        2: (1, 2),
        3: (2, 1),
        4: (2, 0),
        5: (0, 0)
    }

    draw_graph_iterations(edges1, pos1, path1)

    g2 = FleuryAlgorithmGraph([1, 2, 3, 4, 5])

    edges2 = [
        (1, 2),
        (2, 3),
        (3, 4),
        (4, 5),
        (5, 1),
        (1, 3),
        (1, 4),
        (2, 4),
        (2, 5),
        (3, 5)
    ]

    for u, v in edges2:
        g2.add_edge(u, v)

    print("\n--- Graph 2 Euler Circuit ---")

    path2 = g2.get_euler_path(1)

    print(path2)

    pos2 = {
        1: (0, 2),
        2: (2, 3),
        3: (4, 2),
        4: (3, 0),
        5: (1, 0)
    }

    draw_graph_iterations(edges2, pos2, path2)


if __name__ == "__main__":
    main_manual()