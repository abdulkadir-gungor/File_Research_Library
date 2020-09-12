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
from lib.image.jpg.data_calculate.BigUnsignedLength import BigUnsignedLength as clength
from lib.hexlib.ShowHex import show2HexBytes as s2hex
from lib.image.jpg.kind import Kind
class APPHEX:
    #
    #
    def __init__(self, bytesData:bytes):
        self.s0_app_marker = bytesData[0:2]
        self.s1_app_length = bytesData[2:4]
        self.s1_app_length_int = clength(data=self.s1_app_length)
        self.s2_all_data = bytesData

    def show(self, columSize:int=10, linesHalt:int=-1):
        txt1 ='\tApp Marker       : '  +  self.s0_app_marker.hex(sep=' ')  + "  '" + Kind.findType(self.s0_app_marker).shortname + "'"
        txt2 ='\tApp Length       : '  +  self.s1_app_length.hex(sep=' ')  + '  (' + str(self.s1_app_length_int) +' bayt)'
        print(txt1)
        print(txt2)
        print("")
        s2hex(dataBytes=self.s2_all_data, dataName=Kind.findType(self.s0_app_marker).shortname, columnSize=columSize, linesHalt=linesHalt)

