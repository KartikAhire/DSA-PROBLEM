## valid paranthesis == > 

def isvalid(s):
    stack = [ ]
    
    for bracket in s :
        if bracket == "(" or bracket == "{" or bracket == "[" :
            stack.append(bracket)
            
        else :
            if len(stack) == 0 :
                return False
            
            ch = stack.pop()
            
            if (bracket == ")" and ch =="(") \
                (bracket == "}" and ch =="{") \
                (bracket == "]" and ch =="[") :
                    
                continue
            
            else : 
                return False
    return len(stack) == 0 

print(isvalid("{{[]}}()"))
























