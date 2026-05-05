# second largest elemtns

def largest_num(num):
    largest = num[0]
    second = 0 
    
    for i in range(len(num)):
        if largest < num[i] :
            second = largest
            largest = num[i]
          
            
        elif num[i] < largest and num[i] > second :
            
            second = num[i]
            
            
    return second

print(largest_num([1,2,5,36,37,376,26,2]))
            
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
            
            
# def second_largest(nums):
    
#     largest = nums[0]
#     second = 0
    
#     for i in range(len(nums)):
#         if nums[i] > largest:
#             second = largest
#             largest = nums[i]
#         elif nums[i] < largest and nums[i] > second:
#             second = nums[i]
            
#     return second
