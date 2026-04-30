def somar(a, b):
    n = a + b
    return n

def subtrair(a, b):
    n = a - b
    return n

def multiplicar(a, b):
    n = a * b
    return n

def dividir(a, b):
    if b != 0:
        n = a / b
    else:
        n = 0
    return n


#Início
n1 = float(input('Informe o primeiro número: '))
n2 = float(input('Informe o segundo número: '))
print(f'\n Os números escolhidos forma {n1} e {n2}\n')
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
    

    

