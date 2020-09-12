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
from  lib.image.jpg.data_calculate.BigUnsignedLength import BigUnsignedLength as clength
from lib.hexlib.ShowHex import show2HexBytes as s2hex


# JFIF Extension Class
class JFXX:
    # JFXX Olup Olmadığını Kontrol Etmek İçin
    # statik bir fonksiyon
    @staticmethod
    def check(bytesData: bytes) -> bool:
        if len(bytesData) > 8:
            return bytesData[4:9] == b'JFXX\x00'
        else:
            return False
    #
    def __init__(self, bytesData:bytes ):
        self.s0_app_marker = bytesData[0:2]
        self.s1_app_length = bytesData[2:4]
        self.s2_jfxx_marker = bytesData[4:9]
        self.s3_jfxx_thumbnail_format = bytesData[9:10]
        if len(bytesData)>10:
            self.s4_jfxx_thumbnail_data = bytesData[10:]
        else:
            self.s4_jfxx_thumbnail_data = b''
    #
    def version(self):
        return 'JFIF Extension (JFXX)'

    #
    def showVersion(self):
        print('\t'+self.version())

    #
    def showAll(self):
        txt1_format = "\t{:<21} : '{}'   {}"
        txt1_tmp1 = "(-" + Kind.findType(bytesData=self.s0_app_marker).shortname + "-)"
        txt1 = txt1_format.format('App Marker', self.s0_app_marker.hex(sep=' '),txt1_tmp1 )
        txt2_tmp1 = '('+str(clength(data=self.s1_app_length))+' bayt)'
        txt2 = txt1_format.format('App Length', self.s1_app_length.hex(sep=' '),txt2_tmp1)
        txt3 = txt1_format.format('JFXX Marker', self.s2_jfxx_marker.hex(sep=' '), "'JFXX\\x00'")

        if self.s3_jfxx_thumbnail_format == b'10':
            txt4_tmp1 = '(-JPEG format-)'
        elif self.s3_jfxx_thumbnail_format == b'11':
            txt4_tmp1 = '(-1 byte per pixel palettized format-)'
        elif self.s3_jfxx_thumbnail_format == b'13':
            txt4_tmp1 = '(-3 byte per pixel RGB format-)'
        else:
            txt4_tmp1 = '(?)'
        txt4 = txt1_format.format('JFXX Thumbnail Format', self.s3_jfxx_thumbnail_format.hex(), txt4_tmp1)

        print(txt1)
        print(txt2)
        print(txt3)
        print(txt4)
        s2hex(dataBytes=self.s4_jfxx_thumbnail_data, dataName="'JFXX Thumbnail Data'", columnSize=20)

    #
    def all(self) -> str:
        txt1_format = "\t{:<21} : '{}'   {}\n"
        txt1_tmp1 = "(-" + Kind.findType(bytesData=self.s0_app_marker).shortname + "-)"
        txt1 = txt1_format.format('App Marker', self.s0_app_marker.hex(sep=' '),txt1_tmp1 )
        txt2_tmp1 = '('+str(clength(data=self.s1_app_length))+' bayt)'
        txt2 = txt1_format.format('App Length', self.s1_app_length.hex(sep=' '),txt2_tmp1)
        txt3 = txt1_format.format('JFXX Marker', self.s2_jfxx_marker.hex(sep=' '), "'JFXX\\x00'")

        if self.s3_jfxx_thumbnail_format == b'10':
            txt4_tmp1 = '(-JPEG format-)'
        elif self.s3_jfxx_thumbnail_format == b'11':
            txt4_tmp1 = '(-1 byte per pixel palettized format-)'
        elif self.s3_jfxx_thumbnail_format == b'13':
            txt4_tmp1 = '(-3 byte per pixel RGB format-)'
        else:
            txt4_tmp1 = '(?)'
        txt4 = txt1_format.format('JFXX Thumbnail Format', self.s3_jfxx_thumbnail_format.hex(), txt4_tmp1)
        thumbnail_length = len(self.s4_jfxx_thumbnail_data)
        txt2_format = "\t{:<21} : '{}"
        txt5 = ''
        for kk in range(0,thumbnail_length):
            if kk%10 == 0:
                if kk==0:
                    txt5 = txt2_format.format('JFIF Thumbnail Data',self.s4_jfxx_thumbnail_data[kk:kk+1].hex() )
                else:
                    txt5 += "'\n"+txt2_format.format('',self.s4_jfxx_thumbnail_data[kk:kk+1].hex() )
            else:
                txt5 += ' ' + self.s4_jfxx_thumbnail_data[kk:kk+1].hex()
            if kk == thumbnail_length-1:
                txt5 += "'"

        result = txt1 + txt2 + txt3 + txt4 + txt5
        return  result



    #
    def show(self):
        txt1_format = "\t{:<21} : '{}'   {}"
        txt1_tmp1 = "(-" + Kind.findType(bytesData=self.s0_app_marker).shortname + "-)"
        txt1 = txt1_format.format('App Marker', self.s0_app_marker.hex(sep=' '),txt1_tmp1 )
        txt2_tmp1 = '('+str(clength(data=self.s1_app_length))+' bayt)'
        txt2 = txt1_format.format('App Length', self.s1_app_length.hex(sep=' '),txt2_tmp1)
        txt3 = txt1_format.format('JFXX Marker', self.s2_jfxx_marker.hex(sep=' '), "'JFXX\\x00'")
        if self.s3_jfxx_thumbnail_format == b'10':
            txt4_tmp1 = '(-JPEG format-)'
        elif self.s3_jfxx_thumbnail_format == b'11':
            txt4_tmp1 = '(-1 byte per pixel palettized format-)'
        elif self.s3_jfxx_thumbnail_format == b'13':
            txt4_tmp1 = '(-3 byte per pixel RGB format-)'
        else:
            txt4_tmp1 = '(?)'
        txt4 = txt1_format.format('JFXX Thumbnail Format', self.s3_jfxx_thumbnail_format.hex(), txt4_tmp1)
        print(txt1)
        print(txt2)
        print(txt3)
        print(txt4)