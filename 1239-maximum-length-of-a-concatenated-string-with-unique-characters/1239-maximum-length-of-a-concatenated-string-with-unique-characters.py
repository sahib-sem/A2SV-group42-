class Solution:
    def maxLength(self, arr: List[str]) -> int:
        
        self.ans = ''
        self.max_length = 0
        def backtrack(temp , i):
            
            
            
            string = ''.join(temp)
            count = Counter(string)
            valid = True
            for j in count.values():
                if j > 1:
                    valid = False
                    
            if valid:
                if len(string) > self.max_length:
                    self.ans = string
                    self.max_length = len(string)
            
            if i >= len(arr):
                return
            backtrack(temp , i + 1)
            temp.append(arr[i])
            
            backtrack(temp , i + 1)
            temp.pop()
            
        backtrack([] , 0)
        return len(self.ans)
            
        
            
            
            