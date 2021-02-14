from tkinter import filedialog
from tkinter import *


class lfp_reader():
    # SELECCIONAR ARCHIVO

    def __init__(self):
        self.lfp_file = Tk()
        self.lfp_file.filename = filedialog.askopenfilename(
            initialdir="/", title="Seleccionar archivo", filetypes=(("LFP", "*.lfp"), ("all files", "*.*")))

    # OBTENER
    def get_lines(self, keyword):
        lfp_stream = open(self.lfp_file.filename)
        lfp_lines = lfp_stream.readlines()
        selected_lines = [words for words in lfp_lines if keyword in words]
        lfp_stream.close()
        return selected_lines
