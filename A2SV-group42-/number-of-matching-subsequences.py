class TrieNode:
    def __init__(self):
        
        self.children = {}
        self.is_end = False
        self.visited = False
        
class Trie:
    
    def __init__(self):
        self.root = TrieNode()
    
    def add(self, word):
        
        curr = self.root
        
        for char in word:
            
            if char not in curr.children:
                curr.children[char] = TrieNode()
            
            curr = curr.children[char]
        
        curr.is_end = True


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        
        '''
            i = 0, curr 
            abcde ->    a bb acd
            
            1, curr['a']  1, curr
            curr.is_end: return 1
            i == len(s) return 0
        
        '''
#         self.ans = 0
#         def recursion(i , curr,word_count ,temp = ""):
            
            
                
#             if i == len(s):
#                 return 
            
            
#             if s[i] in curr.children and not curr.children[s[i]].visited:
#                 if curr.children[s[i]].is_end:
                    
#                     self.ans += word_count[temp + s[i]]
                    
#                 curr.children[s[i]].visited = True
#                 recursion(i + 1, curr.children[s[i]],word_count ,temp + s[i])
                
                
                
#             recursion(i + 1, curr ,word_count ,temp)
            
        
#         trie = Trie()
        
#         for word in words:
#             trie.add(word)
        
#         word_count = Counter(words)
#         recursion(0, trie.root, word_count)
        
#         return self.ans

        # letter_indices = {}
        
        letter_indices = defaultdict(list)
        
        for idx, char in enumerate(s):
            letter_indices[char].append(idx)
        
        def check_can_make_substring(word, letter_indices):
            pointers = {chr(i):0 for i in range(ord('a') , ord('a') + 27)}
            
            i = 0
            
            prev = -1
            
            while i < len(word):
                
                char = word[i]
                
                ptr = pointers[char]
                
                if not char in letter_indices or ptr >= len(letter_indices[char]):
                    return False
                
                idx = letter_indices[char][ptr]
                
                if prev >= idx:
                    
                    while ptr < len(letter_indices[char]) - 1:
                        
                        ptr += 1
                        idx = letter_indices[char][ptr]
                        if idx > prev:
                            break
                    
                    if prev >= idx:
                        return False
                
                prev = idx
                pointers[char] += 1
                
                i += 1
            
            return True
        
        ans = 0
        
        word_count = Counter(words)
        
        for word, count in word_count.items():
            
            ans += count if check_can_make_substring(word, letter_indices) else 0
        
        return ans
                    
                
                