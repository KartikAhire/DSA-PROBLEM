# Problem Statement

# Write a program to reverse a given integer number N.

# The program should take an integer as input and print the reversed number.

# If the number contains trailing zeros, they should be removed after reversing.

# Input Format
# A single integer N
# Output Format
# Print the reversed number


num = int(input("emter the numbers : "))

reversed = 0

while num > 0 :
    digit = num % 10 
    
    reversed = reversed * 10 + digit 
    
    n = n // 10 
    
print(reversed)
    