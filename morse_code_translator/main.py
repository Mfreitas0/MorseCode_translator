from functions_MorseCode.decode_MorseCode import decode_morse, text_to_MorseCode


while True:
    option = input(f'\nEscolha uma Opção:\nTexto para Código Morse[1]\nCódigo Morse para Texto[2]\n')

    if option.lower() == 'exit':
        break
    elif option == '1':
        text = input(f'Digite o texto:\n')
        print(text_to_MorseCode(text))
    elif option == '2':
        morse_code = input(f'Digite o codigo:\n')
        print(decode_morse(morse_code))
    if not option.isdigit():
        print('Escolha uma Opção Válida!!\nPara Sair Digite [exit]')
