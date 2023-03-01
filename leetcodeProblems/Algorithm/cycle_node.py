def detectCycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return None
    while head != slow:
        slow = slow.next
        head = head.next
    return head

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def create_linked_list_cycle(nums, pos):
    # create a linked list from the list of numbers
    head = ListNode(nums[0])
    curr = head
    for num in nums[1:]:
        curr.next = ListNode(num)
        curr = curr.next

    # create a cycle in the linked list at the specified position
    if pos >= 0:
        cycle_node = head
        for i in range(pos):
            cycle_node = cycle_node.next
        curr.next = cycle_node

    return head
nums = [3, 2, 0, -4]
head = create_linked_list_cycle(nums, 2)
detectCycle(head)