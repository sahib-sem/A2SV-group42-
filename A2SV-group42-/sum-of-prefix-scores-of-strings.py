class TrieNode:
    def __init__(self):
        
        self.children = {}
        self.count = 0

class Trie:
    
    def __init__(self):
        
        self.root = TrieNode()
    
    def add(self, word: str) -> None:
        
        # add word to the trie
        
        curr = self.root
        
        for char in word:
            
            if char not in curr.children:
                
                curr.children[char] = TrieNode()
            
            curr = curr.children[char]
            curr.count += 1
    
    def score(self, word:str) -> int:
        
        curr = self.root
        ans = 0
        
        for char in word:
            
            curr = curr.children[char]
            ans += curr.count
        
        return ans


class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        
        trie = Trie()
        
        for word in words:
            
            trie.add(word)
            
        ans = []
        
        for word in words:
            
            res = trie.score(word)
            
            ans.append(res)
        
        return ans
            
        