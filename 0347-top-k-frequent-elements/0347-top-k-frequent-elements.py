class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # simple solution use a hash table 
#         nums = Counter(nums)
#         count = 0
#         ans = []
#         nums = dict(sorted(nums.items() , key = lambda x: -x[1] ))
        
#         for item in nums.keys():
#             if count == k:
#                 break
#             ans.append(item)
#             count += 1
        
#         return ans 
       
        nums = Counter(nums)
        nums = [[val, key] for key, val in nums.items()]
        self.ans = []
        def quickselect(nums , start , end , k):
            if end - start <= 0:
                self.ans = nums[start:]
                return 
            
            
            pivot = nums[start][0]
            write = start + 1
            for read in range(start + 1, end + 1):
                if nums[read][0] <= pivot:
                    nums[write] , nums[read] = nums[read] , nums[write]
                    write += 1
            nums[start] , nums[write - 1] = nums[write - 1] , nums[start]
            length = end - write + 2
            
            if length == k:
                self.ans = nums[write - 1:]
                return 
            if k < length:
                quickselect(nums, write, end , k )
            else:
                quickselect(nums, start, write - 2, k - length)
        
        quickselect(nums, 0 , len(nums) - 1, k)
        
        self.ans = [ans[1] for ans in self.ans]
        
        return self.ans
        
        
            
        
        
            
            
        
        
        