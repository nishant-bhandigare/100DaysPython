# Caesar Cipher Encrypter

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text, shift):
    cipher_text = ""
    for i in range(0, len(plain_text)):
        pos = alphabet.index(plain_text[i])
        new_pos = pos + shift
        if new_pos > len(alphabet):
            new_pos-=len(alphabet)
        cipher_text+=alphabet[new_pos]

    print(f"The encoded text is {cipher_text}")

def decrypt(cipher_text, shift):
    plain_text = ""
    for i in range(0, len(cipher_text)):
        pos = alphabet.index(cipher_text[i])
        new_pos = pos - shift
        if new_pos < 0:
            new_pos+=len(alphabet)
        plain_text+=alphabet[new_pos]

    print(f"The decoded text is {plain_text}")

def caesar(text, shift, direction):
    if direction == "encode":
        encrypt(plain_text=text, shift=shift)
    elif direction == "decode":
        decrypt(cipher_text=text, shift=shift)


caesar(text=text, shift=shift, direction=direction)