n = 10 

first = 0 
second = 1 

while n > 0:
    
    next_sum = first + second 
    print(next_sum)
    
    first = second 
    second = next_sum
    
    n = n - 1
