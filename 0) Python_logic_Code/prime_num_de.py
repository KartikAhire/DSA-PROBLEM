def prime_num(n):
    
    count = 0 
    
    if n <= 1 :
        
        return "not prime num"
    
    else :
        
        for i in range(2,n):
            if n % i == 0 :
                count = count + 1
                
                
    if count == 0 :
        return "prime"
    
    else :
        return "not prime"
    
    
print(prime_num(11))
        