class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_dic={}
        s2_dic={}
        for i in range(97,123):
            s1_dic[chr(i)]=0
            s2_dic[chr(i)]=0
        for char in s1:
            s1_dic[char]+=1
        start=0
        for end in range(len(s2)):
            curr=s2[end]
            s2_dic[curr]+=1
            if end-start+1>=len(s1):
                if s2_dic==s1_dic:
                    return True
                s2_dic[s2[start]]-=1
                start+=1
        return False
                
        