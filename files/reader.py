from tkinter import filedialog
from tkinter import *

root = Tk()
root.wm_withdraw()


class lfp_reader():
    # SELECCIONAR ARCHIVO

    def __init__(self):
        self.filename = filedialog.askopenfilename(
            initialdir="/", title="Seleccionar archivo", filetypes=(("LFP", "*.lfp"), ("all files", "*.*")))
        root.destroy()

    # OBTENER
    def get_lines(self, keyword):
        # LEER LINEAS
        lfp_stream = open(self.filename)
        lfp_lines = lfp_stream.readlines()
        selected_lines = [words for words in lfp_lines if keyword in words]

        # CERRAR STREAM
        lfp_stream.close()
        return selected_lines
