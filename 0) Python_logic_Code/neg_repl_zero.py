arr = [1,-2,3,-4,-5,6,3,-7]

for i in range(len(arr)):
    if arr[i] < 0 :
        arr[i] = 0
        
print(arr)