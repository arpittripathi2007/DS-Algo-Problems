'''
Unweighted graph for weighted we go for Djikstra's
'''
from collections import defaultdict
import math
  
# function for adding edge to graph
graph = defaultdict(list)
class Graph:
    def addEdge(self, graph,u,v):
        graph[u].append(v)
    
    def print_graph(self, dist, node_):
        if node_:
            print(dist[node_])
        else:
           for key, value in dist.items():
               print('({0})--{1}-->'.format(key, value), end='')

    def bfs(self, graph, src, V):
        dist = {i:float('inf') for i in range(V)}
        queue_node = list() 
        queue_node.append(src)
        dist[src] = 0
        
        while(queue_node):
            current_node = queue_node[0]
            queue_node.pop(0)

            for item in graph[current_node]:
                if(dist[item] ==  float('inf')):
                    queue_node.append(item)
                    dist[item] =  dist[current_node]+1
        return dist




if __name__ == "__main__":
    V = 6
    graph_ = Graph()
    graph_.addEdge(graph, 0, 1)
    graph_.addEdge(graph, 0, 3)
    graph_.addEdge(graph, 1, 2)
    graph_.addEdge(graph, 2, 3)
    graph_.addEdge(graph, 3, 4)
    graph_.addEdge(graph, 4, 5)

    dist = graph_.bfs(graph, 0, V)
    graph_.print_graph(dist, 5)
    graph_.print_graph(dist, False)


