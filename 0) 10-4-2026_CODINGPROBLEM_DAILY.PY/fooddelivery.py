# #💻 Food Delivery Charges

# order_amount = int(input())
# is_prime = input().lower()
# is_raining = input().lower()

# # Step 1: Check Prime (highest priority)
# if is_prime == "yes":
#     charge = 0

# else:
#     # Step 2: Base delivery charge
#     if order_amount < 500:
#         charge = 50
#     elif order_amount <= 1000:
#         charge = 30
#     else:
#         charge = 0

#     # Step 3: Add rain charge
#     if is_raining == "yes":
#         charge += 20

# # Step 4: Output
# print(charge)

amount = int(input("Enter amount: "))
is_prime = input("Is number prime (yes/no): ").lower()

# Step 1: Check Prime (user input based)
if is_prime == "yes":
    final_amount = amount - (0.10 * amount)
else:
    final_amount = amount

# Step 2: Output
print(final_amount)





fees = int(input("enter feees : "))

is_scholership = input('is scholership (yes/no) : ').lower()

if is_scholership == "yes" :
    finelsfeess = fees - 0.50 * fees 
else :
    finelsfeess = fees 
    
print(finelsfeess)