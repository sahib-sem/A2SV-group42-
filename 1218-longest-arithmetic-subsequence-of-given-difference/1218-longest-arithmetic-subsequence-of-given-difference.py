class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        
        # traverse in reverse order 
        
        dp = defaultdict(int)
        
        for i in range(len(arr)):
            num = arr[i]
            
            dp[num] = dp[num - difference] + 1
        
        return max(dp.values())
            
            
        
        
        
                
                
        
        