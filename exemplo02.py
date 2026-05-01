from auxiliar.operacoes import dobro, triplo, quadrado, metade

n = float(input('Informe um número: '))

print('\n //////// MENUDE DE OPÇÕES ////////\n [1] - Dobro \n [2]- Triplo\n [3] - Quadrado\n [4] - Metade')
opcao = float(input('Escolha uma opção: '))

match opcao:
    case 1:#calcula dobro
        resposta = dobro(n)        
    case 2:#calcula triplo
        resposta = triplo(n)      
    case 3:#calcula quadrado
        resposta = quadrado(n)      
    case 4:#calcula metade
        resposta = metade(n)
    case _:
        print('Opção inválida')

print(resposta)