# CAESER-CIPHER
Caesar cipher shift is the number of positions by which each letter in a text is shifted to encrypt or decrypt it. For example, a shift of 3 would mean that each letter is replaced by the letter three positions ahead in the alphabet. So, "a" would become "d," "b" would become "e," and so on.

Key Features

Encryption: Encrypts a given text by shifting each letter by the specified shift amount.
Decryption: Decrypts an encrypted text by shifting each letter back by the same amount.
User-friendly interface: Prompts the user to choose between encryption and decryption, enter the text, and specify the shift amount.
Continuous usage: Allows the user to perform multiple encryption/decryption operations until they choose to quit.


How it Works:- 

Import necessary modules: Imports the art module to display a logo.
Define the alphabet: Creates a list containing all the letters of the alphabet.
Define the encrypt function:
Takes the original text and shift amount as input.
Shifts each letter in the text by the specified amount, wrapping around to the beginning of the alphabet if necessary.
Returns the encrypted text.
Define the decrypt function:
Calls the encrypt function with the same original text and a negative shift amount to decrypt.
Define the caesar function:
Takes the original text, shift amount, and encode/decode option as input.
Calls the appropriate encrypt or decrypt function based on the option.

Main loop:
Continuously prompts the user for input until they choose to quit.
Calls the caesar function with the user's input.
Prints the encrypted or decrypted result.
Asks the user if they want to continue.
Usage

Run the script.
Choose whether to encrypt or decrypt.
Enter the text you want to process.
Specify the shift amount.
The encrypted or decrypted text will be displayed.
You can continue using the game or quit by typing "no" when prompted.
This project demonstrates the use of functions, parameters, string manipulation, and user input in Python. It provides a basic implementation of the Caesar Cipher algorithm, which can be further enhanced with additional features or made more secure by using a stronger encryption method.
