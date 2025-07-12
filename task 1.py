def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

# Input from user
message = input("Enter your message: ")
shift = int(input("Enter shift value: "))

# Encrypt
encrypted = encrypt(message, shift)
print("🔐 Encrypted message:", encrypted)

# Decrypt
decrypted = decrypt(encrypted, shift)
print("🔓 Decrypted message:", decrypted)
