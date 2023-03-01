class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
       
        
        # if player is True player1 is playing and false player2 is playing
        # choice 1 for end and 0 for start of the array
        def recursive(start , end , arr):
            if start > end:
                return 0
            choice1 = arr[start] + min(recursive(start + 2 , end , arr), recursive(start + 1 , end - 1, arr))
            choice2 = arr[end] + min(recursive(start + 1 , end - 1 , arr), recursive(start , end - 2, arr))
            
            return max(choice1 , choice2)
        total = sum(nums) 
        player1 = recursive(0, len(nums) - 1 , nums)
        player2 = total - player1
        
        if player1 >= player2:
            return True