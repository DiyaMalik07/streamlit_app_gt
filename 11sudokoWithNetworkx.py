import networkx as nx
import matplotlib.pyplot as plt

def solve_sudoku_coloring(G, fixed_map):
    print("\n--- Coloring Trace for 4x4 Sudoku Graph ---")
    color_dict = fixed_map.copy()
    color_names = {0: 'Red (1)', 1: 'Blue (2)', 2: 'Green (3)', 3: 'Yellow (4)'}

    for node, c_id in color_dict.items():
        print(f"Vertex {node} -> FIXED CLUE assigned {color_names[c_id]}")

    for node in sorted(G.nodes()):
        if node not in color_dict:
            used_colors = {color_dict[nbr] for nbr in G.neighbors(node) if nbr in color_dict}

            for color in range(4):
                if color not in used_colors:
                    color_dict[node] = color
                    break

            assigned = color_names.get(color_dict.get(node, -1), 'UNSOLVABLE')
            print(f"Vertex {node} -> assigned {assigned}")

    chromatic_num = max(color_dict.values()) + 1
    print(f">> Chromatic Number achieved: {chromatic_num}")
    return color_dict

def apply_greedy_coloring(G, title, strategy_func=None):
    print(f"\n--- Coloring Trace for {title} ---")
    if strategy_func is None:
        strategy_func = lambda graph, colors: sorted(graph.nodes())

    color_dict = nx.greedy_color(G, strategy=strategy_func)
    color_names = {
        0: 'Red (R)', 1: 'Blue (B)', 2: 'Green (G)',
        3: 'Yellow (Y)', 4: 'Orange (O)', 5: 'Purple (P)',
        6: 'Cyan (C)', 7: 'Magenta (M)', 8: 'Brown (Br)'
    }
    color_hex = {
        0: '#FF6666', 1: '#66B2FF', 2: '#66FF66',
        3: '#FFFF66', 4: '#FFB266', 5: '#B266FF',
        6: '#66FFFF', 7: '#FF66FF', 8: '#CC9966'
    }

    for node in sorted(G.nodes()):
        c_id = color_dict[node]
        c_name = color_names.get(c_id, f'Color-{c_id}')
        print(f"Vertex {node} -> assigned {c_name}")

    node_colors = [color_hex.get(color_dict[node], '#CCCCCC') for node in G.nodes()]
    chromatic_num = max(color_dict.values()) + 1
    print(f">> Minimal Chromatic Number achieved: {chromatic_num}")
    return node_colors, color_dict

def main():
    fig, axes = plt.subplots(1, 2, figsize=(18, 8))
    fig.suptitle("Graph Coloring Algorithms", fontsize=18, fontweight='bold')

    G_sudoku = nx.Graph()
    row_straight, row_curved = [], []
    col_straight, col_curved = [], []
    block_edges = []

    for r in range(4):
        for c in range(4):
            G_sudoku.add_node((r, c))

    for r1 in range(4):
        for c1 in range(4):
            for r2 in range(4):
                for c2 in range(4):
                    if (r1, c1) < (r2, c2):  
                        if r1 == r2:
                            if abs(c1 - c2) == 1:
                                row_straight.append(((r1, c1), (r2, c2)))
                            else:
                                row_curved.append(((r1, c1), (r2, c2)))
                        elif c1 == c2:
                            if abs(r1 - r2) == 1:
                                col_straight.append(((r1, c1), (r2, c2)))
                            else:
                                col_curved.append(((r1, c1), (r2, c2)))
                        elif (r1//2 == r2//2) and (c1//2 == c2//2):
                            block_edges.append(((r1, c1), (r2, c2)))

    G_sudoku.add_edges_from(row_straight + row_curved + col_straight + col_curved + block_edges)
    pos_sudoku = {(r, c): (c, -r) for r in range(4) for c in range(4)}

    fixed_clues = {(0, 1): 2, (1, 2): 2, (3, 1): 1}
    cdict_sudoku = solve_sudoku_coloring(G_sudoku, fixed_clues)

    palette_sudoku = ['#FF6666', '#66B2FF', '#66FF66', '#FFFF66'] 
    num_map_sudoku = {0: '1', 1: '2', 2: '3', 3: '4'}

    colors_sudoku = [palette_sudoku[cdict_sudoku[node]] for node in G_sudoku.nodes()]
    labels_sudoku = {node: num_map_sudoku[cdict_sudoku[node]] for node in G_sudoku.nodes()}

    axes[0].set_title("4x4 Sudoku Graph (Straight Blocks, Curved Jumps)", fontsize=14, fontweight='bold')

    # 1. Straight lines (Rows = Crimson, Cols = SeaGreen, Blocks = DodgerBlue)
    nx.draw_networkx_edges(G_sudoku, pos_sudoku, ax=axes[0], edgelist=row_straight, 
                           edge_color='crimson', width=1.5, alpha=0.7)
    nx.draw_networkx_edges(G_sudoku, pos_sudoku, ax=axes[0], edgelist=col_straight, 
                           edge_color='seagreen', width=1.5, alpha=0.7)

    # Block diagonals are now drawn as pure straight lines
    nx.draw_networkx_edges(G_sudoku, pos_sudoku, ax=axes[0], edgelist=block_edges, 
                           edge_color='dodgerblue', width=1.5, alpha=0.8)

    # Use DiGraph method for drawing clean curves without arrowheads
    G_directed = nx.DiGraph(G_sudoku)

    # 2. Row curves
    for u, v in row_curved:
        rad = 0.4 if u[0] < 2 else -0.4
        nx.draw_networkx_edges(G_directed, pos_sudoku, ax=axes[0], edgelist=[(u,v)], 
                               edge_color='crimson', width=1.5, alpha=0.8, 
                               connectionstyle=f"arc3,rad={rad}",
                               arrows=True, arrowstyle='-')

    # 3. Column curves 
    for u, v in col_curved:
        rad = -0.4 if u[1] < 2 else 0.4
        nx.draw_networkx_edges(G_directed, pos_sudoku, ax=axes[0], edgelist=[(u,v)], 
                               edge_color='seagreen', width=1.5, alpha=0.8, 
                               connectionstyle=f"arc3,rad={rad}",
                               arrows=True, arrowstyle='-')

    # Draw Nodes and Labels
    nx.draw_networkx_nodes(G_sudoku, pos_sudoku, ax=axes[0], node_color=colors_sudoku, 
                           node_size=800, edgecolors='black', linewidths=1.5)
    nx.draw_networkx_labels(G_sudoku, pos_sudoku, ax=axes[0], labels=labels_sudoku, 
                            font_color='black', font_weight='bold', font_size=14)

    clue_nodes = list(fixed_clues.keys())
    clue_colors = [palette_sudoku[fixed_clues[node]] for node in clue_nodes]
    nx.draw_networkx_nodes(G_sudoku, pos_sudoku, ax=axes[0], nodelist=clue_nodes, 
                           node_color=clue_colors, node_size=800, edgecolors='black', linewidths=3.0)
    axes[0].axis('off')

    # --- Target MultiGraph ---
    G_multi = nx.MultiGraph()
    pos_multi = {
        'a': (0, 1), 'c': (0, 0), 'b': (1, 1), 'd': (1, 0),
        'g': (1.5, 0.5), 'e': (2, 1), 'f': (2, 0)
    }
    G_multi.add_nodes_from(pos_multi.keys())

    straight_edges_multi = [
        ('a', 'c'), ('a', 'b'), ('a', 'd'),
        ('c', 'b'), ('c', 'd'), ('b', 'd'), ('c', 'e'),
        ('b', 'e'), ('d', 'f'),
        ('a', 'g'), ('g', 'f'), ('g', 'e'), ('e', 'f')
    ]
    G_multi.add_edges_from(straight_edges_multi)
    G_multi.add_edge('e', 'f', key='curved')

    colors_multi, _ = apply_greedy_coloring(G_multi, "Target MultiGraph")

    axes[1].set_title("Target MultiGraph Coloring", fontsize=14, fontweight='bold')
    nx.draw_networkx_nodes(G_multi, pos_multi, ax=axes[1], node_color=colors_multi, node_size=600, edgecolors='black')
    nx.draw_networkx_labels(G_multi, pos_multi, ax=axes[1], font_color='black', font_weight='bold')
    nx.draw_networkx_edges(G_multi, pos_multi, ax=axes[1], edgelist=straight_edges_multi, edge_color='darkslateblue', width=2)
    nx.draw_networkx_edges(G_multi, pos_multi, ax=axes[1], edgelist=[('e', 'f')], connectionstyle='arc3, rad=-0.6', edge_color='darkslateblue', width=2)
    axes[1].axis('off')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()