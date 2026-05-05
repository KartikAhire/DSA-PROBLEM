def sum_positive_num(list):
    
    sum = 0 
    
    for i in range(len(list)):
        
        if list[i] > 0 :
            sum = sum + list[i]
            
    return sum


print(sum_positive_num([-4,6,-3,4,12,-4,6,-1]))