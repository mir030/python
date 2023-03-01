class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        length = 0
        temp = head
        while temp:
            temp = temp.next
            length += 1

        # Special case: remove the head node
        if n == length:
            return head.next

        remove_node = length - n
        prev = None
        curr = head  # Copying the whole linked list
        for i in range(remove_node):
            prev = curr
            curr = curr.next
        prev.next = curr.next
        return head


lst = [1, 2, 3, 4, 5]
nxt = None
for num in reversed(lst):
    nxt = ListNode(num, nxt)
solution = Solution()
print(solution.removeNthFromEnd(nxt, 2))
