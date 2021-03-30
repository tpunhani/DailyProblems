# Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
    if headA and headB:
        a, b = headA, headB
            
        while a!=b:
            a = a.next if a else headB
            b = b.next if b else headA
                
        return a


