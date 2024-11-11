from services.usuario_services import UsuarioService
from repositories.usuario_repository import UsuarioRepository
from config.database import Session
import os

def limpar_terminal():
    return os.system("cls||clear")

class Menu:

    def menu_escolhas():
        session = Session()
        repository = UsuarioRepository(session)
        service = UsuarioService(repository)
        while True:
            limpar_terminal()
            print("---Menu---")
            print("1 - Adicionar um usuário.")
            print("2 - Pesquisar um usuário.")
            print("3 - Atualizar dados de um usuário.")
            print("4 - Excluir um usuário.")
            print("5 - Exibir todos os usuários cadastrados.")
            print("0 - Sair.")
            opcao = int(input("Digite a opção desejada: "))

            match (opcao):
                case 1:
                    limpar_terminal()
                    service.criar_usuario()
                    input("Aperte enter para continuar...")
                case 2:
                    limpar_terminal()
                    service.pesquisar_id()
                    input("Aperte enter para continuar...")

                case 3:
                    limpar_terminal()
                    service.alterar_atributos()
                    input("Aperte enter para continuar...")
                case 4:
                    limpar_terminal()
                    service.apagar_usuario()
                    input("Aperte enter para continuar...")

                case 5:
                    limpar_terminal()
                    # Listar todos os usuários cadastrados.
                    print("\nListando usuários cadastrados.")
                    lista_usuario = service.listar_todos_usuarios()
                    for usuario in lista_usuario:
                        print(
                            f" Id: {usuario.id} - Nome: {usuario.nome} - Email: {usuario.email} - Senha: {usuario.senha}"
                        )
                    input("Aperte enter para continuar...")
                case 0:
                    limpar_terminal()
                    print("Obrigado!")
                    break

                case _:
                    limpar_terminal()
                    print("Opção inválida.")
                    input("Aperte enter para continuar...")
