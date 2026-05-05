# arr = [1,2,3,4,5,1]

# duplicatrs_arr = [ ]

# for i in range(len(arr)):
#     if arr[i] not in duplicatrs_arr :
#         duplicatrs_arr.append(arr[i])
        
        
# print(duplicatrs_arr) 







# duplicstes remove 










arr = [1,2,3,4,5,2,3,6,7,4]

dupli_arr = [ ]

for i in range(len(arr)):
    if arr[i] not in dupli_arr : 
        dupli_arr.append(arr[i])
        
print(dupli_arr)




nums = [3,1,3,4,2]
n = len(nums)

for i in range(n):
    for j in range(i+1, n):
        if nums[i] == nums[j]:
            print(nums[i])
            break