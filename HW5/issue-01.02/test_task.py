"""Morse Code Translator"""
import doctest
import pytest

LETTER_TO_MORSE = {
    'A': '.-', 'B': '-...', 'C': '-.-.',
    'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..',
    'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-',
    'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----',
    '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', '0': '-----',
    ', ': '--..--', '.': '.-.-.-', '?': '..--..',
    '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-',
    ' ': ' '
}

MORSE_TO_LETTER = {
    morse: letter
    for letter, morse in LETTER_TO_MORSE.items()
}


@pytest.mark.parametrize('msg, exp', [
    ('... --- ...', 'SOS'),
    ('.... . .-.. .-.. ---', 'HELLO'),
    ('.---- ..--- ...-- ....- ..... -.... --... ---.. ----.', '123456789')
])
def test_decode(msg, exp):
    """Проверяет вывод функции по заданным параметрам"""
    assert decode(msg) == exp


def encode(message: str) -> str:
    """
    Кодирует строку в соответсвие с таблицей азбуки Морзе

    >>> encode('SOS')
    '... --- ...'
    >>> encode('AAABBBCCCDDDEEEFFF') # doctest: +ELLIPSIS
    '.- .- ... ..-. ..-.'
    >>> encode('11223344556677889900')
    '.---- .---- ..--- ..--- ...-- ...-- ....- ....- ..... ..... -.... -....
     --... --... ---.. ---.. ----. ----. ----- -----'
    >>> encode('error')
    Traceback (most recent call last):
    KeyError: 'e'
    """
    encoded_signs = [
        LETTER_TO_MORSE[letter] for letter in message
    ]

    return ' '.join(encoded_signs)


def decode(morse_message: str) -> str:
    """
    Декодирует строку из азбуки Морзе в английский
    """
    decoded_letters = [
        MORSE_TO_LETTER[letter] for letter in morse_message.split()
    ]

    return ''.join(decoded_letters)


if __name__ == '__main__':
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)
