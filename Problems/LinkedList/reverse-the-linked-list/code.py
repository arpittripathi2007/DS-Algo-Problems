class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def traverse(self):
        if self.head is None:
            print('Linked List is Empty')
        else:
            node = self.head
            while node is not None:
                print(node.data, '--->', end = ' ') 
                node = node.next

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            print(new_node.data)
            self.head = new_node
        else:
            node = self.head
            while node.next is not None:
                node = node.next
            node.next = new_node

    def reverseList(self):
        
        prev_node = None
        node = self.head
        head_ = None
        while node is not None:
            next_node = node.next
            node.next = prev_node
            prev_node = node
            head_ = node
            node = next_node
        return head_

    def _print_list_helper(self, node):              
        if node is not None:                  
            print(node.data, '--->', end = ' ') 
            self._print_list_helper(node.next)
    
if __name__ == "__main__":
    linked_list = LinkedList()
    list_node = [1,2,3,4,5]
    for item in list_node:
        linked_list.insert_at_end(item)

    linked_list.traverse()
    print()
    reversed_list  = linked_list.reverseList()
    linked_list._print_list_helper(reversed_list)
    
