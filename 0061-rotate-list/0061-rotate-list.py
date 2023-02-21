# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k==0:
            return head
        length=0
        curr2=head
        legth=0
        while curr2:
            curr2=curr2.next
            length+=1
        k=k%length
        before=head
        for i in range(k):
            curr=head
            
            while curr:
                if curr.next and not curr.next.next:
                    before=curr.next
                    curr.next=None
                curr=curr.next
            if before:
                before.next=head
            else:
                before=head
            head=before
        return before
            
        
        