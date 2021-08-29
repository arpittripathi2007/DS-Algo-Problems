

# Problem Statement
===================

Given the head of a singly linked list, return true if it is a palindrome.

Example 1:
Input: head = [1,2,2,1]
Output: true


# URL
================

https://leetcode.com/problems/palindrome-linked-list/

# CODE
================

```

def isPalindrome(head: Optional[ListNode]) -> bool:
    if(not head or not head.next):
        return True
    
    slow = head
    fast = head
    
    # finding the middle
    while(fast.next and fast.next.next):
        slow = slow.next
        fast = fast.next.next
    
    slow.next = self.reverse(slow.next)
    # pre is the returned reversed other half linkedlist
    slow = slow.next
    while(slow):
        if(head.val != slow.val):
            return False
        head = head.next
        slow = slow.next
        
    return True

def reverse(head):
    # reversing the other half of linked list
    pre = None
    nex = None
    while(head):
        nex = head.next
        head.next = pre
        pre = head
        head = nex
    return pre
```