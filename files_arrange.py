# -*- coding: utf-8 -*-

import os, time, shutil, zipfile


# Нужно написать скрипт для упорядочивания фотографий (вообще любых файлов)
# Скрипт должен разложить файлы из одной папки по годам и месяцам в другую.
# Например, так:
#   исходная папка
#       icons/cat.jpg
#       icons/man.jpg
#       icons/new_year_01.jpg
#   результирующая папка
#       icons_by_year/2018/05/cat.jpg
#       icons_by_year/2018/05/man.jpg
#       icons_by_year/2017/12/new_year_01.jpg
#
# Входные параметры основной функции: папка для сканирования, целевая папка.
# Имена файлов в процессе работы скрипта не менять, год и месяц взять из времени создания файла.
# Обработчик файлов делать в обьектном стиле - на классах.
#
# Файлы для работы взять из архива icons.zip - раззиповать проводником в папку icons перед написанием кода.
# Имя целевой папки - icons_by_year (тогда она не попадет в коммит)
#
# Пригодятся функции:
#   os.walk
#   os.path.dirname
#   os.path.join
#   os.path.normpath
#   os.path.getmtime
#   time.gmtime
#   os.makedirs
#   shutil.copy2
#
# Чтение документации/гугла по функциям - приветствуется. Как и поиск альтернативных вариантов :)
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Основная функция должна брать параметром имя zip-файла и имя целевой папки.
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828


class Sorter:

    def __init__(self, file_name):
        self.file_name = file_name

    def sorter_zip(self):
        zip_file = 'icons.zip'
        zfile = zipfile.ZipFile(zip_file)
        file_info_list = zfile.infolist()
        for content in file_info_list:
            name, date = content.filename, content.date_time
            if name.endswith('/'):
                continue
            directory = self.create_directory_zip(date)
            content.filename = os.path.basename(content.filename)
            zfile.extract(content, directory)

    def create_directory_zip(self, date):
        sorted = 'sorted'
        if date[1] < 10:
            date_mon = '0' + str(date[1])
        else:
            date_mon = str(date[1])
        date_year = str(date[0])
        directory = os.path.join(sorted, date_year, date_mon)
        return directory

    # def sorter(self):
    #     file_name = 'sorted'


a = Sorter(file_name='icons.zip')
a.sorter_zip()
