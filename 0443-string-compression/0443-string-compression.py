class Solution:
    def compress(self, chars: List[str]) -> int:
        j=0
        lst=[]
        while j<len(chars):
            i=j
            curr=chars[i]
            count=0
            while i<len(chars) and chars[i]==curr:
                count+=1
                i+=1
            j=i
            
            lst.append(curr)
            if count==1:
                continue
            count_lst=list(str(count))
            lst.extend(count_lst)

        chars[:]=lst
        
        return len(chars)
                