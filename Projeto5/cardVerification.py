def valideLuhn(code): # Primeiro eu fiz o algoritmo em python pois já sou mais familializado
    x = 0
    aux = False

    for i in range(len(code) -1, -1, -1): # Dentro do vetor vai voltar da direita pra esquerda
        digito = int(code[i])

        if aux:
            digito *= 2 # Pegando os segundos valores
            if digito > 9: # confirmando se o valor está entre 0 ou 9
                digito -= 9 # se for maior vai receber 9
                
        x += digito # Pegamos o valor aqui ->
        aux = not aux # Variavel auxiliar não é falsa
    
    return x % 10 == 0 # E verificamos se é divisivel por 10 ->

codigoCartao = input("Digite o código aqui: ")
validando = valideLuhn(codigoCartao)

if(validando == True):
    print("Código do cartao verdadeiro")
else:
    print("Código do cartao falso")