# Gym Membership Discount

age = int(input("enter the age : "))
months = int(input("enter the month : "))

fees = 5000 


if age >= 60 and  months >= 12 :
    discount = 40 
    
elif age >= 60 :
    discount = 30
    
elif months >= 12 :
    discount = 20 
    
else :
    discount = 0 
    
finel_discount = fees * discount // 100 

finel_amount = fees - discount

print(finel_amount)