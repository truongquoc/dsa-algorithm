class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result = []

        # Base case: If there is only one number, the only permutation is the number itself
        if len(nums) == 1:
            return [nums[:]]

        for i in range(len(nums)):
            # 1. Remove the first element
            n = nums.pop(0)
            
            # 2. Get all permutations of the remaining elements
            perms = self.permute(nums)

            # 3. Add the removed element back to the end of every sub-permutation
            for perm in perms:
                perm.append(n)
            
            # 4. Add these completed permutations to our final result
            result.extend(perms)
            
            # 5. Backtrack: Put the element back into nums so the next 'i' can use it
            nums.append(n)

        return result
    
    
# Example usage:
solution = Solution()
print(solution.permute([1, 2, 3]))