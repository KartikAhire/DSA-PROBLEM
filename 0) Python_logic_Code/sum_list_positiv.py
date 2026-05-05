list = [1,2,-3,-5,4,6,-9]
n = len(list)
sum = 0 

for  i in range(0 , n ):
    if list[i] > 0:
        sum = sum + list[i]
        
print(sum)