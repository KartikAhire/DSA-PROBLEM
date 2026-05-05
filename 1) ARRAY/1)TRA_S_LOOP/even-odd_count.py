arr = [1,2,4,5,2,6,23,52,2,45,2]
n = len(arr)

count_even = 0
count_odd = 0

for i in range(0,n):
    if arr[i] % 2  == 0 :
        count_even=count_even+1
        
    else :
        count_odd = count_odd + 1
        
print("even value:",count_even)
print("odd value:",count_odd)
 

