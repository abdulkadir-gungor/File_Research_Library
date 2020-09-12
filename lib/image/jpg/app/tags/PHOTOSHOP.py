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

#
#
#
class PHOTOSHOP:
    #
    @staticmethod
    def check( bytesData:bytes ) -> bool:
        if len(bytesData)>14 :
            if bytesData[4:14] == b'Photoshop\x20':
                return True
        return False
    #
    def __init__(self, bytesData: bytes):
        self.s0_app_marker = bytesData[0:2]
        self.s1_app_length = bytesData[2:4]
        self.s1_app_length_int = clength(data=self.s1_app_length)
        self.s2_photoshop_marker = bytesData[4:18]
        self.s2_photoshop_marker_str = self.s2_photoshop_marker.decode(encoding='utf-8',errors='replace') + '\\00'
        self.s3_photoshop_tags = []
        self.s4_all_data = bytesData
        self.find()
    #
    def find(self):
        data_length = len(self.s4_all_data)
        ii_start = 18
        while True:
            if data_length >= (ii_start+12):
                if self.s4_all_data[ii_start:ii_start+4] == b'8BIM':
                    item = photoshoptags()
                    item.t0_index = ii_start
                    item.t1_identifier_mark = self.s4_all_data[ii_start:ii_start+4]
                    item.t2_tag = self.s4_all_data[ii_start+4:ii_start+6]
                    item.t3_padding = self.s4_all_data[ii_start+6:ii_start+8]
                    item.t4_count  = self.s4_all_data[ii_start+8:ii_start+12]
                    item.t4_count_int = clength(data=item.t4_count)
                    ii_start += 12
                    item.t5_data  = self.s4_all_data[ii_start:(ii_start+item.t4_count_int)]
                    self.s3_photoshop_tags.append(item)
                    ii_start += item.t4_count_int
                else:
                    if self.s4_all_data[ii_start:ii_start+1] == b'\x00':
                        ii_start += 1
                    else:
                        break
            else:
                break
    #
    def showHeader(self):
        txt1  = '\tApp Marker                   : ' + self.s0_app_marker.hex(sep=' ')  + "  '" + Kind.findType(self.s0_app_marker).shortname + "'"
        txt2  = '\tApp Length                   : ' + self.s1_app_length.hex(sep=' ')  + '  (' + str(self.s1_app_length_int) +' bayt)'
        txt3  = '\tPhotoshop Marker (Hex)       : ' + self.s2_photoshop_marker.hex(sep=' ')
        txt4  = '\tPhotoshop Marker (Str)       : ' + self.s2_photoshop_marker_str
        txt5  = '\tPhotoshop Tags Count         : ' + str(len(self.s3_photoshop_tags))
        txt6 =  '\t<<8BIM>4bayt> - <<Tag>2bayt> - <<Padding>2bayt>- <<Count>4bayt> - <<Data>Variable>'
        #
        print(txt1)
        print(txt2)
        print(txt3)
        print(txt4)
        print(txt5)
        print(txt6)

    #
    def showTag(self, index:int):
        item = self.s3_photoshop_tags[(index-1)]
        print("\t" + "#" * 83)
        print("\tIndex         : " + str(index))
        print("\tOffset        : " + str(item.t0_index) )
        print("\tIdentifier    : " + item.t1_identifier_mark.hex(sep=' ') + "  '"+item.t1_identifier_mark_str +"'")
        print("\tTag (Hex)     : " + item.t2_tag.hex(sep=' ') )
        print("\tPadding (Hex) : " + item.t3_padding.hex(sep=' ') )
        print("\tCount         : " + item.t4_count.hex(sep=' ') +"  ("+ str(item.t4_count_int) +" bayt)")
        print()
        s2hex(dataBytes=item.t5_data, dataName='DATA', columnSize=20)
        print("\t" + "#" * 83)

    #
    def showTags(self):
        for ii in range(1,(len(self.s3_photoshop_tags)+1) ):
            if ii != 1:
                print("")
            self.showTag(index=ii)

    #
    def showTagsNames(self):
        txt1 = '\t << Total {} Body Tags >>'.format( len(self.s3_photoshop_tags) )
        txt2 = "\tIndex: {:<3} \tTag Marker: '{}'"
        for ii in range(1, (len(self.s3_photoshop_tags) + 1)):
            if ii == 1:
                print(txt1)
                print('\t' + '-' * 50)
            print(txt2.format( ii , self.s3_photoshop_tags[ii-1].t2_tag.hex(sep=' ')))



class photoshoptags:
    def __init__(self):
        self.t0_index = -1
        self.t1_identifier_mark = b''
        self.t1_identifier_mark_str = '8BIM'
        self.t2_tag = b''
        self.t3_padding = b''
        self.t4_count = b''
        self.t4_count_int = -1
        self.t5_data = b''
