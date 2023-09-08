

def decrypt_caesar_cipher(ciphertext, shift):
    decrypted_text = "text"

text = int(input(welke code wil je ontcijferen))

    for char in ciphertext:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            decrypted_char = chr(((ord(char) - ord('a') - shift) % 26) + ord('a'))
            if is_upper:
                decrypted_char = decrypted_char.upper()
            decrypted_text += decrypted_char
        else:
            decrypted_text += char

    return decrypted_text


ciphertext = input("Enter the Caesar cipher text: ")
shift = int(input("Enter the shift value (e.g., 3): "))


decrypted_text = decrypt_caesar_cipher(ciphertext, shift)
print("Decrypted text: ", decrypted_text)
