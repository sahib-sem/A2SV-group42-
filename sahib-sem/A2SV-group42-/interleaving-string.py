class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        @cache
        def dp(str1_ptr, str2_ptr, str3_ptr):
            if str1_ptr > len(s1) or str2_ptr > len(s2) or str3_ptr > len(s3):
                return False
            if str1_ptr == len(s1) and str2_ptr == len(s2) and str3_ptr == len(s3):
                return True
            
            if str1_ptr == len(s1):
                return s3[str3_ptr:] == s2[str2_ptr: ]
            
            if str2_ptr == len(s2):
                return s1[str1_ptr: ] == s3[str3_ptr: ]
            
            if s3[str3_ptr] == s1[str1_ptr] and s3[str3_ptr] == s2[str2_ptr]:
                return dp(str1_ptr + 1, str2_ptr, str3_ptr + 1) or dp(str1_ptr, str2_ptr + 1, str3_ptr + 1)
            
            if s3[str3_ptr] == s1[str1_ptr]:
                return dp(str1_ptr + 1, str2_ptr, str3_ptr + 1)
            
            if s3[str3_ptr] == s2[str2_ptr]:
                return dp(str1_ptr, str2_ptr + 1, str3_ptr + 1)
            
            return False
        
        return dp(0, 0, 0)

