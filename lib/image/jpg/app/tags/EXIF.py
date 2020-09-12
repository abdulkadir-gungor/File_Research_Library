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
from lib.hexlib.ShowHex import  show4HexBytes as s4hex
from lib.image.jpg.app.tags.EXIF_TAGS import find_exif_tag as ftag
from lib.image.jpg.app.tags.EXIF_TAGS import find_exif_gps_tag as fgtag
from lib.image.jpg.kind import Kind

# EXIF Definition
# JPG/jpeg Only Big Endian
# Others formats may be Little Endian
class EXIF:
    #
    #
    @staticmethod
    def check( bytesData:bytes ):
        if len(bytesData) > 10:
            return bytesData[4:10] == b'Exif\x00\x00'
        return False
    #
    def __init__(self, bytesData: bytes):
        self.s0_app_marker = bytesData[0:2]
        self.s1_app_length = bytesData[2:4]
        self.s1_app_length_int = clength(data=self.s1_app_length)
        self.s2_exif_marker = bytesData[4:10]
        self.s2_exif_marker_str ='Exif\\x00\\x00'
        self.s3_exif_byte_order = bytesData[10:12]
        if self.s3_exif_byte_order == b'MM':
            self.s3_exif_byte_order_str = 'Big Endian'
            self.s3_exif_byte_order_int = 1
        elif self.s3_exif_byte_order == b'II':
            self.s3_exif_byte_order_str = 'Little Endian'
            self.s3_exif_byte_order_int = 2
        else:
            self.s3_exif_byte_order_str = 'Unknown'
            self.s3_exif_byte_order_int = -1
        self.s4_exif_version_number = bytesData[12:14]
        self.s5_exif_image_file_directory_ifd = bytesData[14:18]
        #      ---- 0IFD ----
        self.s6_exif_0IFD_1tags_counts = bytesData[18:20]
        self.s6_exif_0IFD_2tags_counts_int = clength(self.s6_exif_0IFD_1tags_counts)
        self.s6_exif_0IFD_3tags =[]
        #   ---- Exif IFD ----
        self.s7_exif_ExifIFD_0offset = -1
        self.s7_exif_ExifIFD_1counts = b'\x00\x00'
        self.s7_exif_ExifIFD_2counts_int = 0
        self.s7_exif_ExifIFD_3tags = []
        #  ---- InterOperability IFD ----
        self.s8_exif_InterOperability_0offset = -1
        self.s8_exif_InterOperability_1counts = b'\x00\x00'
        self.s8_exif_InterOperability_2counts_int = 0
        self.s8_exif_InterOperability_3tags = []
        # ---- GPS IFD ----
        self.s9_exif_GpsIFD_0offset = -1
        self.s9_exif_GpsIFD_1counts = b'\x00\00'
        self.s9_exif_GpsIFD_2counts_int = 0
        self.s9_exif_GpsIFD_3tags = []
        # ---- 1IFD (Thumbnail Exif) ----
        self.s10_exif_1IFD_0offset = -1
        self.s10_exif_1IFD_1counts = b'\x00\x00'
        self.s10_exif_1IFD_2counts_int = 0
        self.s10_exif_1IFD_3tags = []
        # ---- All Data ----
        self.s11_data = bytesData
        # ########################################################################
        # Find "1IFD" , "0IFD" , "Exif IFD" , "InterOperability IFD" , "GPS IFD"
        # ########################################################################
        # ---- Define 1IFD Offset ----
        jj = 20 + self.s6_exif_0IFD_2tags_counts_int * 12
        ifd1_offset = self.s11_data[jj:jj+4]
        if ifd1_offset != b'\x00\x00\x00\x00':
            ifd1_offset_int = clength(ifd1_offset)
            self.s10_exif_1IFD_0offset = ifd1_offset_int + 10
            self.s10_exif_1IFD_1counts = self.s11_data[self.s10_exif_1IFD_0offset:self.s10_exif_1IFD_0offset+2]
            self.s10_exif_1IFD_2counts_int = clength(self.s10_exif_1IFD_1counts)
        #
        # ---- (1) Define OIFD Tags  ----
        for ii in  range(0, self.s6_exif_0IFD_2tags_counts_int):
            jj = 20 + ii * 12
            item = exif_Tag.assignExifTag( self.s11_data[jj:jj+12] )
            #
            # Exif IFD
            if item.t1_tag_1bytes == b'\x87\x69':
                kk = clength( item.t4_value_offset_1bytes )
                self.s7_exif_ExifIFD_0offset = kk + 10
                self.s7_exif_ExifIFD_1counts = self.s11_data[self.s7_exif_ExifIFD_0offset:self.s7_exif_ExifIFD_0offset+2]
                self.s7_exif_ExifIFD_2counts_int = clength( self.s7_exif_ExifIFD_1counts )
            # InterOperability IFD
            elif  item.t1_tag_1bytes == b'\xA0\x05':
                kk = clength(item.t4_value_offset_1bytes)
                self.s8_exif_InterOperability_0offset = kk + 10
                self.s8_exif_InterOperability_1counts = self.s11_data[self.s8_exif_InterOperability_0offset:self.s8_exif_InterOperability_0offset+2]
                self.s8_exif_InterOperability_2counts_int = clength( self.s8_exif_InterOperability_1counts )
            # GPS IFD
            elif item.t1_tag_1bytes == b'\x88\x25':
                kk = clength(item.t4_value_offset_1bytes)
                self.s9_exif_GpsIFD_0offset = kk + 10
                self.s9_exif_GpsIFD_1counts = self.s11_data[self.s9_exif_GpsIFD_0offset:self.s9_exif_GpsIFD_0offset+2]
                self.s9_exif_GpsIFD_2counts_int = clength( self.s9_exif_GpsIFD_1counts )
            else:
                # find tag func
                if not item.t1_tag_3bool:
                    item.t1_tag_2str = ftag(item.t1_tag_1bytes)
                self.s6_exif_0IFD_3tags.append(item)
        #
        #  ---- (2) Define Exif IFD ----
        for ii in range(0,self.s7_exif_ExifIFD_2counts_int):
            jj = (self.s7_exif_ExifIFD_0offset+2) + ii * 12
            #
            item = exif_Tag.assignExifTag(self.s11_data[jj:jj + 12])
            #
            # find Tag
            item.t1_tag_2str = ftag(item.t1_tag_1bytes)
            #
            self.s7_exif_ExifIFD_3tags.append(item)
        #
        #  ---- (2) Define InterOperability IFD ----
        for ii in range(0,self.s8_exif_InterOperability_2counts_int):
            jj = (self.s8_exif_InterOperability_0offset + 2) + ii * 12
            #
            item = exif_Tag.assignExifTag(self.s11_data[jj:jj + 12])
            #
            # find Tag
            item.t1_tag_2str = ftag(item.t1_tag_1bytes)
            #
            self.s8_exif_InterOperability_3tags.append(item)
        #
        #  ---- (3) Define GPS IFD ----
        for ii in range(0,self.s9_exif_GpsIFD_2counts_int):
            jj = (self.s9_exif_GpsIFD_0offset+2) + ii * 12
            #
            item = exif_Tag.assignExifTag(self.s11_data[jj:jj + 12])
            #
            # find Tag
            item.t1_tag_2str = fgtag(item.t1_tag_1bytes)
            #
            self.s9_exif_GpsIFD_3tags.append(item)
        #
        #  ---- (4) Define 1IFD ----
        for ii in range(0,self.s10_exif_1IFD_2counts_int):
            jj = (self.s10_exif_1IFD_0offset+2) + ii * 12
            #
            item = exif_Tag.assignExifTag(self.s11_data[jj:jj + 12])
            #
            # find Tag
            item.t1_tag_2str = ftag(item.t1_tag_1bytes)
            #
            self.s10_exif_1IFD_3tags.append(item)
        #
        #

    # (1)
    def show0IFDTags(self):
        count=1
        for tag in self.s6_exif_0IFD_3tags:
            bayt_length = tag.t2_type_2obj.t3_length * tag.t3_count_2int
            print()
            print("\t" + "#" * 63)
            print("\tTag No          : "+str(count))
            print("\tTag (Hex)       : '" + tag.t1_tag_1bytes.hex(sep=' ')+"'" )
            print("\tTag Name        : "  + tag.t1_tag_2str)
            print("")
            print("\tData Type (Hex) : " + tag.t2_type_1bytes.hex(sep=' ' ))
            print("\tData Type (str) : "  + tag.t2_type_2obj.t2_name )
            print("\tData Length     : "  + str(bayt_length) + " bayt")
            if tag.t4_value_offset_3offset_bool:
                start_offset = clength( tag.t4_value_offset_1bytes ) + 10
                print("")
                print("\t(Data)")
                s4hex(dataBytes=self.s11_data[ start_offset : start_offset + bayt_length], columnSize=20)
            else:
                print("")
                print("\t(Data)")
                s4hex(dataBytes=tag.t4_value_offset_1bytes, columnSize=20)
            print("\t" + "#" * 63)
            count += 1
    # (1a)
    def show0IFDTag(self, index:int):
        index -= 1
        tag = self.s6_exif_0IFD_3tags[index]
        #
        bayt_length = tag.t2_type_2obj.t3_length * tag.t3_count_2int
        print()
        print("\t" + "#" * 63)
        print("\tTag No          : " + str(index+1))
        print("\tTag (Hex)       : '" + tag.t1_tag_1bytes.hex(sep=' ') + "'")
        print("\tTag Name        : " + tag.t1_tag_2str)
        print("")
        print("\tData Type (Hex) : " + tag.t2_type_1bytes.hex(sep=' '))
        print("\tData Type (str) : " + tag.t2_type_2obj.t2_name)
        print("\tData Length     : " + str(bayt_length) + " bayt")
        if tag.t4_value_offset_3offset_bool:
            start_offset = clength(tag.t4_value_offset_1bytes) + 10
            print("")
            print("\t(Data)")
            s4hex(dataBytes=self.s11_data[start_offset: start_offset + bayt_length], columnSize=20)
        else:
            print("")
            print("\t(Data)")
            s4hex(dataBytes=tag.t4_value_offset_1bytes, columnSize=20)
        print("\t" + "#" * 63)
        #

    # (2)
    def showExifIFDTags(self):
        count=1
        for tag in self.s7_exif_ExifIFD_3tags:
            bayt_length = tag.t2_type_2obj.t3_length * tag.t3_count_2int
            print()
            print("\t" + "#" * 63)
            print("\tTag No          : "+str(count))
            print("\tTag (Hex)       : '" + tag.t1_tag_1bytes.hex(sep=' ')+"'" )
            print("\tTag Name        : "  + tag.t1_tag_2str)
            print("")
            print("\tData Type (Hex) : " + tag.t2_type_1bytes.hex(sep=' ' ))
            print("\tData Type (str) : "  + tag.t2_type_2obj.t2_name )
            print("\tData Length     : "  + str(bayt_length) + " bayt")
            if tag.t4_value_offset_3offset_bool:
                start_offset = clength( tag.t4_value_offset_1bytes ) + 10
                print("")
                print("\t(Data)")
                s4hex(dataBytes=self.s11_data[ start_offset : start_offset + bayt_length], columnSize=20)
            else:
                print("")
                print("\t(Data)")
                s4hex(dataBytes=tag.t4_value_offset_1bytes, columnSize=20)
            print("\t" + "#" * 63)
            count += 1

    # (2a)
    def showExifIFDTag(self, index:int):
        index -= 1
        tag = self.s7_exif_ExifIFD_3tags[index]
        #
        bayt_length = tag.t2_type_2obj.t3_length * tag.t3_count_2int
        print()
        print("\t" + "#" * 63)
        print("\tTag No          : " + str(index+1))
        print("\tTag (Hex)       : '" + tag.t1_tag_1bytes.hex(sep=' ') + "'")
        print("\tTag Name        : " + tag.t1_tag_2str)
        print("")
        print("\tData Type (Hex) : " + tag.t2_type_1bytes.hex(sep=' '))
        print("\tData Type (str) : " + tag.t2_type_2obj.t2_name)
        print("\tData Length     : " + str(bayt_length) + " bayt")
        if tag.t4_value_offset_3offset_bool:
            start_offset = clength(tag.t4_value_offset_1bytes) + 10
            print("")
            print("\t(Data)")
            s4hex(dataBytes=self.s11_data[start_offset: start_offset + bayt_length], columnSize=20)
        else:
            print("")
            print("\t(Data)")
            s4hex(dataBytes=tag.t4_value_offset_1bytes, columnSize=20)
        print("\t" + "#" * 63)
        #

    # (3)
    def showInterOperabilityIFDTags(self):
        count=1
        for tag in self.s8_exif_InterOperability_3tags:
            bayt_length = tag.t2_type_2obj.t3_length * tag.t3_count_2int
            print()
            print("\t" + "#" * 63)
            print("\tTag No          : "+str(count))
            print("\tTag (Hex)       : '" + tag.t1_tag_1bytes.hex(sep=' ')+"'" )
            print("\tTag Name        : "  + tag.t1_tag_2str)
            print("")
            print("\tData Type (Hex) : " + tag.t2_type_1bytes.hex(sep=' ' ))
            print("\tData Type (str) : "  + tag.t2_type_2obj.t2_name )
            print("\tData Length     : "  + str(bayt_length) + " bayt")
            if tag.t4_value_offset_3offset_bool:
                start_offset = clength( tag.t4_value_offset_1bytes ) + 10
                print("")
                print("\t(Data)")
                s4hex(dataBytes=self.s11_data[ start_offset : start_offset + bayt_length], columnSize=20)
            else:
                print("")
                print("\t(Data)")
                s4hex(dataBytes=tag.t4_value_offset_1bytes, columnSize=20)
            print("\t" + "#" * 63)
            count += 1

    # (3a)
    def showInterOperabilityIFDTag(self, index:int):
        index -= 1
        tag = self.s8_exif_InterOperability_3tags[index]
        #
        bayt_length = tag.t2_type_2obj.t3_length * tag.t3_count_2int
        print()
        print("\t" + "#" * 63)
        print("\tTag No          : " + str(index+1))
        print("\tTag (Hex)       : '" + tag.t1_tag_1bytes.hex(sep=' ') + "'")
        print("\tTag Name        : " + tag.t1_tag_2str)
        print("")
        print("\tData Type (Hex) : " + tag.t2_type_1bytes.hex(sep=' '))
        print("\tData Type (str) : " + tag.t2_type_2obj.t2_name)
        print("\tData Length     : " + str(bayt_length) + " bayt")
        if tag.t4_value_offset_3offset_bool:
            start_offset = clength(tag.t4_value_offset_1bytes) + 10
            print("")
            print("\t(Data)")
            s4hex(dataBytes=self.s11_data[start_offset: start_offset + bayt_length], columnSize=20)
        else:
            print("")
            print("\t(Data)")
            s4hex(dataBytes=tag.t4_value_offset_1bytes, columnSize=20)
        print("\t" + "#" * 63)
        #

    # (4)
    def showGpsIFDTags(self):
        count=1
        for tag in self.s9_exif_GpsIFD_3tags:
            bayt_length = tag.t2_type_2obj.t3_length * tag.t3_count_2int
            print()
            print("\t" + "#" * 63)
            print("\tTag No          : "+str(count))
            print("\tTag (Hex)       : '" + tag.t1_tag_1bytes.hex(sep=' ')+"'" )
            print("\tTag Name        : "  + tag.t1_tag_2str)
            print("")
            print("\tData Type (Hex) : " + tag.t2_type_1bytes.hex(sep=' ' ))
            print("\tData Type (str) : "  + tag.t2_type_2obj.t2_name )
            print("\tData Length     : "  + str(bayt_length) + " bayt")
            if tag.t4_value_offset_3offset_bool:
                start_offset = clength( tag.t4_value_offset_1bytes ) + 10
                print("")
                print("\t(Data)")
                s4hex(dataBytes=self.s11_data[ start_offset : start_offset + bayt_length], columnSize=20)
            else:
                print("")
                print("\t(Data)")
                s4hex(dataBytes=tag.t4_value_offset_1bytes, columnSize=20)
            print("\t" + "#" * 63)
            count += 1

    # (4a)
    def showGpsIFDTag(self, index:int):
        index -= 1
        tag = self.s9_exif_GpsIFD_3tags[index]
        #
        bayt_length = tag.t2_type_2obj.t3_length * tag.t3_count_2int
        print()
        print("\t" + "#" * 63)
        print("\tTag No          : " + str(index+1))
        print("\tTag (Hex)       : '" + tag.t1_tag_1bytes.hex(sep=' ') + "'")
        print("\tTag Name        : " + tag.t1_tag_2str)
        print("")
        print("\tData Type (Hex) : " + tag.t2_type_1bytes.hex(sep=' '))
        print("\tData Type (str) : " + tag.t2_type_2obj.t2_name)
        print("\tData Length     : " + str(bayt_length) + " bayt")
        if tag.t4_value_offset_3offset_bool:
            start_offset = clength(tag.t4_value_offset_1bytes) + 10
            print("")
            print("\t(Data)")
            s4hex(dataBytes=self.s11_data[start_offset: start_offset + bayt_length], columnSize=20)
        else:
            print("")
            print("\t(Data)")
            s4hex(dataBytes=tag.t4_value_offset_1bytes, columnSize=20)
        print("\t" + "#" * 63)
        #

    # (5)
    def show1IFDTags(self):
        count=1
        for tag in self.s10_exif_1IFD_3tags:
            bayt_length = tag.t2_type_2obj.t3_length * tag.t3_count_2int
            print()
            print("\t" + "#" * 63)
            print("\tTag No          : "+str(count))
            print("\tTag (Hex)       : '" + tag.t1_tag_1bytes.hex(sep=' ')+"'" )
            print("\tTag Name        : "  + tag.t1_tag_2str)
            print("")
            print("\tData Type (Hex) : " + tag.t2_type_1bytes.hex(sep=' ' ))
            print("\tData Type (str) : "  + tag.t2_type_2obj.t2_name )
            print("\tData Length     : "  + str(bayt_length) + " bayt")
            if tag.t4_value_offset_3offset_bool:
                start_offset = clength( tag.t4_value_offset_1bytes ) + 10
                print("")
                print("\t(Data)")
                s4hex(dataBytes=self.s11_data[ start_offset : start_offset + bayt_length], columnSize=20)
            else:
                print("")
                print("\t(Data)")
                s4hex(dataBytes=tag.t4_value_offset_1bytes, columnSize=20)
            print("\t" + "#" * 63)
            count += 1

    # (5a)
    def show1IFDTag(self, index:int):
        index -= 1
        tag = self.s10_exif_1IFD_3tags[index]
        #
        bayt_length = tag.t2_type_2obj.t3_length * tag.t3_count_2int
        print()
        print("\t" + "#" * 63)
        print("\tTag No          : " + str(index+1))
        print("\tTag (Hex)       : '" + tag.t1_tag_1bytes.hex(sep=' ') + "'")
        print("\tTag Name        : " + tag.t1_tag_2str)
        print("")
        print("\tData Type (Hex) : " + tag.t2_type_1bytes.hex(sep=' '))
        print("\tData Type (str) : " + tag.t2_type_2obj.t2_name)
        print("\tData Length     : " + str(bayt_length) + " bayt")
        if tag.t4_value_offset_3offset_bool:
            start_offset = clength(tag.t4_value_offset_1bytes) + 10
            print("")
            print("\t(Data)")
            s4hex(dataBytes=self.s11_data[start_offset: start_offset + bayt_length], columnSize=20)
        else:
            print("")
            print("\t(Data)")
            s4hex(dataBytes=tag.t4_value_offset_1bytes, columnSize=20)
        print("\t" + "#" * 63)
        #

    #
    def showHeader(self):
        txt1  = '\tApp Marker                             : '  +  self.s0_app_marker.hex(sep=' ')  + "  '" + Kind.findType(self.s0_app_marker).shortname + "'"
        txt2  = '\tApp Length                             : '  +  self.s1_app_length.hex(sep=' ')  + '  (' + str(self.s1_app_length_int) +' bayt)'
        txt3  = '\tExif Marker                            : '  +  self.s2_exif_marker.hex(sep=' ') +  "  '" + self.s2_exif_marker_str +  "'"
        txt4  = '\tExif Byte Order                        : '  + self.s3_exif_byte_order.hex(sep=' ') + "  '"+self.s3_exif_byte_order.decode(encoding='Ascii', errors='replace') +"'  '" + self.s3_exif_byte_order_str +  "'"
        txt5  = '\tExif Version Number                    : '  + self.s4_exif_version_number.hex(sep=' ') + "  (" + str(clength(self.s4_exif_version_number)) + ")"
        txt6  = '\tExif IFD                               : '  + self.s5_exif_image_file_directory_ifd.hex(sep=' ')
        txt7  = "\tExif 'OIFD' Tags Count                 : "  + str(len(self.s6_exif_0IFD_3tags))
        txt8  = "\tExif 'Exif IFD' Tags Count             : "  + str(len(self.s7_exif_ExifIFD_3tags))
        txt9  = "\tExif 'Interoperability IFD' Tags Count : "  + str(len(self.s8_exif_InterOperability_3tags))
        txt10 = "\tExif 'GPS IFD' Tags Count              : "  + str(len(self.s9_exif_GpsIFD_3tags))
        txt11 = "\tExif '1IFD' Tags Count                 : "  + str(len(self.s10_exif_1IFD_3tags))
        txt12 = "\t                                     +           "
        txt13 = "\t                                     ----------- "
        txt14 = "\tExif Total Tags Count                  : " + str(len(self.s6_exif_0IFD_3tags)+len(self.s7_exif_ExifIFD_3tags)+len(self.s8_exif_InterOperability_3tags)+len(self.s9_exif_GpsIFD_3tags)+len(self.s10_exif_1IFD_3tags))

        print(txt1)
        print(txt2)
        print(txt3)
        print(txt4)
        print(txt5)
        print(txt6)
        print()
        print(txt7)
        print(txt8)
        print(txt9)
        print(txt10)
        print(txt11)
        print(txt12)
        print(txt13)
        print(txt14)

    #
    def showAllTagNames(self):
        format1 = '\t{:>3}. {}'
        #
        print( '\n\t  A) 0IFD TAGS ({})'.format(len(self.s6_exif_0IFD_3tags) ) )
        print('\t--------------------------------------------------')
        count = 1
        for item  in self.s6_exif_0IFD_3tags:
            print( format1.format( count, item.t1_tag_2str ) )
            count += 1

        #
        print('\n\t  B) EXIF TAGS ({})'.format(len(self.s7_exif_ExifIFD_3tags)))
        print('\t--------------------------------------------------')
        count = 1
        for item in self.s7_exif_ExifIFD_3tags:
            print(format1.format(count, item.t1_tag_2str))
            count += 1

        #
        print('\n\t  C) INTEROPERABILITY IFD TAGS ({})'.format(len(self.s8_exif_InterOperability_3tags) ) )
        print('\t--------------------------------------------------')
        count = 1
        for item in self.s8_exif_InterOperability_3tags:
            print(format1.format(count, item.t1_tag_2str))
            count += 1

        #
        print('\n\t  D) GPS IFD TAGS ({})'.format(len(self.s9_exif_GpsIFD_3tags)))
        print('\t--------------------------------------------------')
        count = 1
        for item in self.s9_exif_GpsIFD_3tags:
            print(format1.format(count, item.t1_tag_2str))
            count += 1

        #
        print('\n\t  E) 1IFD TAGS ({})'.format(len(self.s10_exif_1IFD_3tags)))
        print('\t--------------------------------------------------')
        count = 1
        for item in self.s10_exif_1IFD_3tags:
            print(format1.format(count, item.t1_tag_2str))
            count += 1


    # s1
    def show0IFDTagNames(self):
        format1 = '\t{:>3}. {}'
        #
        print( '\t     0IFD TAGS ({})'.format(len(self.s6_exif_0IFD_3tags) ) )
        print('\t---------------------------------')
        count = 1
        for item  in self.s6_exif_0IFD_3tags:
            print( format1.format( count, item.t1_tag_2str ) )
            count += 1
    # s2
    def showExifIFDTagNames(self):
        format1 = '\t{:>3}. {}'
        #
        print('\t     EXIF TAGS ({})'.format(len(self.s7_exif_ExifIFD_3tags)))
        print('\t---------------------------------')
        count = 1
        for item in self.s7_exif_ExifIFD_3tags:
            print(format1.format(count, item.t1_tag_2str))
            count += 1

    # s3
    def showInteroperabilityIFDTagNames(self):
        format1 = '\t{:>3}. {}'
        #
        print('\t     INTEROPERABILITY IFD TAGS ({})'.format(len(self.s8_exif_InterOperability_3tags) ) )
        print('\t--------------------------------------------------')
        count = 1
        for item in self.s8_exif_InterOperability_3tags:
            print(format1.format(count, item.t1_tag_2str))
            count += 1

    # s4
    def showGpsIFDTagNames(self):
        format1 = '\t{:>3}. {}'
        #
        print('\t     GPS IFD TAGS ({})'.format(len(self.s9_exif_GpsIFD_3tags)))
        print('\t------------------------------------')
        count = 1
        for item in self.s9_exif_GpsIFD_3tags:
            print(format1.format(count, item.t1_tag_2str))
            count += 1

    # s5
    def show1IFDTagNames(self):
        format1 = '\t{:>3}. {}'
        #
        print('\t   1IFD TAGS ({})   -(Thumbnail JPG/JPEG)-'.format(len(self.s10_exif_1IFD_3tags)))
        print('\t--------------------------------------------------')
        count = 1
        for item in self.s10_exif_1IFD_3tags:
            print(format1.format(count, item.t1_tag_2str))
            count += 1

class exif_Tag:
    #
    #
    @staticmethod
    def assignExifTag( bytesData:bytes ):
        item = exif_Tag()
        #
        item.t1_tag_1bytes = bytesData[0:2]
        item.t2_type_1bytes = bytesData[2:4]
        item.t3_count_1bytes = bytesData[4:8]
        item.t4_value_offset_1bytes = bytesData[8:12]
        #
        item.t2_type_2obj = exif_Data_Type.find( item.t2_type_1bytes )
        item.t3_count_2int = clength( item.t3_count_1bytes )
        item.t3_count_3baytslength = item.t3_count_2int * item.t2_type_2obj.t3_length
        #
        if item.t1_tag_1bytes == b'\x87\x69':
            item.t1_tag_2str = 'Exif IFD'
            item.t1_tag_3bool = True
            item.t4_value_offset_2int = 1
            item.t4_value_offset_3offset_bool = True
            item.t4_value_offset_4type_str = 'OFFSET'
        elif item.t1_tag_1bytes == b'\xA0\x05':
            item.t1_tag_2str = 'Interoperability IFD'
            item.t1_tag_3bool = True
            item.t4_value_offset_2int = 1
            item.t4_value_offset_3offset_bool = True
            item.t4_value_offset_4type_str = 'OFFSET'
        elif item.t1_tag_1bytes == b'\x88\x25':
            item.t1_tag_2str = 'GPS IFD'
            item.t1_tag_3bool = True
            item.t4_value_offset_2int = 1
            item.t4_value_offset_3offset_bool = True
            item.t4_value_offset_4type_str = 'OFFSET'
        elif item.t3_count_3baytslength > 4:
            item.t4_value_offset_2int = 1
            item.t4_value_offset_3offset_bool = True
            item.t4_value_offset_4type_str = 'OFFSET'
        elif item.t3_count_3baytslength <= 4:
            item.t4_value_offset_2int = 2
            item.t4_value_offset_3offset_bool = False
            item.t4_value_offset_4type_str = 'VALUE'
        else:
            item.t4_value_offset_4type_str = 'UNKNOWN'
        return item

    #
    #
    def __init__(self):
        self.t1_tag_1bytes  =b''
        self.t1_tag_2str    =''
        self.t1_tag_3bool   = False
        self.t2_type_1bytes =b''
        self.t2_type_2obj   =exif_Data_Type()
        self.t3_count_1bytes = b''
        self.t3_count_2int   = -1
        self.t3_count_3baytslength = -1
        self.t4_value_offset_1bytes =b''
        self.t4_value_offset_2int = -1
        self.t4_value_offset_3offset_bool = False
        self.t4_value_offset_4type_str = ''

class exif_Data_Type:
    #
    @staticmethod
    def find( bytesData:bytes ):
        item = exif_Data_Type()
        if len(bytesData) == 2:
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
        else:
            item.t2_name = 'ERROR'
            item.t4_info = 'A serious error has occurred'
        return item

    #
    #
    def __init__(self):
     self.t1_no = -1
     self.t2_name = ''
     self.t3_length = -1
     self.t4_info = ''