import ceasercypher_art
print(ceasercypher_art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def ceaser( plain_text ,  n, d):
    cipher_text = ""
    for letter in plain_text:
        if letter in alphabet:
            num =alphabet.index(letter)
            if d == "encode":
                num+=n 
                cipher_text += alphabet[num] 
            if d =="decode":
                num-=n 
                cipher_text += alphabet[num] 
        else:
            cipher_text+= letter
            
    
    print(f"The {direction}d text is {cipher_text}")
shift = shift%26
ceaser(plain_text=text, n = shift, d =direction )

a =True
while a:
        user_input = input("Type 'yes' to continue or 'no' to exit\n")
        if user_input == "yes".lower():
            direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
            text = input("Type your message:\n").lower()
            shift = int(input("Type the shift number:\n"))
            shift = shift%26
            ceaser(plain_text=text, n = shift, d =direction )
        elif user_input =="no".lower():
            print("Thank you")
            a= False

        
        else:
            print("Invalid input")
       

