# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N, A):
    # Implement your solution here
    counter = [0] * N
    max_count = 0
    last_max = 0
    
    for num in A:
        if 1 <= num <= N:
            if counter[num-1] < last_max:
                counter[num-1] = last_max
            counter[num-1] += 1
            max_count = max(max_count, counter[num-1])
        elif num == N + 1:
            last_max = max_count
    for i in range(N):
        if counter[i] < last_max:
            counter[i] = last_max
    return counter

N = 5
A = [3, 4, 4, 6, 1, 4, 4]
print(solution(N, A))  # Output: [3, 2, 2,