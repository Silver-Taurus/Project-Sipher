''' Project Sipher '''

from abc import ABC, abstractmethod
from math import ceil
from math import gcd
from random import randint

class CipherSubRoutine(ABC):
    ''' Class for supporting the main cipher class by providing the sub-routines needed'''

    def __init__(self, text, length):
        self.__text = text
        self.__length = length

    @abstractmethod
    def _caesar_sub_routine(self, key):
        ''' Caesar Cipher sub-routine for crypting text '''
        output = ''
        for char in self.__text:
            if char == ' ':
                output += char
            else:
                output += chr((ord(char) + key-97) % 26 + 97)
        return output

    @abstractmethod
    def _transposition_sub_routine(self, key, mode):
        ''' Transposition Cipher sub-routine for crypting text '''
        output = []
        if mode == 'encode':
            # Row-Wise reading and Col-Wise Filling
            for i in range(key):
                for j in range(i, self.__length, key):
                    output.append(self.__text[j])
            return ''.join(output)
        else:
            # Col-Wise reading and Row-Wise Filling
            cols = ceil(self.__length/key)
            for i in range(cols):
                for j in range(i, self.__length, cols):
                    output.append(self.__text[j])
            return ''.join(output)

    @abstractmethod
    def _affine_sub_routine(self, key, mode):
        output = []

        if mode == 'encode':
            for ch in self._text:
                if ch != ' ':
                    output.append(chr((((key[0] * (ord(ch) - ord('a'))) + key[1]) % 26) + ord('a')))
                else:
                    output.append(' ')
            
        elif mode == 'decode':
            a_inv = 0 
            for i in range(1, 26): 
                if ((key[0]*i) % 26) == 1 :
                    a_inv = i
                    break
            print(self._text)
            print(a_inv)
            print(ord('a'))
            for ch in self._text:
                if ch != ' ' :
                    output.append(chr((a_inv * (ord(ch) - ord('a') - key[1])) % 26 + ord('a')))
                else :
                    output.append(' ')

        return ''.join(output)
            


class Cipher(CipherSubRoutine):
    ''' Class for performing the cipher methods on a given text '''
    # Cipher Constructor for taking input of text and passing it to CipherSubRoutine Constructor.
    def __init__(self):
        self.__ciphers = {'Reverse Cipher': self.__reverse_cipher, \
            'Caesar Cipher': self.__caesar_cipher, \
            'Transposition Cipher': self.__transposition_cipher, \
            'Affine Cipher': self.__affine_cipher, \
            'One Time Pad Cipher': self.__otp_cipher, \
            'RSA Cipher': self.__rsa_cipher
            }
        self._text = input('\nEnter the text: ')
        self._length = len(self._text)
        super().__init__(self._text, self._length)

    # Abstract Cipher Sub-Routines
    def _caesar_sub_routine(self, key):
        ''' Calling abstract base class sub-routine '''
        return super()._caesar_sub_routine(key)

    def _transposition_sub_routine(self, key, mode):
        ''' Calling abstract base class sub-routine '''
        return super()._transposition_sub_routine(key, mode)

    def _affine_sub_routine(self, key, mode):
        ''' Calling abstract base class sub-routine '''
        return super()._affine_sub_routine(key, mode)

    # Primary Cipher Routines
    def __reverse_cipher(self, mode):
        ''' Cipher Routine to encode into or decode from Reverse Cipher '''
        return self._text.lower()[::-1]

    def __caesar_cipher(self, mode):
        ''' Cipher Routine to encode into or decode from Caesar Cipher '''
        key = int(input('Enter the key:'))
        if mode == 'encode':
            return self._caesar_sub_routine(key)
        else:
            return self._caesar_sub_routine(26-key)

    def __transposition_cipher(self, mode):
        ''' Cipher Routine to encode into or decode form Transposition Cipher '''
        while True:
            try:
                key = int(input('Enter the key: '))
                if (key == 1) or (key < self._length):
                    assert ValueError
            except ValueError:
                print('Key cannot be < 2 or >= the length of entered text!!!\n')
            else:
                break
        return self._transposition_sub_routine(key, mode)

    def __affine_cipher(self, mode):
        ''' Cipher Routine to encode into or decode from Affine Cipher '''
        key_a = key_b = 0

        if mode == 'encode':
            while True:
                choice = input("Enter key Automatically/Manually [A/m]: ")

                if choice == 'A' or choice == 'a' or choice == '':
                    while True:
                        key_a = randint(1, 10**5)
                        if gcd(key_a, 26) == 1 :
                            break
                    key_b = randint(1, 10**5)
                    break
                
                elif choice == 'm' or choice == 'M':
                    while True:
                        try:
                            n = int(input('Range 1 to n from which a valid key is choosen\nEnter n (should be greater than 1): '))
                            if n < 2:
                                assert ValueError
                            keys_a = []
                            for i in range(1, n):
                                if gcd(i,26) == 1 :
                                    print(i, end = ' ')
                                    keys_a.append(i)
                            key_a = int(input('\nEnter key-a: '))
                            if key_a not in keys_a:
                                assert ValueError
                            key_b = int(input('Enter key-b: '))
                            if key_b < 0:
                                assert ValueError
                        except ValueError:
                            print('\nEntered value is invalid!!!')
                        else:
                            break
                    break

                else:
                    print('Invalid Choice!!!')
        
            print('\nkey-a = {}\nkey-b = {}'.format(key_a, key_b))
        
        else:
            try:
                key_a = int(input('\nEnter key-a: '))
                if key_a < 2 or gcd(key_a, 26) != 1:
                    assert ValueError
        
                key_b = int(input('Enter key-b: '))
                if key_b < 0:
                    assert ValueError

            except ValueError:
                print('Entered key is invalid!!! Aborting...')
                exit()
    
        return self._affine_sub_routine((key_a, key_b), mode)


    def __vigenere_cipher(self, mode):
        pass

    def __otp_cipher(self, mode):
        pass

    def __rsa_cipher(self, mode):
        pass

    def __primary_cipher_routine(self, mode):
        ''' primary cipher routine for performing the cipher algorithm with the defined mode leagally '''

        cipher_keys = {}
        print('\n\nCipher list:')
        for num, func_name in enumerate(self.__ciphers.keys(), 1):
            print('{}. {}'.format(num, func_name))
            cipher_keys['{}'.format(num)] = '{}'.format(func_name)

        cipher = None
        while(True):
            try:
                cipher = input('\nEnter Your Choice: ')
                if cipher not in cipher_keys.keys():
                    assert ValueError
            except ValueError:
                print('Invalid Choice!!!\n')
            else:
                break

        if mode == 'encode':
            print('\nThe encoded string is:', self.__ciphers[cipher_keys[cipher]](mode))
        else:
            print('\nThe decoded string is:', self.__ciphers[cipher_keys[cipher]](mode))

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
            break

        cipher = Cipher()
        if choice == '1':
            cipher.encode()
        elif choice == '2':
            cipher.decode()
        else:
            cipher.hack()


if __name__ == '__main__':
    main()
