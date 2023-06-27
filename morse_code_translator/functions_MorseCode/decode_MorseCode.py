from .morseCode_dict import MORSE_CODE_DICT

def decode_morse(morse_code):
    words = []
    morse_code = [i for i in morse_code.split(' ')]
    for j in morse_code:   
        if not '  '  in words:
            words.append(' ')
        for i in MORSE_CODE_DICT.items():
            if j == i[1]:
                words.append(i[0])
    return ' '.join(words).strip().replace('   ', '')



def text_to_MorseCode(text):
    code = []
    for j in text.upper():
        if j == ' / ':
            code.append(' ')
        for i in MORSE_CODE_DICT.items():
            if j == i[0]:
                code.append(i[1])
    return ' '.join(code).strip().replace('   ', '')


# print(decode_morse('.... . .-.. .-.. ---  / .-- --- .-. .-.. -.. -....-  / . ..-  / ... --- ..-  / ---  / -- .- .-. -.-. --- ... '))
# print(decode_morse('...   ---   ...'))
