# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# curr=curr2=head
# while curr and curr.next:
#     while curr and curr.next and curr.val==curr.next.val:
#         curr=curr.next
#     curr2.next=curr.next
#     curr2=curr2.next
#     if curr:
#         curr=curr.next
# return head
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        duplicate_head = duplicates = ListNode(0)
        curr = curr2 = head
        
        while curr and curr.next:
            duplicate = None
            while curr and curr.next and curr.val == curr.next.val:
                
                duplicate = curr.val
                curr = curr.next
            if duplicate is not None:
                duplicate = ListNode(duplicate)
                duplicates.next = duplicate
                duplicates = duplicates.next
            curr2.next = curr.next
            curr2 = curr2.next
            if curr:
                curr = curr.next
        prev = None
        curr = head
        duplicate_head = duplicate_head.next
        print(head , duplicate_head)
        while curr and duplicate_head:
            if curr.val == duplicate_head.val:
                duplicate_head = duplicate_head.next 
                if prev:
                    prev.next = curr.next
                    curr = prev.next
                else:
                    temp = curr.next
                    curr.next = None 
                    curr = temp
                    head = curr
            else:
                prev = curr 
                curr = curr.next
        return head
            
            
                
            
        