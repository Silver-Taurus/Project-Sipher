#! /usr/bin/env python3

''' Python script containing Sub-Routines for different Ciphers '''

import abc
import math

class CipherSubRoutine(abc.ABC):
    ''' Class for supporting the main cipher class by providing the sub-routines needed'''

    def __init__(self, text, length):
        self.__text = text
        self.__length = length

    # Cipher Sub-Routines
    def _caesar_sub_routine(self, key):
        ''' Caesar Cipher sub-routine for crypting text '''
        # Adds the key to the character in the text
        return ''.join(list(map(lambda char: chr((ord(char) - ord('a') + key) % 26 + ord('a')) if char.isalpha() else char, self.__text)))

    def _transposition_sub_routine(self, key, mode):
        ''' Transposition Cipher sub-routine for crypting text '''
        if mode == 'encode':
            # Row-Wise reading and Col-Wise Filling of the text
            return ''.join([self.__text[j] for i in range(key) for j in range(i, self.__length, key)])
        else:
            # Col-Wise reading and Row-Wise Filling of the text
            cols = math.ceil(self.__length/key)
            return ''.join([self.__text[j] for i in range(cols) for j in range(i, self.__length, cols)])

    def _affine_sub_routine(self, key, mode):
        ''' Affine Cipher sub-routine for crypting text '''
        if mode == 'encode':
            # new_char = (a * char + b) % 26
            return ''.join(list(map(lambda char: chr((key[0] * (ord(char) - ord('a')) + key[1]) % 26 + ord('a')) if char.isalpha() else char, self.__text)))
            
        elif mode == 'decode':
            # new char = a^-1(char - b) % 26, where a^-1 is the modulus multiplicative inverse
            a_inv = 0
            for i in range(1, 26): 
                if ((key[0]*i) % 26) == 1 :
                    a_inv = i
                    break
            return ''.join(list(map(lambda char: chr((a_inv * (ord(char) - ord('a') - key[1])) % 26 + ord('a')) if char.isalpha() else char, self.__text)))
            
    def _vigenere_sub_routine(self, keys, mode):
        ''' Vigenere Cipher sub-routine for crypting text '''
        if mode == 'encode':
            # new_char[i] = (char[i] + keys[i]) % 26
            return ''.join(list(map(lambda char, key: chr((ord(char) + ord(key) - 2 * ord('a')) % 26 + ord('a')) if char.isalpha() else char , self.__text, keys)))
        else:
            # new_char[i] = (char[i] - keys[i] + 26) % 26
            return ''.join(list(map(lambda char, key: chr((ord(char) - ord(key) + 26) % 26 + ord('a')) if char.isalpha() else char, self.__text, keys)))
