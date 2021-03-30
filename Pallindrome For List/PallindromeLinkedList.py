# Given the head of a singly linked list, return true if it is a palindrome.

def isPalindrome(self, head: ListNode) -> bool:
    slow = fast = head
        
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
            
    secondHalf = None
        
    while slow:
        tmp = slow.next
        slow.next = secondHalf
        secondHalf = slow
        slow = tmp
            
    while head and secondHalf:
        if head.val != secondHalf.val:
            return False
        head = head.next
        secondHalf = secondHalf.next
            
    return True


