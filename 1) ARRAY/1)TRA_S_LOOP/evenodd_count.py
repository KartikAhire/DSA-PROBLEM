#Count Even and Odd Numbers

arr = [2,6,4,7,47,48,49,37,236,2,62,51,51,6,8,8,2]

even = 0
odd = 0 


for i in range(len(arr)):
    if arr[i] % 2 == 0 :
        even = even + 1 
        
    else : 
        odd = odd + 1
        
print("even" , even)
print("odd", odd)