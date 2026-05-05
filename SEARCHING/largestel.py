arr  = [1,3,6,8,4,6,2,5]
n = len(arr) 
largest = arr[0]

for i in range(1,n):
    if largest < arr[i] :
        largest = arr[i]
     
        
        
print(largest)