#! /usr/bin/env python3

''' Project Sipher '''

import math
import string
import random
from Crypto.Util.number import isPrime
from cipher_sub_routines import CipherSubRoutine

class Cipher(CipherSubRoutine):
    ''' Class for performing the cipher methods on a given text '''

    # Cipher Constructor for taking input of text and passing it to CipherSubRoutine Constructor.
    def __init__(self):
        self.__ciphers = {
            'Reverse Cipher': self.__reverse_cipher, \
            'Caesar Cipher': self.__caesar_cipher, \
            'Transposition Cipher': self.__transposition_cipher, \
            'Affine Cipher': self.__affine_cipher, \
            'Vigenere Cipher': self.__vigenere_cipher, \
            'One Time Pad Cipher': self.__otp_cipher, \
            'RSA Cipher': self.__rsa_cipher
            }
        self.__text = input('\nEnter the text: ').lower()
        self.__length = len(self.__text)

    #---------------------------- Primary Cipher Routines --------------------------------------
    def __reverse_cipher(self):
        ''' Cipher Routine to encode into or decode from Reverse Cipher '''
        return self.__text[::-1]

    @CipherSubRoutine.safe_run
    def __caesar_cipher(self, mode):
        ''' Cipher Routine to encode into or decode from Caesar Cipher '''
        key = int(input('(integer >0 and not a multiple of 26)\nEnter the key: '))
        if key < 1 or key%26 == 0:
            raise KeyError
        if mode == 'encode':
            return self._caesar_sub_routine(key)
        else:
            return self._caesar_sub_routine(26-key)

    @CipherSubRoutine.safe_run
    def __transposition_cipher(self, mode):
        ''' Cipher Routine to encode into or decode form Transposition Cipher '''
        key = int(input('(integer >2 and < {})\nEnter the key: '.format(self.__length)))
        if (key < 2) or (key >= self.__length):
            raise KeyError
        return self._transposition_sub_routine(key, mode)

    @CipherSubRoutine.safe_run
    def __affine_cipher(self, mode):
        ''' Cipher Routine to encode into or decode from Affine Cipher '''
        key_a = key_b = 0

        if mode == 'encode':
            while True:
                choice = input("Enter key Automatically/Manually [A/m]: ")

                if choice == 'A' or choice == 'a' or choice == '':
                    while True:
                        key_a = random.randint(1, 10**5)
                        if math.gcd(key_a, 26) == 1 :
                            break
                    key_b = random.randint(1, 10**5)
                    break

                elif choice == 'm' or choice == 'M':
                    n = int(input('Range 1 to n from which a valid key is choosen\nEnter n'
                        '(should be greater than 1): '))
                    if n < 2:
                        raise KeyError
                    keys_a = []
                    for i in range(1, n):
                        if math.gcd(i,26) == 1 :
                            print(i, end = ' ')
                            keys_a.append(i)
                    key_a = int(input('\nEnter key-a: '))
                    if key_a not in keys_a:
                        raise KeyError
                    key_b = int(input('Enter key-b: '))
                    if key_b < 0:
                        raise KeyError
                    break

                else:
                    print('Invalid Choice!!!')

            print('\nkey-a = {}\nkey-b = {}'.format(key_a, key_b))

        else:
            key_a = int(input('\n(integer >1 and should be co-prime with 26)\nEnter the key-a: '))
            if key_a < 2 or math.gcd(key_a, 26) != 1:
                raise KeyError
            key_b = int(input('(positive integer)\nEnter the key-b: '))
            if key_b < 0:
                raise KeyError

        return self._affine_sub_routine((key_a, key_b), mode)

    @CipherSubRoutine.safe_run
    def __vigenere_cipher(self, mode):
        ''' Cipher Routine to encode into or decode from Vigenere Cipher '''
        key = input('(alphabets only and length of key should be >0 and < {})\nEnter the key: '.format(self.__length))
        if any(char.isdigit() for char in key) or len(key) > self.__length:
            raise KeyError
        key = list(key)
        if self.__length != len(key):
            for i in range(self.__length - len(key)):
                key.append(key[i % len(key)])
        return self._vigenere_otp_sub_routine(key, mode)

    @CipherSubRoutine.safe_run
    def __otp_cipher(self, mode):
        ''' Cipher Routine to encode into or decode from One Time Pad Cipher '''
        if mode == 'encode':
            while True:
                choice = input('Enter key Automatically/Manually [A/m]: ')
                if choice in ('A', 'a', ''):
                    key = ''.join(random.choice(string.ascii_letters).lower() for _ in self.__text)
                    print('Encryption key is:', key)
                    break
                elif choice in ('M', 'm'):
                    key = input('\n(alphabets only and length of key should be = {})\nEnter the key: '.format(self.__length))
                    if len(key) != self.__length or any(not ch.isalpha() for ch in key):
                        raise KeyError
                    break
                else:
                    print('Invalid Choice!!!')
        else:
            key = input('(alphabets only and length of key should be = {})\nEnter the key: '.format(self.__length))
            if len(key) != self.__length or any(not ch.isalpha() for ch in key):
                raise KeyError
        return self._vigenere_otp_sub_routine(key, mode)

    def __rsa_cipher(self, mode):
        ''' Cipher Routine to encode into or decode from RSA Cipher '''
        if mode == 'encode':
            while True:
                choice = input('Enter key Automatically [A/m]: ')
                if choice in ('A', 'a', ''):
                   primes = [i for i in range(1000, 100000) if isPrime(i)]
                   p = random.choice(primes)
                   primes.remove(p)
                   q = random.choice(primes)
                   print('P = {} and Q = {}'.format(p, q))
                   break

                elif choice in ('M', 'm'):
                   #print("Enter range min and max :")
                   range_min, range_max = int(input("Enter min range :")), int(input("Enter max range :"))
                   primes = [i for i in range(range_min, range_max) if isPrime(i)]
                   print(primes)
                   p,q = int(input("Enter p:")), int(input("Enter q:"))
                   print(p, q)


    @CipherSubRoutine.safe_run
    def __primary_cipher_routine(self, mode):
        ''' primary cipher routine for applying the cipher algorithm with the defined mode leagally '''
        cipher_keys = {}
        print('\n\nCipher list:')
        for num, func_name in enumerate(self.__ciphers.keys(), 1):
            print('{}. {}'.format(num, func_name))
            cipher_keys[num] = func_name

        choice = int(input('\nEnter Your Choice: '))
        print('\nThe {}d string is:'.format(mode), self.__ciphers[cipher_keys[choice]]() \
            if choice == 1 else self.__ciphers[cipher_keys[choice]](mode))

    def encode(self):
        ''' Encode-Routine for Encoding the plaintext into ciphertext '''
        self.__primary_cipher_routine('encode')

    def decode(self):
        ''' Decode-Routine for Decoding the ciphertext into plaintext '''
        self.__primary_cipher_routine('decode')

    def hack(self):
        ''' Hack-Routine for Hacking the ciphertext without key(s) into plaintext '''
        pass


def main():
    ''' Main Driver Program '''

    print('''
     _/_/_/                        _/                        _/
   _/    _/  _/  _/_/    _/_/          _/_/      _/_/_/  _/_/_/_/
  _/_/_/    _/_/      _/    _/  _/  _/_/_/_/  _/          _/
 _/        _/        _/    _/  _/  _/        _/          _/
_/        _/          _/_/    _/    _/_/_/    _/_/_/      _/_/
                             _/
                          _/
              _/_/_/  _/            _/
            _/            _/_/_/    _/_/_/      _/_/    _/  _/_/
            _/_/    _/  _/    _/  _/    _/  _/_/_/_/  _/_/
               _/  _/  _/    _/  _/    _/  _/        _/
        _/_/_/    _/  _/_/_/    _/    _/    _/_/_/  _/
                     _/
                    _/
    ''' )

    options = ['1', '2', '3', '4']
    while(True):
        try:
            choice = input('''\n\nMain Menu:
                1. Encode into ciphertext
                2. Decode into plaintext
                3. Hack the ciphertext
                4. Exit
                \nEnter Your Choice: ''')

            if choice not in options:
                print('Please enter a valid choice!')
                continue
            elif choice == '4':
                exit()

            print('\n(Press `Ctrl+C` to return to Main Menu)')

            cipher = Cipher()
            if choice == '1':
                cipher.encode()
            elif choice == '2':
                cipher.decode()
            else:
                cipher.hack()

        except KeyboardInterrupt:
            continue

if __name__ == '__main__':
    main()
