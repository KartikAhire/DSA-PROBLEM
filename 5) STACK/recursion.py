n = 4
stack = []

# Push values
while n > 0:
    stack.append(n)
    n -= 1

result = 1

# Pop and multiply
while stack:
    result *= stack.pop()

print(result)
