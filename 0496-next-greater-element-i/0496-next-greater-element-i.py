class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for num1 in nums1:
            look_for = False
            greater_element = -1
            for num2 in nums2:
                if num2 > num1 and look_for:
                    greater_element = num2
                    break
                
                if num1 == num2:
                    look_for = True
            ans.append(greater_element)
        return ans
                    
        
                
                
                
                
            
            
        
        