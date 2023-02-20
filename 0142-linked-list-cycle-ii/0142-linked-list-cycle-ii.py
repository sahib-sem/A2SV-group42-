# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tortoise=head
        rabbit=head
        cycle=False
        while rabbit and rabbit.next:
            rabbit=rabbit.next.next
            tortoise=tortoise.next
            if rabbit== tortoise:
                cycle=True
                break
        if not cycle:
            return None
        tortoise=head
        while True:
            if tortoise==rabbit:
                return tortoise
            tortoise=tortoise.next
            rabbit=rabbit.next
            
        
            
        