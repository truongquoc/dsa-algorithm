class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        digitToChars = {'2':'abc','3': 'def', '4':'ghi', '5': 'jkl', 
        '6': 'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        res= []
        def backtrack(i, currStr):
            if len(currStr) == len(digits):
                res.append(currStr)
                return

            for c in digitToChars[digits[i]]:
                backtrack(i+1, currStr + c)

        backtrack(0, '')
        return res

    
solution = Solution()
print(solution.letterCombinations("23"))  # Example usage