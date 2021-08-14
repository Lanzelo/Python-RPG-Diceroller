# ROLADOR DE DADOS AAAAAAAAAAAAAAAAAAA

import random

# Função rolador de dados, base pra app rolador

d4 = 4
d6 = 6
d8 = 8
d10 = 10
d12 = 12
d20 = 20
d100 = 100

def diceroll(n, dice): # n = int, dice = 'string'
    rolagem = []
#    n = int(input("Quantos dados você quer rolar: "))
#    d = input("Qual dado você deseja usar (d4, d6, d8, d10, d12, d20): ")

    if dice == d4:
        for i in range(n): # enquanto x não chegar em n
            rolagem.append(random.randint(1,4))
        return rolagem

    elif dice == d6: 
        for i in range(n):
            rolagem.append(random.randint(1,6))
        return rolagem

    elif dice == d8: 
        for i in range(n):
            rolagem.append(random.randint(1,8))
        return rolagem 

    elif dice == d10: 
        for i in range(n):
            rolagem.append(random.randint(1,10))
        return rolagem 

    elif dice == d12:
        for i in range(n):
            rolagem.append(random.randint(1,12))
        return rolagem

    elif dice == d20:
        for i in range(n):
            rolagem.append(random.randint(1,20))
        return rolagem

    elif dice == d100:
        for i in range(n):
            rolagem.append(random.randint(1,100))
        return rolagem

    else:
        print('Dado não encontrado')
