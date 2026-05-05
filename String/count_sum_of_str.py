#Count the sum of numbers in a string

str = "kar45kjd5403jfd453"


aplhabets = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

sum = 0 

for i in str :
    if i not in aplhabets :
        sum = sum + int(i)
print(sum)