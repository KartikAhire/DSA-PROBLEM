
# #right rotate 
# def rotate_array(arr):
#     n = len(arr)
    
#     last = arr[n-1]
#     for i in range(n-1,0,-1):
#         arr[i] = arr[i-1]
        
#     arr[0] = last 
    
#     return arr


# print(rotate_array([1,2,3,4,5]))


# left rotate 













def left_rotate(arr):
    n = len(arr)
    
    first = arr[0]
    
    for i in range(0 , n-1 ):
        arr[i] = arr[i+1]
        
        
    arr[n-1] = first 
    
    return arr 

print(left_rotate([1,2,3,4,5]))