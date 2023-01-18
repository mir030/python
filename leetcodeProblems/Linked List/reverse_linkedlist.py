def reverse_linkedlist(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    current = head
    prev = None

    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

