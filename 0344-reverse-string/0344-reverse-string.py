class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        start = 0
        end = len(s) - 1
            
        def recursive(string , s , e):
            if s >= e:
                return string
            string[e] ,string[s] = string[s] , string[e]
            
            return recursive(string,s + 1, e - 1)
        return recursive(s ,start, end)
    
            