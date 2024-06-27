# O arquivo de entrada contém um valor inteiro N (0 < N < 1000000).
notas = int(input())

print(notas)
print(f"{notas//100} nota(s) de R$ 100,00")
notas %= 100
print(f"{notas//50} nota(s) de R$ 50,00")
notas %= 50
print(f"{notas//20} nota(s) de R$ 20,00")
notas %= 20
print(f"{notas//10} nota(s) de R$ 10,00")
notas %= 10
print(f"{notas//5} nota(s) de R$ 5,00")
notas %= 5
print(f"{notas//2} nota(s) de R$ 2,00")
notas %= 2
print(f"{notas} nota(s) de R$ 1,00")

# accept in 27/06/2024 by Gustavo Xavier