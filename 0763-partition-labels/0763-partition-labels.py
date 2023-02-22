class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d={c:i for i,c in enumerate(s)}
        res,size,end=[],1,0
        for i,c in enumerate(s):
            end=max(end,d[c])
            if i==end:
                res.append(size)
                size=1
            else:
                size+=1
        return res