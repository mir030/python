def isPalindrome(head):
    fast = current = head
    # find the mid-node
    while fast and fast.next:
        fast = fast.next.next
        current = current.next
    # reverse the second half
    prev = None
    while current:
        nxt = current.next
        current.next = prev
        prev = current
        current = nxt
    # compare the first and second half nodes
    while prev:  # while node and head:
        if prev.val != head.val:
            return False
        prev = prev.next
        head = head.next
    return True

from class_linked_list import *

linked_list = to_linked_list([1, 2, 3, 4, 3, 2, 1])
solution = isPalindrome(linked_list)

print(solution)