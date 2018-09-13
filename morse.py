#!/usr/bin/env python3
""" Class allowing for the manipulation of Morse code
"""


class Morse:
    """Morse: Allowing for the enciphering and deciphering of Morse code
    """
    morse_alphabet = {' ': '/', 'a': 'o-', 'b': '-ooo', 'c': '-o-o', 'd': '-oo',
                      'e': 'o', 'f': 'oo-o', 'g': '--o', 'h': 'oooo', 'i': 'oo',
                      'j': 'o---', 'k': '-o-', 'l': 'o-oo', 'm': '--', 'n': '-o',
                      'o': '---', 'p': 'o--o', 'q': '--o -', 'r': '-o-', 's': 'ooo',
                      't': '-', 'u': 'oo-', 'v': 'ooo-', 'w': 'o--', 'x': '-oo-',
                      'y': '-o--', 'z': '--oo', '1': 'o----', '2': 'oo---',
                      '3': 'ooo--', '4': 'oooo-', '5': 'ooooo', '6': '-oooo',
                      '7': '--ooo', '8': '---oo', '9': '----o', '0': '-----'}

    inverted_morse_alphabet = dict([[v, k] for k, v in morse_alphabet.items()])
    inverted_morse_alphabet[' '] = ''

    @staticmethod
    def plain_in(text):
        """plain_in: Encipher plain text into Morse code

        :param text: Space separated plain text
        :rtn str: Enciphered version of 'text' input
        """
        return ' '.join(Morse.morse_alphabet.get(letter) for letter in text)

    @staticmethod
    def morse_in(text):
        """morse_in: Decipher Morse code into plain text

        :param text: '/' separated Morse code
        :rtn str: Deciphered version of 'text' input
        """
        return ''.join(Morse.inverted_morse_alphabet.get(letter) for letter in text.split())


def main():
    """main: Command line useage of Morse class
    """
    parser = argparse.ArgumentParser(description='Simple Morse code converter\
    Morse code is represented with "o" "-" characters')

    parser.add_argument('-m', '--morse-input', action="store", type=str,
                        help='Convert "/" separated Morse code into plain English')
    parser.add_argument('-p', '--plain-input', action="store", type=str,
                        help='Convert " " separated English into "/" separated Morse code')
    arguments = parser.parse_args()

    if arguments.plain_input:
        print(Morse.plain_in(arguments.plain_input))
    elif arguments.morse_input:
        print(Morse.morse_in(arguments.morse_input))


if __name__ == '__main__':
    import argparse
    main()
