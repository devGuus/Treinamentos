POINTS = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

def contar_pontos(chave):
    points = 0
    for i in chave.upper():
        if 'A' <= i <= 'Z':
            points += POINTS[ord(i) - ord('A')]
    return points

jogador1 = input("Jogador 1: ")
jogador2 = input("Jogador 2: ")

pts_jogador1 = contar_pontos(jogador1)
pts_jogador2 = contar_pontos(jogador2)

if pts_jogador1 > pts_jogador2:
    print("Jogador 1 VENCEU!")
elif pts_jogador1 < pts_jogador2:
    print("Jogador 2 VENCEU!")
else:
    print("EMPATE!")