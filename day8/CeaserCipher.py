import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(art.logo)


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for letter in start_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position + shift_amount) % 26
            end_text += alphabet[new_position]
        else:
            end_text += letter
    print(f"The {cipher_direction}d text is {end_text}")


retry = "y"
while retry == "y":
    direction = input(
        "Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if direction in {"encode", "decode"}:
        caesar(text, shift, direction)
    else:
        print("Only 'encode' and 'decode' allowed.")
    retry = input("Do you want to work on another cipher? Y / N\n").lower()
