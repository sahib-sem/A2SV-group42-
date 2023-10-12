class Solution:
    def countOrders(self, n: int) -> int:
        
        mod = 10**9 + 7
        
        def dp(to_be_picked_up , pickup , to_be_delivered, delivery, memo = {} ):
            
            if pickup == n and delivery == n:
                return 1
            
            if (pickup, delivery) in memo:
                return memo[(pickup, delivery)]
            ans1 , ans2 = 0, 0
            
            if to_be_picked_up > 0:
                ans1 = to_be_picked_up * dp(to_be_picked_up - 1, pickup + 1, to_be_delivered + 1, delivery ,memo)
            
            if to_be_delivered > 0:
                ans2 = to_be_delivered * dp(to_be_picked_up , pickup , to_be_delivered - 1, delivery + 1, memo)
            
            memo[(pickup, delivery)] = ans1 + ans2
            return ans1 + ans2 
        
        return dp(n, 0, 0, 0) % mod
        