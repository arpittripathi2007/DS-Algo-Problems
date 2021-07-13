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

    def removeNthFromEnd(self, n: int):
        dummy_node = Node(0)
        dummy_node.next = self.head
        slow = dummy_node
        fast = dummy_node
        count = 0
        
        while count<=n and fast is not None:
            fast = fast.next
            count += 1
        
        while fast is not None:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dummy_node.next

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
    res_list  = linked_list.removeNthFromEnd(2)
    linked_list._print_list_helper(res_list)
    
