import sys
from PIL import Image

# Function to encode a message into an image
def encode_image(image_path, message):
    # Open the image
    img = Image.open(image_path)
    width, height = img.size
    pixel_index = 0
    # Convert the message into binary format
    binary_message = ''.join(format(ord(char), '08b') for char in message)
    binary_message += '1111111111111110'  # Message delimiter (to mark the end of the message)

    data_index = 0  
    for row in range(height):
        for col in range(width):
            # Get the pixel values (R, G, B)
            pixel = list(img.getpixel((col, row)))
            for color_channel in range(3):  # We only modify the first three channels (RGB)
                if data_index < len(binary_message):
                    # Modify the least significant bit of the color channel
                    pixel[color_channel] = int(format(pixel[color_channel], '08b')[:-1] + binary_message[data_index], 2)
                    data_index += 1
                if data_index >= len(binary_message):
                    break
            img.putpixel((col, row), tuple(pixel))
            if data_index >= len(binary_message):
                break
        if data_index >= len(binary_message):
            break

    # Save the encoded image
    encoded_image_path = 'encoded_image.png'
    img.save(encoded_image_path)
    print("Steganography complete. Encoded image saved as", encoded_image_path)
    
# Main function to handle command-line arguments
def main():
    if len(sys.argv) != 3:
        print("Usage: python encrypt.py <image_path> <message>")
        return
    image_path = sys.argv[1]
    message = sys.argv[2]
    encode_image(image_path, message)

if __name__ == "__main__":
    main()
