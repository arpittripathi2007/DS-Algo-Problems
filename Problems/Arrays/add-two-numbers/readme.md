

# Problem Statement
===================

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]


# URL
================

https://leetcode.com/problems/add-two-numbers/

# CODE
================

```
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def addTwoNumbers(l1, l2):
    dummy = ListNode()
    temp = dummy
    carry = 0
    
    while(l1 or l2 or carry == 1):
        sum_ = 0
        if l1:
            sum_ += l1.val
            l1 = l1.next
        if l2:
            sum_ += l2.val
            l2 = l2.next
        sum_ += carry
        carry = sum_ // 10
        new_node = ListNode(sum_ % 10)
        temp.next = new_node
        temp = temp.next
    return dummy.next
```