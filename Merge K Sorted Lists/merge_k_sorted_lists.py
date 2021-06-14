class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        lists = [node for node in lists if node is not None]
        if not lists: return None
        elif len(lists) == 1: return lists[0]
        
        curr = head = ListNode()
        while any(lists):
            mx = 0
            # You can compare the last max rather than everything all over
            for i in range(len(lists)):
                if lists[i].val < lists[mx].val:
                    mx = i
            curr.next = lists[mx]
            
            
            lists[mx] = lists[mx].next
            if lists[mx] is None:
                    lists.pop(mx)
                    
            curr = curr.next
            
            

        return head.next