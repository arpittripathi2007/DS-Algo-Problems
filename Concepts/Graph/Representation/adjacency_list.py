'''
this file contains two way of creating adjacency list
1) Creating a Node Class and defining its data and next pointer
2) Creating simple list with index 0,1,2 each have list as value

'''

## creating the node class

class adjNode:
    def __init__(self, data):
        self.vertex  = data
        self.next = None

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [None]* self.V

    def add_edge(self, src, dest):
        # Adding the node to the source node
        node = adjNode(dest)
        node.next = self.graph[src]
        self.graph[src] = node
 
        # Adding the source node to the destination as
        # it is the undirected graph
        node = adjNode(src)
        node.next = self.graph[dest]
        self.graph[dest] = node

    def print_graph(self):
        for i in range(self.V):
            print("Adjacency list of vertex {}\n head".format(i), end="")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.vertex), end="")
                temp = temp.next
            print()


## method 2 [[]]
graph_ = list(list())
def add_edge(graph_, vertex, edge):
    ## if the list is available at the given index
    if graph_[vertex]:
        graph_[vertex].append(edge)
        graph_[edge].append(vertex)
    ## if the list is not available at the given index
    else:
        graph_[vertex]= [edge]
        graph_[edge] = [vertex]

def print_graph(graph_):
    for item in graph_:
        print("Adjacency list of vertex {}\n head".format(item), end="")
        for item_ in item:
            print(" -> {}".format(item_), end="")
        print()




if __name__ == "__main__":
    V = 5
    graph = Graph(V)
    graph.add_edge(0, 1)
    graph.add_edge(0, 4)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 4)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)
 
    graph.print_graph()
    
    # graph_ = [[] for i in range(V)]
    # add_edge(graph_, 0, 1)
    # add_edge(graph_, 0, 4)
    # add_edge(graph_, 1, 2)
    # add_edge(graph_, 1, 3)
    # add_edge(graph_, 1, 4)
    # add_edge(graph_, 2, 3)
    # add_edge(graph_, 3, 4)

    # print_graph(graph_)


