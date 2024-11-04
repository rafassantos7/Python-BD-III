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
                    print("\nAdicionando usuário.")
                    nome = input("Digite seu nome: ")
                    email = input("Digite seu email: ")
                    senha = input("Digite seu senha: ")

                    service.criar_usuario(nome=nome, email=email, senha=senha)

                case 2:
                    email = str(input("Digite o email do usuário: "))
                    repository.pesquisar_usuario_por_email(email)
                    input("Aperte uma tecla para continuar...")

                case 3:
                    repository.atualizar_usuario(usuario)

                case 4:
                    pass  

                case 5:
                     # Listar todos os usuários cadastrados.
                    print("\nListando usuários cadastrados.")
                    lista_usuario = service.listar_todos_usuarios()
                    for usuario in lista_usuario:
                        print(f"Nome: {usuario.nome} - Email: {usuario.email} - Senha: {usuario.senha}")
