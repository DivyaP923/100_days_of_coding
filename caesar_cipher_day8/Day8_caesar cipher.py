import Day10.art as art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(art.logo)

def caesar(original_text,shift_number,encode_or_decode):
    
    if encode_or_decode == 'decode':
        shift_number *= -1
    shifted_index = 0
    output_text=''
    for letter in original_text:
        if letter in alphabet:
            shifted_index = int(alphabet.index(letter)) + shift_number
            #to shift letters with greater index value example to shift Z with index 10 or something below expression is used
            # if we do 35%25 it will give us the reminder 10
            shifted_index %= len(alphabet)
            output_text += alphabet[shifted_index]
        else:
            output_text += letter
    print(f"Here is the {encode_or_decode}d result: {output_text}")

# Run the cipher program in a loop
run_request = True
while run_request:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text, shift, direction)

    # Ask user if they want to continue
    run_again = input("Type 'yes' if you want to go again, otherwise type 'no':\n").lower()
    if run_again == 'no':
        run_request = False


