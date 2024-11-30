import networkx as nx
import gravis as gv

def drawGraph(edges):
    g = nx.Graph()
    for source, target, strength in edges:
        g.add_edge(source, target, strength=strength, color='black',)

    fig = gv.d3(g, show_edge_label=True, edge_label_data_source='strength',node_drag_fix=True)
    fig.display()

if __name__ == '__main__':
    edges = [
        ('A', 'B', 1),
        ('B', 'C', 3),
        ('B', 'D', 2),
        ('B', 'E', 1),
        ('C', 'D', 1),
        ('C', 'E', 4),
        ('D', 'A', 2),
        ('D', 'E', 2),
        ('E', 'F', 3),
        ('G', 'D', 1),
    ]
    drawGraph(edges)