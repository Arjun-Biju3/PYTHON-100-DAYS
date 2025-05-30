class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def getLength(self,head):
        count = 0
        current = head
        while current:
            count += 1
            current = current.next
        return count

    def rotateRight(self,head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        length = self.getLength(head)
        k = k % length
        for i in range(k):
            start = head
            while start.next.next != None:
                start = start.next
            target = start.next
            start.next = None
            target.next = head
            head = target
        start = head
        while start:
            print(start.val)
            start = start.next
    
head =  ListNode(1, 
         ListNode(2, 
         ListNode(3, 
         ListNode(4, 
         ListNode(5)))))
sol = Solution()
sol.rotateRight(head,2)
#[1,2,3,4,5]