class Solution:
    def countVowels(self, word: str) -> int:
        
        
        
        vowels = set({'a' , 'e' , 'i' , 'o' , 'u' } )
        
        n = len(word)
        
        ans = 0
        
        for i in range(n):
            
            if word[i] in vowels:
                
                ans += (i + 1) * (n - i)
        
        return ans