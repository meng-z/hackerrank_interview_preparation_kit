"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


def has_cycle(head):
    if not head or not head.next or not head.next.next:
        return 0
    
    fast = head.next.next
    slow = head.next
    while slow or fast:
        if fast == slow:
            return 1
        
        fast = fast.next.next
        slow = slow.next
        
    return 0
