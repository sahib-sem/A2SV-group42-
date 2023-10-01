class Trie:
    def __init__(self):
        
        self.root = {}
    
    def add(self, num):
        
        bits = bin(num).replace("0b", "")
        bits = "0" * (32 - len(bits)) + bits
        curr = self.root
        
        for b in bits:
            
            
            if b not in  curr:
                curr[b] = {}
            
            curr = curr[b]
    
    def max_sum(self, num1):
        
        bits = bin(num1).replace("0b","")
        bits = "0" * (32 - len(bits)) + bits
        curr = self.root
        lst = []
        
        for b in bits:
            
            if b == "1":
                if "0" in curr:
                    curr = curr["0"]
                    lst.append("0")
                else:
                    curr = curr["1"]
                    lst.append("1")
                
            else:
                if "1" in curr:
                    curr = curr["1"]
                    lst.append("1")
                else:
                    curr = curr["0"]
                    lst.append("0")
                    
        num2 = int("".join(lst) , 2)
        
        
        return num1 ^ num2

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        
        trie = Trie()
        
        maximum = 0
        
        for num in nums:
            
            trie.add(num)
            res = trie.max_sum(num)
        
            maximum = max(res, maximum)
        
        
        
        return maximum
        