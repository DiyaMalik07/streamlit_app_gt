import matplotlib.pyplot as plt

def solve_sudoku_coloring(nodes, neighbors_dict, fixed_map):
    print("\n--- Coloring Trace for 4x4 Sudoku Graph ---")
    color_dict = fixed_map.copy()
    color_names = {0: 'Red (1)', 1: 'Blue (2)', 2: 'Green (3)', 3: 'Yellow (4)'}

    for node, c_id in color_dict.items():
        print(f"Vertex {node} -> FIXED CLUE assigned {color_names[c_id]}")

    for node in sorted(nodes):
        if node not in color_dict:
            used_colors = {color_dict[nbr] for nbr in neighbors_dict[node] if nbr in color_dict}

            for color in range(4):
                if color not in used_colors:
                    color_dict[node] = color
                    break

            assigned = color_names.get(color_dict.get(node, -1), 'UNSOLVABLE')
            print(f"Vertex {node} -> assigned {assigned}")

    chromatic_num = max(color_dict.values()) + 1
    print(f">> Chromatic Number achieved: {chromatic_num}")
    return color_dict

def apply_greedy_coloring(nodes, neighbors_dict, title):
    print(f"\n--- Coloring Trace for {title} ---")
    
    color_dict = {}
    for node in sorted(nodes):
        used_colors = {color_dict[nbr] for nbr in neighbors_dict[node] if nbr in color_dict}
        color = 0
        while color in used_colors:
            color += 1
        color_dict[node] = color

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

    for node in sorted(nodes):
        c_id = color_dict[node]
        c_name = color_names.get(c_id, f'Color-{c_id}')
        print(f"Vertex {node} -> assigned {c_name}")

    node_colors = [color_hex.get(color_dict[node], '#CCCCCC') for node in nodes]
    chromatic_num = max(color_dict.values()) + 1
    print(f">> Minimal Chromatic Number achieved: {chromatic_num}")
    return node_colors, color_dict

def main():
    fig, axes = plt.subplots(1, 2, figsize=(18, 8))
    fig.suptitle("Graph Coloring Algorithms", fontsize=18, fontweight='bold')

    sudoku_nodes = [(r, c) for r in range(4) for c in range(4)]
    sudoku_neighbors = {node: set() for node in sudoku_nodes}
    
    row_straight, row_curved = [], []
    col_straight, col_curved = [], []
    block_edges = []

    for r1 in range(4):
        for c1 in range(4):
            for r2 in range(4):
                for c2 in range(4):
                    if (r1, c1) < (r2, c2):  
                        is_edge = False
                        if r1 == r2:
                            is_edge = True
                            if abs(c1 - c2) == 1:
                                row_straight.append(((r1, c1), (r2, c2)))
                            else:
                                row_curved.append(((r1, c1), (r2, c2)))
                        elif c1 == c2:
                            is_edge = True
                            if abs(r1 - r2) == 1:
                                col_straight.append(((r1, c1), (r2, c2)))
                            else:
                                col_curved.append(((r1, c1), (r2, c2)))
                        elif (r1//2 == r2//2) and (c1//2 == c2//2):
                            is_edge = True
                            block_edges.append(((r1, c1), (r2, c2)))
                        
                        if is_edge:
                            sudoku_neighbors[(r1, c1)].add((r2, c2))
                            sudoku_neighbors[(r2, c2)].add((r1, c1))

    pos_sudoku = {(r, c): (c, -r) for r in range(4) for c in range(4)}
    fixed_clues = {(0, 1): 2, (1, 2): 2, (3, 1): 1}
    cdict_sudoku = solve_sudoku_coloring(sudoku_nodes, sudoku_neighbors, fixed_clues)

    palette_sudoku = ['#FF6666', '#66B2FF', '#66FF66', '#FFFF66'] 
    num_map_sudoku = {0: '1', 1: '2', 2: '3', 3: '4'}

    ax0 = axes[0]
    ax0.set_title("4x4 Sudoku Graph (Straight Blocks, Curved Jumps)", fontsize=14, fontweight='bold')

    for u, v in row_straight:
        ax0.plot([pos_sudoku[u][0], pos_sudoku[v][0]], [pos_sudoku[u][1], pos_sudoku[v][1]], color='crimson', linewidth=1.5, alpha=0.7, zorder=1)
    for u, v in col_straight:
        ax0.plot([pos_sudoku[u][0], pos_sudoku[v][0]], [pos_sudoku[u][1], pos_sudoku[v][1]], color='seagreen', linewidth=1.5, alpha=0.7, zorder=1)
    for u, v in block_edges:
        ax0.plot([pos_sudoku[u][0], pos_sudoku[v][0]], [pos_sudoku[u][1], pos_sudoku[v][1]], color='dodgerblue', linewidth=1.5, alpha=0.8, zorder=1)

    for u, v in row_curved:
        rad = 0.4 if u[0] < 2 else -0.4
        p = plt.matplotlib.patches.FancyArrowPatch(pos_sudoku[u], pos_sudoku[v], connectionstyle=f"arc3,rad={rad}", color='crimson', linewidth=1.5, alpha=0.8, arrowstyle='-', zorder=1)
        ax0.add_patch(p)

    for u, v in col_curved:
        rad = -0.4 if u[1] < 2 else 0.4
        p = plt.matplotlib.patches.FancyArrowPatch(pos_sudoku[u], pos_sudoku[v], connectionstyle=f"arc3,rad={rad}", color='seagreen', linewidth=1.5, alpha=0.8, arrowstyle='-', zorder=1)
        ax0.add_patch(p)

    for node in sudoku_nodes:
        color = palette_sudoku[cdict_sudoku[node]]
        lw = 3.0 if node in fixed_clues else 1.5
        circle = plt.Circle(pos_sudoku[node], radius=0.12, facecolor=color, edgecolor='black', linewidth=lw, zorder=2)
        ax0.add_patch(circle)
        ax0.text(pos_sudoku[node][0], pos_sudoku[node][1], num_map_sudoku[cdict_sudoku[node]], color='black', weight='bold', fontsize=14, ha='center', va='center', zorder=3)

    ax0.set_xlim(-0.5, 3.5)
    ax0.set_ylim(-3.5, 0.5)
    ax0.axis('off')

    pos_multi = {
        'a': (0, 1), 'c': (0, 0), 'b': (1, 1), 'd': (1, 0),
        'g': (1.5, 0.5), 'e': (2, 1), 'f': (2, 0)
    }
    multi_nodes = list(pos_multi.keys())
    
    straight_edges_multi = [
        ('a', 'c'), ('a', 'b'), ('a', 'd'),
        ('c', 'b'), ('c', 'd'), ('b', 'd'), ('c', 'e'),
        ('b', 'e'), ('d', 'f'),
        ('a', 'g'), ('g', 'f'), ('g', 'e'), ('e', 'f')
    ]
    
    multi_neighbors = {node: set() for node in multi_nodes}
    for u, v in straight_edges_multi + [('e', 'f')]: 
        multi_neighbors[u].add(v)
        multi_neighbors[v].add(u)

    colors_multi, _ = apply_greedy_coloring(multi_nodes, multi_neighbors, "Target MultiGraph")

    ax1 = axes[1]
    ax1.set_title("Target MultiGraph Coloring", fontsize=14, fontweight='bold')

    for u, v in straight_edges_multi:
        ax1.plot([pos_multi[u][0], pos_multi[v][0]], [pos_multi[u][1], pos_multi[v][1]], color='darkslateblue', linewidth=2, zorder=1)
        
    p_multi = plt.matplotlib.patches.FancyArrowPatch(pos_multi['e'], pos_multi['f'], connectionstyle='arc3, rad=-0.6', color='darkslateblue', linewidth=2, arrowstyle='-', zorder=1)
    ax1.add_patch(p_multi)

    for i, node in enumerate(multi_nodes):
        circle = plt.Circle(pos_multi[node], radius=0.08, facecolor=colors_multi[i], edgecolor='black', linewidth=1, zorder=2)
        ax1.add_patch(circle)
        ax1.text(pos_multi[node][0], pos_multi[node][1], node, color='black', weight='bold', fontsize=12, ha='center', va='center', zorder=3)

    ax1.set_xlim(-0.3, 2.3)
    ax1.set_ylim(-0.3, 1.3)
    ax1.axis('off')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()