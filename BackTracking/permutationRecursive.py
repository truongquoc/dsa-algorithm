class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []
        
        def backtrack(start):
            # Base case: if we've reached the end of the array
            if start == len(nums):
                res.append(nums[:]) # Append a copy
                return
            
            for i in range(start, len(nums)):
                # 1. Swap the current element into the start position
                nums[start], nums[i] = nums[i], nums[start]
                
                # 2. Recurse for the next position
                backtrack(start + 1)
                
                # 3. Backtrack: swap back to original state
                nums[start], nums[i] = nums[i], nums[start]
                
        backtrack(0)
        return res
    
# Example usage:
solution = Solution()
print(solution.permute([1, 2, 3]))