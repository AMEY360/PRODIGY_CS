def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            # Shift character within a-z or A-Z
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char  # Non-alphabetical characters remain unchanged
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)  # Reuse encryption by shifting in the opposite direction

def main():
    print("=== Caesar Cipher Encryption/Decryption ===")
    choice = input("Type 'e' to encrypt or 'd' to decrypt: ").lower()

    if choice not in ('e', 'd'):
        print("Invalid choice. Please select 'e' or 'd'.")
        return

    message = input("Enter your message: ")
    try:
        shift = int(input("Enter the shift value (integer): "))
    except ValueError:
        print("Invalid shift. Please enter a valid integer.")
        return

    if choice == 'e':
        encrypted = encrypt(message, shift)
        print(f"\n🔒 Encrypted Message: {encrypted}")
    else:
        decrypted = decrypt(message, shift)
        print(f"\n🔓 Decrypted Message: {decrypted}")

if __name__ == "__main__":
    main()
