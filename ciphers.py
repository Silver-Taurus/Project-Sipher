#! /usr/bin/env python3

''' Project Sipher '''

import math
import random
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
        super().__init__(self.__text, self.__length)

    # Primary Cipher Routines
    def __reverse_cipher(self):
        ''' Cipher Routine to encode into or decode from Reverse Cipher '''
        return self.__text[::-1]

    @CipherSubRoutine.safe_run
    def __caesar_cipher(self, mode):
        ''' Cipher Routine to encode into or decode from Caesar Cipher '''
        key = int(input('Enter the key: '))
        if key < 0 or key == 0 or key%26 == 0:
            raise KeyError
        if mode == 'encode':
            return self._caesar_sub_routine(key)
        else:
            return self._caesar_sub_routine(26-key)

    @CipherSubRoutine.safe_run
    def __transposition_cipher(self, mode):
        ''' Cipher Routine to encode into or decode form Transposition Cipher '''
        key = int(input('Enter the key: '))
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
            key_a = int(input('\nEnter key-a: '))
            if key_a < 2 or math.gcd(key_a, 26) != 1:
                raise KeyError            
            key_b = int(input('Enter key-b: '))
            if key_b < 0:
                raise KeyError
        return self._affine_sub_routine((key_a, key_b), mode)

    @CipherSubRoutine.safe_run
    def __vigenere_cipher(self, mode):
        ''' Cipher Routine to encode into or decode from Vigenere Cipher '''
        key = input('Enter the key: ')
        if any(char.isdigit() for char in key) or len(key) > self.__length:
            raise KeyError
        key = list(key)
        if self.__length != len(key):
            for i in range(self.__length - len(key)):
                key.append(key[i % len(key)])
        return self._vigenere_sub_routine(key, mode)

    def __otp_cipher(self, mode):
        pass

    def __rsa_cipher(self, mode):
        pass

    def __primary_cipher_routine(self, mode):
        ''' primary cipher routine for applying the cipher algorithm with the defined mode leagally '''
        cipher_keys = {}
        print('\n\nCipher list:')
        for num, func_name in enumerate(self.__ciphers.keys(), 1):
            print('{}. {}'.format(num, func_name))
            cipher_keys['{}'.format(num)] = '{}'.format(func_name)
        choice = None
        while(True):
            try:
                choice = input('\nEnter Your Choice: ')
                print('\nThe {}d string is:'.format(mode), self.__ciphers[cipher_keys[choice]]() \
                    if choice=='1' else self.__ciphers[cipher_keys[choice]](mode))
                func = self.__ciphers[cipher_keys[choice]]
            except KeyError:
                print('Invalid Choice!!!\n')
            else:
                break

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