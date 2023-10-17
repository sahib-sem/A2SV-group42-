class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        
        
        # nums[i - 2] == nums[i]
        # nums[i - 1] != nums[i]
        
        if len(nums) == 1:
            
            return 0
            
        even = defaultdict(int)
        odd = defaultdict(int)
        n = len(nums)
        
        for i in range(0, n, 2):
            
            even[nums[i]] += 1
        
        for i in range(1, n , 2):
    
            odd[nums[i]] += 1
                
        
        mid_even = n // 2
        mid_odd = ceil(n / 2)
        
        even = [(v, k) for k, v in even.items()]
        odd = [(v, k) for k, v in odd.items()]
        even.sort(reverse = True)
        odd.sort(reverse = True)
        
        
        ans1 = mid_even - even[0][0]
        
        if odd[0][1] != even[0][1]:
            
            ans1 += mid_odd - odd[0][0]
        
        else:
            
            o , e = mid_odd , mid_even 
            if 1 < len(odd):
                o =  mid_odd - odd[1][0]
            if 1 < len(even):
                e = mid_even - even[1][0]
            
            ans1 = min(ans1 + o, mid_odd - odd[0][0] + e)
        
        return ans1
     
        
        