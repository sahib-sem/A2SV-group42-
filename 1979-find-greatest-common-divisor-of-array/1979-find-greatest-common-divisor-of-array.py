class Solution:
    def findGCD(self, nums: List[int]) -> int:
        smallest = min(nums)
        largest = max(nums)
        def find_gcd(a, b):
            if b == 0:
                return a
            return find_gcd(b, a % b)
        
        return find_gcd(smallest, largest)
        