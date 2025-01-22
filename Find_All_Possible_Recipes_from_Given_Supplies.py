from collections import defaultdict, Counter

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        available = set(supplies)
        ans = []
        ingredient_to_recipe = defaultdict(set)
        in_degree = Counter()
        
        # First pass: check initial recipes that can be made directly
        for rcp, ingredient in zip(recipes, ingredients):
            non_available = 0
            for ing in ingredient:
                if ing not in available:
                    non_available += 1
                    ingredient_to_recipe[ing].add(rcp)
            if non_available == 0:
                ans.append(rcp)
            else:
                in_degree[rcp] = non_available
        
        # Second pass: check if we can make dependent recipes
        for rcp in ans:
            for recipe in ingredient_to_recipe.pop(rcp, set()):
                in_degree[recipe] -= 1
                if in_degree[recipe] == 0:
                    ans.append(recipe)
        
        return ans
