from collections import defaultdict, deque

class Solution:
    def findAllRecipes(self, recipes: list[str], ingredients: list[list[str]], supplies: list[str]) -> list[str]:
        graph = defaultdict(list)
        indegree = defaultdict(int)

        for i in range(len(ingredients)):
            for j in range(len(ingredients[i])):
                graph[ingredients[i][j]].append(recipes[i])
                indegree[recipes[i]] += 1
        
        queue = deque([i for i in supplies])
        recipes = set(recipes)
        possible_recipes = []

        while queue:
            node = queue.popleft()

            for nei in graph[node]:
                indegree[nei] -= 1

                if indegree[nei] == 0:
                    queue.append(nei)
                    possible_recipes.append(nei)
        
        return possible_recipes