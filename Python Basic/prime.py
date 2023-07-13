# a = int(input("Enter an interger: "))
# def prime_checker(number):
#     is_prime = True
#     for i in range (2, number):
#         if number%i == 0:
#             is_prime = False
#     if is_prime:
#         print(f"1 & {number}")
#         # print("Its a prime number.")
#     else:
#         print("Its not a prime number")  

# prime_checker(a)















# Evaluate and print the equation Y=8X²+ 1, for X values from -5 to 5 using the range function and for loop

from math import pow


for i in range (-5 , 6):
    print("Y=8X²+ 1")
    b = int(8*pow(i,2)+1)
    print(f"Y={b}")

    
 