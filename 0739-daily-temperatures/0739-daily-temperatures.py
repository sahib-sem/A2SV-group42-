class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [[temperatures[0],0]]
        ans = defaultdict(int)
        j = 0
        for i in range(1,len(temperatures)):
            while stack and stack[-1][0] < temperatures[i]:
                ans[stack[-1][1]] = i - stack[-1][1]
                stack.pop()
            stack.append([temperatures[i],i])
           
        return [ans[i] for i in range(len(temperatures)) ]
        
        