from services.usuario_services import UsuarioService
from repositories.usuario_repository import UsuarioRepository
from config.database import Session
from system.system_config import Menu as sistema


def main():
    sistema.menu_escolhas()
    
    
if __name__ == "__main__":
    main()
