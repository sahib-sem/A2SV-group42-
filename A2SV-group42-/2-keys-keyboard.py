class Solution:
    def minSteps(self, n: int) -> int:

        def dp(curr_screen , previous_copied , steps, memo = {}):
            if len(curr_screen) > n:
                return float('inf')
            if len(curr_screen) == n:
                return steps
            if (curr_screen , previous_copied) in memo:
                return memo[(curr_screen,  previous_copied)]
            
            ans1, ans2 = float('inf') , float('inf')
            if len(curr_screen) != len(previous_copied):
                ans1 = dp(curr_screen, curr_screen, steps + 1, memo)
            if previous_copied != "":
                ans2 = dp(curr_screen + previous_copied , previous_copied , steps + 1, memo)

            memo[(curr_screen, previous_copied)] = min(ans1, ans2)
            return min(ans1, ans2)
        
        return dp("A" ,"", 0)

            


        
        
        