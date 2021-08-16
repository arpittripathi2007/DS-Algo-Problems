'''
this file contains two way of creating dictionary Single headed
'''
from collections import defaultdict
  
# function for adding edge to graph
graph = defaultdict(list)
class Graph:
    def addEdge(self, graph,u,v):
        graph[u].append(v)
    
    def print_graph(self, graph_):
        print(graph_)

    def bfs(self, graph, src, V):
        visited = {i:False for i in range(V)}
        print(visited, src)
        queue_node = list() 
        queue_node.append(src)
        visited[src] = True
        
        while(queue_node):
            current_node = queue_node[0]
            queue_node.pop(0)
            print(current_node)

            for item in graph[current_node]:
                if(not visited[item]):
                    queue_node.append(item)
                    visited[item] = True 




if __name__ == "__main__":
    V = 6
    graph_ = Graph()
    graph_.addEdge(graph, 0, 1)
    graph_.addEdge(graph, 1, 3)
    graph_.addEdge(graph, 2, 2)
    graph_.addEdge(graph, 3, 4)
    graph_.addEdge(graph, 4, 5)

    graph_.print_graph(graph)
    graph_.bfs(graph, 0, V)


