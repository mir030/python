class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def palindromeLinkedList(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    node1 = prev
    node2 = head
    while node1 and node2:
        if node1.val != node2.val:
            return False
        node1 = node1.next
        node2 = node2.next
    return True


from leetcodeProblems.LinkedList import class_linked_list

list = [1, 1, 2, 1]
linked_list = class_linked_list.to_linked_list(list)
print(palindromeLinkedList(linked_list))
