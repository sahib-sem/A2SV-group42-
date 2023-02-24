class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        min_queue = deque()
        max_queue = deque()
        
        start = 0
        max_length = 0
        
        for end in range(len(nums)):
            
            while min_queue and min_queue[-1] > nums[end]:
                min_queue.pop()
            min_queue.append(nums[end])
            
            while max_queue and max_queue[-1] < nums[end]:
                max_queue.pop()
            max_queue.append(nums[end])
            
            while max_queue[0] - min_queue[0] > limit:
                num = nums[start]
                if num == max_queue[0]:
                    max_queue.popleft()
                if num == min_queue[0]:
                    min_queue.popleft()
                start += 1
            max_length = max(max_length , end - start + 1)
        return max_length
            
            
        
        