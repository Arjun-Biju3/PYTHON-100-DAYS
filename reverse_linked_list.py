class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        num = []
        dummy = ListNode(0)
        current = dummy
        while head:
            num.append(head.val)
            head = head.next

        num = num[::-1]
        for i in num:
            node = ListNode(i)
            current.next = node
            current = current.next
        node = dummy.next
        while node:
            print(node.val)
            node = node.next
        return node
            
Solution().reverseList(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))))
