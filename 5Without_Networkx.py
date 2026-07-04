import matplotlib.pyplot as plt 
import numpy as np 

def userInput(): 
    rows = int(input("Enter number of rows: ")) 
    m = np.zeros((rows, rows)) 
    for i in range(rows): 
        for j in range(rows): 
            m[i][j] = eval(input(f'Enter value of m[{i}][{j}]: ')) 
    return m 

def buildGraph(m): 
    rows = m.shape[0] 
    nodes = [] 
    edges = [] 
    for i in range(rows): 
        for j in range(i+1): 
            if m[i][j] > 0: 
                for node in nodes: 
                    if node[0] == i or node[1] == i or node[0] == j or node[1] == j: 
                        edges.append(((i, j), node)) 
                nodes.append((i, j)) 
    return nodes, edges 

def plotGraph(nodes, edges): 
    fig, ax = plt.subplots() 
    pos = {node: node for node in nodes} 
    # draw edges 
    for n1, n2 in edges: 
        x = [pos[n1][0], pos[n2][0]] 
        y = [pos[n1][1], pos[n2][1]] 
        ax.plot(x, y, 'b-') 
    for node in nodes: 
        ax.plot(*pos[node], 'ro', markersize=10) 
        ax.annotate(str(node), pos[node], textcoords="offset points", xytext=(5,5)) 
    plt.show() 

# main 
if __name__ == "__main__":
    m = userInput() 
    nodes, edges = buildGraph(m) 
    plotGraph(nodes, edges)