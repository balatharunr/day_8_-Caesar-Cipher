alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(original_text, shift_amount):
    cipher_text = ""
    for letter in original_text:
        if letter in alphabet:
            shifted_position = (alphabet.index(letter) + shift_amount) % 26
            cipher_text += alphabet[shifted_position]
        else:
            cipher_text += letter
    print(f"Here is the encoded result: {cipher_text}")
def decrypt(original_text, shift_amount):
    output_text = ""
    for letter in original_text:
        if letter in alphabet:
            shifted_position = (alphabet.index(letter)-shift_amount) % 26
            output_text += alphabet[shifted_position]
        else:
            output_text += letter
    print(f"Here is the decoded result: {output_text}")

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

if direction == "encode":
    encrypt(original_text=text, shift_amount=shift)
elif direction == "decode":
    decrypt(original_text=text,shift_amount=shift)
else:
    print("Invalid Input")
