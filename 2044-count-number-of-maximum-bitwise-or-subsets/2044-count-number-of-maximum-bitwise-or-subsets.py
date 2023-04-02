class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_so_far = []
        
        i = 0
        max_ = float('-inf')
        while i < (1 << len(nums)):
            current = i
            j = len(nums) - 1
            total = 0
            while current and j >= 0:
                
                if (current) & 1:
                    if not total:
                        total = nums[j]
                    else:
                        total |= nums[j]
                j -= 1
                current >>= 1
            
            if total > max_:
                max_ = total
                max_so_far = [max_ , 1]
            elif total == max_:
                max_so_far[-1] += 1
            i += 1
        print(max_so_far)
        return max_so_far[-1]
                    