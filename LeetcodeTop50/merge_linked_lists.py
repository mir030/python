class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeLinkedLists(list1, list2):
    seek, target = (list1, list2) if list1.val < list2.val else (list2, list1)
    head = seek
    while seek and target:
        while seek.next and seek.next.val < target.val:
            seek = seek.next
        seek.next, target = target, seek.next
        seek = seek.next
    return head
