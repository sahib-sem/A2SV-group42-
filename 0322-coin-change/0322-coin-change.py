class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        memo = {}
        coins.sort(key = lambda x : -x)
        self.ans = float('inf')
        
        def dp(rem_sum):
            
            if rem_sum < 0:
                return float('inf')
            
            if rem_sum == 0:
                return 0
            if rem_sum in memo:
                return memo[rem_sum]
            
            for coin in coins:
                
                needed_coins = 1 + dp(rem_sum - coin)
                if rem_sum not in memo:
                    memo[rem_sum] = needed_coins
                else:
                    memo[rem_sum] = min(memo[rem_sum], needed_coins)
            
            return memo[rem_sum]
        
        ans = dp(amount)
        
        return -1 if ans == float('inf') else ans 
           
                
        