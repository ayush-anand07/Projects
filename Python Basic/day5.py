# fruits = ["Apple", "Peach", "Pear"]

# for fruit in fruits:
#     print(fruit)
#     print(fruit + " Pie")

# total_height = 0
# students_height = ((input("Enter the height of students"))).split( )
# for height in students_height:
#     total_height = total_height+int(height)
# print(total_height)

# number_of_student = 0

# for students in students_height:
#     number_of_student+=1

# print(number_of_student)

# avg = total_height/number_of_student
# avg = "{:.2f}" .format(avg)
# print(avg)


# highest_score = 0 
# students_scores = input("Enter the marks of students: ").split( )
# for score in students_scores:
#     if score > highest_score:
#         highest_score = score
# print(f"highest score is: {highest_score}" )


# totalsum = 0
# for i in range(2, 101, 2):
#     # print(i)
#     totalsum +=i
# print (totalsum)

# for number in range(1, 101):

#     if number %3 == 0 and number % 5 == 0:
#         print("FizzBuzz")

#     if number %5 == 0:
#         print("Buzz")
    
#     if number %3 == 0:
#         print("Fizz")
    
#     else:
#         print(number)
 
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# for letter in  letters:
#     a = ''.join((random.choices(letters, k = nr_letters)))
# for number in numbers:
#     b = ''.join(random.choices(numbers, k = nr_numbers ))
# for symbol in symbols:
#     c = ''.join(random.choices(symbols, k = nr_symbols))
# print((a+c+b))

#*************************************************XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX************************************

# password=""
# for char in range (0, nr_letters):                        simple password
#     random_char = random.choice(letters)
#     password+= random_char
# for sym in range (0, nr_symbols):
#     random_sym =random.choice(symbols)
#     password += random_sym
# for num in range(0, nr_numbers):
#     random_num = random.choice(numbers)
#     password += random_num

# print(password)

#***************************************************XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX*********************************

# password_list= []
# for char in range (0, nr_letters):
#     random_char = random.choice(letters)
#     password_list+= random_char
# for sym in range (0, nr_symbols):                        # shuffled passowrd
#     random_sym =random.choice(symbols)
#     password_list += random_sym
# for num in range(0, nr_numbers):
#     random_num = random.choice(numbers)
#     password_list += random_num

# print(password_list)
# random.shuffle(password_list)

# password = ""
# for j in password_list:
#     password+= j
# print(password)


#**************************************************XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX****************************************

