print("Bem vindo ao quiz em de python para iniciantes!\nDeseja iniciar? {S/N}")
iniciarQuiz = input()
respostas_usuario = []
# Coloque as respostas em ordem aqui
respostas_corretas = ["b", "c"]
qtd_perguntas = len(respostas_corretas) # quantidade de perguntas

# Analisa se a resposta está correta e retorna a quantidade de acertos
def analisarResposta(respostas_user, lista_resp):
    score = 0
    for user, correta in zip(respostas_user, lista_resp):
        if user == correta:
            score += 1
    return score

# Iniciar o quiz
if iniciarQuiz != "S" and iniciarQuiz != "s":
    print("Encerrando Quiz...")
    quit()

# Primeira pergunta
print("Perfeito! Vamos para primeira pergunta\nQual comando utilizamos para imprimir alguma informação na tela ou terminal?\n(A) printf()\n(B) print()\n(C) system_out_println()\n(D) Console.WriteLine()")
resposta = input("Resposta: ").strip().lower() # Garante que a resposta fique minuscula para conferir
respostas_usuario.append(resposta) # Aplicando a resposta na lista de respostas

# Segunda pergunta
print("Qual destas estruturas de controle permite executar um bloco de código repetidamente?\n(A) if\n(B) def\n(C) for\n(D) import")
resposta = input("Resposta: ").strip().lower() # Garante que a resposta fique minuscula para conferir
respostas_usuario.append(resposta) # Aplicando a resposta na lista de respostas

# Contando os pontos
pontuacao_total = analisarResposta(respostas_usuario, respostas_corretas)

# score de acertos
if pontuacao_total == qtd_perguntas:
    print(f"Parabéns, você acertou todas as respostas!!🎉\nProntuação: {pontuacao_total}/{qtd_perguntas}") # Acertou Todas
elif pontuacao_total > 0:
    print(f"Bom trabalho! Você acertou algumas perguntas. Continue praticando!\nProntuação: {pontuacao_total}/{qtd_perguntas}") # Acertou algumas
else:
    print(f"Não desista, sei que na próxima você vai se sair melhor!\nProntuação: {pontuacao_total}/{qtd_perguntas}") # Errou todas