class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        cars = []
        stack = []
        
        for i in range(len(position)):
            
            cars.append([position[i],speed[i]])
            
        cars.sort(reverse = True)
        
        for car_pos , car_speed in cars:
            
            time = (target - car_pos) / car_speed             
            stack.append(time)
            
            while len(stack) >= 2 and stack[-2] >= stack[-1]:
                stack.pop()
                
        return len(stack)
        
        