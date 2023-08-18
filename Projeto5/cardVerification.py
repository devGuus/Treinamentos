def valideLuhn(code):
    x = 0
    aux = False

    for i in range(len(code) -1, -1, -1):
        digito = int(code[i])

        if aux:
            digito *= 2
            if digito > 9:
                digito -= 9
                
        x += digito
        aux = not aux
    
    return x % 10 == 0

codigoCartao = input("Digite o código aqui: ")
validando = valideLuhn(codigoCartao)

if(validando == True):
    print("Código do cartao verdadeiro")
else:
    print("Código do cartao falso")