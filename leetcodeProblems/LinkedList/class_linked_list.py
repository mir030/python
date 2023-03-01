class LinkedlistNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def to_linked_list(iterable):
    next = None
    for val in reversed(iterable):
        next = LinkedlistNode(val, next)
    return next


def to_native_list(head):
    lst = []
    while head:
        lst.append(head.val)
        head = head.next
    return lst

