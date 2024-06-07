import subprocess
from PIL import Image

print("WELCOME TO IMAGE PIXEL MANIPULATION AND ENCRYPTION")

def encrypt_image(image_path, secret_key):
    # Open image
    image = Image.open(image_path)
    width, height = image.size

    # Convert key to bytes
    key_bytes = secret_key.encode()

    # Load pixel data
    pixels = image.load()

    # Loop through each pixel in the image
    for y in range(height):
        for x in range(width):
            red, green, blue = pixels[x, y]

            red ^= key_bytes[0]
            green ^= key_bytes[1]
            blue ^= key_bytes[2]

            pixels[x, y] = (red, green, blue)

    encrypted_image_path = image_path.split('.')[0] + '_encrypted.png'
    image.save(encrypted_image_path)
    print("🔒 Image encrypted successfully and saved as:", encrypted_image_path)
    open_file(encrypted_image_path)

    return encrypted_image_path


def decrypt_image(encrypted_image_path, secret_key):
    # Open encrypted image
    image = Image.open(encrypted_image_path)
    width, height = image.size

    # Convert secret key to bytes
    key_bytes = secret_key.encode()

    # Load pixel data
    pixels = image.load()

    for y in range(height):
        for x in range(width):
            red, green, blue = pixels[x, y]

            red ^= key_bytes[0]
            green ^= key_bytes[1]
            blue ^= key_bytes[2]

            pixels[x, y] = (red, green, blue)

    # Save the decrypted image
    decrypted_image_path = encrypted_image_path.split('_encrypted')[0] + '_decrypted.png'
    image.save(decrypted_image_path)
    print("🔓 Image decrypted successfully and saved as:", decrypted_image_path)
    open_file(decrypted_image_path)


def open_file(file_path):
    subprocess.run(['start', '', file_path], shell=True) 

image_path = input("ENTER THE IMAGE FILE PATH: ")
secret_key = input("ENTER THE SECRET KEY: ")

# Encrypt the image
encrypted_image_path = encrypt_image(image_path, secret_key)

# Decrypt the image
decrypt_image(encrypted_image_path, secret_key)
