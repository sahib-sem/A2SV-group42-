class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        self.ans = False
        
        def backtrack(num, lst = []):
            
            if len(lst) > 2:
                if int(lst[-1]) != int(lst[-2]) + int(lst[-3]):
                    lst.pop()
                    return
                
                if len(''.join(lst)) == n:
                    self.ans = True
                    return
            
            for i in range(len(num)):
                split = num[: i + 1]
                
                if len(str(int(split))) == len(split):
                    lst.append(split)

                    if i < len(num):
                        backtrack(num[i + 1:])
                
            if lst:
                lst.pop()
        
        backtrack(num)
        
        return self.ans
            
            