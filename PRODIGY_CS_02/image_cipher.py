from PIL import Image
import os

def encrypt_image(input_path, output_path, key):
    try:
        img = Image.open(input_path)
        encrypted = Image.new(img.mode, img.size)
        pixels = img.load()
        enc_pixels = encrypted.load()

        for i in range(img.size[0]):
            for j in range(img.size[1]):
                r, g, b = pixels[i, j]
                # Apply key-based encryption (modulo 256 to keep in byte range)
                enc_pixels[i, j] = ((r + key) % 256, (g + key) % 256, (b + key) % 256)

        encrypted.save(output_path)
        print(f"✅ Encrypted image saved as {output_path}")
    except Exception as e:
        print(f"❌ Error encrypting image: {e}")

def decrypt_image(input_path, output_path, key):
    try:
        img = Image.open(input_path)
        decrypted = Image.new(img.mode, img.size)
        pixels = img.load()
        dec_pixels = decrypted.load()

        for i in range(img.size[0]):
            for j in range(img.size[1]):
                r, g, b = pixels[i, j]
                # Reverse the encryption
                dec_pixels[i, j] = ((r - key) % 256, (g - key) % 256, (b - key) % 256)

        decrypted.save(output_path)
        print(f"✅ Decrypted image saved as {output_path}")
    except Exception as e:
        print(f"❌ Error decrypting image: {e}")

def main():
    print("=== Image Encryption/Decryption Tool ===")
    choice = input("Choose operation - (e)ncrypt or (d)ecrypt: ").lower()

    if choice not in ['e', 'd']:
        print("Invalid choice! Please select 'e' or 'd'.")
        return

    input_path = input("Enter the path to the image file: ")
    key = int(input("Enter a numeric key (e.g., 10): "))

    if not os.path.exists(input_path):
        print("File not found.")
        return

    if choice == 'e':
        output_path = "encrypted_image.png"
        encrypt_image(input_path, output_path, key)
    else:
        output_path = "decrypted_image.png"
        decrypt_image(input_path, output_path, key)

if __name__ == "__main__":
    main()
