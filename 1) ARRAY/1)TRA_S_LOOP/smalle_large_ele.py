arr = [12,4,5,3,2,9]

smallest = arr[0]
largest = arr[0]

for i in range(1, len(arr)):
    if arr[i]  < smallest:
        smallest = arr[i]
        
    if arr[i] > largest :
        largest = arr[i]
        
print(smallest)
print(largest)