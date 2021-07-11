from __future__ import print_function


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
    
    def insert_at_begining(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            node = self.head
            while node.next is not None:
                node = node.next
            node.next = new_node

    def insert_after_node(self, data, x):
        node =  self.head
        while node is not None:
            if x == node.data:
                break
            node = node.next
        if node is None:
            print('Node is not present in the Linked List')
        else:
            new_node = Node(data)
            new_node.next = node.next
            node.next = new_node
    
    def insert_before_node(self, data, x):
        if self.head is None:
            print('Linked List is Empty')

        elif self.head.data == x:
            self.insert_at_begining(data)
        else:
            node = self.head
            while node.next is not None:
                if node.next.data == x:
                    break
                node = node.next
            if node.next is None:
                print('Node is not present in the Linked List')
            else:
                new_node = Node(data)
                new_node.next = node.next
                node.next = new_node

    def delete_at_begining(self):
        if self.head is None:
            print('Linked List is Empty')
        else:
            self.head = self.head.next
    
    def delete_at_end(self):
        if self.head is None:
            print('Linked List is Empty')
        else:
            node = self.head
            while node.next.next is not None:
                node = node.next
            node.next = None

    def delete_by_value(self, x):
        if self.head is None:
            print('Linked List is Empty')
            return
        if x == self.head.data:
            self.head = self.head.next
            return
        node = self.head
        while node.next is not None:
            if x ==  node.next.data:
                break
            node = node.next
        if node.next is None:
            print('Node is not present in the Linked List')
        else:
            node.next = node.next.next




if __name__ == "__main__":
    linked_list = LinkedList()

    linked_list.traverse()
    linked_list.insert_at_begining(20)
    linked_list.insert_at_begining(10)

    linked_list.traverse()
    print('')

    linked_list.insert_at_end(30)
    linked_list.insert_at_end(80)
    linked_list.traverse()
    print('')


    linked_list.insert_after_node(40, 30)
    linked_list.insert_after_node(50, 40)
    linked_list.traverse()
    print('')

    linked_list.insert_before_node(70, 80)
    linked_list.insert_before_node(60, 70)
    linked_list.traverse()
    print('')

    linked_list.delete_at_begining()
    linked_list.delete_at_begining()
    linked_list.traverse()
    print('')

    linked_list.delete_at_end()
    linked_list.delete_at_end()
    linked_list.traverse()
    print('')

    linked_list.delete_by_value(40)
    linked_list.delete_by_value(300)
    linked_list.traverse()
    print('')


