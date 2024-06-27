#  leia três valores com ponto flutuante de dupla precisão: A, B e C
A, B, C = map(float, input().split())
pi = 3.14159
# a) a área do triângulo retângulo que tem A por base e C por altura.
area_triagulo = (A*C) / 2
# b) a área do círculo de raio C. (pi = 3.14159)
area_circulo = pi * (C **2)
# c) a área do trapézio que tem A e B por bases e C por altura.
area_trapezio = ((A+B) * C) / 2
# d) a área do quadrado que tem lado B.
area_quadrado = B ** 2
# e) a área do retângulo que tem lados A e B.
area_retangulo = A * B
# O valor calculado deve ser apresentado com 3 dígitos após o ponto decimal.
print(f"TRIANGULO: {area_triagulo:.3f}")
print(f"CIRCULO: {area_circulo:.3f}")
print(f"TRAPEZIO: {area_trapezio:.3f}")
print(f"QUADRADO: {area_quadrado:.3f}")
print(f"RETANGULO: {area_retangulo:.3f}")

# accept in 26/06/2024 by Gustavo Xavier