class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        my_words = {value: index for index, value in enumerate(wordDict)}
        memo = {}

        def can_segment(start):
            # if start in memo:
            #     return True
            if start in memo:
                return memo[start]
            if start == len(s):
                return True

            if start > len(s):
                return False
            
            for end in range(start, len(s)+1):
                segment = s[start:end+1]
                if segment in my_words:
                    if can_segment(end+1):
                        memo[start] = True
                        return True
            
            memo[start] = False
            return False

        return can_segment(0)

s= "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
solution = Solution()
print(solution.wordBreak(s, wordDict))  # Example usage

