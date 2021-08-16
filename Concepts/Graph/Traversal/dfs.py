'''
this file contains two way of creating dictionary Single headed
'''
from collections import defaultdict
  
# function for adding edge to graph
graph = defaultdict(list)
def addEdge(graph,u,v):
    graph[u].append(v)
  
def print_graph(graph_):
    print(graph_)

if __name__ == "__main__":
    V = 5
    addEdge(graph, 0, 1)
    addEdge(graph, 0, 4)
    addEdge(graph, 1, 2)
    addEdge(graph, 1, 3)
    addEdge(graph, 1, 4)
    addEdge(graph, 2, 3)
    addEdge(graph, 3, 4)

    print_graph(graph)


