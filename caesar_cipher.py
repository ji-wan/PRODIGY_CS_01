letters = 'abcdefghijklmnopqrstuvwxyz'
num_letters = len(letters)

def caesar_cipher(text, mode, key):
    result = ''
    
    if mode == 'decrypt':
        key = -key  # reverse the key for decryption
    
    for letter in text:
        letter = letter.lower()
        if not letter == ' ':
            index = letters.find(letter)
            if index == -1:
                result += letter  # if the letter is not in the alphabet, add it to the result as is
            else:
                new_index = index + key
                if new_index >= num_letters:
                    new_index -= num_letters
                elif new_index < 0:
                    new_index += num_letters
                
                result += letters[new_index]
    return result    

print()
print('*** caesar cipher program ***')
print()

print('do you want to encrypt or decrypt?')
user_input = input('encrypt/decrypt: ').lower()
print()

if user_input == 'encrypt':
    print('enter the text you want to encrypt: ')
    print()
    key = int(input('enter the key (1 through 26): '))
    text = input('enter the text to encrypt: ')
    ciphertext = caesar_cipher(text, user_input, key)
    print('encrypted text: ', ciphertext)
    
elif user_input == 'decrypt':
    print('enter the text you want to decrypt: ')
    print()
    key = int(input('enter the key (1 through 26): '))
    text = input('enter the text to decrypt: ')
    plaintext = caesar_cipher(text, user_input, key)
    print('decrypted text: ', plaintext)