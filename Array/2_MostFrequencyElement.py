def maxFrequency(nums, k) -> int:
    left, right, total, mfe = 0, 0, 0, 0

    while right < len(nums):
        total+=nums[right]

        if nums[right] * (right-left+1) - total <= k:
            right+=1
            mfe+=1
        else:
            total-=nums[left]
            left+=1
            right+=1
            mfe-=1
            
    return mfe

nums = [1,4,8,13]
k = 5
print(maxFrequency(nums, k))  # Output: 3