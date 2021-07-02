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
        i = 0
        curr = head
        prev = []
        new_head = head
        last_group = None
        while curr != None or (i % k == 0 and i != 0 and k != 1):
            if i % k == 0 and i != 0 and k != 1:
                # reverse here
                for j in range(k-1, -1, -1):
                    if j == 0:
                        prev[0].next = curr
                        if new_head == head:
                            new_head = prev[k-1]
                        if last_group is not None:
                            last_group.next = prev[k-1]
                    else:
                        prev[j].next = prev[j-1]
                last_group = prev[0]
                prev = [curr]
                if curr is not None:
                    curr = curr.next
            else:
                # pass
                prev.append(curr)
                curr = curr.next
            i += 1
        return new_head

if __name__ == "__main__":
    head = LinkedList(1)
    node_1 = LinkedList(2)
    node_2 = LinkedList(3)
    node_3 = LinkedList(4)
    node_4 = LinkedList(5)
    head.next = node_1
    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4
    s = Solution()
    node = s.reverseKGroup(head, 5)
    while(node != None):
        print(node.val)
        node = node.next