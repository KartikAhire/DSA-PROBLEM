arr = [3,4,2,1,6,9]

smallest_element = arr[0]

for i in range(1,len(arr)):
    if arr[i] < smallest_element:
        smallest_element = arr[i]
        
        
        
        
print(smallest_element)