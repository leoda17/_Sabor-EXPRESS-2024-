import os

tenis = [
    {"nome": "Adidas Dame 8", "tamanho": 42, "cor": "Preto/Branco", "ativo": True},
    {"nome": "Nike LeBron Witness 8", "tamanho": 44, "cor": "Azul/Cinza", "ativo": False},
    {"nome": "Nike Renew Elevate 3", "tamanho": 40, "cor": "Branco", "ativo": True}
]

def exibir_nome_do_programa():
    print("""

██████╗░░█████╗░░██████╗██╗░░██╗███████╗████████╗██████╗░░█████╗░██╗░░░░░██╗░░░░░
██╔══██╗██╔══██╗██╔════╝██║░██╔╝██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░██║░░░░░
██████╦╝███████║╚█████╗░█████═╝░█████╗░░░░░██║░░░██████╦╝███████║██║░░░░░██║░░░░░
██╔══██╗██╔══██║░╚═══██╗██╔═██╗░██╔══╝░░░░░██║░░░██╔══██╗██╔══██║██║░░░░░██║░░░░░
██████╦╝██║░░██║██████╔╝██║░╚██╗███████╗░░░██║░░░██████╦╝██║░░██║███████╗███████╗
╚═════╝░╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝╚══════╝░░░╚═╝░░░╚═════╝░╚═╝░░╚═╝╚══════╝╚══════╝

██╗░░██╗██╗░█████╗░██╗░░██╗███████╗
██║░██╔╝██║██╔══██╗██║░██╔╝╚════██║
█████═╝░██║██║░░╚═╝█████═╝░░░███╔═╝
██╔═██╗░██║██║░░██╗██╔═██╗░██╔══╝░░
██║░╚██╗██║╚█████╔╝██║░╚██╗███████╗
╚═╝░░╚═╝╚═╝░╚════╝░╚═╝░░╚═╝╚══════╝
""")
    
def mostra_escolhas():
    print("1. Cadastrar Novo Tênis")
    print("2. Listar Tênis Disponíveis")
    print("3. Ativar/Desativar Tênis")
    print("4. Sair")

def escolhe_opcao():
    def exibir_subtitulo(texto):
        os.system("cls" if os.name == 'nt' else 'clear')
        linha = "_" * 65
        print(linha)
        print(texto)
        print(linha)
        print(" ")

    def retorna_menu():
        input("Digite uma tecla para voltar ao menu principal ")
        main()

    def cadastrar_tenis():
        exibir_subtitulo("Cadastrar Novo Tênis")

        nome_tenis = input("Digite o nome do tênis: ")
        try:
            tamanho = int(input("Digite o tamanho do tênis: "))
        except ValueError:
            print("Tamanho inválido. Deve ser um número inteiro.")
            retorna_menu()
            return
        cor = input("Digite a cor do tênis: ")
        ativo = input("O tênis está ativo? (Sim/Não): ").strip().lower() == 'sim'
        tenis.append({"nome": nome_tenis, "tamanho": tamanho, "cor": cor, "ativo": ativo})
        print(f"O tênis {nome_tenis} foi cadastrado com sucesso\n")
        retorna_menu()

    def listar_tenis():
        exibir_subtitulo("Lista de Tênis Disponíveis")
        if tenis:
            for i, tenis_item in enumerate(tenis, start=1):
                status = "Ativo" if tenis_item["ativo"] else "Inativo"
                print(f"{i}. Nome: {tenis_item['nome']} | Tamanho: {tenis_item['tamanho']} | Cor: {tenis_item['cor']} | Status: {status}")
        else:
            print("Nenhum tênis cadastrado.")
        retorna_menu()

    def ativar_desativar_tenis():
        exibir_subtitulo("Ativar/Desativar Tênis")
        listar_tenis()
        if tenis:
            try:
                escolha = int(input("Digite o número do tênis para ativar/desativar: "))
                if 1 <= escolha <= len(tenis):
                    tenis_item = tenis[escolha - 1]
                    tenis_item["ativo"] = not tenis_item["ativo"]
                    status = "Ativo" if tenis_item["ativo"] else "Inativo"
                    print(f"O tênis {tenis_item['nome']} agora está {status}.")
                else:
                    print("Número inválido. Por favor, escolha um número da lista.")
            except ValueError:
                print("Entrada inválida. Por favor, insira um número válido.")
        retorna_menu()

    def finalizar_programa():
        os.system("cls" if os.name == 'nt' else 'clear')
        print("Finalizando o programa\n")
        exit()

    def opcao_invalida():
        print("Opção inválida!")
        input("Aperte qualquer tecla para voltar")
        main()

    try:
        opcao_escolhida = int(input("Escolha uma opção: "))

        if opcao_escolhida == 1:
            cadastrar_tenis()
        elif opcao_escolhida == 2:
            listar_tenis()
        elif opcao_escolhida == 3:
            ativar_desativar_tenis()
        elif opcao_escolhida == 4:
            finalizar_programa()
        else:
            opcao_invalida()
    except ValueError:
        opcao_invalida()

def main():
    exibir_nome_do_programa()
    while True:
        mostra_escolhas()
        escolhe_opcao()

if __name__ == "__main__":
    main()
