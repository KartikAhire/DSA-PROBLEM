num = int(input("Enter a number: "))
sum = 0

while num > 0:
    digit = num % 10   # get last digit
    sum += digit       # add it to sum
    num = num // 10    # remove last digit

print("Sum of digits is:", sum)
