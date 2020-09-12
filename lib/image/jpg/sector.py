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
from lib.image.jpg.kind import Kind

class Sector:
    def __init__(self, item:object=None):
        if item == None:
            self.no = 0
            self.root = 0
            self.start = 0
            self.end = 0
            self.applistno = -1
            self.type = Kind()
        else:
            self.no = item.no
            self.root = item.root
            self.start = item.start
            self.end = item.end
            self.applistno = item.applistno
            self.type = Kind(item=item.type)