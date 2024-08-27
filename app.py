import os

def exibir_nome_do_programa():
    print("""

███████╗░█████╗░███████╗███████╗███╗░░██╗██████╗░░█████╗░
██╔════╝██╔══██╗╚════██║██╔════╝████╗░██║██╔══██╗██╔══██╗
█████╗░░███████║░░███╔═╝█████╗░░██╔██╗██║██║░░██║███████║
██╔══╝░░██╔══██║██╔══╝░░██╔══╝░░██║╚████║██║░░██║██╔══██║
██║░░░░░██║░░██║███████╗███████╗██║░╚███║██████╔╝██║░░██║
╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚══════╝╚═╝░░╚══╝╚═════╝░╚═╝░░╚═╝

███████╗░██████╗██████╗░██╗███╗░░██╗██████╗░░█████╗░██╗░░░░░░█████╗░
██╔════╝██╔════╝██╔══██╗██║████╗░██║██╔══██╗██╔══██╗██║░░░░░██╔══██╗
█████╗░░╚█████╗░██████╔╝██║██╔██╗██║██║░░██║██║░░██║██║░░░░░███████║
██╔══╝░░░╚═══██╗██╔═══╝░██║██║╚████║██║░░██║██║░░██║██║░░░░░██╔══██║
███████╗██████╔╝██║░░░░░██║██║░╚███║██████╔╝╚█████╔╝███████╗██║░░██║
╚══════╝╚═════╝░╚═╝░░░░░╚═╝╚═╝░░╚══╝╚═════╝░░╚════╝░╚══════╝╚═╝░░╚═╝
""")

def exibir_opcoes():
    print('1. Cadastrar novo animal')
    print('2. Listar animais disponíveis')
    print('3. Consultar detalhes de um animal')
    print('4. Sair\n')

def finalizar_app():
    os.system('cls')
    print('Finalizando o sistema da Fazenda Espindola\n')

def opcao_invalida():
    print('Opção inválida!\n')
    input('Digite uma tecla para voltar ao menu principal')
    main()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        
        if opcao_escolhida == 1:
            print('Cadastrar novo animal')
        elif opcao_escolhida == 2:
            print('Listar animais disponíveis')
        elif opcao_escolhida == 3:
            print('Consultar detalhes de um animal')
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except ValueError:
        print('Entrada inválida. Por favor, insira um número.\n')
        input('Digite uma tecla para voltar ao menu principal')
        main()

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ =='__main__':
    main()
