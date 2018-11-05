Loading = False #если правда значит в текущей сессии уже была загрузка индекс таблиц
Indexing = False # если правда значит в текущей сессии проводилась индексация
deff_item = 0# пункт меню по умолчанию
import os #для метода listdir() получающего список файлов в указанной папке
from sys import argv as param,exit #для параметров командной строки
from PyQt5.QtWidgets import QFileDialog,QApplication,QInputDialog #стандартные диалоги
add = QApplication(param) #создания экземпляра этого класса методы QFileDialog не работают

import tkinter #Для коротких диалогов типа да/нет
from tkinter import messagebox
# hide main window
root = tkinter.Tk()
root.withdraw()

import time #для замеров времени

actions = ['Индексация текстов в папке',
		   'Загрузка таблиц индексации',
           'Обработка запроса',
           'Выход из программы']
		   
import re #для регулярных выражений
def text_to_words(text): #возможно преобразование из текста в слова будет переделываться
	"""Получает строку, возвращает слова(состоят только из букв) из которых состоит строка"""
	words = re.split(r'[^ёЁа-яА-Яa-zA-Z]+', text.lower())#создает список слов, все буквы делаем строчными
	#words = [word for word in words if word.isalpha()]#оставит только сочетания букв
	#words = [word for word in words if re.match(r'[^ёЁа-яА-Яa-zA-Z]+', word)]#оставит только сочетания англ.,рус. букв
	#words = [word for word in words if word not in stopwords.words('russian')]#удаляет стопслова
	#words = [stemmer.stem(w) for w in words if len(w) > 0]#
	return words

while True:
	#Спрашиваем пользователя что делать
	action,pressed_OK = QInputDialog.getItem(None, #без виджета предка
                                         'Выбрать необходимое действие', #заголовок окна
                                         'Выбор действия', #приглашающая надпись
                                         actions, #список действий
                                         deff_item, # по умолчанию выбрано первое 'Индексация текстов в папке'
                                         False #выбираемые строки не редактируемы
                                        )
	if action == actions[3] or not pressed_OK: #'Выход из программы'
		exit()
	elif action == actions[0]: #'Индексация текстов в папке'
		yes = False
		if Indexing:
			yes = messagebox.askyesno('Внимание', 'В текущей секции индексация проведена, игнорировать?')
		else:
			yes = True

		if yes:
			# try:
			with open('indexer.py', "r", encoding="utf-8") as source_file:
				exec(source_file.read())
				Indexing = True
				deff_item = 1
			# except Exception:
				# Indexing = False
				# messagebox.showerror("Ошибка!", 'При индексации произошла ошибка')
			Loading = False
	elif action == actions[1]: #'Загрузка таблиц индексации'
		if Indexing:
			yes = True
		else:
			yes = messagebox.askyesno('Внимание', 'В текущей секции индексация не проведена, игнорировать?')
		if 	yes:
			if Loading:
				yes = messagebox.askyesno('Внимание', 'В текущей секции загрузка индекс таблиц проведена, игнорировать?')
		if 	yes:
			try:
				with open('loader.py', "r", encoding="utf-8") as source_file:
					exec(source_file.read())
				Loading = True
				deff_item = 2
				messagebox.showinfo("Информация",'Загрузка индекс таблиц завершена')
			except Exception:
				Loading = False
				messagebox.showerror("Ошибка!", 'При загрузке индекс таблиц произошла ошибка')
	elif action == actions[2]: #'Обработка запроса'
		if Loading:
			with open('Query.py', "r", encoding="utf-8") as source_file:
					exec(source_file.read())
		else:
			messagebox.showwarning("Внимание",'Сначала произведите загрузку таблиц индексации')
exit()