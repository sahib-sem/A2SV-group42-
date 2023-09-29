
'''
        
        sort the input string using length in reverse order
        
        o(K^2 nlogn) 
        word ->
        
        bruteforce will pass
        
        
            w 5    o(k * n)
            
         o  4 
         
      r 3
     
    l 2
    
   d 1
    
'''

class TrieNode:
    
    def __init__(self):
        
        self.children = {}
        self.count = 0
        self.is_end = False
    

class Trie:
    
    def __init__(self):
        
        self.root = TrieNode()
    
    def add(self, word:str) -> None:
        curr = self.root
        
        for char in word:
            
            if char not in curr.children:
                curr.children[char] = TrieNode()
                
            curr = curr.children[char]
            curr.count += 1
        
        curr.is_end = True
    
    def check_can_make_one_by_one(self, word:str) -> bool:
        
        n = len(word)
        
        curr = self.root
        
        for char in word: # world -> w 
            
            if char not in curr.children:
                return False
            
            curr = curr.children[char]
        
            if curr.count < n:
                return False
            
            if not curr.is_end:
                return False
            
            n -= 1
        
        return True
            
        
        

class Solution:
    def longestWord(self, words: List[str]) -> str:
        
        words = sorted(words , key = lambda x : (len(x), x))
        
        trie = Trie()
        
        for word in words:
            trie.add(word)
        
        maximum_length = 0
        ans = ""
        
        for word in words:
            
            res = trie.check_can_make_one_by_one(word) 
            
            if res and len(word) > maximum_length:
                maximum_length = len(word)
                ans = word
        
        
        return ans
            
        