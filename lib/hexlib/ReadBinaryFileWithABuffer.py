#!/usr/bin/python3
############################################################################
#
#   © 2020 ABDULKADİR GÜNGÖR All Rights Reserved
#   Contact email address: abdulkadir_gungor@outlook.com
#
#	Developper:	Abdulkadir GÜNGÖR (abdulkadir_gungor@outlook.com)
#	Date:	08/2020
#	All Rights Reserved (Tüm Hakları Saklıdır)
#
############################################################################
class ReadBinaryFileWithABuffer:

    # Nesne nin başlatılması
    def __init__(self, filename:str, buffer:int=1024):
        self.filename=filename
        self.buffer=buffer
        self.file_seek_end = self.__file_end(file=filename)
        self.__seek_current = 0

    # Buffer değeri kadar imleçin kaldığı yerden oku
    def read(self)->bytes:
        data = b''
        if self.__seek_current < self.file_seek_end:
            with open(file=self.filename, mode='rb') as file:
                file.seek(self.__seek_current, 0)
                data = file.read(self.buffer)
                if not data:
                    data = b''
                check = self.getCurrent() + self.buffer
                if check < self.file_seek_end:
                    self.setCurrent(check)
                else:
                    self.setCurrent(self.file_seek_end)
        else:
            self.setCurrent(self.file_seek_end)
        return data

    # Index değerine git buffer değeri kadar oku
    def readIndex(self, index:int)->bytes:
        data = b''
        if index < self.file_seek_end:
            with open(file=self.filename, mode='rb') as file:
                file.seek(index, 0)
                data = file.read(self.buffer)
                if not data:
                    data = b''
            check = index + self.buffer
            if check < self.file_seek_end:
                self.setCurrent(check)
            else:
                self.setCurrent(self.file_seek_end)
        else:
            self.setCurrent(self.file_seek_end)
        return data

    # Konumu öğren
    def getCurrent(self) -> int:
        return  self.__seek_current

    # Konumu istediğin yere ata
    def setCurrent(self , seek:int):
        self.__seek_current = seek

    # Okurken konumu başa al
    def resetRead(self):
        self.__seek_current=0

    # Nesneyi yeniden kullanmaya izin veren fonksiyon
    def reset(self, filename:str, buffer:int=1024):
        self.filename=filename
        self.buffer=buffer
        self.file_seek_end = self.__file_end(file=filename)
        self.__seek_current = 0

    # Özel Statik Method
    # Dosya Sonunu öğrenmek için
    @staticmethod
    def __file_end (file:str) -> int:
        with open(file=file, mode='rb') as file:
            result=file.seek(0,2)
        return result
