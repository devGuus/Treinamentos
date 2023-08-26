import PySimpleGUI as sg

def codifique(texto, chave):
    resultado = ''
    for i in texto:
        if i.isalpha():
            base = ord('A') if i.isupper() else ord('a')
            novoTexto = chr((ord(i) - base + chave) % 26 + base)
            resultado += novoTexto
        else:
            resultado += i
    return resultado

def descriptografe(texto, chave):
    return codifique(texto, -chave)

layout = [
    [sg.Text("Bem-vindo ao CriptoTech")],
    [sg.Text("Deseja criptografar? (Digite-1)\nDeseja descriptografar? (Digite-2)")],
    [sg.InputText(key="escolha")],
    [sg.Button("Ok"), sg.Button("Sair")],
]

window = sg.Window("CriptoTech", layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == "Sair":
        break
    if values["escolha"] == "1":
        layout_encrypt = [
            [sg.Text("----Criptografia----")],
            [sg.Text("Digite a chave: "), sg.InputText(key="key_encrypt")],
            [sg.Text("Digite o texto: "), sg.InputText(key="text_encrypt")],
            [sg.Button("Criptografar")],
            [sg.Text("", size=(30, 1), key="output_encrypt")],
        ]
        window_encrypt = sg.Window("Criptografia", layout_encrypt)
        while True:
            event_encrypt, values_encrypt = window_encrypt.read()
            if event_encrypt == sg.WINDOW_CLOSED:
                break
            if event_encrypt == "Criptografar":
                key = int(values_encrypt["key_encrypt"])
                cripto = values_encrypt["text_encrypt"]
                textoCodificado = codifique(cripto, key)
                window_encrypt["output_encrypt"].update(f"Texto codificado: {textoCodificado}")
        window_encrypt.close()

    elif values["escolha"] == "2":
        layout_decrypt = [
            [sg.Text("----Descriptografia----")],
            [sg.Text("Digite a chave: "), sg.InputText(key="key_decrypt")],
            [sg.Text("Digite o texto: "), sg.InputText(key="text_decrypt")],
            [sg.Button("Descriptografar")],
            [sg.Text("", size=(30, 1), key="output_decrypt")],
        ]
        window_decrypt = sg.Window("Descriptografia", layout_decrypt)
        while True:
            event_decrypt, values_decrypt = window_decrypt.read()
            if event_decrypt == sg.WINDOW_CLOSED:
                break
            if event_decrypt == "Descriptografar":
                key = int(values_decrypt["key_decrypt"])
                cripto = values_decrypt["text_decrypt"]
                textoDesco = descriptografe(cripto, key)
                window_decrypt["output_decrypt"].update(f"Texto descodificado: {textoDesco}")
        window_decrypt.close()

    elif values["escolha"] == "0":
        break
    else:
        sg.popup_error("ERRO:Código invalido")

window.close()