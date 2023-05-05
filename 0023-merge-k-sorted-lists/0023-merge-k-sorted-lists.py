# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy=new_head=ListNode(0)
        new_lst = []
        arr = []
        for lst in lists:
            temp = []
            while lst:
                temp.append(lst.val)
                lst = lst.next
            new_lst.append(temp)

        for i in range(len(new_lst)):
            if new_lst[i]:
                heapq.heappush(arr, (new_lst[i][0] ,i, 0))
                
        while arr:
            num, arr_idx, ele_idx = heapq.heappop(arr)
            
            new_head.next = ListNode(num)
            new_head = new_head.next
            
            if ele_idx + 1 < len(new_lst[arr_idx]):
                heapq.heappush(arr, (new_lst[arr_idx][ele_idx + 1] , arr_idx , ele_idx + 1))
        
        return dummy.next
                
            
            
                
                