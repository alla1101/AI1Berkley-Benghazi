from DrawProblem import drawGraph
from itertools import combinations

# startingPoint="A"
# goalPoint="G"

node_number = 5 # minimum 2

# steps_to_solve = 2 # minimum 2 , maximum node_number
def createGraph(node_number):
    alphabets = [char for char in "BCDEFHIJKLMNOPQRSTUVWXYZ"]
    count = node_number - 2
    graph_items=['A']
    for char in alphabets:
        if count ==0:
            break
        graph_items.append(char)
        count-=1
    graph_items.append('G')
    edges = list(combinations(graph_items, 2))  # 
    real_edges=[]
    for i,g in edges:
        real_edges.append((i,g,1))
    return real_edges

edges = createGraph(9)
drawGraph(edges)