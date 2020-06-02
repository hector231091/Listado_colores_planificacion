from tkinter import *
import pandas as pd

from input_preparation import ProfilePreparation

RAL_FILE_NAME = "RALES.csv"


def read_csv_preparation():
    # Crear el dataframe desde el archivo .csv
    df = pd.read_csv(RAL_FILE_NAME, delimiter=';', encoding='cp1252')

    # Crear una lista de listas para poder acceder de forma más sencilla a la lista.
    preparations_lines = [list(row) for row in df.values]

    return len(preparations_lines)


AMOUNT_OF_ROWS = read_csv_preparation()
# AMOUNT_OF_ROWS = 10

root = Tk()
# root.state("zoomed")
root.geometry("1600x900")

preparation = ProfilePreparation(root, read_csv_preparation())
preparation.pack(fill="both")
preparation.place(relx=0, rely=0, relwidth=1, relheigh=1)

root.mainloop()

# Cosas a realizar:
# 	1.- Ver la forma de pasar un archivo a UTF-8 con el propio programa para no tener que hacer un paso más a la hora de cargar el .csv al programa.
#	2.- El número de filas debe determinarlo el tamaño del archivo que cargamos "len(preparations_lines)".
