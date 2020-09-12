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
class WriteFile:

    # Nesne nin başlatılması
    def __init__(self, filename:str):
        self.filename=filename

    # Dosyaya bayt olarak ekleme yap
    def appendByte(self, data:bytes):
        with open(file=self.filename, mode='ab') as file:
            file.write(data)
            file.flush()

    # Dosyaya string olarak ekleme yap
    def appendStr(self, data:str, encoding='utf-8'):
        with open(file=self.filename, mode='a' , encoding=encoding) as file:
            file.write(data)
            file.flush()

    # Dosyayı sil. Dosyaya bayt olarak yaz.
    def writeByte(self, data:bytes):
        with open(file=self.filename, mode='wb') as file:
            file.write(data)
            file.flush()

    # Dosyayı sil. Dosyaya string olarak yaz
    def writeStr(self, data:str):
        with open(file=self.filename, mode='w') as file:
            file.write(data)
            file.flush()
