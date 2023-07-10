class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        
        #[0, 4, 8, 3, , 6]
        # [1, 2, 4, 6, 7, 12, 20]
        #     4  5  7  8  13   13
             
        answer = 0
        prefix_sum = 0
        
        for i in range(len(nums)):
            
            prefix_sum += nums[i]
            answer = max(answer, math.ceil(prefix_sum / (i + 1)))
            
        return answer  
        