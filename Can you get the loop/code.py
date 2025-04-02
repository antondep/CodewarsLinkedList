class Node:
    def __init__(self):
        self.next = None

def loop_size(node):
    slow = node
    fast = node

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast: 
            break
    else:
        return 0

    count = 1
    fast = fast.next
    while slow != fast:
        fast = fast.next
        count += 1
    
    return count
