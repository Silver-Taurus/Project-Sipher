#! /usr/bin/env python3

''' Project Sipher '''

import math
import string
import random
from Crypto.Util.number import isPrime
from cipher_sub_routines import CipherSubRoutine
from cipher_sub_routines import single_cipher_dispatch

@single_cipher_dispatch
def get_cipher_func(cipher):
    return KeyError('No Such Cipher Exists!!!')

def safe_run(func):
    ''' A decorator sub-routine for handling exceptions '''
    def decorated_function(*args, **kwargs):
        while True:
            try:
                return func(*args, **kwargs)
            except KeyError or TypeError:
                print(f'{CipherSubRoutine.exceptions[func.__name__]}!!!\n')
            except ValueError:
                print('Invalid Literal!!!\n')
            else:
                break
    return decorated_function

class Cipher(CipherSubRoutine):
    ''' Class for performing the cipher methods on a given text '''

    # Cipher Constructor for taking input of text and passing it to CipherSubRoutine Constructor.
    def __init__(self):
        self._text = input('\nEnter the text: ').lower()
        self._length = len(self._text)
        super().__init__(self._text, self._length)
    
    #---------------------------- Properties (Getters and Setters) --------------------------------
    @property
    def text(self):
        return self._text
    
    @text.setter
    def text(self, _):
        print('\nWarning... Inititalised text is not meant to be changed manually!!!\n')

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, _):
        print('\nWarning... Internally Calculated length is not meant to be changed manually!!!\n')

    #---------------------------- Main Methods ----------------------------------------------------
    def _primary_cipher_routine(self, mode):
        ''' primary cipher routine for applying the cipher algorithm with the defined mode legally '''
        cipher_menu = {}
        print('\n\nCipher list:')
        for n, fn_name in enumerate(get_cipher_func.registry.keys(), 1):
            if n != 1:
                print(f'{n-1}. {fn_name}')
                cipher_menu[n-1] = fn_name

        choice = int(input('\nEnter Your Choice: '))
        print(f'\nThe {mode}d string is:', get_cipher_func(cipher_menu[1])(self) if choice == 1 \
            else get_cipher_func(cipher_menu[choice])(self, mode))

    def encode(self):
        ''' Encode-Routine for Encoding the plaintext into ciphertext '''
        self._primary_cipher_routine('encode')

    def decode(self):
        ''' Decode-Routine for Decoding the ciphertext into plaintext '''
        self._primary_cipher_routine('decode')

    def hack(self):
        ''' Hack-Routine for Hacking the ciphertext without key(s) into plaintext '''
        pass

    #---------------------------- Primary Cipher Routines -----------------------------------------
    @get_cipher_func.register('Reverse Cipher')
    def _reverse_cipher(self):
        ''' Cipher Routine to encode into or decode from Reverse Cipher '''
        return self.text[::-1]

    @get_cipher_func.register('Caesar Cipher')
    @safe_run
    def _caesar_cipher(self, mode):
        ''' Cipher Routine to encode into or decode from Caesar Cipher '''
        key = int(input('(integer >0 and not a multiple of 26)\nEnter the key: '))
        if key < 1 or key%26 == 0:
            raise KeyError
        if mode == 'encode':
            return self._caesar_sub_routine(key)
        else:
            return self._caesar_sub_routine(26-key)

    @get_cipher_func.register('Transposition Cipher')
    @safe_run
    def _transposition_cipher(self, mode):
        ''' Cipher Routine to encode into or decode form Transposition Cipher '''
        key = int(input(f'(integer >2 and < {self.length})\nEnter the key: '))
        if (key < 2) or (key >= self.length):
            raise KeyError
        return self._transposition_sub_routine(key, mode)

    @get_cipher_func.register('Affine Cipher')
    @safe_run
    def _affine_cipher(self, mode):
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

            print(f'\nkey-a = {key_a}\nkey-b = {key_b}')

        else:
            key_a = int(input('\n(integer >1 and should be co-prime with 26)\nEnter the key-a: '))
            if key_a < 2 or math.gcd(key_a, 26) != 1:
                raise KeyError
            key_b = int(input('(positive integer)\nEnter the key-b: '))
            if key_b < 0:
                raise KeyError

        return self._affine_sub_routine((key_a, key_b), mode)

    @get_cipher_func.register('Vignere Cipher')
    @safe_run
    def _vigenere_cipher(self, mode):
        ''' Cipher Routine to encode into or decode from Vigenere Cipher '''
        key = input(f'(alphabets only and length of key should be >0 and <{self.length})\nEnter the key: ')
        if any(char.isdigit() for char in key) or len(key) > self.length:
            raise KeyError
        key = list(key)
        if self._length != len(key):
            for i in range(self.length - len(key)):
                key.append(key[i % len(key)])
        return self._vigenere_otp_sub_routine(key, mode)

    @get_cipher_func.register('Otp Cipher')
    @safe_run
    def _otp_cipher(self, mode):
        ''' Cipher Routine to encode into or decode from One Time Pad Cipher '''
        if mode == 'encode':
            while True:
                choice = input('Enter key Automatically/Manually [A/m]: ')
                if choice in ('A', 'a', ''):
                    key = ''.join(random.choice(string.ascii_letters).lower() for _ in self.text)
                    print('Encryption key is:', key)
                    break
                elif choice in ('M', 'm'):
                    key = input(f'\n(alphabets only and length of key should be = {self.length})\nEnter the key: ')
                    if len(key) != self.length or any(not ch.isalpha() for ch in key):
                        raise KeyError
                    break
                else:
                    print('Invalid Choice!!!')
        else:
            key = input(f'(alphabets only and length of key should be = {self.length})\nEnter the key: ')
            if len(key) != self.length or any(not ch.isalpha() for ch in key):
                raise KeyError
        return self._vigenere_otp_sub_routine(key, mode)

    @get_cipher_func.register('RSA Cipher')
    def _rsa_cipher(self, mode):
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
                   break
                else :
                   break

            n = p*q
            phi = (p-1)*(q-1)
            e = 2
            while(e < phi):
                if math.gcd(e, phi) == 1 :
                    break
                else :
                    e += 1
            return self._rsa_sub_routine(e, n, 'encode')

        if mode == 'decode' :
            p, q, e = int(input('Enter key public key p:')), int(input('Enter public key q:')), int(input('Enter e :'))
            n = p*q
            phi = (p-1)*(q-1)
            d = (1 + (2*phi))/e
            return self._rsa_sub_routine(d, n, 'decode')

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
