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
from lib.image.jpg.data_calculate.LittleUnsignedLength import LittleUnsignedLength as llength
from lib.image.jpg.data_calculate.BigUnsignedLength import BigUnsignedLength as blength
from lib.hexlib.ShowHex import show2HexBytes as s2hex
from lib.image.jpg.kind import Kind

class MPF:
    #
    @staticmethod
    def check( bytesData:bytes ) -> bool:
        if len(bytesData)>8 :
            if bytesData[4:8] == b'MPF\x00':
                return True
        return False
    #
    def __init__(self, bytesData: bytes):
        self.s0_app_marker = bytesData[0:2]
        self.s1_app_length = bytesData[2:4]
        self.s1_app_length_int = blength(self.s1_app_length)
        self.s2_mpf_marker = bytesData[4:8]
        self.s2_mpf_marker_str = 'MPF\\00'
        self.s3_mpf_byte_order = bytesData[8:10]
        if self.s3_mpf_byte_order == b'MM':
            self.s3_mpf_byte_order_int = 1
            self.s3_mpf_byte_order_str = 'Big Endian'
        elif self.s3_mpf_byte_order == b'II':
            self.s3_mpf_byte_order_int = 2
            self.s3_mpf_byte_order_str ='Little Endian'
        else:
            self.s3_mpf_byte_order_int = -1
            self.s3_mpf_byte_order_str = 'Unknown'
        self.s4_mpf_version = bytesData[10:12]
        self.s5_mpf_IFD = bytesData[12:16]
        self.s6_mpf_IFD_tags_count = bytesData[16:18]
        if self.s3_mpf_byte_order_int == 1:
            self.s6_mpf_IFD_tags_count_int = blength(data=self.s6_mpf_IFD_tags_count)
        elif self.s3_mpf_byte_order_int == 2:
            self.s6_mpf_IFD_tags_count_int = llength(data=self.s6_mpf_IFD_tags_count)
        else:
            self.s6_mpf_IFD_tags_count_int = -1
        self.s7_mpf_tags = []
        for ii in range(0,self.s6_mpf_IFD_tags_count_int):
            ii_start = 18 + (ii * 12)
            ii_end   = ii_start + 12
            item = mpf_Tag(  bytesData=bytesData[ii_start:ii_end], byte_order=self.s3_mpf_byte_order_int)
            self.s7_mpf_tags.append(item)
        self.s8_all_data = bytesData

    #
    def version(self) -> str:
        return 'MPF'

    #
    def showVersion(self):
        print('\t' + self.version())

    #
    def showHeader(self):
        txt1 = '\tApp Marker         : ' + self.s0_app_marker.hex(sep=' ') + "  '" + Kind.findType(self.s0_app_marker).shortname + "'"
        txt2 = '\tApp Length         : ' + self.s1_app_length.hex(sep=' ') + '  (' + str(self.s1_app_length_int) + ' bayt)'
        txt3 = '\tMPF Marker         : ' + self.s2_mpf_marker.hex(sep=' ') + "  '" + self.s2_mpf_marker_str + "'"
        txt4 = '\tMPF Byte Order     : ' + self.s3_mpf_byte_order.hex(sep=' ') + "  '" + self.s3_mpf_byte_order.decode(encoding='utf-8', errors='replace') + "'  (-"+self.s3_mpf_byte_order_str+"-)"
        txt5 = '\tMPF Version        : ' + self.s4_mpf_version.hex(sep=' ')
        txt6 = '\tMPF IFD            : ' + self.s5_mpf_IFD.hex(sep=' ')
        txt7 = '\tMPF IFD Tags Count : ' + self.s6_mpf_IFD_tags_count.hex(sep=' ') + "  (" + str(self.s6_mpf_IFD_tags_count_int)+")"

        print(txt1)
        print(txt2)
        print(txt3)
        print(txt4)
        print(txt5)
        print(txt6)
        print(txt7)


    #
    def showHex(self):
        self.showHeader()
        print()
        s2hex( dataBytes=self.s8_all_data, dataName=Kind.findType(self.s0_app_marker).shortname )

    #
    def showAll(self):
        self.showHeader()
        print()
        self.showTags()

    #
    def showTag(self, index:int):
        tag = self.s7_mpf_tags[index-1]
        print('\t' + "#" * 83)
        print('\tTag Index  : ' + str(index) )
        print('\tTag  (Hex) : ' + tag.t1_tag.hex(sep=' ')  )
        print('\tType       : ' + tag.t2_type.hex(sep=' ')  + "  '"+ tag.t2_type_obj.t2_name +"'" )
        print('\tCount      : ' + tag.t3_count.hex(sep=' ') + "  ("+ str(tag.t3_count_int) + ")")
        print('\tData Count : ' + str(tag.t4_data_bayt_count) + " bayt")
        if tag.t5_offset:
            if tag.t2_type_obj.t3_length>-1 and tag.t4_data_bayt_count > -1:
                ii_start = tag.t6_data + 10
                ii_end   = ii_start + tag.t4_data_bayt_count
                print()
                s2hex(dataBytes=self.s8_all_data[ii_start:ii_end], dataName='DATA' , columnSize=20)
            else:
                print('\tData (Hex) : ' + tag.t6_data.hex(sep=' ')+"     <ASCII>"+ tag.t6_data.decode(encoding='ASCII',errors='replace') +"<ASCII>" )
        else:
            print('\tData (Hex) : ' + tag.t6_data.hex(sep=' ')+"     <ASCII>"+ tag.t6_data.decode(encoding='ASCII',errors='replace') +"<ASCII>" )
        print('\t' + "#" * 83)

    #
    def showTags(self):
        for ii in range(0, len(self.s7_mpf_tags) ):
            if ii != 0:
                print("")
            self.showTag(index=ii)

    #
    def showTagsNames(self):
        txt1 = '\t << Total {} Body Tags >>'.format( len(self.s7_mpf_tags) )
        txt2 = "\tIndex: {:<3} \tTag Marker: '{}'"
        for ii in range(0, len(self.s7_mpf_tags)):
            if ii==0:
                print(txt1)
                print('\t'+'-'*50)
            print(txt2.format( (ii+1), self.s7_mpf_tags[ii].t1_tag.hex(sep=' ') ))



class mpf_Tag:
    #
    def __init__(self, bytesData:bytes, byte_order:int ):
        self.t1_tag =  bytesData[0:2]
        self.t2_type = bytesData[2:4]
        self.t2_type_obj = mpf_Data_Type.find(  bytesData=self.t2_type , byte_order=byte_order  )
        self.t3_count = bytesData[4:8]
        #
        if byte_order == 1:
            self.t3_count_int = blength(self.t3_count)
        elif byte_order == 2:
            self.t3_count_int = llength(self.t3_count)
        else:
            self.t3_count_int = -1
        #
        if self.t2_type_obj.t3_length > -1 and self.t3_count_int > -1:
            self.t4_data_bayt_count = self.t2_type_obj.t3_length * self.t3_count_int
        else:
            self.t4_data_bayt_count = 0
        #
        if self.t4_data_bayt_count > 4:
            self.t5_offset = True
        else:
            self.t5_offset = False
        #
        if self.t5_offset:
            if byte_order == 1:
                self.t6_data = blength( bytesData[8:12] )
            elif byte_order == 2:
                self.t6_data = llength( bytesData[8:12] )
            else:
                self.t6_data = bytesData[8:12]
        else:
            self.t6_data = bytesData[8:12]
        #
#
class mpf_Data_Type:
    #
    @staticmethod
    def find( bytesData:bytes, byte_order:int ):
        item = mpf_Data_Type()
        if len(bytesData) == 2:
            if byte_order == 1:
                if bytesData[0:1] == b'\x00':
                    if bytesData[1:2] == b'\x01':
                        item.t1_no = 1
                        item.t2_name = 'BYTE'
                        item.t3_length = 1
                        item.t4_info = 'An 8-bit unsigned integer'
                    elif bytesData[1:2] == b'\x02':
                        item.t1_no = 2
                        item.t2_name = 'ASCII'
                        item.t3_length = 1
                        item.t4_info = 'An 8-bit byte containing one 7-bit ASCII code. The final byte is terminated with NULL.'
                    elif bytesData[1:2] == b'\x03':
                        item.t1_no = 3
                        item.t2_name = 'SHORT'
                        item.t3_length = 2
                        item.t4_info = 'A 16-bit (2-byte) unsigned integer'
                    elif bytesData[1:2] == b'\x04':
                        item.t1_no = 4
                        item.t2_name =  'LONG'
                        item.t3_length = 4
                        item.t4_info = 'A 32-bit (4-byte) unsigned integer'
                    elif bytesData[1:2] == b'\x05':
                        item.t1_no = 5
                        item.t2_name = 'RATIONAL'
                        item.t3_length = 8
                        item.t4_info = 'Two LONGs. The first LONG is the numerator and the second LONG expresses the denominator.'
                    elif bytesData[1:2] == b'\x07':
                        item.t1_no = 7
                        item.t2_name = 'UNDEFINED'
                        item.t3_length = 1
                        item.t4_info = 'An 8-bit byte that can take any value depending on the field definition'
                    elif bytesData[1:2] == b'\x09':
                        item.t1_no = 9
                        item.t2_name = 'SLONG'
                        item.t3_length = 4
                        item.t4_info = "A 32-bit (4-byte) signed integer (2's complement notation)"
                    elif bytesData[1:2] == b'\x0A':
                        item.t1_no = 10
                        item.t2_name = 'SRATIONAL'
                        item.t3_length = 8
                        item.t4_info = 'Two SLONGs. The first SLONG is the numerator and the second SLONG is the denominator'
                    else:
                        item.t2_name = 'UNKNOWN'
                        item.t4_info = 'Could not be detected'
                else:
                    item.t2_name = 'UNKNOWN'
                    item.t4_info = 'Could not be detected'
            elif byte_order == 2:
                if bytesData[1:2] == b'\x00':
                    if bytesData[0:1] == b'\x01':
                        item.t1_no = 1
                        item.t2_name = 'BYTE'
                        item.t3_length = 1
                        item.t4_info = 'An 8-bit unsigned integer'
                    elif bytesData[0:1] == b'\x02':
                        item.t1_no = 2
                        item.t2_name = 'ASCII'
                        item.t3_length = 1
                        item.t4_info = 'An 8-bit byte containing one 7-bit ASCII code. The final byte is terminated with NULL.'
                    elif bytesData[0:1] == b'\x03':
                        item.t1_no = 3
                        item.t2_name = 'SHORT'
                        item.t3_length = 2
                        item.t4_info = 'A 16-bit (2-byte) unsigned integer'
                    elif bytesData[0:1] == b'\x04':
                        item.t1_no = 4
                        item.t2_name =  'LONG'
                        item.t3_length = 4
                        item.t4_info = 'A 32-bit (4-byte) unsigned integer'
                    elif bytesData[0:1] == b'\x05':
                        item.t1_no = 5
                        item.t2_name = 'RATIONAL'
                        item.t3_length = 8
                        item.t4_info = 'Two LONGs. The first LONG is the numerator and the second LONG expresses the denominator.'
                    elif bytesData[0:1] == b'\x07':
                        item.t1_no = 7
                        item.t2_name = 'UNDEFINED'
                        item.t3_length = 1
                        item.t4_info = 'An 8-bit byte that can take any value depending on the field definition'
                    elif bytesData[0:1] == b'\x09':
                        item.t1_no = 9
                        item.t2_name = 'SLONG'
                        item.t3_length = 4
                        item.t4_info = "A 32-bit (4-byte) signed integer (2's complement notation)"
                    elif bytesData[0:1] == b'\x0A':
                        item.t1_no = 10
                        item.t2_name = 'SRATIONAL'
                        item.t3_length = 8
                        item.t4_info = 'Two SLONGs. The first SLONG is the numerator and the second SLONG is the denominator'
                    else:
                        item.t2_name = 'UNKNOWN'
                        item.t4_info = 'Could not be detected'
                else:
                    item.t2_name = 'UNKNOWN'
                    item.t4_info = 'Could not be detected'
        else:
            item.t2_name = 'ERROR'
            item.t4_info = 'A serious error has occurred'
        return item

    #
    def __init__(self):
     self.t1_no = -1
     self.t2_name = ''
     self.t3_length = -1
     self.t4_info = ''
