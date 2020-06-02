from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk

import pandas as pd

RAL_FILE_NAME = "RALES.csv"

CELL_MARGIN = 7
CELL_PADDING = 3

class ProfilePreparation(Frame):
	def __init__(self, parent, rows_to_show):
		Frame.__init__(self, parent, background="cyan")

		self.rows_to_show = rows_to_show

		self.__init_horizontal_header()

		self.__labels = []
		self.__init_empty_skeleton(self.__labels)
		self.__print_order_list()

	def __init_horizontal_header(self):
		colour_label = Label(self, text="COLOR", anchor="center", relief="groove")
		colour_label.grid(row=0,
					column=0,
					padx=(0, CELL_PADDING),
					pady=CELL_PADDING,
					ipadx=CELL_MARGIN,
					ipady=CELL_MARGIN,
					sticky=W + E + N + S)

		colour_name_label = Label(self, text="NOMBRE DEL COLOR", anchor="center", relief="groove")
		colour_name_label.grid(row=0,
				 column=1,
				 padx=(0, CELL_PADDING),
				 pady=CELL_PADDING,
				 ipadx=CELL_MARGIN,
				 ipady=CELL_MARGIN,
				 sticky=W + E + N + S)

		article_label = Label(self, text="ARTÍCULO", anchor="center", relief="groove")
		article_label.grid(row=0,
					 column=2,
					 padx=(0, CELL_PADDING),
					 pady=CELL_PADDING,
					 ipadx=CELL_MARGIN,
					 ipady=CELL_MARGIN,
					 sticky=W + E + N + S)

		article_name_label = Label(self, text="NOMBRE DEL ARTÍCULO", anchor="center", relief="groove")
		article_name_label.grid(row=0,
						  column=3,
						  padx=(0, CELL_PADDING),
						  pady=CELL_PADDING,
						  ipadx=CELL_MARGIN,
						  ipady=CELL_MARGIN,
						  sticky=W + E + N + S)

		situation_label = Label(self, text="BANDEJA", anchor="center", relief="groove")
		situation_label.grid(row=0,
				   column=4,
				   padx=(0, CELL_PADDING),
				   pady=CELL_PADDING,
				   ipadx=CELL_MARGIN,
				   ipady=CELL_MARGIN,
				   sticky=W + E + N + S)

		quantity_label = Label(self, text="CANTIDAD", anchor="center", relief="groove")
		quantity_label.grid(row=0,
				   column=5,
				   padx=(0, CELL_PADDING),
				   pady=CELL_PADDING,
				   ipadx=CELL_MARGIN,
				   ipady=CELL_MARGIN,
				   sticky=W + E + N + S)

		state_label = Label(self, text="ESTADO", anchor="center", relief="groove")
		state_label.grid(row=0,
				   column=6,
				   padx=(0, CELL_PADDING),
				   pady=CELL_PADDING,
				   ipadx=CELL_MARGIN,
				   ipady=CELL_MARGIN,
				   sticky=W + E + N + S)

	def __init_empty_skeleton(self, labels):
		for i in range(self.rows_to_show):
			row = []
			labels.append(row)
			self.__create_empty_record(i, row)

	def __create_empty_record(self, index, row):
		global_index = index + 1
		column0 = self.__create_empty_record_label()
		column0.grid(row=global_index,
		             column=0,
		             padx=CELL_PADDING,
		             pady=CELL_PADDING,
		             ipadx=CELL_MARGIN,
		             ipady=CELL_MARGIN,
		             sticky=W + E + N + S)
		row.append(column0)

		column1 = self.__create_empty_record_label()
		column1.grid(row=global_index,
		             column=1,
		             padx=CELL_PADDING,
		             pady=CELL_PADDING,
		             ipadx=CELL_MARGIN,
		             ipady=CELL_MARGIN,
		             sticky=W + E + N + S)
		row.append(column1)

		column2 = self.__create_empty_record_label()
		column2.grid(row=global_index,
		             column=2,
		             padx=CELL_PADDING,
		             pady=CELL_PADDING,
		             ipadx=CELL_MARGIN,
		             ipady=CELL_MARGIN,
		             sticky=W + E + N + S)
		row.append(column2)

		column3 = self.__create_empty_record_label()
		column3.grid(row=global_index,
		             column=3,
		             padx=CELL_PADDING,
		             pady=CELL_PADDING,
		             ipadx=CELL_MARGIN,
		             ipady=CELL_MARGIN,
		             sticky=W + E + N + S)
		row.append(column3)

		column4 = self.__create_empty_record_label()
		column4.grid(row=global_index,
		             column=4,
		             padx=CELL_PADDING,
		             pady=CELL_PADDING,
		             ipadx=CELL_MARGIN,
		             ipady=CELL_MARGIN,
		             sticky=W + E + N + S)
		row.append(column4)

		column5 = self.__create_empty_record_label()
		column5.grid(row=global_index,
		             column=5,
		             padx=CELL_PADDING,
		             pady=CELL_PADDING,
		             ipadx=CELL_MARGIN,
		             ipady=CELL_MARGIN,
		             sticky=W + E + N + S)
		row.append(column5)

		column6 = self.__create_empty_record_checkbutton()
		column6.grid(row=global_index,
		             column=6,
		             padx=CELL_PADDING,
		             pady=CELL_PADDING,
		             ipadx=CELL_MARGIN,
		             ipady=CELL_MARGIN,
		             sticky=W + E + N + S)
		row.append(column6)

	def __create_empty_record_entry(self):
		return Entry(self,
					 background="white",
					 relief="groove",
					 justify="center")

	def __create_empty_record_label(self):
		return Label(self,
					 background="white",
					 relief="groove",
					 justify="center")

	def __create_empty_record_checkbutton(self):
		return Checkbutton(self,
						   relief="groove",
						   justify="center")

	def __read_csv_preparation(self):

	 	# Crear el dataframe desde el archivo .csv
	 	df = pd.read_csv(RAL_FILE_NAME, delimiter=';', encoding='cp1252')

	 	# Crear una lista de listas para poder acceder de forma más sencilla a la lista.
	 	preparations_lines = [list(row) for row in df.values]

	 	return preparations_lines

	def __print_order_list(self):

		for i in range(len(self.__read_csv_preparation())):

			# Color
			self.__labels[i][0].configure(text=self.__read_csv_preparation()[i][0])
			# Nombre del color
			self.__labels[i][1].configure(text=self.__read_csv_preparation()[i][0])
			# Artículo
			self.__labels[i][2].configure(text=self.__read_csv_preparation()[i][2])
			# Nombre del artículo
			self.__labels[i][3].configure(text=self.__read_csv_preparation()[i][4])
			# Bandeja
			self.__labels[i][4].configure(text=self.__read_csv_preparation()[i][1])
			# Cantidad
			self.__labels[i][5].configure(text=self.__read_csv_preparation()[i][5])
