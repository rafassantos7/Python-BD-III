from app.system.system_config import Menu as sistema
import os
import sys


def main():
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
    sistema.menu_escolhas()
    
    
if __name__ == "__main__":
    main()
