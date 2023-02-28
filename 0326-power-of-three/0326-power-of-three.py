class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1.0:
            return False
        if n == 1.0:
            return True
        return self.isPowerOfThree(n/3)
        