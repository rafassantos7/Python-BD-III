from services.usuario_services import UsuarioService
from repositories.usuario_repository import UsuarioRepository
from config.database import Session

class Menu:
    
    def menu_escolhas():
        session = Session()
        repository = UsuarioRepository(session)
        service = UsuarioService(repository)
        while True:
            print("---Menu---")
            print("1 - Adicionar um usuário.")
            print("2 - Pesquisar um usuário.")
            print("3 - Atualizar dados de um usuário.")
            print("4 - Excluir um usuário.")
            print("5 - Exibir todos os usuários cadastrados.")
            print("0 - Sair.")
            opcao = int(input("Digite a opção desejada: "))
            
            match(opcao):
                case 1:   
                    service.criar_usuario()
                    input("Aperte enter para continuar...")
                case 2:
                    service.pesquisar_id()
                    input("Aperte enter para continuar...")

                case 3:
                    service.alterar_atributos()
                    input("Aperte enter para continuar...")
                case 4:
                    service.apagar_usuario()
                    input("Aperte enter para continuar...")

                case 5:
                     # Listar todos os usuários cadastrados.
                    print("\nListando usuários cadastrados.")
                    lista_usuario = service.listar_todos_usuarios()
                    for usuario in lista_usuario:
                        print(f" Id: {usuario.id} - Nome: {usuario.nome} - Email: {usuario.email} - Senha: {usuario.senha}")
                
                case 0:
                    break

                case _:
                    print("Opção inválida.")
                
