# list1 = [1,2,3,4]
# list2 = [5,3,4,6]

# merge = []

# for i in range(len(list1)) :
#     merge.append(list1[i])
    
# for j in range(len(list2)) :
#     merge.append(list2[j])
    
    
# print(merge)




def merge_two_list(list1, list2):
    merge = []
    
    for i in range(len(list1)):
        merge.append(list1[i])
        
    for j in range(len(list2)):
        merge.append(list2[j])
        
    return merge

n1 = merge_two_list([1,2,3,4,5] , [2,3,4,98,6])

print(n1)
