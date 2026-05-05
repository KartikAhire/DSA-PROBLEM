#Remove all characters from string except alphabets

string = "kartik@123"
aplhabets = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


remove_character  = ""

for i in string :
    if i in aplhabets :
        remove_character = remove_character + i
print(remove_character)