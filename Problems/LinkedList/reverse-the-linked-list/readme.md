

# Problem Statement
===================

Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

# URL
================

https://leetcode.com/problems/reverse-linked-list/

# CODE
================

```
def reverseList(self, head: ListNode) -> ListNode:
    prev_node = None
    head_ = None
    while head is not None:
        next_node = head.next
        head.next = prev_node
        prev_node = head
        head_ = head
        head = next_node
    return head_
```