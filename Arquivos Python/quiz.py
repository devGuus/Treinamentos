print("Bem vindo ao quiz em de python para iniciantes!\nDeseja iniciar? {S/N}")
iniciarQuiz = input()
score = 0
qtd_perguntas = 2

def analisarResposta(resposta, correta):
    if resposta == correta:
        return "correta"
    else:
        return "errada"

def contarPontos(resposta):
    if resposta == "correta":
        return 1
    else:
        return 0

if iniciarQuiz != "S" and iniciarQuiz != "s":
    quit()
# Primeira pergunta
print("Perfeito! Vamos para primeira pergunta\nQual comando utilizamos para imprimir alguma informação na tela ou terminal?\n(A) printf()\n(B) print()\n(C) system_out_println()\n(D) Console.WriteLine()")
questao1 = input("Resposta: ")
resposta1 = "B"


# Segunda pergunta
print("Qual destas estruturas de controle permite executar um bloco de código repetidamente?\n(A) if\n(B) def\n(C) for\n(D) import")
questao2 = input("Resposta: ")

if questao2 == "C" or questao2 == "c":
    print("Correto")
    score += 1
else:
    print("Errada")

# score de acertos
print(f"Quantidade de acertos: {score}/{qtd_perguntas}")