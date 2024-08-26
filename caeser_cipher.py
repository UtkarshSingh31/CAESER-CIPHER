#PROJECT:- CAESAR CIPHER PROJECT

#SHIFT THE CHARACTER BY 3RD SHIFT
# encode :- move the character by 3rd elements 
# decode:-  move back the character by 3rd elements

from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# create function ecrypt two i/p:- original_text ad shift_amount
# ex:- hello
def encrypt(original_text,shift_amount):
    # shift each letter by shift_amount
    cipher_text= " "
    
    # what happens if we try to shift letter z by any shift number
    # solution used modulo operator
    for letter in original_text:
        if letter not in alphabet:
            cipher_text +=letter 
        else :
            shifted_position=alphabet.index(letter)  + shift_amount 
            shifted_position %= len(alphabet) #0-25
            cipher_text += alphabet[shifted_position]
    print(f"Here is the encoded result: {cipher_text}")

def decrypt(original_text,shift_amount):
    cipher_text=" "
    for letter in original_text:
        shifted_position=alphabet.index(letter) - shift_amount
        shifted_position %= len(alphabet)
        cipher_text += alphabet[shifted_position]
    print(f"Here is the decoded result: {cipher_text}")
     
# COMBINE ENCRYPT AND DECRYPT IN ONE FUNCTION
def caesar(orginal_text,shift_amount,encode_or_decode):
    if encode_or_decode=="encode":
        encrypt(original_text=text,shift_amount=shift)
    else:
        decrypt(original_text=text,shift_amount=shift)
        # or
        #shift_amount *=-1
        
should_continue = True

while should_continue:
    direction=input("Type 'encode' to encrypt, type 'decode' to decrypt: \n").lower()
    text=input("Type your message:\n").lower()
    shift=int(input("Type the shift number:\n"))
    caesar(orginal_text=text, shift_amount=shift,encode_or_decode=direction)
    
    restart=input("Type yes if you want to go again. Otherwise Type no.\n ").lower()
    if restart== "no":
        should_continue=False
    else:
        should_continue=True