class Solution:
    def maxArea(self, height: List[int]) -> int:
        i,j=0,len(height)-1
        max_=0
        while j>i:
            l=height[i]
            r=height[j]
            width=j-i
            if l<r:
                area=width*l
                max_=max(max_,area)
                i+=1
            else:
                area=width*r
                max_=max(max_,area)
                j-=1
        return max_ 
                