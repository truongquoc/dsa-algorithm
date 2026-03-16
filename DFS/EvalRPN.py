
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def dfs():
            token = tokens.pop()
            if token not in "+-*/":
                return int(token)
            right_operand = dfs()
            left_operand = dfs()
            
            if token == '+':
                return left_operand + right_operand
            elif token == '-':
                return left_operand - right_operand
            elif token == '*':
                return left_operand * right_operand
            elif token == '/':
                return int(left_operand / right_operand)

        return dfs()
    
tokens = ["2","1","+","3","*"]
solution = Solution()
print(solution.evalRPN(tokens))  # Output: 9
        
        




        