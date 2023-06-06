class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        # arr maximize an element , arr[0] = 1, abs (arr[i] - arr[i - 1] ) <= 1
        # [1 , ]
        arr.sort()
        arr[0] = 1
        for i in range(1, len(arr)):
            if arr[i] - arr[i - 1] > 1:
                arr[i] = arr[i - 1] + 1
        
        return arr[-1]
            
            
            