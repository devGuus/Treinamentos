def multiplica(x, y):
    return x * y

def soma(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def divisao(x, y):
    return x / y

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