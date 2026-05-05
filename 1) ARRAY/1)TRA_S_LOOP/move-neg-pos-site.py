arr = [-1,-2,3,-5,5,9,-6]

neg = []
pos = []

for x in arr :
    if x < 0 :
        neg.append(x)
        
    else :
        pos.append(x)
        
arr_site = neg+pos

print(arr_site)