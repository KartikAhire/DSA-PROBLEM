arr = [12, 3, 4, 5, 13, 9]

smallest = arr[0]
second_smallest = float('inf')

for i in range(1, len(arr)):
    if arr[i] < smallest:
        second_smallest = smallest
        smallest = arr[i]
    elif arr[i] > smallest and arr[i] < second_smallest:
        second_smallest = arr[i]

print(second_smallest)
