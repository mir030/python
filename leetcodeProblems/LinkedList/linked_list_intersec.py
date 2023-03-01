def linkedListIntersection(headA, headB):
    node1 = headA
    node2 = headB

    while node1 != node2:
        if node1:
            node1 = node1.next
        else:
            node1 = headB
        if node2:
            node2 = node2.next
        else:
            node2 = headA
    return node1

