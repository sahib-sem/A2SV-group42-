class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_count=Counter(p)
        index=[]
        start=0
        curr_count={}
        for end in range(len(s)):
            if curr_count.get(s[end]):
                curr_count[s[end]] += 1
            else:
                curr_count[s[end]] = 1
            if end-start+1 >= len(p):
                if p_count==curr_count:
                    index.append(start)
                curr_count[s[start]] -= 1
                if not curr_count[s[start]]:
                    del curr_count[s[start]]
                start += 1
        return index
                           
        
                           
                           
                