A = [1, 2, 3]
B = [4, 5, 6]



for i in range(len(A)):
    count = 0
    for j in range(len(B)):
        if A[i] == B[j]:
            count += 1

if count == 0:
    print("it is disjoint")
else:
    print("it is not disjoint")
