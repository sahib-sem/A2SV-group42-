class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        # the queue will be a monotollically increasing queue
        #res = min(res, i + 1 - d.popleft()[0])
        
        queue = deque([(0 , 0)])
        n = len(nums)
        prefix_sum = 0
        min_length = n + 1
        
        for end in range(n):
            
            prefix_sum += nums[end]
          
            while queue and prefix_sum - queue[0][1] >= k:
        
                removed = queue.popleft()
                min_length = min(min_length , end + 1 - removed[0])
                
            while queue and prefix_sum <= queue[-1][1] :
                queue.pop()
                
            queue.append((end + 1,prefix_sum))
        
                
        return min_length if min_length != n + 1 else -1
            
                
            
            
        
        
        
            
            
            
                
        