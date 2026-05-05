# find the sum of list 

def sum_list(numbers):
    
    sum = 0 
    
    for i in range(len(numbers)):
        sum = sum + numbers[i]
        
        
    return sum 

print(sum_list([1,2,3,4,5,6,7]))