class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        nums = [0, 1]
        i = 2
        if n < 1:
            return 0
        while i <= n:
            if i % 2 == 0:
                new_num = nums[i // 2]
            else:
                new_num = nums[i // 2] + nums[i //2 + 1]
            
            nums.append(new_num)
            i += 1
        
        
        return max(nums)
            
        