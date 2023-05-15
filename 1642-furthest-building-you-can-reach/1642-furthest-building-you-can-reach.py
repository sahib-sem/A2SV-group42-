class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        
        jumps = []
        
        i = 0
        
        while i < len(heights) - 1:
            
            diff = heights[i + 1] -  heights[i]
            if  diff > 0:
                jumps.append((diff, i + 1))
            
            i += 1
        
        total = 0
        heap = []
        best = [0, 0]
        top_k = 0
        for jump in jumps:
            
            if len(heap) < ladders:
                top_k += jump[0]
                heapq.heappush(heap, jump[0])
            else:
                if heap and jump[0] > heap[0]:
                    top_k -= heapq.heappop(heap)
                    top_k += jump[0]
                    heapq.heappush(heap, jump[0])
                
                
            if (total  + jump[0])- top_k > bricks:
                break
            best = jump
            total += jump[0]
        
        ans = best[1]
        while ans < len(heights) - 1:
            if heights[ans] >= heights[ans + 1]:
                ans += 1
            else:
                break
            
        
        return ans
                
                