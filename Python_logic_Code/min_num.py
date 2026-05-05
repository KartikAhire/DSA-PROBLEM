list = [3,4,1,2,5]
min_num = list[0]

for i in range(len(list)):
    if min_num > list[i] :
        min_num = list[i]
print(min_num)