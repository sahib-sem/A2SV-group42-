class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        
        dp = {(nums[0] , None): 1}
        
        for i in range(1, len(nums)):
            
            num = nums[i]
            lst = list(dp.items())
            
            for key, val in lst:
                
                if num > key[0]:
                    
                    if key[1] == None:
                        dp[(num, False)] = max(val + 1, dp.get((num, False) , 0))
                        
                    if key[1] == True:
                        dp[(num, False)] = max(val + 1, dp.get((num, False) , 0))
                elif num < key[0]:
                    
                    if key[1] == None:
                        dp[(num, True)] = max(val + 1, dp.get((num, True) , 0))
                    
                    if key[1] == False:
                        dp[(num, True)] = max(val + 1, dp.get((num, True) , 0))
            
        
        return max(dp.values())