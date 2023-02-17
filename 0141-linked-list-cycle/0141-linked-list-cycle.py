# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        rabbit=head
        tortoise=head
        while tortoise and rabbit and rabbit.next:
            tortoise=tortoise.next
            rabbit=rabbit.next.next
            if tortoise==rabbit:
                return True
            
                
        return False
        