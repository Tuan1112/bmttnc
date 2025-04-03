import sys
from PIL import Image

# Function to decode the hidden message from an image
def decode_image(encoded_image_path):
    img = Image.open(encoded_image_path)  # Open the encoded image
    width, height = img.size  # Get the size of the image
    binary_message = ""  # Initialize the binary message string

    # Iterate through each pixel
    for row in range(height):
        for col in range(width):
            pixel = img.getpixel((col, row))  # Get the pixel value (R, G, B)
            for color_channel in range(3):  # Loop through the RGB channels
                binary_message += format(pixel[color_channel], '08b')[-1]  # Extract the LSB of each color channel

    # Convert the binary message to characters
    message = ""
    for i in range(0, len(binary_message), 8):
        char = chr(int(binary_message[i:i+8], 2))  # Convert 8 bits to a character
        if char == '\0':  # End of message delimiter (null character)
            break
        message += char  # Append the character to the message

    return message

# Main function to handle command-line arguments
def main():
    if len(sys.argv) != 2:
        print("Usage: python decrypt.py <encoded_image_path>")
        return

    encoded_image_path = sys.argv[1]  # Get the encoded image path from command line arguments
    decoded_message = decode_image(encoded_image_path)  # Decode the hidden message
    print("Decoded message:", decoded_message)  # Print the decoded message

if __name__ == "__main__":
    main()
