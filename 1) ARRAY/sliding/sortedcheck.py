arr = [2,4,5,6,7]
n = len(arr)
sorted_array = True

for i in range(n-1):
    
    if arr[i] > arr[i+1]:
        sorted_array = False
        break
    
print(sorted_array)
        