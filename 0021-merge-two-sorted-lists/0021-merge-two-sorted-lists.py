# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        answer=None
        if not list2:
            return list1
        if not list1:
            return list2
        if list1 and list2 and list1.val<=list2.val:
            answer=dummy=ListNode(list1.val)
            list1=list1.next
        else:
            answer=dummy=list2
            list2=list2.next
        while list1 and list2:
            if list1.val <list2.val:
                dummy.next =ListNode(list1.val)
                dummy=dummy.next
                list1=list1.next
            else:
                dummy.next=ListNode(list2.val)
                list2=list2.next
                dummy=dummy.next
        while list1:
            dummy.next=ListNode(list1.val)
            dummy=dummy.next
            list1=list1.next
        while list2:
            dummy.next=ListNode(list2.val)
            dummy=dummy.next
            list2=list2.next
        return answer
        