from auxiliar.operacoes_basicas import somar, subtrair, multiplicar, dividir
import random
import os

#Início
n1 = random.randint (1, 10)
n2 = random.randint (1, 10)
print(f'\n Os números escolhidos foram {n1} e {n2}\n')
print("\n //////// Menu de Opções ////////\n [1] - Soma\n [2]- Subtração\n [3] - Multiplicação\n [4] - Divisão ")
opcao = float(input('Informe a operação desejada: '))
match opcao:
    case 1:
        resposta = somar(n1, n2)
        print (f'O resultado da operação é {resposta}')
    case 2:
        resposta = subtrair(n1, n2)
        print (f'O resultado da operação é {resposta}')
    case 3:
        resposta = multiplicar(n1, n2)
        print (f'O resultado da operação é {resposta}')
    case 4:
        resposta = dividir(n1, n2)
        print (f'O resultado da operação é {resposta}')
    case _:
        resposta = print("Opção inválida!!")
