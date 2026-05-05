str = "madssm" 
original = str

rev = ""

for ch in original:
    rev = ch + rev  
    
if original == rev :
    print("palindrome")
    
else :
    print("not palindrome")
    