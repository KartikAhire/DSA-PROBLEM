arr = [1,3,4,1,2]

duplicates = 0

for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i] == arr[j]:
            duplicates = arr[i]
print(duplicates)