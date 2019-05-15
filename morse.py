#!/usr/bin/env python3
"""
This file is part of pymorse.

Copyright (C) 2019, James Lee <jamesl33info@gmail.com>.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import argparse


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
    main()
