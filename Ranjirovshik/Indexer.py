#выдает запрос на местоположение папки с текстовыми файлами, индексирует их и выдает запрос на место сохранения индекс файлов, сохраняет их
directory = QFileDialog.getExistingDirectory(None, 'выбор пути к папке с текстами', "C:\\Users\\Husim\\Desktop\\ucheba\\_progr\\Sbornik")
index_directory = QFileDialog.getExistingDirectory(None, 'выбор пути для сохранения индекс файлов', "C:\\Users\\Husim\\Desktop\\ucheba\\_progr\\Sbornik")
directory,index_directory=directory.strip(),index_directory.strip() #удаление пробелов вначале и в конце(возможно это лишнее)
#print(directory)
#удаление обратного слеша в конце(это тоже лишнее но пусть будет)
while directory.endswith('\\'):
	directory=directory[:-1]
while index_directory.endswith('\\'):
	index_directory=index_directory[:-1]
files = os.listdir(directory)#Получаем список файлов в переменную files
files = [file for file in files if file[-4:].lower() == '.txt'] #работаем только с форматом txt

def get_words(file, directory):
	"""Принимает кортеж (имя файла, путь к файлу) вернет кортеж (сортированный список слов из текста и каждое слово
	в списке 1 раз, соответствующий список количеств встреч слов в файле)"""
	with open(directory + '\\' + file, "r") as rfile:#открывает файл для чтения
		text = rfile.read()#помещает файл в строку
	words = text_to_words(text)
	if words != []:
		words.sort() #сортируем, чтобы одинаковые слова сбились в кучки
		#удаляем слова - пустые строки
		if words[0] == '':
			index_empty = 0
			for word in words:
				if word == '':
					index_empty+=1
				else:
					break
			words=words[index_empty:]
	if words != []:
		cou=[] #количества встреч слов в тексте до обработки пустой список
		wo=words[0] #подсчитываемое слово, сначала это первое слово из текста
		ind=[wo] #первое слово из текста добавляем в список слов
		n=0 #счетчик слов, считать не начали еще и он обнулен
		for w in words:
			if w != wo: #Если текущее слово не то которое подсчитываем
				wo=w #изменим подсчитываемое
				cou.append(n) #считаем другое слово, поэтому можно записать количество предудушего
				n=1 #одно слово уже есть
				ind.append(w) #добавим новое слово в список слов
			else:
				n+=1 #увеличим счетчик раз встретили тоже самое слово
		cou.append(n) #когда посмотрели на последнее слово нужно записать его количество
		return (ind, cou)
	else:
		return ([], [])
t1=time.time()
words_doc = dict() #пустой словарь
#structure words_doc = {word : [(number_file,count_word_in_file), ... ] , ... }
for ifile in range(len(files)): #для каждого интекса файлов из files
	ind,cou = get_words(files[ifile], directory)
	for iword in range(len(ind)):
		if ind[iword] in words_doc:
			words_doc[ind[iword]].append((ifile, cou[iword]))
		else:
			words_doc[ind[iword]]=[(ifile, cou[iword])]
print("получение словаря {слово:[(номер файла,частота слова в файле)]} заняло "+str(time.time() - t1)+" сек.")
#t1=time.time()
# def frequency_to_weight(words_doc):
	# """Преобразовывает частоты в веса"""
	# words = words_doc.keys() #получаем список всех слов
	# words_counts = [] #список количеств слов во всех текстах
	# for wd in words: #для каждого слова из списка слов
		# k=len(words_counts) #индекс добавленного в конец элемента равен длинне списка до добавления
		# words_counts.append(0) #добавляем ноль в конец списка
		# for tuple in words_doc[wd]: # для каждого кортежа из списка кортежей
			# words_counts[k] += tuple[1] #суммируем все частоты для конкретного слова wd в последнем элементе списка words_counts
		# for n in range(len(words_doc[wd])): #заменяем частоты весами
			# words_doc[wd][n]=(words_doc[wd][n][0], words_doc[wd][n][1]/(1 + words_counts[k] - words_doc[wd][n][1]))
	# return words_doc
#words_doc = frequency_to_weight(words_doc)
#print("перевод частот в веса " + str(time.time() - t1) + " сек.")
t2=time.time()
for wkey in words_doc: #сортируем списки по убыванию частот
	words_doc[wkey].sort(key=lambda x:x[1], reverse=True)
print("сортировка списков в словаре заняла " + str(time.time() - t2) + " сек.")
t3=time.time()
def save_data_to_csv(path, files, directory, words_doc):
	"""Сохраняет в файл список файлов(при извлечении обязательно убрать 1 элемент, это путь к файлам) и словарь списков,
	также рядом с приставкой _index файл, с начальными позицыями для списков кортежей"""
	with open(path + "\\" + "baze.csv", "w", encoding="utf-8") as wfile: #открывает файл для записи
		wfile.write(';'.join([directory] + [file for file in files]) + '\n') #записываем путь к файлам, названия файлов
		wfile.write(';'.join(words_doc.keys()) + '\n') #записываем список слов
		index = []
		for lst in words_doc.values(): #записываем списки весов
			index.append(str(wfile.tell())) #запоминаем позицию в файле
			str_row=[]
			for ftuple in lst:
				str_row.append(str(ftuple[0]))
				str_row.append(str(ftuple[1]))
			wfile.write(';'.join(str_row) + '\n')
	with open(path + "\\" + "index.csv", "w", encoding="utf-8") as hfile: #открывает файл для записи
		hfile.write(';'.join(index) + '\n') #записываем индексы
	return
save_data_to_csv(index_directory, files, directory, words_doc)
print("сохранение базы index таблиц заняло " + str(time.time() - t3) + " сек.")
