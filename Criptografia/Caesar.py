import PySimpleGUI as sg

def codifique(texto, chave):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    retorno = ''
    for i in texto:
        if i.isalpha():
            index = alphabet.index(i.upper()) # Utilize index
            txt_encriptado = chave[index]

            if i.islower():
                retorno += txt_encriptado.lower()
            else:
                retorno += txt_encriptado
        else:
            retorno += i
    return retorno
def descriptografe(texto, chave):
    pass
# EXP: VCHPRZGJNTLSKFBDQWAXEUYMOI
# Texto: HELLO WORLD 
# Saida: JRSSB YBWSP
sg.theme("DarkAmber")

layout = [
    [sg.Text("Bem-vindo ao CriptoTech")],
    [sg.Text("Cifra de Substituição Simples\n\n")],
    [sg.Text("Deseja criptografar? (Digite-1)")],
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
                key = values_encrypt["key_encrypt"]
                cripto = values_encrypt["text_encrypt"]
                textoCodificado = codifique(cripto, key)
                window_encrypt["output_encrypt"].update(f"Texto codificado: {textoCodificado}")
        window_encrypt.close()

    elif values["escolha"] == "0":
        break
    else:
        sg.popup_error("ERRO:Código invalido")

window.close()