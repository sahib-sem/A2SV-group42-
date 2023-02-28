class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        start = 0
        max_length = 0
        picked_fruit = {}
        
        for end in range(len(fruits)):
            
            num = fruits[end]
            picked_fruit[num] = picked_fruit.get(num, 0 ) + 1
            
            while len(picked_fruit) > 2:
                
                num2 = fruits[start]
                picked_fruit[num2] -= 1
                if not picked_fruit[num2]: del picked_fruit[num2]
                start += 1
            max_length = max(max_length , end - start + 1)
        
        return max_length
        