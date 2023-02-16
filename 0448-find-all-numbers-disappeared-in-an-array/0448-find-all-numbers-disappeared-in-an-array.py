class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        set1=set(range(1,len(nums)+1))
        set2=set(nums)
        answer=set1.difference(set2)
        return list(answer)