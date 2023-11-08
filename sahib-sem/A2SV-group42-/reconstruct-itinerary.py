class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        '''

        
        '''

        graph = defaultdict(list)

        tickets = sorted(tickets, reverse = True)
        for fr , to in tickets:
            graph[fr].append(to)
        

        ans = []

        def dfs(current):
            nonlocal ans

            while graph[current]:
                dfs(graph[current].pop())

            ans.append(current)

        dfs("JFK")
        return ans[::-1]
        
    

            
            
            




            
        
        
            
        
        