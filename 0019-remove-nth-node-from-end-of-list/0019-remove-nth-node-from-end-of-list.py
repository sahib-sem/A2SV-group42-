class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l=head
        r=head
        for i in range(n):
            r=r.next
        prev=None
        while r:
            prev=l
            l=l.next
            r=r.next
        if prev:
            prev.next=l.next
        else:
            return l.next
        return head
            
        