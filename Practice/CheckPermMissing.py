# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    N = len(A)
    num_set = set()

    for num in A:
        if num < 1 or num > N:
            return 0
        num_set.add(num)
    
    for i in range(1, N+1):
        if i not in num_set:
            return 0
    
    return 1

A = [4, 1, 3, 2]
print(solution(A))  # Output: 1