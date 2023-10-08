class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        
        ipv6_valid_characters = set()
        
        for idx in range(ord('a') , ord('a') + 6):
            ipv6_valid_characters.add(chr(idx))
            ipv6_valid_characters.add(chr(idx).upper())
            
        for digit in range(10):
            ipv6_valid_characters.add(str(digit))
        
        
        def validIpv4(Ip4):
            
            subsections = Ip4.split(".")
            
            if len(subsections) != 4:
                return False
            
            ans = True
            for sub in subsections:
                
                
                try:
                    
                    res = int(sub)
                    
                    if res > 255 or res < 0:
                        ans = False
                    
                    if len(str(res)) < len(sub):
                        ans = False
                
                except:
                    ans = False
            
                
                if not ans:
                    break
                
            return ans
        
        def validIpv6(Ip6):
            
            subsections = Ip6.split(':')
            
            if len(subsections) != 8:
                return False
            
            for sub in subsections:
                
                if len(sub) == 0 or len(sub) > 4:
                    return False
                
                for char in sub:
                    if char not in ipv6_valid_characters:
                        return False
                
            return True
        
        if validIpv4(queryIP):
            return "IPv4"
        
        if validIpv6(queryIP):
            return "IPv6"
        
        return "Neither"
        