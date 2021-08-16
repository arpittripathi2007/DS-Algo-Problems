'''
Unweighted graph for weighted we go for Djikstra's
URL=https://www.geeksforgeeks.org/snake-ladder-problem-2/
'''
from collections import defaultdict
import math
  
# function for adding edge to graph
graph = defaultdict(list)
parent = []

class Graph:
    def addEdge(self, graph,u,v):
        graph[u].append(v)
    
    def print_graph(self, dist, node_):
        if node_:
            print(dist[node_])
        else:
           for key, value in dist.items():
               print('({0})--{1}-->'.format(key, value), end='')
        
        print(node_, '---->', end='')
        parent_node = parent[node_]
        while(parent_node>0):
            print(parent_node, '--->', end='')
            parent_node = parent[parent_node]
        if parent_node == 0:
            print(parent_node)

    def bfs(self, graph, src, V, parent):
        dist = {i:float('inf') for i in range(V)}
        queue_node = list() 
        queue_node.append(src)
        dist[src] = 0
        parent[src] = 0
        
        while(queue_node):
            current_node = queue_node[0]
            queue_node.pop(0)

            for item in graph[current_node]:
                if(dist[item] ==  float('inf')):
                    queue_node.append(item)
                    dist[item] =  dist[current_node]+1
                    parent[item] = current_node
        return dist




if __name__ == "__main__":
    V = 6
    board = [0 for i in range(50)]
    parent = [float('inf') for i in range (37)]

    ## +ve are ladders and -ve are snakes
    board[2] = 13
    board[5] = 2
    board[9] = 18
    board[18] = 11
    board[17] = -13
    board[20] = -14
    board[24] = -8
    board[25] = 10
    board[32] = -2
    board[34] = -22
    
    graph_ = Graph()

    for i in range(37):
        for dice in range(1,7):
            dist = i + dice 
            dist += board[dist]
            if(dist <= 36):
                graph_.addEdge(graph, i, dist)

    dist = graph_.bfs(graph, 0, 37, parent)
    graph_.print_graph(dist, 36)


