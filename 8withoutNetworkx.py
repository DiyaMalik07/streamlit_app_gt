import matplotlib.pyplot as plt


class Graph:

    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):

        if u not in self.graph:
            self.graph[u] = []

        if v not in self.graph:
            self.graph[v] = []

        self.graph[u].append(v)
        self.graph[v].append(u)

    def shortest_path(self, start, end):

        queue = [[start]]
        visited = []

        while queue:

            path = queue.pop(0)
            node = path[-1]

            if node == end:
                return path

            if node not in visited:

                visited.append(node)

                for neighbour in self.graph[node]:

                    new_path = list(path)
                    new_path.append(neighbour)

                    queue.append(new_path)

        return []

    def all_paths(self, start, end, path=[]):

        path = path + [start]

        if start == end:
            return [path]

        paths = []

        for node in self.graph[start]:

            if node not in path:

                newpaths = self.all_paths(node, end, path)

                for p in newpaths:
                    paths.append(p)

        return paths

    def find_cycle(self, start):

        visited = []

        def dfs(node, parent, path):

            visited.append(node)
            path.append(node)

            for neighbour in self.graph[node]:

                if neighbour == parent:
                    continue

                if neighbour in path:
                    cycle_start = path.index(neighbour)
                    return path[cycle_start:] + [neighbour]

                if neighbour not in visited:

                    result = dfs(neighbour, node, path.copy())

                    if result:
                        return result

            return None

        return dfs(start, None, [])


def draw_graph(ax, edges, pos, title, highlight_nodes=None, highlight_edges=None):

    ax.set_title(title)

    for u, v in edges:

        x1, y1 = pos[u]
        x2, y2 = pos[v]

        color = 'gray'
        width = 1.5

        if highlight_edges and ((u, v) in highlight_edges or (v, u) in highlight_edges):
            color = 'red'
            width = 3

        ax.plot([x1, x2], [y1, y2], color=color, linewidth=width)

    for node, (x, y) in pos.items():

        color = 'lightblue'

        if highlight_nodes and node in highlight_nodes:
            color = 'orange'

        circle = plt.Circle((x, y), 0.08, color=color, ec='black')
        ax.add_patch(circle)

        ax.text(x, y, node, ha='center', va='center', fontsize=10)

    ax.set_xlim(-1, 3)
    ax.set_ylim(-1, 3)
    ax.set_aspect('equal')
    ax.axis('off')


def edges_from_path(path):

    edges = []

    for i in range(len(path) - 1):
        edges.append((path[i], path[i + 1]))

    return edges


def main():

    fig, axes = plt.subplots(2, 4, figsize=(18, 10))

    g1 = Graph()

    edges1 = [
        ('A', 'B'),
        ('B', 'C'),
        ('C', 'D'),
        ('F', 'D'),
        ('A', 'F'),
        ('A', 'D'),
        ('F', 'C'),
        ('A', 'C')
    ]

    for u, v in edges1:
        g1.add_edge(u, v)

    pos1 = {
        'A': (0, 1),
        'B': (1, 2),
        'C': (2, 1),
        'F': (0, 0),
        'D': (2, 0)
    }

    path1 = g1.shortest_path('B', 'D')

    all_paths1 = g1.all_paths('B', 'D')
    trail1 = max(all_paths1, key=len)

    walk1 = g1.find_cycle('A')

    print("\n--- Graph 1 Results ---")
    print("Path:", path1)
    print("Trail:", trail1)
    print("Walk:", walk1)

    draw_graph(
        axes[0][0],
        edges1,
        pos1,
        "Graph 1"
    )

    draw_graph(
        axes[0][1],
        edges1,
        pos1,
        "Path",
        path1,
        edges_from_path(path1)
    )

    draw_graph(
        axes[0][2],
        edges1,
        pos1,
        "Trail",
        trail1,
        edges_from_path(trail1)
    )

    draw_graph(
        axes[0][3],
        edges1,
        pos1,
        "Closed Walk",
        walk1,
        edges_from_path(walk1)
    )

    g2 = Graph()

    edges2 = [
        ('A', 'B'),
        ('B', 'C'),
        ('C', 'E'),
        ('D', 'E'),
        ('A', 'D'),
        ('A', 'C'),
        ('A', 'E'),
        ('B', 'D'),
        ('B', 'E'),
        ('C', 'D')
    ]

    for u, v in edges2:
        g2.add_edge(u, v)

    pos2 = {
        'A': (0, 1),
        'B': (1, 2),
        'C': (2, 1),
        'D': (0.5, 0),
        'E': (1.8, 0)
    }

    path2 = g2.shortest_path('A', 'E')

    all_paths2 = g2.all_paths('A', 'E')
    trail2 = max(all_paths2, key=len)

    walk2 = g2.find_cycle('A')

    print("\n--- Graph 2 Results ---")
    print("Path:", path2)
    print("Trail:", trail2)
    print("Walk:", walk2)

    draw_graph(
        axes[1][0],
        edges2,
        pos2,
        "Graph 2"
    )

    draw_graph(
        axes[1][1],
        edges2,
        pos2,
        "Path",
        path2,
        edges_from_path(path2)
    )

    draw_graph(
        axes[1][2],
        edges2,
        pos2,
        "Trail",
        trail2,
        edges_from_path(trail2)
    )

    draw_graph(
        axes[1][3],
        edges2,
        pos2,
        "Closed Walk",
        walk2,
        edges_from_path(walk2)
    )

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()