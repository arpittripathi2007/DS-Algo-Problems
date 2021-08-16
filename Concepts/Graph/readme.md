

# QUICK SORT
===================
## What is a Graph?
A graph is a collection of nodes where each node might point to other nodes. These nodes are connected to each other through a set of edges. Graphs are similar to trees but trees follow certain rules when it comes to its edges:
For a tree with N nodes, it will have (N-1) edges; one edge for each parent-child relationship. All nodes must be reachable from the root and there must be exactly one possible path from root to a node.

### Edges can be of two types:
* Directed edges in which connections are one-way (Unidirectional). One of the end points is the origin and the other end point is the destination.
* Undirected edges in which connections are two-way (Bidirectional).


## When are Graphs Used?
Many real-world systems are modelled using graphs. If you look at a social network like Facebook, friendships can be represented by undirected graphs. If someone is your friend, you are also their friend.
However, you have other social networks like Twitter and Instagram which can be represented by directional graphs. You can follow someone but they do not necessarily follow you back. They would also have to click “follow” (or create an edge) for it to be two way.

### Weighted Edges
Not all edges are created equal. Sometimes in a graph, some connections may be preferable to others. If we go back to the example of representing streets as graphs, usually if you wanted to get from point A to point B, you would want to take the path with the least traffic. An edge with less traffic may be “worth more”. A highway with a higher speed limit may also be “worth more” than a side road with a lower speed limit.

## Graph Traversal
There are two common ways to find the path from one node to another node in a graph:
* Depth First Search (DFS)
* Breadth First Search (BFS)

### Depth First Search (DFS)
Preorder, or traversing all the way down a branch before moving on to the next. Visit a node, then visit one of its children, and continue to visit the children of its children until the end of a branch.
DFS can be implemented using recursion or iteration. To see a recursive code implementation of DFS

### Breadth First Search (BFS)
Level-order, or traversing layer by layer. Visit a node, then visit all of its children before moving on to grandchildren. You can start BFS in a graph at any node you want. This node that you choose to start at is sometimes called the search key. You can visit any adjacent nodes (children) in any order that you like.