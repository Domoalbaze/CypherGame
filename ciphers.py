
def rot_13(message):
    result = ""
    for char in message:
        if char.isalpha():
            char_code = ord(char)
            if char.islower():
                new_char_code = ((char_code - ord('a') + 13) % 26) + ord('a')
            else:
                new_char_code = ((char_code - ord('A') + 13) % 26) + ord('A') 
            result += chr(new_char_code)
        else:
            result += char
    return result
   

def cesar_cipher_encrypt(plaintext):
    result = ''
    plaintext = plaintext.upper()
    for char in plaintext:
        if char.isalpha(): #Only shift letter, preserve any other chatacter
            shiftedindex = chr(((ord(char) - 65 + 3) % 26) + 65)
            result += shiftedindex
        else: 
            result += char
    return result
         


def columnar_transposition_encrypt(plaintext):
    key = 8
    ciphertext = [''] * key 
    for col in range(key):
        pointer = col
        while pointer < len(plaintext):
            ciphertext[col] += plaintext[pointer] 
            pointer += key
    return ''.join(ciphertext)



def affine_cipher(plain):  # e(x) = (ax+b) mod m [a,b = key]
    k1, k2, k3 = (7, 8, 26)
    ciphertext = ''
    plain = plain.lower()
    for char in plain:
        if char.isalpha():
            shiftedIndex = (k1 * (ord(char) - 97) + k2) % k3
            encrypted_char = chr(shiftedIndex + 97)
            ciphertext += encrypted_char
        else:
            ciphertext += char

    return ciphertext

def atbash(plaintext):
    plaintext = plaintext.upper()
    letterdict = {'A' : 'Z', 'B' : 'Y', 'C' : 'X', 'D' : 'W', 'E' : 'V',
        'F' : 'U', 'G' : 'T', 'H' : 'S', 'I' : 'R', 'J' : 'Q',
        'K' : 'P', 'L' : 'O', 'M' : 'N', 'N' : 'M', 'O' : 'L',
        'P' : 'K', 'Q' : 'J', 'R' : 'I', 'S' : 'H', 'T' : 'G',
        'U' : 'F', 'V' : 'E', 'W' : 'D', 'X' : 'C', 'Y' : 'B', 'Z' : 'A'}
    ciphertext = ''
    for letter in plaintext:
        if letter.isalpha():
            if letter in letterdict:
                ciphertext += letterdict[letter]
        else:
            ciphertext += letter
    return ciphertext


def reverse_string(plaintext):
    reversed_string = plaintext[::-1]
    return reversed_string




def vigenere_square(plaintext):
    key = 'SECRET'
    while len(plaintext) > len(key):
        key += key
    key = key[:len(plaintext)]
    ciphertext = []
    for p, k in zip(plaintext, key):
        if p.isalpha():
            shift = ord(k.upper()) - ord('A')
            if p.isupper():
                new_char = chr(((ord(p) - ord('A') + shift) % 26) + ord('A'))
            else:
                new_char = chr(((ord(p) - ord('a') + shift) % 26) + ord('a'))
        else:
            new_char = p

        ciphertext.append(new_char)

    return "".join(ciphertext)