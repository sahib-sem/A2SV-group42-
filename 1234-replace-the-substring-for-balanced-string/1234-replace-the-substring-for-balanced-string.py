class Solution:
    def balancedString(self, s: str) -> int:
        
        count_map = {'Q':0 , 'W':0 , 'E':0 , 'R':0}
        to_be_decrement = {}
        
        n = len(s)
        
        for i in range(n):
            
            char = s[i]
            count_map[char] = count_map[char]  + 1
        amount = n // 4
        
        for key,val in count_map.items():
            if val > amount:
                to_be_decrement[key] = val - amount
            
        curr = {}
        start = 0
        min_length = n + 1
        
        if to_be_decrement == {}:
            return 0
        
        have = 0
        need = len(to_be_decrement)
        for end in range(n):
            char = s[end]
            curr[char] = curr.get(char , 0) + 1
            
            if char in to_be_decrement and curr[char] == to_be_decrement[char]:
                have += 1
         
            while have == need:
                
                min_length = min(min_length , end - start + 1)
                if s[start] in to_be_decrement and to_be_decrement[s[start]] == curr[s[start]]:
                    have -= 1
                curr[s[start]] -= 1
                start += 1
        return min_length if min_length != n + 1 else 0
                
            
            
        
        
        