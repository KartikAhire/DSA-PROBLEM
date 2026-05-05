prices = [10 , 4 , 5 ,90 , 120 , 80]
n = len(prices)
span = [0] * n 

stack = []

for i  in range(n):
    while stack  and prices[stack[-1]] <= prices[i]:
        stack.pop()
        
    if not stack :
        span[i] = i+1
        
    else :
        span[i] = i - stack[-1]
        
    stack.append(i)
    
print(span)