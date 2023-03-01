def reverseLinkedList(head):
    current = head
    prev = None

    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

def reverseLinkedList2(head, prev=None):
    if not head:
        return prev
    current, head.next = head.next, prev
    return reverseLinkedList2(current, head)


def reverseList(self, head):
    return self._reverse(head)

def _reverse(self, node, prev=None):
    if not node:
        return prev
    n = node.next
    node.next = prev
    return self._reverse(n, node)