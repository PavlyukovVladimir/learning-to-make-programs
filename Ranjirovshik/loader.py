#from sys import argv as param #для параметров командной строки
#from PyQt5.QtWidgets import QFileDialog,QApplication #стандартные диалоги
#add = QApplication(param) #создания экземпляра этого класса методы QFileDialog не работают
def Load_data_index_from_csv():
	"""Запросит местоположение и загружает из файла baze.csv (список слов, индексов и файлов), а индексы из "index.csv", вернет (путь к файлам, имена файлов, список слов, индексы)"""
	path=QFileDialog.getExistingDirectory(None,'выбор пути к папке с индекс файлами','D:\\ind')
	with open(path + "\\" + 'baze.csv', "r", encoding="utf-8") as file: #открывает файл для чтения
		files = file.readline().split(';')
		words = file.readline().split(';')
	with open(path + "\\" + "index.csv", "r", encoding="utf-8") as file: #открывает файл для чтения
		sindex = file.readline().split(';')
	# удалить знак конца строки в конце последних элементов словарей
	ind_end_word = len(words) - 1
	words[ind_end_word]=words[ind_end_word][:-1]
	sindex[ind_end_word]=sindex[ind_end_word][:-1]
	ind_end_file=len(files) - 1
	files[ind_end_file]=files[ind_end_file][:-1]
	index=[]
	for si in sindex:
		index.append(float(si))
	return (path, files[0], files[1:], words, index)
path,directory,files,words,index = Load_data_index_from_csv()