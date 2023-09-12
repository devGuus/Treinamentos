def votar(cand1, cand2, name):
    soma_cand1 = 0
    soma_cand2 = 0
    if(name == cand1):
        soma_cand1 += 1
        return soma_cand1 , soma_cand2
    elif(name == cand2):
        soma_cand2 += 1
        return soma_cand1 , soma_cand2
    return 0

def print_win(cand1, cand2):
    if cand1 > cand2:
        print("Lulinha venceu novamente, faz o L")
    elif(cand1 == cand2):
        print("É um empate, agora lutem até a morte")
    else:
        print("Bozo win, bora comprar viagra") 

cand1 = 'Lula'
cand2 = 'Bolsonaro'
aux = 1
lulinha = 0
bozo = 0

print("Canditato 1 = Lula\nCandidato 2 = Bolsonaro")
while aux != 0:
    nome_candidato = input("Digite o nome do candidato que deseja votar:\n")
    contabilizar = votar(cand1, cand2, nome_candidato)
    total_cand1, total_cand2 = contabilizar   
    if total_cand1 == 1:
        lulinha += 1
    else:
        bozo += 1
    aux = int(input("Deseja continuar votando? 1/Sim 0/Nao\n"))

print_win(lulinha, bozo)