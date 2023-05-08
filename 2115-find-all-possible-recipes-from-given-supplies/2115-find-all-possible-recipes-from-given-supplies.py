class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        # build a graph between the recipes 
        recipe_set = set(recipes)
        graph = defaultdict(list)
        recipe_idx = {item:i for i, item in enumerate(recipes)}
        inDegree = [0 for _ in range(len(recipes))]
        
        for idx, ingredient in enumerate(ingredients):
            for item in ingredient:
                if item in recipe_set:
                    graph[item].append(recipes[idx])
                    inDegree[idx] += 1
                elif item not in supplies:
                    inDegree[idx] = -1
                    break
        
        queue = deque()
        for i in range(len(inDegree)):
            if inDegree[i] == 0:
                queue.append(recipes[i])
        
        order = []
        while queue:
            
            current = queue.popleft()
            order.append(current)
            
            for nei in graph[current]:
                
                inDegree[recipe_idx[nei]] -= 1
                
                if inDegree[recipe_idx[nei]] == 0:
                    queue.append(nei)
                
                
        
        return order
        
        
        