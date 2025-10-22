from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
keep_going = 'yes'

def caesar(operation, text, shift):
    output_text = ''
    index_shift = shift
    if operation == 'decode':
        index_shift = shift * -1

    for letter in text:
        if letter not in alphabet:
            output_text += letter
        else:
            letter_index = alphabet.index(letter) + index_shift
            letter_index %= len(alphabet)

            output_text += alphabet[letter_index]
    print(f'Here is the {operation}d result:', output_text)

print(logo)
while keep_going == 'yes':
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    input_text = input("Type your message:\n").lower()
    input_shift = int(input("Type the shift number:\n"))
    caesar(direction, input_text, input_shift)
    keep_going = input("Type 'yes' if you want to go again. Otherwise, type 'no'")

