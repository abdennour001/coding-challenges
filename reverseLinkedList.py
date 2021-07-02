def reverseLinkedList(head):
    node = head
    previous = None
    i = 0
    while(node != None):
        next_ = node.next
        node.next = previous
        previous = node
        node = next_
    return previous


class LinkedList:

    def __init__(self, value):
        self.value = value
        self.next = None


if __name__ == "__main__":
    head = LinkedList(0)
    node_1 = LinkedList(1)
    node_2 = LinkedList(2)
    node_3 = LinkedList(3)
    head.next = node_1
    node_1.next = node_2
    node_2.next = node_3
    node = reverseLinkedList(head)
    while(node != None):
        print(node.value)
        node = node.next
