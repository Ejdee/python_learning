import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo.logo)

restart = True
while restart:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    def caesar (text, shift, alphabet, direction):
        end_text = ""
        while shift > 26:
            shift -= 26
        for i in text:
            if i not in alphabet:
                end_text += i
            else:
                if direction == "decode":
                    position = alphabet.index(i, 25)
                    new_position = position - shift
                else:
                    position = alphabet.index(i)
                    new_position = position + shift
                end_text += alphabet[new_position]
        print(f"The {direction}d message is {end_text}.")

    caesar(text, shift, alphabet, direction)

    user_try = input("Do you want to try one more? / 'y' for yes / 'n' for no: \n")

    if user_try == "n":
        restart = False