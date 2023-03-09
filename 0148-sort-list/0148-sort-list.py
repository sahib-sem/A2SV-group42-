# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def splitList(h1):
            slow = fast = h1
            prev = None
            
            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next
                
            if prev:
                prev.next = None
            return [h1, slow]
        
        def mergeSort(h1):
            
            if not h1 or not h1.next:
                return h1
            l1 , l2 = splitList(h1)
            left = mergeSort(l1)
            right = mergeSort(l2)
            return mergeTwoLists(left, right)
                
        def mergeTwoLists( list1, list2):
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
        return mergeSort(head)

            
            
        