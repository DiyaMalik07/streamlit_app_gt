import networkx as nx 
import matplotlib.pyplot as plt 
import numpy as np 

#user input 
def userInput(): 
    rows = int(input("Enter number of rows: ")) 
    m = np.zeros((rows, rows)) 
    for i in range(rows): 
        for j in range(rows): 
            m[i][j] = eval(input(f'Enter value of m[{i}][{j}]: ')) 
    return m 

def buildGraph(m): 
    G = nx.Graph() 
    rows = m.shape[0] 
    for i in range(rows): 
        for j in range(i+1): 
            if m[i][j] > 0: 
                G.add_node((i, j)) 
                
    nodes = list(G.nodes) 
    for n1 in nodes: 
        for n2 in nodes: 
            if n1 != n2 and (n1[0] == n2[0] or n1[1] == n2[1] or n1[0] == n2[1] or n1[1] == n2[0]): 
                G.add_edge(n1, n2)
                
    return G 

#plot graph 
def plotGraph(G): 
    nx.draw(G, with_labels=True) 
    plt.show() 

#main 
if __name__ == "__main__":
    m = userInput() 
    G = buildGraph(m) 
    plotGraph(G)