num = 4
count = 0

if num <= 1 :
    print("it is not prime num")
    
else :
    for  i in range(2,num):
        if num % i == 0:
            count = count + 1 
    
    if count == 0:
        print("prime num")
        
    else :
        print("it is not prime num")