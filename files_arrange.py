# -*- coding: utf-8 -*-

import os
import shutil
import time
import zipfile


class SorterFiles:
    """Script for organizing files

    The script decomposes files from one
    folders (zip_archive - no preliminary
    unzip) by year and month to another.

        Input parameters:
    folder_name ----------- folder to scan,
    where_to_copy --------- target folder.
        start work script
    .sorter() ------------- start_work
    """

    def __init__(self, folder_name, where_to_copy):
        self.folder_name = folder_name
        self.where_to_copy = where_to_copy

    def sorter_zip(self):
        zip_file = self.folder_name
        zfile = zipfile.ZipFile(zip_file)
        file_info_list = zfile.infolist()
        for content in file_info_list:
            name, date = content.filename, content.date_time
            if name.endswith('/'):
                continue
            directory = self.create_directory_zip(date)
            content.filename = os.path.basename(content.filename)
            zfile.extract(content, directory)
        zfile.close()

    def create_directory_zip(self, date):
        sorted = self.where_to_copy
        if date[1] < 10:
            date_mon = '0' + str(date[1])
        else:
            date_mon = str(date[1])
        date_year = str(date[0])
        directory = os.path.join(sorted, date_year, date_mon)
        return directory

    def sorter_folder(self):
        file_name = self.folder_name
        for dir_file, dir_name, files in os.walk(file_name):
            for file in files:
                dir = os.path.join(dir_file, file)
                date_creat = os.path.getctime(dir)
                date_creat = time.gmtime(date_creat)
                directory = self.create_directory(date_creat)
                shutil.copy2(dir, directory)

    def create_directory(self, date):
        new_folder = self.where_to_copy
        directory = os.path.join(new_folder, str(date[0]), str(date[1]))
        if os.path.isdir(directory):
            pass
        else:
            os.makedirs(directory)
        return directory

    def sorter(self):
        if self.folder_name[-4:] == '.zip':
            self.sorter_zip()
        else:
            self.sorter_folder()


# a = Sorter(file_name='icons', where_to_copy='New')
# a.sorter()
