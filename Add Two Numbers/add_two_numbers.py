class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    n, iteration = 0, 1
    while l1 or l2:
        if l1:
            n += l1.val * iteration
            l1 = l1.next
        if l2:
            n += l2.val * iteration
            l2 = l2.next
        iteration *= 10
        
    
    initial_node = current = ListNode()
    for char in reversed(str(n)):
        current.val = int(char)
        current.next =  ListNode()
        current, prev = current.next, current
    
    prev.next = None
    return initial_node
        