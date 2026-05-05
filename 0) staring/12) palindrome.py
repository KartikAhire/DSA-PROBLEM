original = 121

reversed = original

R = 0

while reversed > 0 :
    last_digit = reversed % 10 
    
    R = R*10 + last_digit 
    
    reversed = reversed // 10
    
if original == R :
    print("it is palindrome")
    
else :
    print("it is not palindrome")