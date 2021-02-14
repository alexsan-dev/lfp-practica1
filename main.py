# IMPORTS
import json
from menu.tools import menu
from files.reader import lfp_reader
from files.parse import parse_lines
from files.html import generate_html

# GLOBALES


class main():
    def __init__(self):
        # GLOBALES
        self.lfp_file = None
        self.json_dict = None
        self.init_menu()

    # MENU PRINCIPAL
    def init_menu(self):
        self.main_menu = menu('(1) Cargar  | (2) Ordenadas | (3) Búsquedas | (4) Todas | (5) Archivo | (6) Salir', {
            1: self.set_file,
            2: self.ordered_list,
            3: self.searched_list,
            4: self.all_list,
            5: self.all_list_file,
        })

    # OPCIONES
    def set_file(self):
        self.lfp_file = lfp_reader()
        self.init_menu()

    # DESPLEGAR LISTA
    def deploy_list(self, keyword, on_file):
        #  MOSTRAR TITULO
        print(f'\n{"-"*14}\n| RESULTADOS |\n{"-"*14}\n')

        # BUSCAR INSTRUCCIONES
        lines = parse_lines(self.lfp_file.get_lines(keyword), keyword)

        # CREAR ARCHIVO
        if on_file:
            generate_html(lines)

        # REGRESAR AL MENU PRINCIPAL
        input("Presiona ENTER para continuar ")
        self.init_menu()

    # LISTA DE ORDENADAS
    def ordered_list(self):
        self.deploy_list('ORDENAR', False)

    # LISTA DE BUSQUEDAS
    def searched_list(self):
        self.deploy_list('BUSCAR', False)

    #  LISTA DE BUSQUEDAS
    def all_list(self):
        self.deploy_list('', False)

    #  GENERAR ARCHIVO
    def all_list_file(self):
        self.deploy_list('', True)


# INICIAR
if __name__ == "__main__":
    main()
