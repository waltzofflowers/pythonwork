alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def caesar(text, shift, direction):

  if direction == "encode":
    txt = ""
    for letter in text:
      index = alphabet.index(letter)
      new_index = index + shift
      txt += alphabet[new_index]
    print(f"The encoded text is {txt}")
      
  elif direction == "decode":
    txt = ""
    for letter in text:
      index = alphabet.index(letter)
      new_index = index - shift
      txt += alphabet[new_index]
    print(f"The decoded text is {txt}")
    

caesar(text, shift, direction)
