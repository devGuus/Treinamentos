def multiplica(x, y):
    return x * y

def soma(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def divisao(x, y):
    return x / y

print("Escolha uma opção:")
escolha = int(input("Calculadora(1) Media Padrão(2) Media Com Peso(3)"))

if escolha == 1:
    pergunta = int(input("Somar(1) Multiplicar(2) Subtrair(3) Dividir(4)"))

    if pergunta == 1:
        num1 = float(input("Digite um número: "))
        num2 = float(input("Digite outro número: "))
        print(soma(num1, num2))
    elif pergunta == 2:
        num1 = float(input("Digite um número: "))
        num2 = float(input("Digite outro número: "))
        print(multiplica(num1, num2))
    elif pergunta == 3:
        num1 = float(input("Digite o primeiro número a ser subtraído: "))
        num2 = float(input("Digite o segundo número a ser subtraído: "))
        print(subtracao(num1, num2))
    elif pergunta == 4:
        num1 = float(input("Digite o dividendo: "))
        num2 = float(input("Digite o divisor: "))
        print(divisao(num1, num2))
    else:
        print("Opção inválida")
elif escolha == 2:
    # Numeros de notas, pode ser que tenha mais de uma prova ou atividades
    n_notas = int(input("Quantidade de notas para contagem: "))
    somador = 0
    # Vamos saber as notas
    for notas in range(n_notas):
        pergunta = float(input(f"Digite a {notas} nota"))
        somador = somador + pergunta # Somamos todas as notas
    # Subtraimos a soma das notas pela quantidade de notas
    print(f" {divisao(somador, n_notas) :.2f}")
elif escolha == 3:
    n_notas = int(input("Quantidade de notas para contagem: "))
    somador = 0

    for notas in range(n_notas):
        pergunta = float(input(f"Digite a {notas} nota "))
        peso = float(input(f"Digite o peso em porcentagem da {notas} nota (Exp: 0.80) "))
        somador = somador + (pergunta * peso)

    print(f" {divisao(somador, n_notas) :.2f}")