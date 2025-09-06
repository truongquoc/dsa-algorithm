
def build_heap(arr):
    n= len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
    
def pop_heap(arr):
    n = len(arr)
    if n == 0:
        return None
    arr[0], arr[n - 1] = arr[n - 1], arr[0]
    max_value = arr.pop()
    heapify(arr, len(arr), 0)
    return max_value
arr = [3, 9, 2, 1, 4, 5]


print("Original array:", arr)
build_heap(arr)

print("Heapified array:", arr)
for _ in range(5):
    print("Popped element:", pop_heap(arr))
print("Array after popping:", arr)