from tkinter import *

import pandas as pd

RAL_FILE_NAME = "RALES.csv"

CELL_MARGIN = 7
CELL_PADDING = 3


class ProfilePreparation(Frame):
    def __init__(self, parent, rows_to_show):
        Frame.__init__(self, parent, background="cyan")

        self.rows_to_show = rows_to_show
        self.__labels = []

        self.canvas = Canvas(parent, borderwidth=0)
        self.inner_frame = Frame(self.canvas)
        self.inner_frame.bind("<Configure>", self.onFrameConfigure)

        self.scrollbar = Scrollbar(parent, orient="vertical", command=self.canvas.yview)
        self.scrollbar.pack(side="right", fill="y")

        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.create_window((4, 4), window=self.inner_frame, anchor="nw", tags="self.frame")
        self.canvas.focus_set()
        self.canvas.bind("<1>", lambda event: self.canvas.focus_set())
        self.canvas.bind("<Up>", lambda event: self.canvas.yview_scroll(-1, "units"))
        self.canvas.bind("<Down>", lambda event: self.canvas.yview_scroll(1, "units"))

        self.__init_horizontal_header(self.inner_frame)
        self.__init_empty_skeleton(self.inner_frame, self.__labels)
        self.__print_order_list()

    def onFrameConfigure(self, event):
        # Esta función es ejecutada cada vez que se añade alguna vista al canvas
        # Su objetivo es actualizar la barra de scroll
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def __init_horizontal_header(self, frame):
        colour_label = Label(frame, text="COLOR", anchor="center", relief="groove")
        colour_label.grid(row=0,
                          column=0,
                          padx=(0, CELL_PADDING),
                          pady=CELL_PADDING,
                          ipadx=CELL_MARGIN,
                          ipady=CELL_MARGIN,
                          sticky=W + E + N + S)

        colour_name_label = Label(frame, text="NOMBRE DEL COLOR", anchor="center", relief="groove")
        colour_name_label.grid(row=0,
                               column=1,
                               padx=(0, CELL_PADDING),
                               pady=CELL_PADDING,
                               ipadx=CELL_MARGIN,
                               ipady=CELL_MARGIN,
                               sticky=W + E + N + S)

        article_label = Label(frame, text="ARTÍCULO", anchor="center", relief="groove")
        article_label.grid(row=0,
                           column=2,
                           padx=(0, CELL_PADDING),
                           pady=CELL_PADDING,
                           ipadx=CELL_MARGIN,
                           ipady=CELL_MARGIN,
                           sticky=W + E + N + S)

        article_name_label = Label(frame, text="NOMBRE DEL ARTÍCULO", anchor="center", relief="groove")
        article_name_label.grid(row=0,
                                column=3,
                                padx=(0, CELL_PADDING),
                                pady=CELL_PADDING,
                                ipadx=CELL_MARGIN,
                                ipady=CELL_MARGIN,
                                sticky=W + E + N + S)

        situation_label = Label(frame, text="BANDEJA", anchor="center", relief="groove")
        situation_label.grid(row=0,
                             column=4,
                             padx=(0, CELL_PADDING),
                             pady=CELL_PADDING,
                             ipadx=CELL_MARGIN,
                             ipady=CELL_MARGIN,
                             sticky=W + E + N + S)

        quantity_label = Label(frame, text="CANTIDAD", anchor="center", relief="groove")
        quantity_label.grid(row=0,
                            column=5,
                            padx=(0, CELL_PADDING),
                            pady=CELL_PADDING,
                            ipadx=CELL_MARGIN,
                            ipady=CELL_MARGIN,
                            sticky=W + E + N + S)

        state_label = Label(frame, text="ESTADO", anchor="center", relief="groove")
        state_label.grid(row=0,
                         column=6,
                         padx=(0, CELL_PADDING),
                         pady=CELL_PADDING,
                         ipadx=CELL_MARGIN,
                         ipady=CELL_MARGIN,
                         sticky=W + E + N + S)

    def __init_empty_skeleton(self, frame, labels):
        for i in range(self.rows_to_show):
            row = []
            labels.append(row)
            self.__create_empty_record(frame, i, row)

    def __create_empty_record(self, frame, index, row):
        global_index = index + 1
        column0 = self.__create_empty_record_label(frame)
        column0.grid(row=global_index,
                     column=0,
                     padx=CELL_PADDING,
                     pady=CELL_PADDING,
                     ipadx=CELL_MARGIN,
                     ipady=CELL_MARGIN,
                     sticky=W + E + N + S)
        row.append(column0)

        column1 = self.__create_empty_record_label(frame)
        column1.grid(row=global_index,
                     column=1,
                     padx=CELL_PADDING,
                     pady=CELL_PADDING,
                     ipadx=CELL_MARGIN,
                     ipady=CELL_MARGIN,
                     sticky=W + E + N + S)
        row.append(column1)

        column2 = self.__create_empty_record_label(frame)
        column2.grid(row=global_index,
                     column=2,
                     padx=CELL_PADDING,
                     pady=CELL_PADDING,
                     ipadx=CELL_MARGIN,
                     ipady=CELL_MARGIN,
                     sticky=W + E + N + S)
        row.append(column2)

        column3 = self.__create_empty_record_label(frame)
        column3.grid(row=global_index,
                     column=3,
                     padx=CELL_PADDING,
                     pady=CELL_PADDING,
                     ipadx=CELL_MARGIN,
                     ipady=CELL_MARGIN,
                     sticky=W + E + N + S)
        row.append(column3)

        column4 = self.__create_empty_record_label(frame)
        column4.grid(row=global_index,
                     column=4,
                     padx=CELL_PADDING,
                     pady=CELL_PADDING,
                     ipadx=CELL_MARGIN,
                     ipady=CELL_MARGIN,
                     sticky=W + E + N + S)
        row.append(column4)

        column5 = self.__create_empty_record_label(frame)
        column5.grid(row=global_index,
                     column=5,
                     padx=CELL_PADDING,
                     pady=CELL_PADDING,
                     ipadx=CELL_MARGIN,
                     ipady=CELL_MARGIN,
                     sticky=W + E + N + S)
        row.append(column5)

        column6 = self.__create_empty_record_checkbutton(frame)
        column6.grid(row=global_index,
                     column=6,
                     padx=CELL_PADDING,
                     pady=CELL_PADDING,
                     ipadx=CELL_MARGIN,
                     ipady=CELL_MARGIN,
                     sticky=W + E + N + S)
        row.append(column6)

    def __create_empty_record_entry(self, frame):
        return Entry(frame,
                     background="white",
                     relief="groove",
                     justify="center")

    def __create_empty_record_label(self, frame):
        return Label(frame,
                     background="white",
                     relief="groove",
                     justify="center")

    def __create_empty_record_checkbutton(self, frame):
        return Checkbutton(frame,
                           relief="groove",
                           justify="center")

    def __read_csv_preparation(self):
        # Crear el dataframe desde el archivo .csv
        df = pd.read_csv(RAL_FILE_NAME, delimiter=';', encoding='cp1252')

        # Crear una lista de listas para poder acceder de forma más sencilla a la lista.
        preparations_lines = [list(row) for row in df.values]

        return preparations_lines

    def __print_order_list(self):
        preparation_lines = self.__read_csv_preparation()
        for i in range(len(preparation_lines)):
            # Color
            self.__labels[i][0].configure(text=preparation_lines[i][0])
            # Nombre del color
            self.__labels[i][1].configure(text=preparation_lines[i][0])
            # Artículo
            self.__labels[i][2].configure(text=preparation_lines[i][2])
            # Nombre del artículo
            self.__labels[i][3].configure(text=preparation_lines[i][4])
            # Bandeja
            self.__labels[i][4].configure(text=preparation_lines[i][1])
            # Cantidad
            self.__labels[i][5].configure(text=preparation_lines[i][5])
