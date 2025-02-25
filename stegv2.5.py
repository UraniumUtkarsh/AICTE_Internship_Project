import cv2
import numpy as np

def encrypt_message(image_path, message, password, output_path="encryptedImage.png"):
    img = cv2.imread(image_path)
    if img is None:
        print(f"Error: Unable to load image. Check the path: {image_path}")
        return
    
    height, width, _ = img.shape
    max_bytes = height * width * 3

    message += "::" + password + "::END"  # Unique end marker
    encoded_data = message.encode('utf-8')  # Convert to bytes

    if len(encoded_data) > max_bytes:
        print(f"Error: Message too large! Max bytes: {max_bytes}, Message length: {len(encoded_data)}")
        return
    
    flat_image = img.flatten()  # Flatten to 1D array
    for i, byte in enumerate(encoded_data):
        flat_image[i] = byte  # Store ASCII values
    
    img = flat_image.reshape(img.shape)  # Reshape back to original
    
    cv2.imwrite(output_path, img)
    print("Message encrypted successfully!")

def decrypt_message(image_path, password):
    img = cv2.imread(image_path)
    if img is None:
        print(f"Error: Unable to load image. Check the path: {image_path}")
        return
    
    flat_image = img.flatten()
    message_bytes = []

    for byte in flat_image:
        if byte == 0:  # Stop if a null byte is encountered (rare, but a safeguard)
            break
        message_bytes.append(byte)
        
        if len(message_bytes) >= 5 and b"::END" in bytes(message_bytes[-5:]):  # Detect end marker
            break

    message = bytes(message_bytes).decode('utf-8', errors='ignore')
    
    if f"::{password}::END" in message:
        message = message.replace(f"::{password}::END", "")
        print("Decrypted message:", message)
    else:
        print("Error: Incorrect password or corrupted data.")

if __name__ == "__main__":
    choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").strip().lower()
    image_path = input("Enter image path: ")
    
    if choice == "e":
        message = input("Enter secret message: ")
        password = input("Enter a passcode: ")
        encrypt_message(image_path, message, password)
    elif choice == "d":
        password = input("Enter passcode for decryption: ")
        decrypt_message(image_path, password)
    else:
        print("Invalid choice.")
