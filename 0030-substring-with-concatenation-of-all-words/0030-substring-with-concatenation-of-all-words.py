class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        
        substring = ''.join(words)
        length = len(substring)
        single_word = len(words[0])
        count_words = dict(Counter(substring))
        
        word_mapping = dict(Counter(words))
        
        start = 0
        current_count = {}
        n = len(s)
        ans = []
        
        for end in range(n):
            
            char = s[end]
            current_count[char] = current_count.get(char , 0) + 1
            
            if end - start + 1 > length:
                current_count[s[start]] -= 1
                if not current_count[s[start]]: del current_count[s[start]]
                start += 1
            
            if current_count == count_words:
                
                curr = ''
                valid = True
                st, ed = start , end
                check = {}
                i = 1
                while st <= ed:
                    
                    curr += s[st]
                    if len(curr) == single_word:
                        if not word_mapping.get(curr, 0):
                            valid = False
                            break
                        else:
                            check[curr] = check.get(curr , 0) + 1
                        curr = ''
                    
                    st += 1
                
                if valid and check == word_mapping:
                    ans.append(start)
            
        return ans
                    
                    
                
            
            
            
            
        
        
        