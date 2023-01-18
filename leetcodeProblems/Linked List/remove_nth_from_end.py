def removeNthFromEnd(head, n):
    def remove(ptr, n):
        if ptr == None:
            return -1
        index = remove(ptr.next, n) + 1
        if index == n:
            ptr.next = ptr.next.next
        return index

    index = remove(head, n)
    if n > index:
        head = head.next
    return head
