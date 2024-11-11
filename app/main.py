import os
import sys


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from app.system.system_config import Menu as sistema


def main():
    sistema.menu_escolhas()


if __name__ == "__main__":
    main()
