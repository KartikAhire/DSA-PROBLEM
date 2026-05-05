arr = [1,3,5,4]
n = len(arr)
largest = arr[0]

for i in range(n):
   
        if largest < arr[i]  :
            largest = arr[i]
            
print(largest)
            