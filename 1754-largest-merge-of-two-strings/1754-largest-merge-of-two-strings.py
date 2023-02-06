class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        i=j=0
        merge=""
        while i<len(word1) and j<len(word2):
            if word1[i]>word2[j]:
                merge+=word1[i]
                i+=1
            elif word1[i]<word2[j]:
                merge+=word2[j]
                j+=1
            else:
                ii=i
                jj=j
                flag=False
                while ii<len(word1) and jj<len(word2):
                    if word1[ii]>word2[jj]:
                        merge+=word1[i]
                        i+=1
                        flag=True
                        break
                    elif word1[ii]<word2[jj]:
                        merge+=word2[j]
                        j+=1
                        flag=True
                        break
                    else:
                        ii+=1
                        jj+=1
                
                if not flag:
                    if jj<len(word2):
                        merge+=word2[j]
                        j+=1
                    elif ii < len(word1):
                        merge+=word1[i]
                        i+=1   
                    else:
                        merge+=word1[i]
                        i+=1               
        merge+=word1[i:]
        merge+=word2[j:]
        return merge
            
            