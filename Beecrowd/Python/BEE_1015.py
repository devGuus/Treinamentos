import math
# Leia os quatro valores correspondentes aos eixos x e y de dois pontos quaisquer no plano, p1(x1,y1) e p2(x2,y2) Valores Flutuantes
x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

# Calcule a distância entre eles
distancia = math.sqrt((x2-x1)**2 + (y2 - y1)**2)

# Print 4 casas decimais após a vírgula
print("{:.4f}" .format(distancia))

# accept in 25/06/2024 by Gustavo Xavier