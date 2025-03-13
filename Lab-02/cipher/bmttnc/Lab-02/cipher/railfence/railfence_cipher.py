class RailfenceCipher:
    def __init__(self):
        pass


    def encrypt_text(self, plain_text, key):
        if key <= 1:
            return plain_text
        rails = ['' for _ in range(key)]
        rail = 0
        direction = 1
        for char in plain_text:
            rails[rail] += char
            rail += direction
            if rail == 0 or rail == key - 1:
                direction *= -1
        return ''.join(rails)

    def decrypt_text(self, cipher_text, key):
        if key <= 1:
            return cipher_text

        pattern = [0] * len(cipher_text)
        rail = 0
        direction = 1
        for i in range(len(cipher_text)):
            pattern[i] = rail
            rail += direction
            if rail == 0 or rail == key - 1:
                direction *= -1

        rail_counts = [pattern.count(r) for r in range(key)]
        rails = {}
        index = 0
        for r in range(key):
            rails[r] = list(cipher_text[index: index + rail_counts[r]])
            index += rail_counts[r]

        result = []
        rail_index = 0
        direction = 1
        for i in range(len(cipher_text)):
            result.append(rails[pattern[i]].pop(0))
        return ''.join(result)
        