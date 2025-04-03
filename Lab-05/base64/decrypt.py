import base64 

def main(): 
    try:
        with open("data.txt", "r") as file:  # Reading the encoded string from file
            encoded_string = file.read().strip()  # Remove any surrounding whitespace/newlines
        
        decoded_bytes = base64.b64decode(encoded_string)  # Decoding the string back to bytes
        decoded_string = decoded_bytes.decode("utf-8")  # Decoding bytes to string
        
        print("Chuỗi sau khi giải mã:", decoded_string)  # Display decoded string
    except Exception as e:  # Handle any exceptions during the process
        print("Lỗi:", e)

if __name__ == "__main__":  # Check if the script is being executed directly
    main()
