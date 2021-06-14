class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        
        curr, prev = head.next, head
        while True:
            prev.val, curr.val = curr.val, prev.val
            
            if curr.next and curr.next.next:
                curr, prev = curr.next.next, curr.next
            else:
                return head