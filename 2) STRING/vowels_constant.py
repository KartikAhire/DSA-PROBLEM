char = "u"

vowels = "aeiouAEIOU"

is_vowels = False

for i in range(len(vowels)):
    if vowels[i] == char : 
        is_vowels = True
        
if is_vowels :
    print("vowels")
    
else : 
    print("consonats")