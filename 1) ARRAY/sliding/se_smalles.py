arr = [1,3,2,4]
smallest = float("inf")
second_smallest = float("inf")

for i in arr : 
    if i > smallest :
        second_smallest = smallest 
        smallest = i 
        
    elif i != smallest and i < second_smallest:
        second_smallest = i 
        
print(second_smallest)