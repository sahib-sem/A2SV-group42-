class Solution:
    def splitString(self, s: str) -> bool:
        n = len(s)
        self.ans = False
        def backtracking(lst,ans ,s):
            if len(lst) > 1:
                if int(lst[-1]) >= int(lst[-2]) or int(lst[-2]) - int(lst[-1]) != 1:
                    lst.pop()
                    return 
                if len(''.join(lst)) == n:
                    self.ans = True
                    return
                
                
            
            for i in range(len(s)):
                
                lst.append(s[:i + 1])
                if i < len(s):
                    backtracking( lst , ans, s[i + 1:])
            if lst:
                lst.pop()     
                
        lst = []
        ans = False
        backtracking(lst , ans, s)
        
        
        return self.ans
                        
                    