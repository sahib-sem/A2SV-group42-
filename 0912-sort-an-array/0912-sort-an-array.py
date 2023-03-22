class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSort(low , end , lst):
            if low == end:
                return [lst[end]]
            mid = low + (end - low) // 2

            left = mergeSort(low , mid , lst)
            right = mergeSort(mid + 1 , end , lst)
            return merge(left , right)

        def merge(lst1 , lst2):
            lst = []
            i = j = 0
            while i < len(lst1) and j < len(lst2):
                if lst1[i] < lst2[j]:
                    lst.append(lst1[i])
                    i += 1
                else:
                    lst.append(lst2[j])
                    j += 1

            while i < len(lst1):
                lst.append(lst1[i])
                i += 1
            while j < len(lst2):
                lst.append(lst2[j])
                j += 1

            return lst
        return mergeSort(0, len(nums) - 1, nums)