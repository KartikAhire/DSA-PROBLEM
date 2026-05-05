# count even and odd numbers using function 


def count_even_odd(numbers_list):
    even = 0 
    odd = 0 
    
    for i in range(len(numbers_list)):
        if numbers_list[i] % 2 == 0 :
            even = even + 1 
            
        else :
            odd = odd + 1 
            
    return "even",even , "odd",odd 
            
print(count_even_odd([1,2,3,4,5,6,7,8]))