arr = [1, 2, 3, 4, 5]

largest = arr[0]
smallest = arr[0]

for i in range(1, len(arr)):
    if arr[i] > largest:
        largest = arr[i]
    if arr[i] < smallest:
        smallest = arr[i]

diff = largest - smallest
print(diff)
