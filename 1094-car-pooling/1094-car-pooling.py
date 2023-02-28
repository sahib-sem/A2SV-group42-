class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        arr = [0] * 1001
        for trip in trips:
            arr[trip[1]] += trip[0]
            arr[trip[-1]] -= trip[0]
        for i in range(1,1001):
            arr[i] += arr[i-1]
        for n in arr:
            if n > capacity:
                return False
        return True
            
            
        