class Node:
    def __init__(self, head=0, next=None):
        self.head = head
        self.next = next

def swap_pairs(head):
    if not head or not head.next:
        return head

    dummy = Node(0)
    dummy.next = head
    prev = dummy
    
    while prev.next and prev.next.next:
        first = prev.next
        second = prev.next.next
        
        first.next = second.next
        second.next = first
        prev.next = second
        
        prev = first
    