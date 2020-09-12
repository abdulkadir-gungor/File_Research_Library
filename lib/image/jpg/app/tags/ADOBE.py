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


class ADOBE:
    #
    @staticmethod
    def check( bytesData:bytes ) -> bool:
        if len(bytesData)>=10 :
            if bytesData[4:10] == b'Adobe\x00':
                return True
        return False
    #
    def __init__(self, bytesData: bytes):
        self.s0_app_marker = bytesData[0:2]
        self.s1_app_length = bytesData[2:4]
        self.s1_app_length_int = clength(data=self.s1_app_length)
        self.s2_adobe_marker = bytesData[4:10]
        self.s2_adobe_marker_str = 'Adobe\\00'
        self.s3_all_data = bytesData
    #
    def version(self):
        return 'ADOBE'
    #
    def showVersion(self):
        print( '\t'+self.version() )
    #
    def show(self):
        txt1 ='\tApp Marker       : '  +  self.s0_app_marker.hex(sep=' ')  + "  '" + Kind.findType(self.s0_app_marker).shortname + "'"
        txt2 ='\tApp Length       : '  +  self.s1_app_length.hex(sep=' ')  + '  (' + str(self.s1_app_length_int) +' bayt)'
        txt3 ='\tAdobe Marker     : '  + self.s2_adobe_marker.hex(sep=' ') + "  '" + self.s2_adobe_marker_str + "'"
        print(txt1)
        print(txt2)
        print(txt3)
        if len(self.s3_all_data) >= 12:
            txt4 = '\tAdobe Starter    : '  + self.s3_all_data[10:12].hex(sep=' ') + "  '" + self.s3_all_data[10:11].hex() + " Bit - ("+self.s3_all_data[11:12].hex() + ")'"
            print(txt4)
        if len(self.s3_all_data) >= 16:
            txt5 = '\tAdobe Data       : ' + self.s3_all_data[12:16].hex(sep=' ')
            print(txt5)
        print()
        s2hex(dataBytes=self.s3_all_data , dataName=Kind.findType(self.s0_app_marker).shortname, columnSize=20)

    #
    def showHeader(self):
        txt1 ='\tApp Marker       : '  +  self.s0_app_marker.hex(sep=' ')  + "  '" + Kind.findType(self.s0_app_marker).shortname + "'"
        txt2 ='\tApp Length       : '  +  self.s1_app_length.hex(sep=' ')  + '  (' + str(self.s1_app_length_int) +' bayt)'
        txt3 ='\tAdobe Marker     : '  + self.s2_adobe_marker.hex(sep=' ') + "  '" + self.s2_adobe_marker_str + "'"
        print(txt1)
        print(txt2)
        print(txt3)
        if len(self.s3_all_data) >= 12:
            txt4 = '\tAdobe Starter    : '  + self.s3_all_data[10:12].hex(sep=' ') + "  '" + self.s3_all_data[10:11].hex() + " Bit - ("+self.s3_all_data[11:12].hex() + ")'"
            print(txt4)
        if len(self.s3_all_data) >= 16:
            txt5 = '\tAdobe Data       : ' + self.s3_all_data[12:16].hex(sep=' ')
            print(txt5)