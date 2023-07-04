class Solution:
    def candy(self, ratings: List[int]) -> int:
        #[1, 3, 2, 1]
        # 1  3  2  1
        candies = [1] * len(ratings)
        n = len(ratings)
        
        
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
        
        for j in range(n - 1, 0, -1):
            if ratings[j - 1] > ratings[j]:
                candies[j - 1] = max(candies[j] + 1 , candies[j - 1])
            
                
                
            
        return sum(candies)
        
    
    #[1, 6, 10,8,7,3,2]
    #[1, 2  3  2 3 3 1]
                
                
        
        
        
        