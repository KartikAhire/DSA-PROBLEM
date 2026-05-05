# largest value

def largest_num(num):
    
    largest = num[0]
    
    for i in range(len(num)):
        if largest < num[i] :
            largest = num[i]
            
            
    return largest


print(largest_num([1,2,3,4,5,1,3,7,38,37,26,2,6,2]))