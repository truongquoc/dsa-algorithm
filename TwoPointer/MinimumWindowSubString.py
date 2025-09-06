class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        t_count = {}
        s_count = {}
        matcher = 0

        for ch in t:
            t_count[ch] = t_count.get(ch, 0) + 1
        
        j = 0
        min_length = float('inf')
        res = ""
        for index, ch in enumerate(s):
            s_count[ch] = s_count.get(ch, 0) + 1

            if ch in t_count and t_count[ch] == s_count[ch]:
                matcher+=1
            
            while j <= index and matcher == len(t_count):
                if index - j + 1 < min_length:
                    res = s[j:index+1]
                    min_length = len(res)
                j+=1
                s_count[s[j-1]]-=1
                
                if s_count.get(s[j-1]) < t_count.get(s[j-1], 0):
                    matcher-=1


        return res


if __name__ == "__main__":
    s = "cabwefgewcwaefgcf"
    t = "cae"
    solution = Solution()
    result = solution.minWindow(s, t)
    print(f"Minimum window substring: '{result}'")


