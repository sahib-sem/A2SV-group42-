'''    
        *
     a 3 + 2 
    
  p  3 + 2
 
p  3 + 2
  
  l  3
  
    e  3  
 


'''


class TrieNode:
    def __init__(self):
        
        self.children = {}
        self.value = 0
        
class Trie:
    def __init__(self):
        
        self.root = TrieNode()
    
    def add(self, word:str , val:int) -> None:  # for adding new key , value
        
        curr = self.root
        
        for char in word:
            
            if char not in curr.children:
                
                curr.children[char] = TrieNode()
            
            curr = curr.children[char]
            curr.value += val
        
    
    def update(self, word, update_val):# updating the value of previous key
        
        curr = self.root
        
        for char in word:
            
            curr = curr.children[char]
            curr.value += update_val
    
    def prefix_sum(self, prefix:str) -> int:
        
        curr = self.root
        
        for char in prefix:
            
            if char in curr.children:
                curr = curr.children[char]
            else:
                return 0
        
        return curr.value
            
    
    
class MapSum:

    def __init__(self):
        
        self.key_val = {}
        self.trie = Trie()
        

    def insert(self, key: str, val: int) -> None:
        
        if key in self.key_val:
            prev = self.key_val[key]
            self.trie.update(key, val - prev)
        
        else:
            self.trie.add(key, val)
        
        self.key_val[key] = val 
            
        

    def sum(self, prefix: str) -> int:
        
        return self.trie.prefix_sum(prefix)
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)