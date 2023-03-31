class Solution:
    def maxProduct(self, words: List[str]) -> int:
        def change_to_num(word):
            num = 0
            for letter in word:
                num |= 1 << ord(letter) - 96
            
            return num
        
        word = [[change_to_num(word),len(word)] for word in words]
        
        max_length = 0
        for i in word:
            for j in word:
                if i[0] & j[0] == 0:
                    max_length = max(max_length , i[1]*j[1])
        
        return max_length
                
        