#Если этот файл исполняется значит должны быть известны path,directory,files,words,index
def get_reit_dict(word, words, index_list, path):
	"""Вернет словарь {файл : количество слова в нем}"""
	with open(path + "\\" + 'baze.csv', "r", encoding="utf-8") as file: #открывает файл для чтения
		if word in words:
			file.seek(int(index_list[words.index(word)]))
			lst = file.readline().split(';')
			# в последнем элементе списка нужно удалить знак конца строки
			ind_end_el = len(lst)
			if ind_end_el == 0:
				dictonary = dict()
			else:
				ind_end_el = ind_end_el - 1
				lst[ind_end_el]=lst[ind_end_el][:-1]
				dictonary = { int(lst[i]) : float(lst[i+1]) for i in range(0, len(lst), 2)}
		else:
			dictonary = dict()
	return dictonary
# промежуточная задача:
# есть список слов lst
# для каждого слова из списка есть словарь dict_from_word {номер_файла : частота_слова_в_нем}
# получить сортированный по убыванию словарь dict_lst {номер_файла : сумма_частот_слов_из_lst_в_этом_файле}
# решение:
# создать пустой словарь dict_lst
# перебрать все слова из lst
	# для каждого слова перебирать соответствующие словари dict_from_word
		# проверять есть ли номер_файла в dict_lst
			# если есть то увеличивать соответствующее ему значение на значение из dict_from_word
			# иначе добавить элемент
# преобразовать словарь в список кортежей (key,value)
# отсортировать кортежи по убыванию второго параметра
def ranking(lst_words, words, index_list, path, get_dict=get_reit_dict):
	"""Вернет список кортежей [(номер_файла), сумма весов слов из lst_words в этом файле] отсортированный по убыванию сумм весов"""
	dict_lst=dict()
	for word in lst_words:
		dict_from_word = get_dict(word, words, index_list, path)
		for number_file in dict_from_word:
			if number_file in dict_lst:
				dict_lst[number_file] += dict_from_word[number_file]
			else:
				dict_lst[number_file] = dict_from_word[number_file]
	return sorted(dict_lst.items(), key=lambda x : x[1], reverse = True)

Qwery,pressed_OK = QInputDialog.getText(None, "Ввод запроса","Введите запрос для ранжирования текстов")
if pressed_OK and Qwery != "":
	lst_words = text_to_words(Qwery)
else:
	lst_words = []

if lst_words != []:
	lst_words.sort() #сортируем, чтобы одинаковые слова сбились в кучки
	#удаляем слова - пустые строки
	if lst_words[0] == '':
		index_empty = 0
		for word in lst_words:
			if word == '':
				index_empty+=1
			else:
				break
		lst_words=lst_words[index_empty:]

if lst_words != []:
	t=time.time()
	os.system('cls')
	print('ранжирование для слов:',end=' ')
	for word in lst_words:
		print(word,end=' ')
	print()
	rankin_lst=ranking(lst_words, words, index, path)
	print('Слова запроса встречаются в ' + str(len(rankin_lst)) + ' файлах')
	print("Обработка запроса заняла "+str(time.time() - t)+" сек.")
	for number_file, weit in rankin_lst[:10]: #Выводить будем только первые 10 значений
		print(files[number_file] + '  ' + str(weit))
else:
	messagebox.showwarning("Внимание",'Введенная строка запроса не содержит допустимых слов')