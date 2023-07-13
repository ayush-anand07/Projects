# def greet( a ):
#     print("hi {} ".format(a))
#     print("bye")
#     print("Ayush")

# a = "ayush"
# greet(a)


# def greet_with_name(name):
#     print("Hello {}".format(name))
#     print(f"How do you do {name}")

# greet_with_name("ayush")

# def greet_with(name, location ):
#     print(f"Hello {name}")
#     print(f" What is it like  in {location} ? ")

# # greet_with("Ayush", "Bihar") #positiona; arg ument
# greet_with(name = "Ayush", location = "Bihar")
# greet_with( location = "Bihar", name = "Ayush")

# import math
# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5

# def paint_cal(height = test_h, width = test_w, cover = coverage ):
#     area = height*width
#     number_of_can = math.ceil((area/cover))
#     print(f"You'll nedd {number_of_can} cans of paint." )

# paint_cal(height = test_h, width = test_w, cover = coverage)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# def encrypt( text, n = int(shift)):
#     cipher_text = ""
#     for letter in text:
#         num =alphabet.index(letter)
#         num-=n     
#         print(alphabet[num])
#         cipher_text += alphabet[num]

#     print(f"The decoded text is {cipher_text}")
#     # print(f"{'' .join(cipher_text)}")

# encrypt(text, shift)

def decrypt(text, n = int(shift)):
    cipher_text = ""
    for letter in text:
        num =alphabet.index(letter)
        num-=n     
        # print(alphabet[num])
        cipher_text += alphabet[num]

    print(f"The decoded text is {cipher_text}")

decrypt(text, shift)

