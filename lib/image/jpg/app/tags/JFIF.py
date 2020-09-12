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
from lib.hexlib.ShowHex import show2HexBytes as s2hex
from  lib.image.jpg.data_calculate.BigUnsignedLength import BigUnsignedLength as clength
from lib.image.jpg.kind import Kind


# JFIF Class
class JFIF:
    # JFIF Olup Olmadığını Kontrol Etmek İçin
    # statik bir fonksiyon
    @staticmethod
    def check( bytesData:bytes ) -> bool:
        if len(bytesData) > 8:
            return bytesData[4:9] == b'JFIF\x00'
        else:
            return False

    #
    def __init__(self, bytesData:bytes ):
        self.s0_app_marker = bytesData[0:2]
        self.s1_app_length = bytesData[2:4]
        self.s2_jfif_marker = bytesData[4:9]
        self.s3_jfif_version_1_major = bytesData[9:10]
        self.s3_jfif_version_2_minor = bytesData[10:11]
        self.s4_jfif_density_units = bytesData[11:12]
        self.s5_jfif_xdensity = bytesData[12:14]
        self.s6_jfif_ydensity = bytesData[14:16]
        self.s7_jfif_xthumbnail = bytesData[16:17]
        self.s8_jfif_ythumbnail = bytesData[17:18]
        if len(bytesData) > 18:
            self.s9_jfif_thumbnaildata = bytesData[18:]
        else:
            self.s9_jfif_thumbnaildata = b''

    #
    def version(self) ->str:
        return 'JFIF '+str(ord(self.s3_jfif_version_1_major))+'.'+str(ord(self.s3_jfif_version_2_minor))
    #
    def showVersion(self):
        print('\t'+self.version())
    #
    def showAll(self):
        txt1_format = "\t{:<20} : '{}'   {}"
        txt1_tmp1 = "(-"+Kind.findType(bytesData=self.s0_app_marker).shortname+"-)"
        txt1 = txt1_format.format('App Marker', self.s0_app_marker.hex(sep=' '),txt1_tmp1 )
        txt2_tmp1 = '('+str(clength(data=self.s1_app_length))+' bayt)'
        txt2 = txt1_format.format('App Length', self.s1_app_length.hex(sep=' '),txt2_tmp1)
        txt3 = txt1_format.format('JFIF Marker', self.s2_jfif_marker.hex(sep=' '),"'JFIF\\x00'" )
        txt4_tmp1 = self.s3_jfif_version_1_major.hex()+' '+self.s3_jfif_version_2_minor.hex()
        txt4_tmp2 = '('+ str(ord(self.s3_jfif_version_1_major))+'.'+str(ord(self.s3_jfif_version_2_minor)) +')'
        txt4 = txt1_format.format('JFIF Version', txt4_tmp1, txt4_tmp2)
        if self.s4_jfif_density_units.lower() == '00':
            txt5_tmp1 = '(-No Units:::Pixel Aspect Ratio-)'
        elif self.s4_jfif_density_units.hex().lower() == '01':
            txt5_tmp1 = '(-Pixels Per Inch [2.54 cm]-)'
        elif self.s4_jfif_density_units.hex().lower() == '02':
            txt5_tmp1 ='(-Pixels Per Centimeter-)'
        else:
            txt5_tmp1 = '(?)'
        txt5 = txt1_format.format('JFIF Density Units',self.s4_jfif_density_units.hex(),txt5_tmp1)
        txt6 = txt1_format.format('JFIF X Density', self.s5_jfif_xdensity.hex(sep=' '),'')
        txt7 = txt1_format.format('JFIF Y Density', self.s6_jfif_ydensity.hex(sep=' '), '')
        txt8 = txt1_format.format('JFIF X Thumbnail', self.s7_jfif_xthumbnail.hex(sep=' '), '')
        txt9 = txt1_format.format('JFIF Y Thumbnail', self.s8_jfif_ythumbnail.hex(sep=' '), '')
        print(txt1)
        print(txt2)
        print(txt3)
        print(txt4)
        print(txt5)
        print(txt6)
        print(txt7)
        print(txt8)
        print(txt9)
        s2hex(dataBytes=self.s9_jfif_thumbnaildata, dataName="'JFIF Thumbnail Data'", columnSize=20)
    #
    def all(self) -> str:
        txt1_format = "\t{:<20} : '{}'   {}"
        txt1_tmp1 = "(-"+Kind.findType(bytesData=self.s0_app_marker).shortname+"-)\n"
        txt1 = txt1_format.format('App Marker', self.s0_app_marker.hex(sep=' '),txt1_tmp1 )
        txt2_tmp1 = '('+str(clength(data=self.s1_app_length))+' bayt)\n'
        txt2 = txt1_format.format('App Length', self.s1_app_length.hex(sep=' '),txt2_tmp1)
        txt3 = txt1_format.format('JFIF Marker', self.s2_jfif_marker.hex(sep=' '),"'JFIF\\x00'\n" )
        txt4_tmp1 = self.s3_jfif_version_1_major.hex()+' '+self.s3_jfif_version_2_minor.hex()
        txt4_tmp2 = '('+ str(ord(self.s3_jfif_version_1_major))+'.'+str(ord(self.s3_jfif_version_2_minor)) +')\n'
        txt4 = txt1_format.format('JFIF Version', txt4_tmp1, txt4_tmp2)
        if self.s4_jfif_density_units.lower() == '00':
            txt5_tmp1 = '(-No Units:::Pixel Aspect Ratio-)\n'
        elif self.s4_jfif_density_units.hex().lower() == '01':
            txt5_tmp1 = '(-Pixels Per Inch [2.54 cm]-)\n'
        elif self.s4_jfif_density_units.hex().lower() == '02':
            txt5_tmp1 ='(-Pixels Per Centimeter-)\n'
        else:
            txt5_tmp1 = '(?)\n'
        txt5 = txt1_format.format('JFIF Density Units',self.s4_jfif_density_units.hex(),txt5_tmp1)
        txt6 = txt1_format.format('JFIF X Density', self.s5_jfif_xdensity.hex(sep=' '),'\n')
        txt7 = txt1_format.format('JFIF Y Density', self.s6_jfif_ydensity.hex(sep=' '), '\n')
        txt8 = txt1_format.format('JFIF X Thumbnail', self.s7_jfif_xthumbnail.hex(sep=' '), '\n')
        txt9 = txt1_format.format('JFIF Y Thumbnail', self.s8_jfif_ythumbnail.hex(sep=' '), '\n')

        thumbnail_length = len(self.s9_jfif_thumbnaildata)
        txt2_format = "\t{:<20} : '{}"
        txt10 = ''
        for kk in range(0,thumbnail_length):
            if kk%10 == 0:
                if kk==0:
                    txt10 = txt2_format.format('JFIF Thumbnail Data',self.s9_jfif_thumbnaildata[kk:kk+1].hex() )
                else:
                    txt10 += "'\n"+txt2_format.format('',self.s9_jfif_thumbnaildata[kk:kk+1].hex() )
            else:
                txt10 += ' ' + self.s9_jfif_thumbnaildata[kk:kk+1].hex()
            if kk == thumbnail_length-1:
                txt10 += "'"

        result = txt1 + txt2 + txt3 + txt4 + txt5 + txt6 + txt7 + txt8 + txt9 + txt10
        return  result

    def show(self):
        txt1_format = "\t{:<20} : '{}'   {}"
        txt1_tmp1 = "(-"+Kind.findType(bytesData=self.s0_app_marker).shortname+"-)"
        txt1 = txt1_format.format('App Marker', self.s0_app_marker.hex(sep=' '),txt1_tmp1 )
        txt2_tmp1 = '('+str(clength(data=self.s1_app_length))+' bayt)'
        txt2 = txt1_format.format('App Length', self.s1_app_length.hex(sep=' '),txt2_tmp1)
        txt3 = txt1_format.format('JFIF Marker', self.s2_jfif_marker.hex(sep=' '),"'JFIF\\x00'" )
        txt4_tmp1 = self.s3_jfif_version_1_major.hex()+' '+self.s3_jfif_version_2_minor.hex()
        txt4_tmp2 = '('+ str(ord(self.s3_jfif_version_1_major))+'.'+str(ord(self.s3_jfif_version_2_minor)) +')'
        txt4 = txt1_format.format('JFIF Version', txt4_tmp1, txt4_tmp2)
        if self.s4_jfif_density_units.lower() == '00':
            txt5_tmp1 = '(-No Units:::Pixel Aspect Ratio-)'
        elif self.s4_jfif_density_units.hex().lower() == '01':
            txt5_tmp1 = '(-Pixels Per Inch [2.54 cm]-)'
        elif self.s4_jfif_density_units.hex().lower() == '02':
            txt5_tmp1 ='(-Pixels Per Centimeter-)'
        else:
            txt5_tmp1 = '(?)'
        txt5 = txt1_format.format('JFIF Density Units',self.s4_jfif_density_units.hex(),txt5_tmp1)
        txt6 = txt1_format.format('JFIF X Density', self.s5_jfif_xdensity.hex(sep=' '),'')
        txt7 = txt1_format.format('JFIF Y Density', self.s6_jfif_ydensity.hex(sep=' '), '')
        txt8 = txt1_format.format('JFIF X Thumbnail', self.s7_jfif_xthumbnail.hex(sep=' '), '')
        txt9 = txt1_format.format('JFIF Y Thumbnail', self.s8_jfif_ythumbnail.hex(sep=' '), '')
        print(txt1)
        print(txt2)
        print(txt3)
        print(txt4)
        print(txt5)
        print(txt6)
        print(txt7)
        print(txt8)
        print(txt9)