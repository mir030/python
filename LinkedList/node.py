class LinkedListNode:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node


node1 = LinkedListNode("3")
node2 = LinkedListNode("7")
node3 = LinkedListNode("10")

node1.next_node = node2
node2.next_node = node3

current_node = node1
while True:
    print(current_node.value, "->")
    if current_node.next_node is None:
        print("None")
        break
    current_node = current_node.next_node