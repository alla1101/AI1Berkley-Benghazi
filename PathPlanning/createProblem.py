from DrawProblem import drawGraph
from itertools import combinations

# Parameters
number_of_nodes = 5 # Not Allowed to Exceed 26

def getNodeNames(node_number):
    alphabets = [char for char in "BCDEFHIJKLMNOPQRSTUVWXYZ"]
    count = node_number - 2
    graph_items=['A']
    for char in alphabets:
        if count ==0:
            break
        graph_items.append(char)
        count-=1
    graph_items.append('G')

#Layers_and_Nodes = [
    #["A"], # Layer 1 : Starting Node
           # Rest Of The Nodes 
    #["G"], # Layer N : Last Node
#]