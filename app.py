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
    print("1. Cadastrar tênis")
    print("2. Listar tênis")
    print("3. Ativar/Desativar tênis")
    print("4. Sair")

def escolhe_opcao():

    def exibir_subtitulo(texto):
        os.system("cls" if os.name == "nt" else "clear")
        print(texto)
        print(" ")

    def retorna_menu():
        input("Digite uma tecla para voltar ao menu principal ")
        main()

    def cadastrar_tenis():
        exibir_subtitulo("Cadastrar tênis")
        nome_tenis = input("Digite o nome do tênis que deseja cadastrar: ")
        tamanho_tenis = int(input("Digite o tamanho do tênis: "))
        cor_tenis = input("Digite a cor do tênis: ")
        ativo = input("O tênis está ativo? (s/n): ").strip().lower() == 's'
        tenis.append({"nome": nome_tenis, "tamanho": tamanho_tenis, "cor": cor_tenis, "ativo": ativo})
        print(f"O tênis {nome_tenis} foi cadastrado com sucesso\n")
        retorna_menu()

    def listar_tenis():
        exibir_subtitulo("Lista de tênis cadastrados")
        for t in tenis:
            nome_tenis = t["nome"]
            tamanho_tenis = t["tamanho"]
            cor_tenis = t["cor"]
            ativo = "Ativo" if t["ativo"] else "Desativado"
            print(f" - {nome_tenis.ljust(20)} | {str(tamanho_tenis).ljust(6)} | {cor_tenis.ljust(15)} | {ativo}")
        retorna_menu()

    def ativar_tenis():
        exibir_subtitulo("Ativar/Desativar tênis")
        nome_tenis = input("Digite o nome do tênis que deseja ativar/desativar: ")
        encontrado = False
        for t in tenis:
            if t["nome"].lower() == nome_tenis.lower():
                t["ativo"] = not t["ativo"]
                status = "ativado" if t["ativo"] else "desativado"
                print(f"O tênis {nome_tenis} foi {status} com sucesso.")
                encontrado = True
                break
        if not encontrado:
            print(f"O tênis {nome_tenis} não foi encontrado.")
        retorna_menu()

    def finalizar_programa():
        os.system("cls" if os.name == "nt" else "clear")
        print("Finalizando o programa\n")

    def opcao_invalida():
        print("Essa opção não é válida")
        input("Aperte qualquer tecla para voltar")
        main()

    try:
        opcao_escolhida = int(input("Escolha uma opção: "))

        if opcao_escolhida == 1:
            cadastrar_tenis()
        elif opcao_escolhida == 2:
            listar_tenis()
        elif opcao_escolhida == 3:
            ativar_tenis()
        elif opcao_escolhida == 4:
            finalizar_programa()
        else:
            opcao_invalida()
    except ValueError:
        opcao_invalida()

def main():
    exibir_nome_do_programa()
    mostra_escolhas()
    escolhe_opcao()

if __name__ == "__main__":
    main()
