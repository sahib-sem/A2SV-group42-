class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def S(string):
            lst = list(string)
            lst.sort()
            count = 1
            i = 0
            while i < len(lst) -1:
                if lst[i] == lst[i + 1]:
                    count += 1
                else:
                    break
                
                i += 1
            return count
        arr = []
        for word in words:
            
            count = S(word)
            arr.append(count)
        arr.sort()
        ans = []
        
        # [ 1 , 2 ,  3, 4]
        # l     m l         h 3
        for query in queries:
            
            count = S(query)
            low = -1
            high = len(arr)
            while high > low + 1:
                
                mid = low + (high - low) // 2
                if arr[mid] <= count:
                    low = mid
                else:
                    high = mid
            
            ans.append(len(arr) - high)
            
        return ans
            
                
        
            
            
                
        