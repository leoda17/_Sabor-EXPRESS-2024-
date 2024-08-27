import os

def exibir_nome_do_programa():
    print("""
███████╗██╗░░░░░█████╗░░██████╗░██████╗░  ██████╗░███████╗████████╗
██╔════╝██║░░░░██╔══██╗██╔════╝██╔══██╗  ██╔══██╗██╔════╝╚══██╔══╝
█████╗░░██║░░░██║░░██║╚█████╗░██████╔╝  ██████╔╝█████╗░░░░░██║░░░
██╔══╝░░██║░░░██║░░██║░╚═══██╗██╔══██╗  ██╔═══╝░██╔══╝░░░░░██║░░░
███████╗███████╗╚█████╔╝██████╔╝██║░░██║  ██║░░░░░███████╗░░░██║░░░
╚══════╝╚══════╝░╚════╝░╚═════╝░╚═╝░░╚═╝  ╚═╝░░░░░╚══════╝░░░╚═╝░░░
""")

def exibir_opcoes():
    print('1. Cadastrar animal')
    print('2. Listar animais')
    print('3. Consultar animal')
    print('4. Sair\n')

def finalizar_app():
    os.system('cls')
    print('Finalizando o sistema de clínica veterinária\n')

def opcao_invalida():
    print('Opção inválida!\n')
    input('Digite uma tecla para voltar ao menu principal')
    main()

def escolher_opcao():
    opcao_escolhida = int(input('Escolha uma opção: '))
    
    if opcao_escolhida == 1:
        print('Cadastrar animal')
    elif opcao_escolhida == 2:
        print('Listar animais')
    elif opcao_escolhida == 3:
        print('Consultar animal')
    elif opcao_escolhida == 4:
        finalizar_app()
    else:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ =='__main__':
    main()
