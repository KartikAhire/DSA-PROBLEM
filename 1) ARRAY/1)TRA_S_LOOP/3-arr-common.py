arr1 = [1, 5, 10, 20, 40, 80]
arr2 = [6, 7, 20, 80, 100]
arr3 = [3, 4, 15, 20, 30, 70, 80, 120]

common = []

for x in arr1:
    if x in arr2 and x in arr3:
        if x not in common:
            common.append(x)

print("Common Elements:", common)
