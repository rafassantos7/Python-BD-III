from app.models.usuario import Usuario
from app.repositories.usuario_repository import UsuarioRepository


class UsuarioService:

    def __init__(self, repository: UsuarioRepository):
        self.repository = repository

    def criar_usuario(self):
        try:
            print("\nAdicionando usuário.")
            nome = input("Digite seu nome: ")
            email = input("Digite seu email: ")
            senha = input("Digite seu senha: ")

            usuario = Usuario(nome=nome, email=email, senha=senha)

            cadastrado = self.repository.pesquisar_usuario_por_email(usuario.email)

            if cadastrado:
                print("Usuário já cadastrado!")
                return

            self.repository.salvar_usuario(usuario)
            print("Usuário cadastrado com sucesso!")

        except TypeError as erro:
            print(f"Erro ao salvar o usuário: {erro}")
        except Exception as erro:
            print(f"Ocorreu um erro inesperado: {erro}")

    def pesquisar_id(self):
        try:
            id_pesquisa = input("Digite o id do usuário: ")
            usuario = self.repository.pesquisar_usuario_por_id(id_pesquisa)
            if usuario:
                print("Usuario pesquisado:")
                print(
                    f"{usuario.id} - {usuario.nome} - {usuario.email} - {usuario.senha}"
                )
                return
            print("Usuario não encontrado.")
        except TypeError as erro:
            print(f"Erro ao pesquisar usuário: {erro}")
        except Exception as erro:
            print(f"Ocorreu um erro inesperado: {erro}")

    def alterar_atributos(self):
        try:
            id_pesquisa = input("Digite o id do usuário que deseja alterar os dados: ")
            usuario = self.repository.pesquisar_usuario_por_id(id_pesquisa)
            if usuario:
                usuario.nome = input("Digite o novo nome:")
                usuario.email = input("Digite o novo email:")
                usuario.senha = input("Digite a novo senha:")
                self.repository.atualizar_usuario(usuario)
                return
        except TypeError as erro:
            print(f"Erro ao alterar daods do usuário: {erro}")
        except Exception as erro:
            print(f"Ocorreu um erro inesperado: {erro}")

    def apagar_usuario(self):
        try:
            id_pesquisa = input("Digite o id do usuário que deseja alterar os dados: ")
            usuario = self.repository.pesquisar_usuario_por_id(id_pesquisa)
            if usuario:
                self.repository.excluir_usuario(usuario)
                print("Usuario deletado com sucesso.")
                return
            print("Usuario não encontrado")
        except TypeError as erro:
            print(f"Erro ao deletar o usuário: {erro}")
        except Exception as erro:
            print(f"Ocorreu um erro inesperado: {erro}")

    def listar_todos_usuarios(self):
        return self.repository.listar_usuarios()
