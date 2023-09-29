
class TrieNode:
    
    def __init__(self):
        
        self.children = {}
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
        
        curr.is_end = True
            
        
        

class Solution:
    def longestWord(self, words: List[str]) -> str:
        
        
        
        trie = Trie()
        
        for word in words:
            trie.add(word)
        
        
        ans = ""
        
        stack = [(trie.root , "")]
        
        while stack:
            
            current, word = stack.pop()
            
            for char, child in current.children.items():
                
                if child.is_end:
                    next_word = word + char
                    stack.append((child, next_word))
                    
                    if len(next_word) > len(ans) or (len(next_word) == len(ans) and next_word < ans):
                        
                        ans = next_word
        
        return ans
                    
            
        