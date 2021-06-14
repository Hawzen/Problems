# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head: 
            return


        curLeft = curRight = last = head
        while True:
            # Discover
            i = k-1
            history = []
            while i:
                if not curRight.next:
                    return head
                history.append(curRight)
                curRight = curRight.next
                i -= 1
                print(curRight.val, i)
            last = curRight

            # Swap
            while curLeft != curRight and curRight.next != curLeft:
                curLeft.val, curRight.val = curRight.val, curLeft.val
                curLeft, curRight = curLeft.next, history.pop(-1)

            # Recovery
            if not last.next:
                break
            curLeft = curRight = last.next

        return head