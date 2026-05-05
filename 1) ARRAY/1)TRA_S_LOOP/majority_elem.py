arr = [1,2,1,3,1]
n = len(arr)
for i in range(n):
    count = 0 
    
    for j in range(n):
        if arr[i] == arr[j]:
            count = count + 1 
            
            
if count > n//2 :
    print(arr[i])