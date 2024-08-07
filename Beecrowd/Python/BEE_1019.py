#  contém um valor inteiro N
segundos = int(input())
# Imprima o tempo lido (segundos), convertido para horas:minutos:segundos

horas = segundos//3600 # 3600 segundos = 1 hora
segundos %= 3600
minutos = segundos//60 # 60 = 1 minuto
segundos %= 60

print(f"{horas}:{minutos}:{segundos}")

# accept in 07/08/2024 by Gustavo Xavier