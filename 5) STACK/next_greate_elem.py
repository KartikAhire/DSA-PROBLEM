arr = [ 1,3,5,2]
n=len(arr)
ans = [-1] * n

for i in range(0,n):
    for j in range(i+1 , n):
        if arr[i] < arr[j] :
            ans[i] = arr[j]
            break            
print(ans)



def nextLargerElement(arr):
    n = len(arr)
    ans = [-1] * n
    stack = []

    for i in range(n - 1, -1, -1):
        while stack and stack[-1] <= arr[i]:
            stack.pop()

        if stack:
            ans[i] = stack[-1]
        else:
            ans[i] = -1   # optional, already -1 hai

        stack.append(arr[i])

    return ans


arr = [1, 3, 5, 2]
print(nextLargerElement(arr))
