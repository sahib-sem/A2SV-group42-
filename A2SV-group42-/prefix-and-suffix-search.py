class TrieNode:
    
    def __init__(self):
        
        self.children = {}
        self.idx = -1

class Trie:
    
    def __init__(self):
        
        self.root = TrieNode()
       
    def add_word(self, word:str , idx:int) -> None:
        
        w = ""
        
        lst = []
        
        for i in range(len(word) - 1, -1 , -1):
            
            w = word[i] + w
            
            lst.append(w + '}' + word)
        
        
        for wd in lst:
            
            curr = self.root
            
            for char in wd:
                
                if char not in curr.children:
                    
                    curr.children[char] = TrieNode()
                
                curr = curr.children[char]
                curr.idx = idx
        
    
    def search(self, pref: str , suf:str) -> int:
        
        searchWord = suf + '}' + pref
        
        curr = self.root
        
        for char in searchWord:
            
            if char not in curr.children:
                
                return -1
            
            curr = curr.children[char]
        
        return curr.idx
    
 

class WordFilter:

    def __init__(self, words: List[str]):
        
        self.trie = Trie()
        
        
        for idx , word in enumerate(words):
            self.trie.add_word(word, idx)
            
        

    def f(self, pref: str, suff: str) -> int:
        
        return self.trie.search(pref, suff)


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)