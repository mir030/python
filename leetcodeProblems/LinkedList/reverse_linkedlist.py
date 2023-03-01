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


from class_linked_list import *

linked_list = to_linked_list([1, 2, 3])
solution = reverse_linkedlist(linked_list)
solution_list = to_native_list(solution)
print(solution_list)