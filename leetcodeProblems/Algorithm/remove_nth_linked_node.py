def removeNthNode(head, n):
    l = 0
    curr = head
    while head:
        head = head.next
        l += 1
    if n == l:
        return head.next
    r = l - n

    result = curr
    c = 1
    while curr:
        if c == r:
            curr.next = curr.next.next
            break
        curr = curr.next
        c += 1
    return result

from leetcodeProblems.LinkedList.class_linked_list import *

head = to_linked_list([1, 2, 3, 4, 5])
removeNthNode(head, 2)