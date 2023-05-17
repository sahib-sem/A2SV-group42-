#User function Template for python3
from collections import defaultdict, deque
class Solution:
    def findOrder(self,alien_dict, N, K):
        
        graph = defaultdict(list)
        inDegree = {chr(i + 97):0 for i in range(k)}
        i = 0
        
        while i < len(alien_dict) - 1:
            word1 = alien_dict[i]
            word2 = alien_dict[i + 1]
            n = min(len(word1), len(word2))
            j = 0
            
            while j < n:
                if word1[j] != word2[j]:
                    
                    graph[word1[j]].append(word2[j])
                    inDegree[word2[j]] += 1
                    
                    break

                j += 1
            
            i += 1
        queue = deque()
        order = []
        
        for key, val in inDegree.items():
            if val == 0:
                queue.append(key)
        
        while queue:
            
            current = queue.popleft()
            order.append(current)
            
            for nei in graph[current]:
                
                inDegree[nei] -= 1
                if inDegree[nei] == 0:
                    queue.append(nei)
        if len(order) != k:
            return 0
        
        return order
                    
 
            



#{ 
 # Driver Code Starts
#Initial Template for Python 3

class sort_by_order:
    def __init__(self,s):
        self.priority = {}
        for i in range(len(s)):
            self.priority[s[i]] = i
    
    def transform(self,word):
        new_word = ''
        for c in word:
            new_word += chr( ord('a') + self.priority[c] )
        return new_word
    
    def sort_this_list(self,lst):
        lst.sort(key = self.transform)

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        line=input().strip().split()
        n=int(line[0])
        k=int(line[1])
        
        alien_dict = [x for x in input().strip().split()]
        duplicate_dict = alien_dict.copy()
        ob=Solution()
        order = ob.findOrder(alien_dict,n,k)
        s = ""
        for i in range(k):
            s += chr(97+i)
        l = list(order)
        l.sort()
        l = "".join(l)
        if s != l:
            print(0)
        else:
            x = sort_by_order(order)
            x.sort_this_list(duplicate_dict)
            
            if duplicate_dict == alien_dict:
                print(1)
            else:
                print(0)


# } Driver Code Ends