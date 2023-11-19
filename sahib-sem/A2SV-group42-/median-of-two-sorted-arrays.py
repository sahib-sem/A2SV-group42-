class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        
        total = len(nums1) + len(nums2)
        half = (total) // 2
        
        l, r = 0 , len(nums1) - 1
        
        while True:
            
            mid1 = (r + l) // 2
            mid2 = half - mid1 - 2
            
            Aleft = nums1[mid1] if mid1 >= 0 else float('-inf')
            Aright = nums1[mid1 + 1] if mid1 < len(nums1) - 1 else float('inf')
            Bleft = nums2[mid2] if mid2 >= 0 else float('-inf')
            Bright = nums2[mid2 + 1] if mid2 < len(nums2) - 1 else float('inf')
            
            if Bright >= Aleft and Aright >= Bleft:
                if total % 2:
                    return min(Aright , Bright)
                
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            
            elif Aleft > Bright:
                r = mid1 - 1
            else:
                l = mid1 + 1
            
        
        
        