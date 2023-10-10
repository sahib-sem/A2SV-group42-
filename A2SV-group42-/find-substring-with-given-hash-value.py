class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        
        
        curr_hash = 0
        
        power_array = [1]
        
        for i in range(1, k):
            power_array.append(power_array[-1] * power)
        
        start = 0
        n = len(s)
        
        s = s[::-1]
        
        for end in range(n):
            
            curr_hash *= power
            s_i = ord(s[end]) - ord('a') + 1
        
            curr_hash += s_i
            curr_hash %= modulo
            
            if end - start + 1 == k:
            
                if curr_hash == hashValue:
                    ans =  s[start: end + 1]
                
                s_i = ord(s[start]) - ord('a') + 1
                curr_hash -= s_i * (power_array[k - 1])
                curr_hash %= modulo
                start += 1
        
        return ans[::-1]
        
        