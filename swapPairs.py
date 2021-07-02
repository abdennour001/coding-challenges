# Definition for singly-linked list.
class LinkedList(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        curr = head
        prev = head
        new_head = head
        last_swap = None
        i = 1
        while curr is not None:
            if i % 2 == 0:
                if new_head == head:
                    new_head = curr
                if last_swap is not None:
                    last_swap.next = curr
                last_swap = prev               
                tmp_next = curr.next
                curr.next = prev
                prev.next = tmp_next
                prev = curr
                curr = tmp_next
                i += 1
            else:
                tmp_next = curr.next
                prev = curr
                curr = tmp_next
                i += 1
        return new_head

if __name__ == "__main__":
    head = LinkedList(1)
    node_1 = LinkedList(2)
    node_2 = LinkedList(3)
    node_3 = LinkedList(4)
    # node_4 = LinkedList(5)
    head.next = node_1
    node_1.next = node_2
    node_2.next = node_3
    # node_3.next = node_4
    s = Solution()
    node = s.reverseKGroup(head, 5)
    while(node != None):
        print(node.val)
        node = node.next