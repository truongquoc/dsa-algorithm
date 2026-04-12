from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        def dfs(target, combination):
            for candidate in candidates:
                diff = target - candidate
                if diff > 0:
                    combination.append(candidate)
                    dfs(diff, combination.copy())
                elif diff == 0:
                    res.append(combination)
                
        dfs(7, [])
        return res
    
    
main = Solution()
print(main.combinationSum([2,3,6,7], 7))