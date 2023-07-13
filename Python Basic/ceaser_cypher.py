import ceasercypher_art
print(ceasercypher_art.logo)
a=0


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',]
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt( text, n = int(shift)):
    cipher_text = ""
    for letter in text:
        num =alphabet.index(letter)
        num+=n
        # print(alphabet[num])
        cipher_text += alphabet[num]
    if n >26:
            n = n%26
    print(f"The encoded text is {cipher_text}")
    # print(f"{'' .join(cipher_text)}")
if direction == "encode":
    encrypt(text, shift)  

def decrypt(text, n = int(shift)):
    cipher_text = ""
    for letter in text:
        num =alphabet.index(letter)
        num-=n     
        # print(alphabet[num])
        cipher_text += alphabet[num]

    print(f"The decoded text is {cipher_text}")
if direction == "decode":
    decrypt(text, shift)



