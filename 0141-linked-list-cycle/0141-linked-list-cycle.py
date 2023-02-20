# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hashset=set()
        while head:
            if not head in hashset:
                hashset.add(head)
            else:
                return True
            head=head.next
        return False
                