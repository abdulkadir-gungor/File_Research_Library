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
from lib.image.jpg.kind import Kind
from lib.hexlib.ShowUTF import showUTF8Bytes as sutf8
from lib.hexlib.ShowUTF import showUTF16BEBytes as sutf16be
from lib.hexlib.ShowUTF import showUTF16LEBytes as sutf16le
from lib.hexlib.ShowUTF import showUTF32BEBytes as sutf32be
from lib.hexlib.ShowUTF import showUTF32BEBytes as suft32le

#
# XMP Definition
# XMP Class
class XMP:
    #
    @staticmethod
    def check( bytesData:bytes ) -> bool:
        if len(bytesData)>33 :
            if bytesData[4:33] == b'http://ns.adobe.com/xap/1.0/\x00':
                return True
        return False
    #
    def __init__(self, bytesData: bytes):
        self.s0_app_marker = bytesData[0:2]
        self.s1_app_length = bytesData[2:4]
        self.s1_app_length_int = clength(data=self.s1_app_length)
        self.s2_xmp_marker = bytesData[4:33]
        self.s2_xmp_marker_str = 'http://ns.adobe.com/xap/1.0/\\x00'
        self.s3_xmp_encoding_bytes   = b''
        self.s3_xmp_encoding_int     = -1
        self.s3_xmp_encoding_hex_str = ''
        self.s3_xmp_encoding_str = ''
        self.s4_xmp_data = bytesData[33:]
        self.encoding()
    #
    def showHeader(self):
        txt1 ='\tApp Marker       : '  +  self.s0_app_marker.hex(sep=' ')  + "  '" + Kind.findType(self.s0_app_marker).shortname + "'"
        txt2 ='\tApp Length       : '  +  self.s1_app_length.hex(sep=' ')  + '  (' + str(self.s1_app_length_int) +' bayt)'
        txt3 ='\tXMP Marker (Hex) : '  +  self.s2_xmp_marker.hex(sep=' ')
        txt4 ='\tXMP Marker (Str) : "' + self.s2_xmp_marker_str + '"'
        txt5 ='\tXMP Encoding     : ' + self.s3_xmp_encoding_str

        print(txt1)
        print(txt2)
        print(txt3)
        print(txt4)
        print(txt5)

    def show(self):
        txt1 ='\tApp Marker       : '  +  self.s0_app_marker.hex(sep=' ')  + "  '" + Kind.findType(self.s0_app_marker).shortname + "'"
        txt2 ='\tApp Length       : '  +  self.s1_app_length.hex(sep=' ')  + '  (' + str(self.s1_app_length_int) +' bayt)'
        txt3 ='\tXMP Marker (Hex) : '  +  self.s2_xmp_marker.hex(sep=' ')
        txt4 ='\tXMP Marker (Str) : "' + self.s2_xmp_marker_str + '"'
        txt5 ='\tXMP Encoding     : ' + self.s3_xmp_encoding_str

        print(txt1)
        print(txt2)
        print(txt3)
        print(txt4)
        print(txt5)
        print("")
        #
        if self.s3_xmp_encoding_int == 1:
            sutf8( bytesData=self.s4_xmp_data.replace(self.s3_xmp_encoding_bytes, b'0xEF 0xBB 0xBF'), columnSize=50 )
        elif self.s3_xmp_encoding_int == 2:
            sutf16be( bytesData=self.s4_xmp_data.replace(self.s3_xmp_encoding_bytes, b'0xFE 0xFF'), columnSize=50  )
        elif self.s3_xmp_encoding_int == 3:
            sutf16le( bytesData=self.s4_xmp_data.replace(self.s3_xmp_encoding_bytes, b'0xFF 0XFE'), columnSize=50 )
        elif self.s3_xmp_encoding_int == 4:
            sutf32be(bytesData=self.s4_xmp_data.replace(self.s3_xmp_encoding_bytes, b'0x00 0x00 0xFE 0XFF'), columnSize=50 )
        elif self.s3_xmp_encoding_int == 5:
            suft32le(bytesData=self.s4_xmp_data.replace(self.s3_xmp_encoding_bytes, b'0xFF 0XFE 0x00 0x00'), columnSize=50 )
        else:
            print('\tData Encoding Unknown')
    #
    def showParams(self, columnSize=50, linesHalt=-1):
        txt1 ='\tApp Marker       : '  +  self.s0_app_marker.hex(sep=' ')  + "  '" + Kind.findType(self.s0_app_marker).shortname + "'"
        txt2 ='\tApp Length       : '  +  self.s1_app_length.hex(sep=' ')  + '  (' + str(self.s1_app_length_int) +' bayt)'
        txt3 ='\tXMP Marker (Hex) : '  +  self.s2_xmp_marker.hex(sep=' ')
        txt4 ='\tXMP Marker (Str) : "' + self.s2_xmp_marker_str + '"'
        txt5 ='\tXMP Encoding     : ' + self.s3_xmp_encoding_str

        print(txt1)
        print(txt2)
        print(txt3)
        print(txt4)
        print(txt5)
        print("")
        #
        if self.s3_xmp_encoding_int == 1:
            sutf8( bytesData=self.s4_xmp_data.replace(self.s3_xmp_encoding_bytes, b'0xEF 0xBB 0xBF'), columnSize=columnSize, linesHalt=linesHalt )
        elif self.s3_xmp_encoding_int == 2:
            sutf16be( bytesData=self.s4_xmp_data.replace(self.s3_xmp_encoding_bytes, b'0xFE 0xFF'), columnSize=columnSize, linesHalt=linesHalt )
        elif self.s3_xmp_encoding_int == 3:
            sutf16le( bytesData=self.s4_xmp_data.replace(self.s3_xmp_encoding_bytes, b'0xFF 0XFE'), columnSize=columnSize, linesHalt=linesHalt )
        elif self.s3_xmp_encoding_int == 4:
            sutf32be(bytesData=self.s4_xmp_data.replace(self.s3_xmp_encoding_bytes, b'0x00 0x00 0xFE 0XFF'), columnSize=columnSize, linesHalt=linesHalt )
        elif self.s3_xmp_encoding_int == 5:
            suft32le(bytesData=self.s4_xmp_data.replace(self.s3_xmp_encoding_bytes, b'0xFF 0XFE 0x00 0x00'), columnSize=columnSize, linesHalt=linesHalt )
        else:
            print('\tData Encoding Unknown')

    #
    def encoding(self):
        #
        if self.s4_xmp_data[17:20] == b'\xef\xbb\xbf':
            self.s3_xmp_encoding_bytes = b'\xef\xbb\xbf'
            self.s3_xmp_encoding_hex_str = 'ef bb bf'
            self.s3_xmp_encoding_str = 'UTF-8'
            self.s3_xmp_encoding_int = 1
        elif self.s4_xmp_data[17:19] == b'\xfe\xff':
            self.s3_xmp_encoding_bytes = b'\xfe\xff'
            self.s3_xmp_encoding_hex_str = 'fe ff'
            self.s3_xmp_encoding_str  = 'UTF-16 (BE)'
            self.s3_xmp_encoding_int = 2
        elif self.s4_xmp_data[17:19] == b'\xff\xfe':
            self.s3_xmp_encoding_bytes =b'\xff\xfe'
            self.s3_xmp_encoding_hex_str = 'ff fe'
            self.s3_xmp_encoding_str  = 'UTF-16 (LE)'
            self.s3_xmp_encoding_int = 3
        elif self.s4_xmp_data[17:21] == b'\x00\x00\xfe\xff':
            self.s3_xmp_encoding_bytes =b'\x00\x00\xfe\xff'
            self.s3_xmp_encoding_hex_str = '00 00 fe ff'
            self.s3_xmp_encoding_str  = 'UTF-32 (BE)'
            self.s3_xmp_encoding_int = 4
        elif self.s4_xmp_data[17:21] == b'\xff\xfe\x00\x00':
            self.s3_xmp_encoding_bytes =b'\xff\xfe\x00\x00'
            self.s3_xmp_encoding_hex_str = 'ff fe 00 00'
            self.s3_xmp_encoding_str  = 'UTF-32 (LE)'
            self.s3_xmp_encoding_int = 5
        else:
            self.s3_xmp_encoding_str = 'UNKNOWN'
            self.s3_xmp_encoding_int = -1