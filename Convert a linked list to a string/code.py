class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def stringify(node:Node):
    head=node
    empt=""
    if head is None:
        return "None"
    while head is not None:
        empt+=str(head.data)+" -> "
        head=head.next
    empt+="None"
    return empt
