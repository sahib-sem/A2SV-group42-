class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        start = 0
        char = {}
        max_length = 0
        
        for end in range(len(s)):
            if char.get(s[end]):
                char[s[end]] += 1
            else:
                char[s[end]] = 1
            maxx = max(char.values())
            sum_ = sum(char.values())
            while len(char) > 1 and sum_ - maxx > k:
                char[s[start]] -= 1
                if not char.get(s[start]):
                    del char[s[start]]
                start += 1
                maxx = max(char.values())
                sum_ = sum(char.values())
            max_length = max(max_length, end - start + 1)
        return max_length
                
        