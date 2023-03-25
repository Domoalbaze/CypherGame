


def caesar(message, shift):
    ciphertext = ""

    for char in message:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted_char = chr(((ord(char) - base + shift) % 26) + base)
            ciphertext += shifted_char
        else:
            ciphertext += char

    return ciphertext


# Example usage:
plaintext = "abd ABC def 123 !,?"
shift = 3
encrypted = caesar(plaintext, shift)
print(encrypted)  