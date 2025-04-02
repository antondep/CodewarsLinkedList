class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Context:
    def __init__(self, first, second):
        self.first = first
        self.second = second

def alternating_split(head):
    if head is None or head.next is None:
        raise ValueError("List must contain at least two nodes.")
    
    first_head = head
    second_head = head.next
    
    first = first_head
    second = second_head
    
    current = head.next.next
    is_first = True
    
    while current:
        if is_first:
            first.next = current
            first = first.next
        else:
            second.next = current
            second = second.next
        is_first = not is_first
        current = current.next
    
    first.next = None
    second.next = None
    
    return Context(first_head, second_head)