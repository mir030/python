def mergeLinkedList(list1, list2):
    if not list1 and not list2:
        return list1
    if not list1 or not list2:
        return list2 if not list1 else list1

    seek, target = (list1, list2) if list1.val < list2.val else (list2, list1)
    head = seek
    while seek and target:
        while seek.next and seek.next.val < target.val:
            seek = seek.next
        seek.next, target = target, seek.next
        seek = seek.next
    return head

from leetcodeProblems.LinkedList.class_linked_list import *

list1 = to_linked_list([1, 2, 4])
list2 = to_linked_list([1, 3, 4])
print(mergeLinkedList(list1, list2))
