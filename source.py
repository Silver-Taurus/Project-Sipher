''' Project Sipher '''

class Cipher():
    ''' Class for performing the cipher methods on a given text '''
    
    def __init__(self):
        self._text = ''

    def __reverse_cipher(self, mode):
        pass

    def __caesar_cipher(self, mode):
        pass

    def __transposition_cipher(self, mode):
        pass

    def __affine_cipher(self, mode):
        pass

    def __vigenere_cipher(self, mode):
        pass

    def __otp_cipher(self, mode):
        pass

    def __rsa_cipher(self, mode):
        pass

    def __cipher_sub_routine(self, mode):
        ''' cipher-sub-routine for performing the cipher conversion task using key(s) with the defined mode '''
        ciphers = {'Reverse Cipher': self.__reverse_cipher(mode), 'Caesar Cipher': self.__caesar_cipher(mode), \
                    'Transposition Cipher': self.__transposition_cipher(mode), 'Affine Cipher': self.__affine_cipher(mode), \
                    'One Time Pad Cipher': self.__otp_cipher(mode), 'Vigenere Cipher': self.__vigenere_cipher(mode), \
                    'RSA Cipher': self.__rsa_cipher(mode)}
        cipher_keys = {}
        print('\nMain Menu:')
        for num, val in enumerate(ciphers.keys(), 1):
            print(f'{num}. {val}')
            cipher_keys[f'{num}'] = f'{val}'
        ciphers[cipher_keys[input('\nEnter Your Choice: ')]]

    def encode(self):
        ''' Encode-Routine for Encoding the plaintext into ciphertext '''
        self._text = input('Enter the Text to encrypt : ')
        self.__cipher_sub_routine('encode')
    
    def decode(self):
        ''' Decode-Routine for Decoding the ciphertext into plaintext '''
        self._text = input('Enter the Text to decrypt : ')
        self.__cipher_sub_routine('decode')

    def hack(self):
        ''' Hack-Routine for Hacking the ciphertext without key(s) into plaintext '''
        pass


def main():
    ''' Main Driver Program '''
    while(True):
        choice = input(''' Main Menu:
            1. Encode into ciphertext
            2. Decode into plaintext
            3. Hack the ciphertext
            4. Exit
            ''')
        cipher = Cipher()
        if choice == '1':
            cipher.encode()
        elif choice == '2':
            cipher.decode()
        elif choice == '3':
            cipher.hack()
        else:
            break


if __name__ == '__main__':
    main()