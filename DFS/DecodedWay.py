class Solution:
    def numDecodings(self, s: str) -> int:
        res=[]
        def dfs(start, decoded):
            if start >= len(s):
                res.append(decoded.copy())
                return
            decoded.append(s[start])
            dfs(start+1, decoded)
            decoded.pop()
            # if start +1 < len(s):
            decoded.append(s[start:start+2])
            dfs(start+2, decoded)
            decoded.pop()

        dfs(0, [])
        return res

main = Solution()
print(main.numDecodings("12"))