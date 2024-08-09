alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text, shift):
    text_list = list(text)
    
    for i in range(len(text_list)):
        index = alphabet.index(text_list[i])
        if index + shift > 25:
            text_list[i] = alphabet[index + shift - 26]
        else:
            text_list[i] = alphabet[index + shift]

    encrypted_text = "".join(text_list)

    return encrypted_text

encrypted_text = encrypt(text, shift)

print(encrypted_text)
