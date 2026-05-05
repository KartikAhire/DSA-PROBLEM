arr = [1,2,2,3,3,4,5]

dupl = []

for i in arr :
    if i not in dupl :
        dupl.append(i)
        
print(dupl)