num1 = 1020

replace = " "

for i in str(num1):
    if  i == "0" :
        replace = replace + "1"
        
    else :
        replace = replace + i
        
print(replace)