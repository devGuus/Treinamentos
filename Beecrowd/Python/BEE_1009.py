# leia o nome de um vendedor, o seu salário fixo e o total de vendas 
nome = input()
salario = float(input())
vendas = float(input())
# soma do salario + comissão
total = (salario + (vendas*0.15))

print("TOTAL = R$ {:.2f}".format(total))

# accept in 21/05/2024 by Gustavo Xavier