def caesar_cipher(text, shift):
    result = ""
    
    for char in text:
        if char.isalpha():

            is_upper = char.isupper()
            

            char_code = ord(char)
            

            char_code = (char_code - ord('A' if is_upper else 'a') + shift) % 26
            

            char = chr(char_code + ord('A' if is_upper else 'a'))
        
        result += char
    
    return result


text = "python codeert tekst met, python codeert met weer"
shift = 10


encoded_text = caesar_cipher(text, shift)

print("Original text:   ", text)
print("Encoded text:    ", encoded_text)

