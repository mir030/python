class LinkedlistNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def to_linked_list(iterable):
    head = None
    for val in reversed(iterable):
        head = LinkedlistNode(val, head)
    return head


l1 = to_linked_list([1, 2, 4])



def to_native_list(head):
    lst = []
    while head:
        lst.append(head.val)
        head = head.next
    return lst


l2 = to_native_list(l1)
