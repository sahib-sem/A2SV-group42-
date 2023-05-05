class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = Counter(words)
        lst = []
        for word, freq in counter.items():
            heapq.heappush(lst, (-1  * freq, word))
        
        res = []
        for _ in range(k):
            res.append(heapq.heappop(lst)[1])
        
        return res
        
            
        