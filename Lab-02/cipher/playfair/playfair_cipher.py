import string

class PlayfairCipher:
    def __init__(self):
        pass

    def generate_key_table(self, key):
        key = key.upper().replace("J", "I")
        table = ""
        for char in key:
            if char in string.ascii_uppercase and char not in table:
                table += char
        for char in string.ascii_uppercase:
            if char == 'J':  
                continue
            if char not in table:
                table += char
        matrix = [list(table[i*5:(i+1)*5]) for i in range(5)]
        return matrix

    def find_position(self, matrix, char):
        for i, row in enumerate(matrix):
            for j, val in enumerate(row):
                if val == char:
                    return i, j
        return None, None

    def preprocess_text(self, text, for_encryption=True):
        text = text.upper().replace("J", "I")
        text = ''.join(filter(str.isalpha, text))
        if for_encryption:
            i = 0
            result = ""
            while i < len(text):
                char1 = text[i]
                if i + 1 < len(text):
                    char2 = text[i+1]
                    if char1 == char2:
                        result += char1 + "X"
                        i += 1
                    else:
                        result += char1 + char2
                        i += 2
                else:
                    result += char1 + "X"
                    i += 1
            return result
        else:
            return text

    def encrypt_text(self, plain_text, key):
        matrix = self.generate_key_table(key)
        prepared_text = self.preprocess_text(plain_text, for_encryption=True)
        encrypted_text = ""
        for i in range(0, len(prepared_text), 2):
            a = prepared_text[i]
            b = prepared_text[i+1]
            row_a, col_a = self.find_position(matrix, a)
            row_b, col_b = self.find_position(matrix, b)
            if row_a == row_b:
                encrypted_text += matrix[row_a][(col_a + 1) % 5]
                encrypted_text += matrix[row_b][(col_b + 1) % 5]
            elif col_a == col_b:
                encrypted_text += matrix[(row_a + 1) % 5][col_a]
                encrypted_text += matrix[(row_b + 1) % 5][col_b]
            else:
                encrypted_text += matrix[row_a][col_b]
                encrypted_text += matrix[row_b][col_a]
        return encrypted_text

    def decrypt_text(self, cipher_text, key):
        matrix = self.generate_key_table(key)
        decrypted_text = ""
        for i in range(0, len(cipher_text), 2):
            a = cipher_text[i]
            b = cipher_text[i+1]
            row_a, col_a = self.find_position(matrix, a)
            row_b, col_b = self.find_position(matrix, b)
            if row_a == row_b:
                decrypted_text += matrix[row_a][(col_a - 1) % 5]
                decrypted_text += matrix[row_b][(col_b - 1) % 5]
            elif col_a == col_b:
                decrypted_text += matrix[(row_a - 1) % 5][col_a]
                decrypted_text += matrix[(row_b - 1) % 5][col_b]
            else:
                decrypted_text += matrix[row_a][col_b]
                decrypted_text += matrix[row_b][col_a]
        return decrypted_text
        