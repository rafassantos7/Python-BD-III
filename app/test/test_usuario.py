from app.models.usuario import Usuario
import pytest

@pytest.fixture
def criar_usuario():
    return Usuario("Rafael","rafael@gmail.com","123")

def test_nome(criar_usuario):
    assert criar_usuario.nome == "Rafael"

def test_usuario_nome_vazio_retorna_mensagem_erro():
    with pytest.raises(ValueError, match= "O nome não pode estar vazio."):
        Usuario("","rafael@gmail.com","123")

def test_usuario_nome_invalido_erro():
    with pytest.raises(TypeError,match= "O nome deve conter letras."):
        Usuario(123,"rafael@gmail.com","123")

def test_usuario_email_tipo_invalido_retorna_mensagem_erro():
    with pytest.raises(TypeError,match= "O email deve conter letras."):
        Usuario("Rafael",789,"123")

def test_usuario_email_vazio_retorna_mensagem_erro():
    with pytest.raises(ValueError, match= "O email não pode estar vazio."):
        Usuario("Rafael","","123")

def test_usuario_email_invalido_retorna_mensagem_erro():
    with pytest.raises(TypeError,match="O email deve conter @."):
        Usuario("Rafael","rafaelgmail.com","123")

def test_senha_vazia_retorna_mensagem_erro():
    with pytest.raises(ValueError, match= "A senha não pode estar vazia."):
        Usuario("Rafael","rafael@gmail.com","")

def test_senha_fragil_retorna_mensagem_erro():
    with pytest.raises(TypeError, match= "A senha só pode conter 10 caracteres."):
        Usuario("Rafael","rafael@gmail.com","12346549874")
