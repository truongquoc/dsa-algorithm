x=5
left, right, square = 1, x, x
if x == 0:
    return 0
if x <=3:
    return 1
while  left < right:
    mid = left + (right-left)//2

    if mid*mid == x:
        return mid
    if mid*mid < x:
        left = mid+1
    elif mid*mid > x:
        right = mid-1
    square = mid