import art


print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""

    if encode_or_decode == "d" :
        encode_or_decode = "decode"
    else:
        encode_or_decode = "encode"

    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in original_text:

        if letter not in alphabet:
            output_text += letter
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {output_text}")


should_continue = True

while should_continue:
    while True :
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        if direction in ["encode","e","decode","d"]:
            break
        else:
            print("Invalid input. use 'encode' or 'decode' you can also use 'e' or 'n':\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    while True:
        restart = input("Type 'y' if you want to go again. Otherwise, type 'n'.\n").lower()
        if restart == "n":
            should_continue = False
            print("Goodbye!")
            break
        if restart == "y":
            print("Restarting...")
            break
        else :
            print("Invalid input. Please type 'y' or 'n'.\n")
