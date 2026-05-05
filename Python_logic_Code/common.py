#Find common elements in two lists

# list1 = [1,2,3,4]
# list2 = [3,5,1,9]

# common = [ ]

# for i in range(len(list1)) :
#     for j in range(len(list2)):
#         if list1[i] == list2[j] :
#             common.append(list1[i])
# print(common)







def common_elements(list1, list2):
    
    result = []
    
    for i in range(len(list1)):
        if list1[i] in list2:
            result.append(list1[i])
            
    return result
