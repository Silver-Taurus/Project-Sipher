''' Project Sipher '''

class Cipher():
    ''' Class for performing the cipher methods on a given text '''

    def __init__(self):
        self._text = ''

    def __caesar_sub_routine(string, shift) :
        final_string = ''

        for i in range(len(string)) :
            char = string[i]
            if char.isupper() :
                final_string += chr((ord(char) + shift-65) % 26 + 65)
            else :
                final_string += chr((ord(char) + shift-97) % 26 + 97)
        #return final_string
        pass

    def __reverse_cipher(self, mode):
        if mode == 'encode' :
            print('The encoded string is : ', self._text[::-1])
        else :
            print('The decoded string is : ', self._text[::-1])
        pass

    def __caesar_cipher(self, mode):
        ''' Routine to encode into and decode from Caesar Cipher '''

        shift = int(input("Enter the shift : "))

        if mode == 'encode' :
            print('The encoded text is : {}'.format(self.__caesar_sub_routine(self._text, shift)))
        else :
            print('The decoded Cipher is : {}'.format(self.__caesar_sub_routine(self._text, 26-shift)))

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
        ciphers = {'Reverse Cipher': self.__reverse_cipher, 'Caesar Cipher': self.__caesar_cipher, \
                    'Transposition Cipher': self.__transposition_cipher, 'Affine Cipher': self.__affine_cipher, \
                    'One Time Pad Cipher': self.__otp_cipher, 'Vigenere Cipher': self.__vigenere_cipher, \
                    'RSA Cipher': self.__rsa_cipher }
        cipher_keys = {}
        print('\n\nCipher list:')
        for num, val in enumerate(ciphers.keys(), 1):
            print(f'{num}. {val}')
            cipher_keys[f'{num}'] = f'{val}'
        ciphers[cipher_keys[input('\nEnter Your Choice: ')]](mode)

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
    print('''
     ____            _           _     ____  _       _                                                      |  _ \ _ __ ___ (_) ___  ___| |_  / ___|(_)_ __ | |__   ___ _ __                                        | |_) | '__/ _ \| |/ _ \/ __| __| \___ \| | '_ \| '_ \ / _ \ '__|                                       |  __/| | | (_) | |  __/ (__| |_   ___) | | |_) | | | |  __/ |                                          |_|   |_|  \___// |\___|\___|\__| |____/|_| .__/|_| |_|\___|_|                                                        |__/                        |_|
    ''' )

    ''' Main Driver Program '''
    while(True):
        choice = input('''\n\nMain Menu:
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
