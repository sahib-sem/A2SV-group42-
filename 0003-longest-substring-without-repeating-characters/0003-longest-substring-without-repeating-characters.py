class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start=0
        char=set()
        longest=0
        for end in range(len(s)):
            while s[end] in char:
                char.remove(s[start])
                start+=1
            char.add(s[end])
            longest=max(longest , end-start+1)
        return longest
                
                