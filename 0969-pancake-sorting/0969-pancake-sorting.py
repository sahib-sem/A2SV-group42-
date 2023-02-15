class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        def flip(end):
            start=0 
            while start<end:
                arr[start],arr[end]=arr[end],arr[start]
                start+=1
                end-=1
        res=[]
        for i in range(len(arr)-1,-1,-1):
            index=i
            for j in range(i,-1,-1):
                if arr[index]<arr[j]:
                    index=j
            if i!=index:
                flip(index)
                flip(i)
                res.append(index+1)
                res.append(i+1)
                
        return res
                    
                    
        