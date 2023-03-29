class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # simple solution use a hash table 
        nums = Counter(nums)
        count = 0
        ans = []
        nums = dict(sorted(nums.items() , key = lambda x: -x[1] ))
        
        for item in nums.keys():
            if count == k:
                break
            ans.append(item)
            count += 1
        
        return ans 
        