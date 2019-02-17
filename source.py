''' Project Sipher '''

from abc import ABC, abstractmethod
from math import ceil

class CipherSubRoutine(ABC):
    ''' Class for supporting the main cipher class by providing the sub-routines needed'''

    def __init__(self, text, length):
        self._text = text
        self._length = length

    @abstractmethod
    def _caesar_sub_routine(self, shift):
        ''' Caesar Cipher sub-routine for crypting text '''
        output = ''
        for char in self._text:
            if char.isupper():
                output += chr((ord(char) + shift-65) % 26 + 65)
            elif char == ' ':
                output += char
            else:
                output += chr((ord(char) + shift-97) % 26 + 97)
        return output

    @abstractmethod
    def _transposition_sub_routine(self, key, mode):
        ''' Transposition Cipher sub-routine for crypting text '''
        input = self._text.lower()
        output = []
        if mode == 'encode':
            # Row-Wise reading and Col-Wise Filling
            for i in range(key):
                for j in range(i, self._length, key):
                    output.append(input[j])
            return ''.join(output)
        else:
            # Col-Wise reading and Row-Wise Filling
            cols = ceil(self._length/key)
            for i in range(cols):
                for j in range(i, self._length, cols):
                    output.append(self._text[j])
            return ''.join(output)

    @abstractmethod
    def _affine_sub_routine(self, mode):
        a,b = 17,20
        input = self._text.lower()
        output = []
        if mode == 'encode' :
            # Applying a simple mathematical function to encrypt text using their unicode
            for i in range(self._length):
                if self._text[i] != ' ' :
                    output.append(chr(((((a * (ord(self._text[i]) - ord('a')) ) + b) % 26) + ord('a'))))
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

    def _affine_sub_routine(self, mode):
        ''' Calling abstract base class sub-routine '''
        return super()._affine_sub_routine(mode)

    # Primary Cipher Routines
    def __reverse_cipher(self, mode):
        ''' Cipher Routine to encode into or decode from Reverse Cipher '''
        return self._text.lower()[::-1]

    def __caesar_cipher(self, mode):
        ''' Cipher Routine to encode into or decode from Caesar Cipher '''
        key = int(input("Enter the key: "))
        if mode == 'encode':
            return self._caesar_sub_routine(key)
        else:
            return self._caesar_sub_routine(26-key)

    def __transposition_cipher(self, mode):
        ''' Cipher Routine to encode into or decode form Transposition Cipher '''
        while(True):
            key = int(input('Enter the key: '))
            if (key is not 1) and (key < self._length):
                break
            else:
                print('Key cannot be < 2 or >= the length of entered text!!!\n')
        return self._transposition_sub_routine(key, mode)

    def __affine_cipher(self, mode):
        ''' Cipher Routineto encode into or decode from Affine Cipher '''
        if mode == 'encode':
            return self._affine_sub_routine(mode)
        else :
            return self._affine_sub_routine(mode)
        pass

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
            cipher = input('\nEnter Your Choice: ')
            if cipher in cipher_keys.keys():
                break
            else:
                print('Invalid Choice!!!\n')

        if mode == 'encode':
            print('\nThe encoded string is: ', self.__ciphers[cipher_keys[cipher]](mode))
        else:
            print('\nThe decoded string is: ', self.__ciphers[cipher_keys[cipher]](mode))

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
