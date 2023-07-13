# year = int(input("Which yuear do you want to check ? "))
# 
# if year%4 == 0:
#     if year%100 == 0:
#         if year%400 == 0:
#             print("Leap Year")
#         else:
#             print("Not leap year")      
#     else:
#         print("Leap year")
# 
# else:
#     print(" Not leap Year")

    
import math
for i in range(int(input())):
    a,b,c,d = map(int,input().split())
    
    x = (math.sqrt(((a-0)**2 + (b-0)**2)))
    y = (math.sqrt(((c-0)**2 + (d-0)**2)))

    print(x,y)