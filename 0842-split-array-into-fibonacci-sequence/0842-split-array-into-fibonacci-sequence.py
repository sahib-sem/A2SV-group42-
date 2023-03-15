class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:
        
        n = len(num)
        self.ans = []
        limit = 2 ** 31
        def backtrack(num , lst = []):
            
            if len(lst) > 2:
                
                if int(lst[-1]) != int(lst[-2]) + int(lst[-3]):
                    lst.pop()
                    return
                if len(''.join(lst)) == n:
                    for i in lst:
                        if not is_int32(i):
                            return
                    self.ans = lst[:]
                    return 
            
            for i in range(len(num)):
                
                split = num[: i + 1]
                
                if len(str(int(split))) == len(split) or split == '0':
                    lst.append(split)
                    
                    if i < len(num):
                        backtrack(num[i + 1:])
            if lst:
                lst.pop()
        
        def is_int32(number):
            if 0 <= int(number) < limit:
                return True
            return False
            
        backtrack(num)
        
        return list(map(int, self.ans))