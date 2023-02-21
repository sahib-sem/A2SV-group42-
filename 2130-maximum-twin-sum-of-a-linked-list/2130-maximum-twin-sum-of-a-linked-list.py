# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        lst=[]
        curr=head
        while curr:
            
            lst.append(curr.val)
            curr=curr.next
        i=0
        j=len(lst)-1
        max_=0
        while j>i:
            current=lst[i]+lst[j]
            max_=max(max_,current)
            j-=1
            i+=1
        return max_
            
            
        
        