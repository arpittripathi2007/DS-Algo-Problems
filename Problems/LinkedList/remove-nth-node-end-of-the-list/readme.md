

# Problem Statement
===================

Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]

# URL
================

https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# CODE
================

```
def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    dummy_node = ListNode(0)
    dummy_node.next = head
    slow = dummy_node
    fast = dummy_node
    count = 0
    head_ = head
    while count<=n and fast is not None:
        fast = fast.next
        count += 1
    
    while fast is not None:
        slow = slow.next
        fast = fast.next
    slow.next = slow.next.next
    return dummy_node.next
```