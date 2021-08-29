

# Problem Statement
===================

Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

 

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

# URL
================

https://leetcode.com/problems/linked-list-cycle/

# CODE
================

```

def getIntersectionNode(headA: ListNode, headB: ListNode) -> ListNode:
    dummy_node_1 = headA
    dummy_node_2 = headB
    if headA == None or headB == None:
        return None
    
    while(dummy_node_1 != dummy_node_2):
        dummy_node_1 = dummy_node_1.next if dummy_node_1 != None else headB
        dummy_node_2 = dummy_node_2.next if dummy_node_2 != None else headA
    
    return dummy_node_1
```