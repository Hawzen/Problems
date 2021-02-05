class ListNode
    def __init__(self, val=0, next=None)
        self.val = val
        self.next = next
class Solution
    def removeNthFromEnd(self, head ListNode, n int) - ListNode
        # None case
        if not head 
            return head
        
        # Compute length 
        current = head
        length = 0
        while current
            current = current.next
            length += 1
        
        n = length - n + 1
        
        # Head case
        if n == 1
            return head.next
        
        index = 2
        prev, current = head, head.next
        while index != n
            prev, current = current, current.next
            index += 1
            
        prev.next = current.next
        return head