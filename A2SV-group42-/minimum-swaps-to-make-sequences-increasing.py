class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        
        '''
        
        exchange =     [(0, (-1, -1))]     [(1, (1, 1))]  [(2, (2, 3))] [(3, (3, 5))]
        
        not_exchange = [(0, (-1, -1))]    [(0, (1, 1))]   [(0, (3, 2))] 
        '''
        
        def dp(i, prev_nums1, prev_nums2, memo = {}):
            
            if i == len(nums1):
                return 0
            
            if (i,prev_nums1, prev_nums2)  in memo:
                return memo[(i,prev_nums1, prev_nums2)]
            
            swap , notSwap = float('inf'), float('inf')
            
            if nums2[i] > prev_nums1 and nums1[i] > prev_nums2:
                
                swap = 1 + dp(i + 1, nums2[i], nums1[i])
            
            if nums1[i] > prev_nums1 and nums2[i] > prev_nums2:
                
                notSwap = dp(i + 1, nums1[i] , nums2[i])
            
            memo[(i,prev_nums1, prev_nums2)] = min(swap, notSwap)
            
            return min(swap, notSwap)
        
        return dp(0, -1, -1)