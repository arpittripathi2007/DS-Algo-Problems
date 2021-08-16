'''
this file contains two way of creating dictionary Single headed
'''
  
# function for adding edge to graph
graph = list(list())
def addEdge(graph,u,v):
    graph[u][v] = 1
  
def print_graph(graph_, V):
    for i in range(V):
        print("{0}:".format(i), end=' ')
        for j in range(V):
            print("{0}".format(graph_[i][j]), end=' ')
        print()


if __name__ == "__main__":
    V = 5
    graph = [[0 for j in range(V)] for i in range(V)]
    addEdge(graph, 0, 1)
    addEdge(graph, 0, 4)
    addEdge(graph, 1, 2)
    addEdge(graph, 1, 3)
    addEdge(graph, 1, 4)
    addEdge(graph, 2, 3)
    addEdge(graph, 3, 4)

    print_graph(graph, V)


