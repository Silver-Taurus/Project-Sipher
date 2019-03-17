#! /usr/bin/env python3

''' Python script containing Sub-Routines for different Ciphers '''

from abc import ABC
import math
from random import choice
import string
from collections import OrderedDict

class CipherSubRoutine(ABC):
    ''' Class for supporting the main cipher class by providing the sub-routines needed'''

    exceptions = {
    '__primary_cipher_routine': 'Invalid Choice', \
    '__caesar_cipher': 'Key cannot be < 1 or a multiple of 26', \
    '__transposition_cipher': 'Key cannot be < 2 or >= the length of entered text', \
    '__affine_cipher': 'Entered value is invalid', \
    '__vigenere_cipher': 'Key should contain alphabets only and length of key should be <= length of text', \
    '__otp_cipher': 'Key should contain alphabets only and length of key should be = length of text', \
    }

    def __init__(self, text, length):
        self.__text = text
        self.__length = length

    #------------------------------ Cipher Sub-Routines --------------------------------------------------
    def _caesar_sub_routine(self, key):
        ''' Caesar Cipher sub-routine for crypting text '''
        # Adds the key to the character in the text
        return ''.join(list(map(lambda char: chr((ord(char) - ord('a') + key) % 26 + ord('a')) \
            if char.isalpha() else char, self._text)))

    def _transposition_sub_routine(self, key, mode):
        ''' Transposition Cipher sub-routine for crypting text '''
        if mode == 'encode':
            # Row-Wise reading and Col-Wise Filling of the text
            return ''.join([self.__text[j] for i in range(key) for j in range(i, self.__length, key)])
        else:
            # Col-Wise reading and Row-Wise Filling of the text
            cols = math.ceil(self.__length/key)
            shaded_boxes = cols*key - self.__length
            output = ['']*cols
            col = row = 0
            for symbol in self.__text:
                output[col] += symbol
                col += 1
                if (col == cols) or (col == cols-1 and row >= key - shaded_boxes):
                    col,row = 0,row+1
            return ''.join(output)

    def _affine_sub_routine(self, key, mode):
        ''' Affine Cipher sub-routine for crypting text '''
        if mode == 'encode':
            # new_char = (a * char + b) % 26
            return ''.join(list(map(lambda char: chr((key[0] * (ord(char) - ord('a')) + key[1]) % 26 + ord('a')) \
                if char.isalpha() else char, self.__text)))

        elif mode == 'decode':
            # new char = a^-1(char - b) % 26, where a^-1 is the modulus multiplicative inverse
            a_inv = 0
            for i in range(1, 26):
                if ((key[0]*i) % 26) == 1 :
                    a_inv = i
                    break
            return ''.join(list(map(lambda char: chr((a_inv * (ord(char) - ord('a') - key[1])) % 26 + ord('a')) \
                if char.isalpha() else char, self.__text)))

    def _vigenere_otp_sub_routine(self, keys, mode):
        ''' Vigenere Cipher sub-routine for crypting text '''
        if mode == 'encode':
            # new_char[i] = (char[i] + keys[i]) % 26
            return ''.join(list(map(lambda char, key: chr((ord(char) + ord(key) - 2 * ord('a')) % 26 + ord('a')) \
                if char.isalpha() else char , self.__text, keys)))
        else:
            # new_char[i] = (char[i] - keys[i] + 26) % 26
            return ''.join(list(map(lambda char, key: chr((ord(char) - ord(key) + 26) % 26 + ord('a')) \
                if char.isalpha() else char, self.__text, keys)))

    def _rsa_sub_routine(self, x, n, mode) :
        ''' Rsa Cipher Sub-Routine for crypting text '''
        if mode == 'encode':
            output_string = ''
            for _ in self.__text :
                output_string.append(ord(_) - ord(a) + 1)
            print ('Output string is : {} '.format(output_string))
            encrypted_data = pow(int(output_string), x) % n
            return string(encrypted_data)

        else:
            encrypted_data = int(self.__text)
            decrypted_data = string(pow(encrypted_data, x) % n)
            output_string = ''
            for _ in decrypted_data :
                output_string.append(chr(int(_) + ord('a') - 1))
            return output_string

def single_cipher_dispatch(default_fn):
    ''' Decorator for dispatching the cipher function corresponding to the cipher name injected '''
    registry = OrderedDict()
    registry['Default'] = default_fn

    def decorated_function(cipher):
        ''' cipher_func is decorated to give the desired function back '''
        return registry.get(cipher, registry['Default'])
    
    def register(cipher):
        ''' Decorator factory (or Parameterized Decorator) that will be a property of our decorated function,
            in order to register any new cipher method made '''
        def register_decorator(cipher_func):
            ''' Register Decorator which adds the injected cipher to the registry and do not modify the cipher_func '''
            registry[cipher] = cipher_func
            return cipher_func
        return register_decorator

    
    decorated_function.register = register
    decorated_function.registry = registry
    return decorated_function
