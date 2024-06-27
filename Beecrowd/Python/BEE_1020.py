# Leia um valor inteiro correspondente à idade de uma pessoa em dias 
idade_dias = int(input())
# considere todo ano com 365 dias e todo mês com 30 dias. 
ano = idade_dias // 365
dias_restantes = idade_dias % 365
# Calcular meses
meses = dias_restantes // 30
dias = dias_restantes % 30
# Imprima a saída conforme exemplo fornecido.
print(f"{ano} ano(s)")
print(f"{meses} mes(es)")
print(f"{dias} dia(s)")

# accept in 26/06/2024 by Gustavo Xavier