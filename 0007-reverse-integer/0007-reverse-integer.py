class Solution:
    def reverse(self, x: int) -> int:
        upper_range=2**31-1
        lower_range=-2**31
        negative=False
        reversed_number=0
        if x<0:
            negative=True
            x*=-1
        unit_digit=10**(len(str(x))-1)
        
        
            
        while x:
            last_digit=x%10
            reversed_number+=last_digit*unit_digit
            unit_digit//=10
            x//=10
        if negative:
            reversed_number*=-1
        if lower_range<=reversed_number<=upper_range:
            return reversed_number
        else: return 0
            
            
            