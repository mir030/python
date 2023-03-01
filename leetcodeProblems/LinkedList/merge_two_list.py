from class_linked_list import *

def mergeTwoLists(list1, list2):
    if not list1 and not list2:
        return list1
    if not list1 or not list2:
        return list1 if not list2 else list2

    seek, target = (list1, list2) if list1.val < list2.val else (list2, list1)
    head = seek
    while seek and target:
        while seek.next and seek.next.val < target.val:
            seek = seek.next
        seek.next, target = target, seek.next
        seek = seek.next
    return head


l1 = to_linked_list([1, 2, 4])
l2 = to_linked_list([1, 3, 4])

result = mergeTwoLists(l1, l2)
print(to_native_list(result))