from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base
from app.config.database import db

Base = declarative_base()


class Usuario(Base):
    # Definindo características da tabela no banco de dados
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(150))
    email = Column(String(150))
    senha = Column(String(150))

    # Definindo características da classe.
    def __init__(self, nome: str, email: str, senha: str) -> None:
        self.nome = self._test_nome(nome)
        self.email = self._test_email(email)
        self.senha = self._test_senha(senha)

    def _test_nome(self,nome):
        if not isinstance (nome,str):
            raise TypeError("O nome deve conter letras.")
        if not nome.strip():
            raise ValueError("O nome não pode estar vazio.")
        return nome

    def _test_email(self,email):
        if not isinstance (email,str):
            raise TypeError("O email deve conter letras.")
        if not email.strip():
            raise ValueError("O email não pode estar vazio.")
        if "@" not in email:
            raise TypeError("O email deve conter @.")
        return email

    def _test_senha(self,senha):
        if not senha.strip():
            raise ValueError("A senha não pode estar vazia.")
        if len(senha) > 10:
            raise TypeError("A senha só pode conter 10 caracteres.")
        return senha
    

# Criando tabela no banco de dados.
Base.metadata.create_all(bind=db)
