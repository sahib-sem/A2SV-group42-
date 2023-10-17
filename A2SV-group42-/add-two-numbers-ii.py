# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        def reverseLinkedList(head):
            
            prev = None
            curr = head
            
            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
                
            return prev
        
        l1, l2 = reverseLinkedList(l1) , reverseLinkedList(l2)

        dummy = curr = ListNode(0)
        carry_over = 0
        
        while l1 and l2:
            
            summ = l1.val + l2.val
            
            summ += carry_over
            carry_over = 0
            
            if summ > 9:
                carry_over = 1
                summ = summ % 10
            
            curr.next = ListNode(summ)
            curr = curr.next
            l1 = l1.next
            l2 = l2.next
        
        print(dummy, carry_over , l1, l2)
        while l1:
            
            summ = l1.val + carry_over
            carry_over = 0
            
            if summ > 9:
                carry_over = 1
                summ = summ % 10
            
            curr.next = ListNode(summ)
            curr = curr.next
            
            l1 = l1.next
            
        while l2:
            
            summ = l2.val + carry_over
            carry_over = 0
            
            if summ > 9:
                carry_over = 1
                summ = summ % 10
            
            curr.next = ListNode(summ)
            curr = curr.next
            
            l2 = l2.next
        if carry_over:
            curr.next = ListNode(carry_over)
            
        return reverseLinkedList(dummy.next)
            
            
        
            
            
            
            
            
            
            
            
            
            
            
            
            