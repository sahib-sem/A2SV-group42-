class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        
        row1 = set(list("qwertyuiop"))
        row2 = set(list("asdfghjkl"))
        row3 = set(list("zxcvbnm"))
        
        ans = []
        
        for word in words:
            new_word = set([w.lower() for w in word])
            
            if row1.intersection(new_word) == new_word or row2.intersection(new_word) == new_word or row3.intersection(new_word) == new_word:
                ans.append(word)
        
        return ans