class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        lst = [0] * len(s)
        lst.append(0)
        
        for shift in shifts:
            direction = shift[-1]
            if direction == 1:
                lst[shift[0]] += 1
                lst[shift[1] + 1] -= 1
            else:
                lst[shift[0]] -= 1
                lst[shift[1] + 1] += 1
                
        ans = ''
        running_sum = 0
        
        for i in range(len(lst)-1):
            running_sum += lst[i]
            char = ord(s[i]) - 97
            char += running_sum 
            while char < 0:
                char += 26
            while char > 25:
                char -= 26
            
            ans += chr(char + 97)
        return ans
                
            
            
            
            
                