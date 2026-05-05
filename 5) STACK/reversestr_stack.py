name = "kartik"

stack = [ ]

for ch in name :
    
    stack.append(ch)
    
    
reverse_str = " "

while stack :
    reverse_str += stack.pop()


print(reverse_str)