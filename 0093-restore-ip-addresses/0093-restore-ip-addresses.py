class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        if len(s) > 12:
            return []
        
        self.string = s
        self.ans = []
        def backtrack (temp, s):
            if len(temp) == 4 and ''.join(temp) == self.string and temp not in self.ans :
                self.ans.append(temp[:])
                return
            for i in range(3):
                x = s[:i + 1]
                if not x:
                    return
                if 0<= int(x) <= 255 and len(str(int(x))) == len(x):
                    temp.append(x)
                    backtrack(temp,s[i+ 1 :])
                    temp.pop()
            
        backtrack([] , s)
        
        return ['.'.join(ans) for ans in self.ans]
                    
                    
                
            