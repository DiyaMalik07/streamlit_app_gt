from __future__ import annotations

import base64
import html
from pathlib import Path

import streamlit as st

ROOT = Path(__file__).parent

# ── Student / college meta ─────────────────────────────────────────────────────
STUDENT_NAME   = "Diya Arun Malik"
ROLL_NO        = "24B-CO-020"
SEMESTER       = "Semester 4"
SUBJECT        = " CMP-226 GRAPH THEORY AND COMBINATORICS"
INSTITUTION    = "GOA COLLEGE OF ENGINEERING"
INSTITUTION_SUB = "Bhausaheb Bandodkar Technical Education Complex"
INSTITUTION_ADDR = "FARMAGUDI – 403 401, GOA"

# ── Experiment data ────────────────────────────────────────────────────────────
EXPERIMENTS = [
    {
        "id": "experiment1",
        "title": "Experiment 1: Standard Graph Models",
        "subject": "Graph Theory",
        "aim": (
            "To implement basic graphs such as complete graph, cycle graph, "
            "path graph and complete bipartite graph."
        ),
        "theory": (
            "A graph G = (V, E) consists of a set of vertices V and a set of edges E connecting pairs of vertices. "
            "Complete graphs K_n contain an edge between every pair of distinct vertices, giving each vertex degree n−1. "
            "Cycle graphs C_n form a closed loop of n vertices where every vertex has degree exactly 2. "
            "Complete bipartite graphs K_{m,n} partition vertices into two disjoint sets, "
            "with every vertex in one set adjacent to all vertices in the other set. "
            "Path graphs P_n are linear chains where consecutive vertices are connected and the two endpoints have degree 1. "
            "Null graphs contain only vertices with no edges, representing the simplest possible graph structure."
        ),
        "conclusion": (
            "The experiment successfully demonstrated the construction and visualization of fundamental graph types "
            "including complete, cycle, path, complete bipartite, wheel, and null graphs using NetworkX. "
            "Each graph's structural properties—degree sequence, edge count, and adjacency—were verified and "
            "matched the expected theoretical values, confirming the correctness of the implementations."
        ),
        "variants": [
            {
                "label": "Using NetworkX",
                "file_name": "1.py",
                "source_path": "1.py",
                "output_images": ["_cached_1_fig_0.png"],
                "output_text_path": "assets/outputs/experiment1-networkx.txt",
            }
        ],
    },
    {
        "id": "experiment2",
        "title": "Experiment 2: Graph Invariants and Isomorphism",
        "subject": "Graph Theory",
        "aim": (
            "To implement graph isomorphism verification in order to compare "
            "structural equivalence between two graphs."
        ),
        "theory": (
            "Two graphs G and H are isomorphic if there exists a bijection φ: V(G) → V(H) that preserves adjacency, "
            "i.e., edge (u,v) ∈ E(G) if and only if (φ(u), φ(v)) ∈ E(H). "
            "Graph invariants such as the number of vertices, edges, and sorted degree sequences are necessary "
            "conditions for isomorphism but are not sufficient on their own. "
            "The girth—the length of the shortest cycle—and the cycle structure serve as additional discriminating invariants. "
            "Graph isomorphism (GI) is a well-studied computational problem that lies between P and NP-complete. "
            "Isomorphic graphs represent structurally identical networks regardless of how their vertices are labelled or drawn. "
            "Practical algorithms such as VF2 use constraint propagation and backtracking to efficiently detect isomorphism."
        ),
        "conclusion": (
            "Graph isomorphism was successfully verified between structurally equivalent graphs using NetworkX's "
            "built-in VF2 isomorphism checker and a manual comparison of degree sequences, cycle structures, and girth. "
            "The experiment confirmed that two graphs are isomorphic only when all structural invariants coincide, "
            "and that matching degree sequences alone are insufficient to guarantee isomorphism."
        ),
        "variants": [
            {
                "label": "Using NetworkX",
                "file_name": "isomorphic2.py",
                "source_path": "isomorphic2.py",
                "output_images": ["_cached_isomorphic2_fig_0.png"],
                "output_text_path": "assets/outputs/experiment2-networkx.txt",
            },
            {
                "label": "Without NetworkX",
                "file_name": "2.py",
                "source_path": "2.py",
                "output_images": ["_cached_2_fig_0.png"],
                "output_text_path": "assets/outputs/experiment2-without-networkx.txt",
            },
        ],
    },
    {
        "id": "experiment3",
        "title": "Experiment 3: Spanning Trees and Subgraphs",
        "subject": "Graph Theory",
        "aim": (
            "To implement generation of various subgraphs such as induced subgraphs, "
            "spanning subgraphs and edge-deleted subgraphs."
        ),
        "theory": (
            "A subgraph H of graph G is a graph whose vertex set and edge set are subsets of those of G. "
            "An induced subgraph is formed by selecting a subset S ⊆ V(G) and retaining all edges of G with both endpoints in S. "
            "A spanning subgraph includes every vertex of G but may omit some edges, preserving the vertex set entirely. "
            "A spanning tree is a connected, acyclic spanning subgraph that uses exactly |V|−1 edges to connect all vertices. "
            "Edge-deleted subgraphs are constructed by removing one or more edges while keeping all vertices intact. "
            "Subgraph analysis is fundamental to decomposing networks, studying connectivity, and solving optimization problems."
        ),
        "conclusion": (
            "The experiment demonstrated the extraction of induced, spanning, and edge-deleted subgraphs from a base graph. "
            "Both NetworkX and manual implementations produced structurally consistent results, confirming the theoretical "
            "definitions of each subgraph type. The spanning tree was verified to connect all vertices with the minimum "
            "number of edges and no cycles, matching the expected properties."
        ),
        "variants": [
            {
                "label": "Using NetworkX",
                "file_name": "3_withNetworkx.py",
                "source_path": "3_withNetworkx.py",
                "output_images": ["_cached_3_withNetworkx_fig_0.png"],
                "output_text_path": "assets/outputs/experiment3-networkx.txt",
            },
            {
                "label": "Without NetworkX",
                "file_name": "3_withoutNetworkx.py",
                "source_path": "3_withoutNetworkx.py",
                "output_images": ["_cached_3_withoutNetworkx_fig_0.png"],
                "output_text_path": "assets/outputs/experiment3-without-networkx.txt",
            },
        ],
    },
    {
        "id": "experiment4",
        "title": "Experiment 4: Graphical Sequences",
        "subject": "Graph Theory",
        "aim": (
            "To implement construction of a graph for a given degree sequence in order to realize "
            "there is a graphical sequence using Havel-Hakimi algorithm."
        ),
        "theory": (
            "A degree sequence is a non-increasing list of non-negative integers representing the degrees of vertices in a graph. "
            "A sequence is called graphical if there exists a simple, undirected graph that realizes it. "
            "The Havel-Hakimi theorem provides a recursive test: sort the sequence in decreasing order, remove the largest degree d, "
            "and subtract 1 from the next d entries; repeat until all zeros appear (graphical) or a negative entry arises (not graphical). "
            "This algorithm also constructs the graph step by step by connecting the highest-degree vertex to its required neighbors. "
            "Graphical sequences are fundamental in network science for generating random graphs with prescribed degree distributions. "
            "The algorithm runs in O(n²) time and guarantees a valid simple graph for any valid degree sequence."
        ),
        "conclusion": (
            "The Havel-Hakimi algorithm was successfully implemented to verify graphical sequences and construct valid simple graphs. "
            "The experiment confirmed that the algorithm correctly identifies whether a given degree sequence is graphical "
            "and produces a concrete graph realization, with the resulting degree sequence matching the input after construction."
        ),
        "variants": [
            {
                "label": "Using NetworkX",
                "file_name": "4_withNetworkx.py",
                "source_path": "4_withNetworkx.py",
                "output_images": ["_cached_4_withNetworkx_fig_0.png"],
                "output_text_path": "assets/outputs/experiment4-networkx.txt",
            },
            {
                "label": "Without NetworkX",
                "file_name": "4_withoutNetworkx.py",
                "source_path": "4_withoutNetworkx.py",
                "output_images": ["_cached_4_withoutNetworkx_fig_0.png"],
                "output_text_path": "assets/outputs/experiment4-without-networkx.txt",
            },
        ],
    },
    {
        "id": "experiment5",
        "title": "Experiment 5: Line Graphs",
        "subject": "Graph Theory",
        "aim": (
            "To implement conversion of a given graph into a line graph where each vertex represents "
            "an edge of the original graph, and adjacency reflects shared endpoints."
        ),
        "theory": (
            "The line graph L(G) of a graph G is constructed by creating one vertex for each edge of G. "
            "Two vertices in L(G) are adjacent if and only if their corresponding edges in G share a common endpoint. "
            "If G has m edges, then L(G) has exactly m vertices; the number of edges in L(G) depends on the degree sequence of G. "
            "The degree of vertex e = {u,v} in L(G) equals deg(u) + deg(v) − 2 in the original graph G. "
            "Whitney's theorem states that two connected graphs with the same line graph are isomorphic, with the exception of K₃ and K_{1,3}. "
            "Line graphs are useful in edge-centric analysis, including modeling traffic flow, scheduling, and edge-coloring problems."
        ),
        "conclusion": (
            "Line graph conversion was successfully implemented, transforming each edge of the original graph into a vertex "
            "in the line graph. The adjacency structure was verified to correctly reflect shared endpoints, "
            "and the degree of each vertex in the line graph matched the formula deg(u) + deg(v) − 2, "
            "confirming the correctness of both the NetworkX and manual implementations."
        ),
        "variants": [
            {
                "label": "Using NetworkX",
                "file_name": "Line Graph With Networkx",
                "source_path": "5With_Networkx.py",
                "output_images": ["image.png"],
                "output_text_path": "assets/outputs/experiment5-networkx.txt",
            },
            {
                "label": "Without NetworkX",
                "file_name": "Line Graph Without Networkx",
                "source_path": "5Without_Networkx.py",
                "output_images": ["image copy.png"],
                "output_text_path": "assets/outputs/experiment5-without-networkx.txt",
            },
        ],
    },
    {
        "id": "experiment6",
        "title": "Experiment 6: Kruskals Algorithm",
        "subject": "Algorithms",
        "aim": (
            "To implement finding the minimum spanning tree for a given graph using Kruskal's algorithm, "
            "ensuring all vertices are connected with the minimum possible total edge weight and without forming cycles."
        ),
        "theory": (
            "A spanning tree of a connected graph G is a subgraph that includes all vertices and is both connected and acyclic, "
            "containing exactly |V|−1 edges. A Minimum Spanning Tree (MST) is a spanning tree whose total edge weight is minimized. "
            "Kruskal's algorithm sorts all edges in non-decreasing order of weight and greedily adds each edge that does not form a cycle, "
            "using a Union-Find (Disjoint Set Union) data structure to detect cycles efficiently. "
            "The algorithm runs in O(E log E) time, making it well-suited for sparse graphs. "
            "Its correctness is guaranteed by the Cut Property: for any cut of the graph, the minimum-weight crossing edge belongs to some MST."
        ),
        "conclusion": (
            "Kruskal's algorithm was successfully implemented to find the Minimum Spanning Tree of a weighted graph. "
            "The algorithm correctly sorted edges by weight, avoided cycles using Union-Find, and selected the minimum-weight "
            "set of edges that connects all vertices. The total MST weight and edge set matched the expected optimal solution."
        ),
        "variants": [
            {
                "label": "Using NetworkX",
                "file_name": "6withnetworkx.py",
                "source_path": "6withnetworkx.py",
                "output_images": ["_cached_6withnetworkx_fig_0.png"],
                "output_text_path": "assets/outputs/experiment6-networkx.txt",
            },
            {
                "label": "Without NetworkX",
                "file_name": "6withoutnetworkx.py",
                "source_path": "6withoutnetworkx.py",
                "output_images": ["_cached_6withoutnetworkx_fig_0.png"],
                "output_text_path": "assets/outputs/experiment6-without-networkx.txt",
            },
        ],
    },
    {
        "id": "experiment7",
        "title": "Experiment 7: Dijkstra Shortest Path",
        "subject": "Algorithms",
        "aim": (
            "To implement shortest path algorithm in order to compute shortest path from the "
            "source vertex to all the vertices in a weighted graph."
        ),
        "theory": (
            "Dijkstra's algorithm computes the shortest path from a single source vertex to all other vertices "
            "in a weighted graph with non-negative edge weights. "
            "It maintains a priority queue of vertices ordered by their tentative distance from the source, "
            "greedily selecting the closest unvisited vertex at each step and relaxing its neighbors' distances. "
            "A distance is 'relaxed' when a shorter path to a neighbor is discovered through the current vertex. "
            "With a binary heap, the algorithm runs in O((V + E) log V) time, making it efficient for large sparse graphs. "
            "Dijkstra's algorithm is the foundation of GPS navigation, OSPF routing protocols, and social network analysis. "
            "It fails on graphs with negative edge weights, for which the Bellman-Ford algorithm is used instead."
        ),
        "conclusion": (
            "Dijkstra's algorithm was implemented to compute shortest paths from a source vertex in a weighted graph. "
            "Both NetworkX and manual priority-queue implementations produced identical shortest-path distances and predecessor paths, "
            "validating the correctness of the greedy relaxation strategy and confirming the theoretical running time."
        ),
        "variants": [
            {
                "label": "Using NetworkX",
                "file_name": "7withnetworkx.py",
                "source_path": "7withnetworkx.py",
                "output_images": ["_cached_7withnetworkx_fig_0.png"],
                "output_text_path": "assets/outputs/experiment7-networkx.txt",
            },
            {
                "label": "Without NetworkX",
                "file_name": "7withoutnetworkx.py",
                "source_path": "7withoutnetworkx.py",
                "output_images": ["assets/outputs/experiment7-without-networkx.png"],
                "output_text_path": "assets/outputs/experiment7-without-networkx.txt",
            },
        ],
    },
    {
        "id": "experiment8",
        "title": "Experiment 8: Walks, Trails, and Closed Walks",
        "subject": "Graph Theory",
        "aim": (
            "To implement generation of closed walks, trails and paths in a connected graph."
        ),
        "theory": (
            "A walk in a graph is any sequence of vertices v₀, v₁, …, vₖ where consecutive vertices are adjacent, "
            "with vertices and edges allowed to repeat. "
            "A trail is a walk in which no edge is repeated, though vertices may be revisited. "
            "A path is a walk in which neither vertices nor edges are repeated, forming a simple route through the graph. "
            "A closed walk (circuit) begins and ends at the same vertex and may repeat edges and vertices internally. "
            "Eulerian trails use every edge exactly once; Hamiltonian paths visit every vertex exactly once. "
            "Understanding these structures is fundamental to analyzing connectivity, routing algorithms, and network flow."
        ),
        "conclusion": (
            "The experiment successfully generated walks, trails, and closed walks in a connected graph using both "
            "NetworkX and manual implementations. The output clearly illustrated the distinction between each structure: "
            "walks allowed repetitions, trails avoided repeated edges, and closed walks returned to the starting vertex. "
            "All generated sequences were verified against the adjacency structure of the graph."
        ),
        "variants": [
            {
                "label": "Using NetworkX",
                "file_name": "8withNetworkx.py",
                "source_path": "8withNetworkx.py",
                "output_images": ["_cached_8withNetworkx_fig_0.png"],
                "output_text_path": "assets/outputs/experiment8-networkx.txt",
            },
            {
                "label": "Without NetworkX",
                "file_name": "8withoutNetworkx.py",
                "source_path": "8withoutNetworkx.py",
                "output_images": ["_cached_8withoutNetworkx_fig_0.png"],
                "output_text_path": "assets/outputs/experiment8-without-networkx.txt",
            },
        ],
    },
    {
        "id": "experiment9",
        "title": "Experiment 9: Eulerian Circuits",
        "subject": "Graph Theory",
        "aim": (
            "To implement an algorithm that checks for the existence of an Eulerian circuit "
            "and construct a circuit that traverses every edge of the graph exactly once."
        ),
        "theory": (
            "An Eulerian circuit is a closed walk in a connected graph that visits every edge exactly once "
            "and returns to the starting vertex. "
            "Euler's theorem (1736) states that a connected graph possesses an Eulerian circuit if and only if "
            "every vertex has even degree. "
            "Hierholzer's algorithm efficiently constructs an Eulerian circuit in O(V + E) time by maintaining a stack "
            "and splicing together sub-circuits discovered during the traversal. "
            "If exactly two vertices have odd degree, the graph contains an Eulerian path (trail) but no circuit. "
            "The concept originated from Euler's celebrated solution to the Königsberg Bridge Problem, "
            "marking the birth of graph theory. "
            "Eulerian circuits have practical applications in circuit board testing, DNA fragment assembly, and postal routing."
        ),
        "conclusion": (
            "Eulerian circuits were successfully identified and constructed using both NetworkX's built-in method "
            "and Hierholzer's algorithm implemented manually. "
            "The experiment confirmed that all vertices of the test graph had even degree, satisfying the necessary "
            "and sufficient condition for an Eulerian circuit to exist, and the constructed circuit traversed every edge exactly once."
        ),
        "variants": [
            {
                "label": "Using NetworkX",
                "file_name": "9withnetworkx.py",
                "source_path": "9withnetworkx.py",
                "output_images": ["_cached_9withnetworkx_fig_0.png", "_cached_9withnetworkx_fig_1.png"],
                "output_text_path": "assets/outputs/experiment9-networkx.txt",
            },
            {
                "label": "Without NetworkX",
                "file_name": "9withoutNetworkx.py",
                "source_path": "9withoutNetworkx.py",
                "output_images": ["_cached_9withoutNetworkx_fig_0.png", "_cached_9withoutNetworkx_fig_1.png"],
                "output_text_path": "assets/outputs/experiment9-without-networkx.txt",
            },
        ],
    },
    {
        "id": "experiment10",
        "title": "Experiment 10: Hamiltonian Circuits",
        "subject": "Graph Theory",
        "aim": (
            "To implement a method that determines whether a graph contains a Hamiltonian circuit "
            "i.e. a cycle that visits every vertex exactly once."
        ),
        "theory": (
            "A Hamiltonian circuit is a cycle in a graph that visits every vertex exactly once before returning "
            "to the starting vertex. "
            "Unlike Eulerian circuits, determining whether a Hamiltonian circuit exists is NP-complete—no polynomial-time "
            "algorithm is known for the general case. "
            "Backtracking algorithms explore all possible vertex orderings, pruning branches where adjacency constraints are violated. "
            "Ore's theorem provides a sufficient condition: if deg(u) + deg(v) ≥ n for every pair of non-adjacent vertices u, v, "
            "the graph is Hamiltonian. "
            "Dirac's theorem simplifies this: if every vertex has degree ≥ n/2, the graph contains a Hamiltonian circuit. "
            "Hamiltonian circuits are central to the Travelling Salesman Problem (TSP) and arise in genome assembly and scheduling."
        ),
        "conclusion": (
            "The backtracking algorithm successfully determined the existence of Hamiltonian circuits in the test graphs. "
            "The algorithm found a valid Hamiltonian cycle in the first graph, confirming that it satisfies Dirac's degree condition, "
            "while correctly reporting no Hamiltonian circuit for the second graph due to the presence of a cut vertex, "
            "which prevents a closed loop that visits every vertex exactly once."
        ),
        "variants": [
            {
                "label": "Using NetworkX",
                "file_name": "10withNetworkx.py",
                "source_path": "10withNetworkx.py",
                "output_images": ["_cached_10withNetworkx_fig_0.png", "_cached_10withNetworkx_fig_1.png"],
                "output_text_path": "assets/outputs/experiment10-networkx.txt",
            },
            {
                "label": "Without NetworkX",
                "file_name": "10withoutNetworkx.py",
                "source_path": "10withoutNetworkx.py",
                "output_images": ["_cached_10withoutNetworkx_fig_0.png"],
                "output_text_path": "assets/outputs/experiment10-without-networkx.txt",
            },
        ],
    },
    {
        "id": "experiment11",
        "title": "Experiment 11: Coloring and Sudoku",
        "subject": "Graph Coloring",
        "aim": (
            "To implement the greedy graph coloring that assigns colors to the vertices such that no two "
            "adjacent vertices share the same color with minimal chromatic number."
        ),
        "theory": (
            "Graph coloring assigns labels (colors) to vertices such that no two adjacent vertices share the same color; "
            "the minimum number of colors required is called the chromatic number χ(G). "
            "The greedy coloring algorithm processes vertices in a given order and assigns each vertex the smallest "
            "color not used by any of its already-colored neighbors—it may not always achieve χ(G). "
            "The Four Color Theorem guarantees that every planar graph can be colored with at most four colors. "
            "Sudoku puzzles are a direct application: each cell maps to a vertex, with edges connecting cells "
            "in the same row, column, or 2×2 box, and the chromatic number equals 4 for a standard 4×4 puzzle. "
            "Graph coloring has broad applications in register allocation in compilers, exam scheduling, "
            "and frequency assignment in wireless communication networks."
        ),
        "conclusion": (
            "The greedy graph coloring algorithm successfully assigned colors to graph vertices with chromatic number 4. "
            "The Sudoku puzzle was modeled as a graph coloring problem, and the coloring correctly satisfied all "
            "row, column, and 2×2 box constraints with exactly 4 colors. "
            "Both the NetworkX and manual implementations produced valid colorings, confirming the "
            "correctness of the greedy approach for this class of structured constraint graphs."
        ),
        "variants": [
            {
                "label": "Graph Coloring — Using NetworkX",
                "file_name": "11usingnetworkx.py",
                "source_path": "11usingnetworkx.py",
                "output_images": ["_cached_11usingnetworkx_fig_0.png"],
                "output_text_path": "assets/outputs/experiment11-colouring-networkx.txt",
            },
            {
                "label": "Graph Coloring — Without NetworkX",
                "file_name": "11withoutNetworkx.py",
                "source_path": "11withoutNetworkx.py",
                "output_images": ["image copy 3.png"],
                "output_text_path": "assets/outputs/experiment11-colouring-without-networkx.txt",
            },
            {
                "label": "Sudoku — Using NetworkX",
                "file_name": "11sudokoWithNetworkx.py",
                "source_path": "11sudokoWithNetworkx.py",
                "output_images": ["image copy 2.png"],
                "output_text_path": "assets/outputs/experiment11-sudoku-networkx.txt",
            },
            {
                "label": "Sudoku — Without NetworkX",
                "file_name": "11sudokoWithoutNetworkx.py",
                "source_path": "11sudokoWithoutNetworkx.py",
                "output_images": ["assets/outputs/experiment11-sudoku-without-networkx.png"],
                "output_text_path": "assets/outputs/experiment11-sudoku-without-networkx.txt",
            },
        ],
    },
]


# ── Helpers ────────────────────────────────────────────────────────────────────
def img_to_b64(path: Path) -> str:
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()


@st.cache_data(show_spinner=False)
def read_text(relative_path: str) -> str:
    path = ROOT / relative_path
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8", errors="replace")


def find_experiment(experiment_id: str) -> dict:
    return next(item for item in EXPERIMENTS if item["id"] == experiment_id)


def set_selected(experiment_id: str | None) -> None:
    st.session_state.selected_experiment_id = experiment_id


# ── CSS ────────────────────────────────────────────────────────────────────────
def inject_css() -> None:
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap');

        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif;
        }

        /* ── Page background ── */
        .stApp {
            background: #f5f6fa;
        }

        .block-container {
            padding-top: 0 !important;
            padding-bottom: 4rem;
            max-width: 1200px;
        }

        /* ── Header ── */
        .gtc-header {
            background: linear-gradient(120deg, #fdfbfb 0%, #ebedee 100%);
            padding: 1.8rem 2rem;
            margin: -1rem -1rem 1.5rem -1rem;
            display: flex;
            align-items: center;
            justify-content: center;
            border-bottom: 4px solid #3b82f6;
            border-radius: 0 0 16px 16px;
            box-shadow: 0 8px 24px rgba(0, 0, 0, 0.06);
        }

        .gtc-header img {
            height: 100px;
            width: auto;
            object-fit: contain;
            flex-shrink: 0;
        }

        .gtc-header-text {
            flex: 1;
            text-align: center;
        }

        .gtc-header-text .college {
            font-size: 1.15rem;
            font-weight: 900;
            color: #0f172a;
            letter-spacing: 0.1em;
            text-transform: uppercase;
            margin: 0 0 0.2rem;
        }

        .gtc-header-text .college-sub {
            font-size: 0.85rem;
            font-weight: 700;
            color: #3b82f6;
            letter-spacing: 0.05em;
            margin: 0 0 0.15rem;
        }

        .gtc-header-text .college-addr {
            font-size: 0.72rem;
            font-weight: 600;
            color: #64748b;
            letter-spacing: 0.06em;
            text-transform: uppercase;
            margin: 0 0 0.5rem;
        }

        .gtc-header-text h1 {
            font-size: clamp(1.3rem, 2.8vw, 1.8rem);
            font-weight: 900;
            margin: 0.4rem 0 0;
            letter-spacing: 0.02em;
            background: linear-gradient(90deg, #1e40af, #3b82f6);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            line-height: 1.2;
        }

        /* ── Dashboard cards ── */
        .exp-card {
            background: white;
            border: 1px solid #e2e8f0;
            border-radius: 12px;
            padding: 1.2rem 1rem 1rem;
            height: 100%;
            box-shadow: 0 2px 8px rgba(0,0,0,0.05);
            transition: box-shadow 0.2s;
        }

        .exp-card:hover {
            box-shadow: 0 6px 20px rgba(0,0,0,0.1);
        }

        .exp-tag {
            display: inline-block;
            padding: 0.22rem 0.6rem;
            border-radius: 20px;
            background: #dbeafe;
            color: #1d4ed8;
            font-size: 0.7rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }

        .exp-card h3 {
            margin: 0.6rem 0 0.4rem;
            font-size: 0.95rem;
            font-weight: 700;
            color: #1e293b;
            line-height: 1.3;
        }

        .exp-card .aim-text {
            font-size: 0.82rem;
            color: #64748b;
            line-height: 1.5;
            margin: 0;
        }

        /* ── Section labels ── */
        .section-label {
            display: flex;
            align-items: center;
            gap: 0.5rem;
            font-size: 0.7rem;
            font-weight: 800;
            text-transform: uppercase;
            letter-spacing: 0.1em;
            color: #64748b;
            margin: 1.4rem 0 0.5rem;
        }

        .section-label::after {
            content: '';
            flex: 1;
            height: 1px;
            background: #e2e8f0;
        }

        /* ── Theory box ── */
        .theory-box {
            background: #f8fafc;
            border-left: 4px solid #3b82f6;
            border-radius: 0 8px 8px 0;
            padding: 1rem 1.2rem;
            font-size: 0.92rem;
            color: #334155;
            line-height: 1.75;
            margin-bottom: 0.5rem;
        }

        /* ── Aim box ── */
        .aim-box {
            background: #eff6ff;
            border: 1px solid #bfdbfe;
            border-radius: 8px;
            padding: 0.75rem 1.1rem;
            font-size: 0.93rem;
            color: #1e40af;
            font-weight: 500;
            line-height: 1.5;
            margin-bottom: 0.3rem;
        }

        /* ── Conclusion box ── */
        .conclusion-box {
            background: #f0fdf4;
            border-left: 4px solid #22c55e;
            border-radius: 0 8px 8px 0;
            padding: 1rem 1.2rem;
            font-size: 0.92rem;
            color: #166534;
            line-height: 1.75;
        }

        /* ── Console box ── */
        .console-box {
            min-height: 140px;
            max-height: 340px;
            overflow: auto;
            padding: 1rem 1.1rem;
            border-radius: 8px;
            background: #0b1220;
            color: #39ff88;
            font-family: 'JetBrains Mono', Consolas, monospace;
            font-size: 0.82rem;
            white-space: pre-wrap;
            line-height: 1.6;
        }

        /* ── Source path ── */
        .source-path {
            color: #94a3b8;
            font-family: 'JetBrains Mono', Consolas, monospace;
            font-size: 0.78rem;
            margin: 0 0 0.6rem;
        }

        /* ── Code block max height ── */
        div[data-testid="stCodeBlock"] {
            max-height: 620px;
            overflow: auto;
            border-radius: 8px;
        }

        /* ── Experiment detail header ── */
        .exp-detail-header {
            background: white;
            border: 1px solid #e2e8f0;
            border-radius: 12px;
            padding: 1.2rem 1.4rem;
            margin-bottom: 1rem;
            box-shadow: 0 2px 8px rgba(0,0,0,0.04);
        }

        .exp-detail-header .exp-num {
            font-size: 0.68rem;
            font-weight: 800;
            color: #6366f1;
            text-transform: uppercase;
            letter-spacing: 0.12em;
            margin: 0;
        }

        .exp-detail-header h2 {
            font-size: 1.3rem;
            font-weight: 800;
            color: #0f172a;
            margin: 0.2rem 0 0;
        }

        /* ── Footer ── */
        .gtc-footer {
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            background: linear-gradient(90deg, #bfdbfe 0%, #dbeafe 50%, #bfdbfe 100%);
            color: #1e3a5f;
            text-align: center;
            padding: 0.6rem 1rem;
            font-size: 0.82rem;
            font-weight: 600;
            letter-spacing: 0.05em;
            border-top: 2px solid #1d4ed8;
            z-index: 9999;
            box-shadow: 0 -2px 10px rgba(30,64,175,0.12);
        }

        .gtc-footer span {
            color: #1d4ed8;
            font-weight: 800;
        }

        /* ── Sidebar ── */
        section[data-testid="stSidebar"] {
            background: #0f172a;
        }

        section[data-testid="stSidebar"] * {
            color: #cbd5e1 !important;
        }

        section[data-testid="stSidebar"] .stRadio label {
            font-size: 0.82rem !important;
        }

        /* Hide default streamlit header */
        header[data-testid="stHeader"] {
            background: transparent;
            height: 0;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


# ── Header ─────────────────────────────────────────────────────────────────────
def render_header() -> None:
    logo_path = ROOT / "assets" / "gec_logo.png"
    logo_html = ""
    if logo_path.exists():
        b64 = img_to_b64(logo_path)
        logo_html = f'<img src="data:image/png;base64,{b64}" alt="GEC Logo" />'

    st.markdown(
        f"""
        <div class="gtc-header">
            <div class="gtc-header-text">
                <p class="college">{html.escape(INSTITUTION)}</p>
                <p class="college-sub">{html.escape(INSTITUTION_SUB)}</p>
                <p class="college-addr">{html.escape(INSTITUTION_ADDR)}</p>
                <h1>{html.escape(SUBJECT)}</h1>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


# ── Footer ─────────────────────────────────────────────────────────────────────
def render_footer() -> None:
    st.markdown(
        f"""
        <div class="gtc-footer">
            <span>{html.escape(STUDENT_NAME)}</span>
            &nbsp;|&nbsp;
            <span>{html.escape(ROLL_NO)}</span>
            &nbsp;|&nbsp;
            <span>{html.escape(SEMESTER)}</span>
        </div>
        """,
        unsafe_allow_html=True,
    )


# ── Sidebar ────────────────────────────────────────────────────────────────────
def render_sidebar() -> None:
    st.sidebar.markdown(
        "<h2 style='color:#f59e0b;font-size:1rem;margin-bottom:0.2rem;'>📂 Navigation</h2>",
        unsafe_allow_html=True,
    )
    st.sidebar.caption("Select an experiment to view details.")

    options = ["🏠  Dashboard"] + [
        f"{exp['id'].replace('experiment','Exp ')} — {exp['title'].split(':')[1].strip()}"
        for exp in EXPERIMENTS
    ]

    selected_id = st.session_state.get("selected_experiment_id")
    selected_index = 0
    if selected_id:
        try:
            exp = find_experiment(selected_id)
            label = f"{exp['id'].replace('experiment','Exp ')} — {exp['title'].split(':')[1].strip()}"
            selected_index = options.index(label)
        except (ValueError, StopIteration):
            selected_index = 0

    choice = st.sidebar.radio(
        "nav",
        options,
        index=selected_index,
        label_visibility="collapsed",
    )

    if choice == "🏠  Dashboard":
        st.session_state.selected_experiment_id = None
    else:
        label = choice.split(" — ")[0].replace("Exp ", "experiment").replace(" ", "")
        # map "experiment1" correctly
        num = choice.split(" — ")[0].replace("Exp ", "").strip()
        matched = next(
            (e for e in EXPERIMENTS if e["id"] == f"experiment{num}"),
            None,
        )
        if matched:
            st.session_state.selected_experiment_id = matched["id"]

    st.sidebar.markdown("---")
    total_variants = sum(len(e["variants"]) for e in EXPERIMENTS)
    st.sidebar.metric("Total Experiments", len(EXPERIMENTS))
    st.sidebar.metric("Total Code Files", total_variants)


# ── Dashboard ──────────────────────────────────────────────────────────────────
def render_dashboard() -> None:
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(
        "<h2 style='font-size:1.15rem;font-weight:800;color:#0f172a;margin-bottom:0.2rem;'>"
        "📋 Experiment Index</h2>",
        unsafe_allow_html=True,
    )
    st.caption("Click **Open** on any experiment to view its aim, theory, source code, output, and conclusion.")
    st.markdown("<br>", unsafe_allow_html=True)

    for start in range(0, len(EXPERIMENTS), 3):
        cols = st.columns(3, gap="medium")
        for col, exp in zip(cols, EXPERIMENTS[start: start + 3]):
            with col:
                num = exp["id"].replace("experiment", "")
                card_html = f"""
                <div class="exp-card">
                    <span class="exp-tag">Exp {num}</span>
                    <h3>{html.escape(exp["title"].split(":", 1)[1].strip())}</h3>
                    <p class="aim-text">{html.escape(exp["aim"])}</p>
                </div>
                """
                st.markdown(card_html, unsafe_allow_html=True)
                st.write("")
                if st.button("Open →", key=f"open-{exp['id']}",
                             use_container_width=True):
                    set_selected(exp["id"])
                    st.rerun()
        st.markdown("<br>", unsafe_allow_html=True)


# ── Console output ─────────────────────────────────────────────────────────────
def render_console(text: str) -> None:
    clean = html.escape(text.strip()) if text.strip() else "[No console output]"
    st.markdown(
        f"<pre class='console-box'>{clean}</pre>",
        unsafe_allow_html=True,
    )


# ── Single variant tab ─────────────────────────────────────────────────────────
def render_variant(variant: dict) -> None:
    left, right = st.columns([1.1, 0.9], gap="large")

    with left:
        st.markdown(
            f"<p class='source-path'>📄 {html.escape(variant['source_path'])}</p>",
            unsafe_allow_html=True,
        )
        st.code(read_text(variant["source_path"]), language="python")

    with right:
        st.markdown(
            "<div class='section-label'>📸 Output Screenshot</div>",
            unsafe_allow_html=True,
        )
        images = [ROOT / p for p in variant["output_images"]]
        existing = [p for p in images if p.exists()]
        if existing:
            for p in existing:
                st.image(str(p), use_container_width=True)
        else:
            st.info("No output screenshot available.")

        st.markdown(
            "<div class='section-label'>🖥 Console Output</div>",
            unsafe_allow_html=True,
        )
        render_console(read_text(variant["output_text_path"]))


# ── Experiment detail page ─────────────────────────────────────────────────────
def render_detail(exp: dict) -> None:
    if st.button("← Back to Dashboard"):
        set_selected(None)
        st.rerun()

    num = exp["id"].replace("experiment", "")

    # ── Header card ──
    st.markdown(
        f"""
        <div class="exp-detail-header">
            <p class="exp-num">Experiment {num} &nbsp;·&nbsp; {html.escape(exp['subject'])}</p>
            <h2>{html.escape(exp['title'])}</h2>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ── AIM ──
    st.markdown(
        "<div class='section-label'>🎯 Aim</div>",
        unsafe_allow_html=True,
    )
    st.markdown(
        f"<div class='aim-box'>{html.escape(exp['aim'])}</div>",
        unsafe_allow_html=True,
    )

    # ── THEORY ──
    st.markdown(
        "<div class='section-label'>📖 Theory</div>",
        unsafe_allow_html=True,
    )
    st.markdown(
        f"<div class='theory-box'>{html.escape(exp['theory'])}</div>",
        unsafe_allow_html=True,
    )

    # ── SOURCE CODE & OUTPUT ──
    st.markdown(
        "<div class='section-label'>💻 Source Code & Output</div>",
        unsafe_allow_html=True,
    )

    variants = exp["variants"]
    if not variants:
        st.warning("No code files found for this experiment.")
        return

    tabs = st.tabs([v["label"] for v in variants])
    for tab, variant in zip(tabs, variants):
        with tab:
            render_variant(variant)

    # ── CONCLUSION ──
    st.markdown(
        "<div class='section-label'>✅ Conclusion</div>",
        unsafe_allow_html=True,
    )
    st.markdown(
        f"<div class='conclusion-box'>{html.escape(exp['conclusion'])}</div>",
        unsafe_allow_html=True,
    )

    st.markdown("<br><br>", unsafe_allow_html=True)


# ── Main ───────────────────────────────────────────────────────────────────────
def main() -> None:
    st.set_page_config(
        page_title=f"{SUBJECT} — Lab Repository",
        page_icon="📐",
        layout="wide",
    )
    inject_css()

    if "selected_experiment_id" not in st.session_state:
        st.session_state.selected_experiment_id = None

    render_header()
    render_sidebar()
    render_footer()

    st.write("")

    selected_id = st.session_state.get("selected_experiment_id")
    if selected_id:
        render_detail(find_experiment(selected_id))
    else:
        render_dashboard()


if __name__ == "__main__":
    main()
