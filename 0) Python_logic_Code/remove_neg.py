#Remove negative numbers from list

def remove_fun(list) :
    ren_neg_num = []
    
    for i in range(len(list)):
        if list[i] > 0 :
            ren_neg_num.append(list[i])
            
    return ren_neg_num

print(remove_fun([1,-2,3,-4,5,-3]))