import math

class TranspositionCipher:
    def encrypt_text(self, plain_text, key):
        plain_text = plain_text.replace(" ", "")
        num_cols = key  
        num_rows = math.ceil(len(plain_text) / num_cols)
        padded_text = plain_text.ljust(num_rows * num_cols, 'X')
        grid = [padded_text[i * num_cols:(i + 1) * num_cols] for i in range(num_rows)]
        
        cipher_text = ""
        for col in range(num_cols):
            for row in range(num_rows):
                cipher_text += grid[row][col]
        return cipher_text

    def decrypt_text(self, cipher_text, key):
        num_cols = key
        num_rows = len(cipher_text) // num_cols
        grid = [[''] * num_cols for _ in range(num_rows)]
        index = 0
        for col in range(num_cols):
            for row in range(num_rows):
                grid[row][col] = cipher_text[index]
                index += 1

        plain_text = "".join("".join(row) for row in grid)
        return plain_text.rstrip("X")