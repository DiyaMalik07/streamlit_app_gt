import matplotlib.pyplot as plt

edges=[
(1,2),(1,4),(1,5),(1,3),
(2,3),(2,4),
(3,5),(3,7),(3,6),
(4,5),
(5,6),(5,7),
(6,7),(6,9),(6,10),
(7,8),(7,9),
(8,9),
(9,10)
]

graph={}
for u,v in edges:
    graph.setdefault(u,[]).append(v)
    graph.setdefault(v,[]).append(u)

def greedy_coloring(graph):
    result={}
    for node in sorted(graph):
        used=set(result[n] for n in graph[node] if n in result)
        color=0
        while color in used:
            color+=1
        result[node]=color
    return result

colors1=greedy_coloring(graph)

color_names=['green','orange','blue','red','yellow']

print("Colors used:",len(set(colors1.values())))
print("Node coloring assignment:")

for node in sorted(colors1):
    print(f"V{node}: color {color_names[colors1[node]]}")

print("\nValid coloring - no adjacent nodes share a color")

color_map=['green','orange','blue','red','yellow']
node_colors={node:color_map[colors1[node]] for node in graph}

pos={
1:(0.5,2),
2:(0,1),
4:(0,0),
3:(1,1),
5:(1,0),
7:(2,1),
6:(2,0),
8:(2.5,2),
9:(3,1),
10:(3,0)
}

plt.figure(figsize=(12,5))

for u,v in edges:
    x=[pos[u][0],pos[v][0]]
    y=[pos[u][1],pos[v][1]]
    plt.plot(x,y,color='gray')

for node,(x,y) in pos.items():
    plt.scatter(x,y,s=1000,color=node_colors[node],edgecolors='black')
    plt.text(x,y,str(node),ha='center',va='center',fontweight='bold')

plt.axis('off')
plt.show()