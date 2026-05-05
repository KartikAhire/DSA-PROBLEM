# arr = [12,2,3,5,6,13,4]
# max_num = arr[0]

# largest_num = 0 

# for i in range(1, len(arr)):
#     if arr[i] > max_num :
#         max_num  = arr[i]
        
        
# print(max_num)


# FIND THE LARGEST ELEMENTS IN THE ARRAY 

arr = [3,5,2,6,3,8,8,3,2,5,2,56,8,4]

max_num = arr[0]

largest = 0  

for i in range(1,len(arr)):
    if arr[i] > max_num :
        max_num = arr[i]
        
print(max_num)