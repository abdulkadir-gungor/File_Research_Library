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

# Verilen index değerleri arasını dosyadan oku
def readIndexBytes(filename:str, startIndex:int, stopIndex:int) -> bytes:
    with open(file=filename, mode='rb') as file:
        file_end = file.seek(0,2)
        if startIndex > file_end:
            return b''
        else:
            if stopIndex > file_end:
                stopIndex = file_end
            read_buffer = stopIndex - startIndex
            file.seek(startIndex,0)
            data = file.read(read_buffer)
            if data:
                return data
            else:
                return b''

# Dosyayı baştan sona oku
def readBytes(filename:str) -> bytes:
    with open(file=filename, mode='rb') as file:
        file_seek_end = file.seek(0,2)
        if file_seek_end > 0:
            file.seek(0,0)
            return file.read()