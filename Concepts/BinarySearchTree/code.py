from __future__ import print_function



class BST:
    def __init__(self, key):
        self.key = key
        self.lchild = None
        self.rchild = None
    
    def insert(self, data):
        if self.key is None:
            self.key = data
            return
        
        if self.key == data:             ## for duplicate value remove this
            return
        
        if self.key > data:              ## self.root.key >= data if duplicate value need to be placed on the left side
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild = BST(data)
        else:                            ## default: duplicate value need to be placed on the right side
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = BST(data)

    def search(self, data):
        if self.key == data:
            print('Node is Found')
            return
        
        if data < self.key:
            if self.lchild:
                self.lchild.search(data)
            else:
                print('Node is not present in the Tree')
        
        if data > self.key:
            if self.rchild:
                self.rchild.search(data)
            else:
                print('Node is not present in the Tree')

    def preorder(self):
        print(self.key, end= " ")
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()
    
    def inorder(self):
        if self.lchild:
            self.lchild.inorder()
        print(self.key, end= " ")
        if self.rchild:
            self.rchild.inorder()
    
    def postorder(self):
        if self.lchild:
            self.lchild.postorder()
        if self.rchild:
            self.rchild.postorder()
        print(self.key, end= " ")

    def delete(self, data, current):
        if self.key == None:
            print('Tree is Empty')
            return
        if data < self.key:
            if self.lchild:
                self.lchild = self.lchild.delete(data, current)
            else:
                print('Node is not present in Tree')
        
        elif data > self.key:
            if self.rchild:
                self.rchild = self.rchild.delete(data, current)
            else:
                print('Node is not present in Tree')
            
        else:
            if self.lchild is None:
                temp = self.rchild
                if data == current:
                    self.key = temp.key
                    self.lchild = temp.lchild
                    self.rchild = temp.rchild
                    temp = None
                    return
                self = None
                return temp
            if self.rchild is None:
                temp = self.lchild
                if data == current:
                    self.key = temp.key
                    self.lchild = temp.lchild
                    self.rchild = temp.rchild
                    temp = None
                    return
                self = None
                return temp


            ''' Delete node with 2 child
             replace with smallest value in right subtree or replace with largest value in left subtree
             I am considering replace with smallest value in right subtree '''

            node = self.rchild
            while node.lchild:
                node = node.lchild
            self.key = node.key
            self.rchild = self.rchild.delete(data, current)
        return self

    def min_node(self):
        current = self
        while current.lchild:
            current = current.lchild
        print('Node with minimum valued Key :', current.key)
    
    def max_node(self):
        current = self
        while current.rchild:
            current = current.rchild
        print('Node with maximum valued Key :', current.key)

def count(node):
    if node is None:
        return 0
    return 1 + count(node.lchild) + count(node.rchild)

        

if __name__ == "__main__":
    root = BST(None)
    print('')

    list_insert = [20, 4, 30, 4, 1, 5, 6]
    for item in list_insert:
        root.insert(item)
    root.search(6)
    root.search(60)
    print('Count is: ', count(root))
    root.preorder()
    print('')
    root.inorder()
    print('')
    root.postorder()
    print(root)
    if count(root) > 1:     ## delete operation on root node when root node is leaf node
        root.delete(10, root.key)
    else:
        print('Delete operation can not be performed')
    print(root)
    if count(root) > 1: 
        root.delete(6, root.key)
    else:
        print('Delete operation can not be performed')
    root.postorder()

    root.min_node()
    root.preorder()
    root.max_node()
    root.preorder()






