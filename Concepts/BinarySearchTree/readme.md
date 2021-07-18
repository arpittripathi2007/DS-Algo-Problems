

# Binary-Search-Tree
===================

## The overview
A binary search tree (BST) is a binary tree where each node has a comparable key (and an associated value) and satisfies the restriction that the key in any node is larger than the keys in all nodes in that node’s left subtree and smaller than the keys in all nodes in that node’s right subtree.

It is made up of nodes that have specific names. A BST is always sorted and the nodes that are on the left side are smaller than the root node and the nodes that are on the right side are larger than the root node. The good thing about this search method is that it does not have to reallocate memory. Meaning that it does not have to create a completely new BST when it wants to add more nodes.
### Key terms
* Root: the topmost node
* Parent: the node that comes before
* Child: the node that comes after
* Leaf: a node that has no children
* Height of the tree: the number of edges on the longest downward path from the root to the leaf
* Height of the node: number of edges on the longest downward path from the node to the leaf
* Level: 1 + the number of edges between the node and the root node
* Depth: number of edges between the node and the root
* Size: number of nodes in the tree


## How to Implement BST
Implementing a bst is pretty simple. The first steps to this are to set up two classes. One that defines what a node is and the second to define what a tree is.
The key components when defining nodes are to check to see if the node is either a leaf or a branch. Then once this is determined to find the height of the node.
The key components when defining trees are to check if the tree is empty or not, check to see what the height of the tree is if it is not empty, be able to see what this tree contains, be able to search through the tree, be able to insert item within the tree, set up recursive and iterative functions to locate specific nodes and to finally be able to delete any node specified.
### Binary Tree Node
Determining if a node exists or not is a key component of a bst so that you can know whether or not there is any information stored within that node or not. Then being able to know if that node is either a parent, child, or leaf is crucial to know for the purpose of searching. If the node is a leaf, then we know that we do not need to search anymore and to stop once we get to a leaf. If the node is a child, then we know that we do need to continue searching if the desired search has not yet been fulfilled. Then this same logic can be said if the node is a parent or root node.
### Binary Search Tree
Determining if a tree exists or not is a key component of a bst so that you can know whether or not there is something to search for. Then knowing that you have the capability to search at a high speed for the data that you are looking for. Being able to insert items into the tree is good to know because then you have more options with your tree when new information will be stored in this data structure. You will not have to create an entirely new structure just to add an additional item. Being able to see what the tree contains is crucial to know for searching purposes. If you are able to search, yet you cannot see what is being searched for within each node, then the tree will no be able to find the desired data. That being said, searching is an important function so that you are able to look through each node to see what it contains and to see if it needs to pull that item or to move onto the next item to continue searching. With search and insert, a key component of those functions is to be able to use a recursive function in order to search. The recursive function will keep running until the desired outcome is either met or has determined that it is not within the tree. Finally, being able to delete from the tree is a difficult function to create, but a highly useful one. With the delete function, it works similar to the search and the insert, but along with it comes the task of being able to reconnect the edge that has been removed from the tree if the node that was removed was not a leaf.
* Check if the tree is empty
* To check if the tree is empty or not you will need to see if there is a root node or not

### Recursion
How this works within the bst is to create conditional statements within the function to see if the item matches up with the data presented. This must be done for the root, left nodes, and the right nodes.
See what is contained in the node
To see what is contained within the node you will need to call the recursive function to check the data stored

### Being able to search the tree
To search the tree and its contents, you will need to call the recursive function and be able to check to see if the contents stored match with the desired search

### Being able to insert a node
To insert, you need to set up conditionals to check for where the item needs to be inserted and to know whether the item needs to be inserted to the left or the right of the root node.

### Inserting into BST
You also need to call the recursive call function to see what data is being stored where to know the proper place of installation.

## Why is BST useful?
This data structure is useful because it allows for a much faster search system than other concrete data structures.
If we can manage to keep a binary search tree well-balanced, we get an ordered data structure with O(log n) worst-case time complexity for all basic operations: lookup, addition and removal.
It allows for fast and easy removal and addition of items along with automatically being sorted rather than an unorganized data structure.
Trees are very flexible data, allowing to move subtrees around with minumum effort


The program is implemented in Python. The program allows the user to select a choice from a list of operations. The code contains following functions:

      1. Insertion
      2. Search
      3. Traversals (Inorder, Preorder, Postorder)
      3. Delete Node
        1. Delete root node
            11. Delete Node with 0 Child or root node is lead node (don't have to perform delete)
            12. Delete Node with 1 Child
            13. Delete Node with 2 Child
        2. Delete other node
            11. Delete Node with 0 Child
            12. Delete Node with 1 Child
            13. Delete Node with 2 Child
      4. Maximum and Minimum Key

