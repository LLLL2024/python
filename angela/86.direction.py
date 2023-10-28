alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def casear(start_test,shift_amount,cirper_diretion):
    end_text = " "
    if direction == "decode":
        shift_amount *= -1
    for letter in start_test:
        position = alphabet.index(letter)
        new_posioton = position + shift_amount
        end_text += alphabet[new_posioton]
    print(end_text)

casear(start_test = text, shift_amount = shift, cirper_diretion = direction)