def getIntersectionNode(headA, headB):
    """
    :type headA, headB: ListNode
    :rtype: ListNode
    """
    top = headA
    bottom = headB

    while top != bottom:
        top = headB if not top else top.next
        bottom = headA if not bottom else bottom.next
    return top