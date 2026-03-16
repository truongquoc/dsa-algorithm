def checkInclusion(s1: str, s2: str) -> bool:
    if len(s1) > len(s2):
            return False 
    char_arr = [0] * 26
    match_arr = [0] * 26
    for c in s1:
        char_arr[ord(c) - ord('a')]+=1

    left = 0
    for right in range(len(s2)):
        idx = ord(s2[right]) - ord('a')
        match_arr[idx] += 1
        # Shrink window if size exceeds s1
        if right - left + 1 > len(s1):
            match_arr[ord(s2[left]) - ord('a')] -= 1
            left += 1
        # Check if window matches
        if match_arr == char_arr:
            return True
    return False
                

s1 = "adc"
s2 = "dcda"
print(checkInclusion(s1, s2))  # Output: True


coins = [1,2,5], amount = 11

dp = [amount + 1] * (amount + 1)
dp[0] = 0
for coin in coins:
    for x in range(coin, amount + 1):
        dp[x] = min(dp[x], dp[x - coin] + 1)
print(dp[amount] if dp[amount] != amount + 1 else -1)
#example 

#eidbaooo
#ab

# "ab"
# "eidboaoo"


