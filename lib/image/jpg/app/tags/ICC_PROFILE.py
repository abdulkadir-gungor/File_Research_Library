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
from lib.image.jpg.data_calculate.BigUnsignedLength import BigUnsignedLength as clength
from lib.hexlib.ShowHex import show2HexBytes as s2hex

# icc_profile definition
class ICC_PROFILE:
    # check: ICC_PROFILE kontrol için
    #        statik method
    @staticmethod
    def check(bytesData: bytes) -> bool:
        if len(bytesData) > 15:
            return bytesData[4:16] == b'ICC_PROFILE\x00'
        else:
            return False

    #
    @staticmethod
    def __s7_icc_profile_and_device_class(bytesData: bytes) -> str:
        if bytesData == b'scnr':
            return 'Input devices  (scanners and digital cameras)'
        elif bytesData == b'mntr':
            return 'Display devices (CRTs and LCDs)'
        elif bytesData == b'prtr':
            return 'Output devices (printers)'
        elif bytesData == b'link':
            return 'Device link profiles'
        elif bytesData == b'spac':
            return 'Color space conversion profiles'
        elif bytesData == b'abst':
            return 'Abstract profiles'
        elif bytesData == b'nmcl':
            return 'Named color profiles'
        return ''

    #
    @staticmethod
    def __s8_icc_color_space_signatures(bytesData: bytes) -> str:
        if bytesData[0:3] == b'XYZ':
            return 'XYZData'
        elif bytesData[0:3] == b'Lab':
            return 'labData'
        elif bytesData[0:3] == b'Lub':
            return 'lubData'
        elif bytesData == b'YCbr':
            return 'YCbCrData'
        elif bytesData[0:3] == b'Yxy':
            return 'YxyData'
        elif bytesData[0:3] == b'RGB':
            return 'rgbData'
        elif bytesData == b'GRAY':
            return 'grayData'
        elif bytesData[0:3] == b'HSV':
            return 'hsvData'
        elif bytesData[0:3] == b'HLS':
            return 'hlsData'
        elif bytesData == b'CMYK':
            return 'cmykData'
        elif bytesData[0:3] == b'CMY':
            return 'cmyData'
        return ''

    #
    @staticmethod
    def __s9_icc_profile_connection_space(bytesData: bytes) -> str:
        if bytesData[0:3] == b'XYZ':
            return 'XYZData'
        elif bytesData[0:3] == b'Lab':
            return 'labData'
        return ''

    #
    @staticmethod
    def s10_func_icc_date_and_time(bytesData: bytes) -> str:
        year = clength(bytesData[0:2])
        month = clength(bytesData[2:4])
        day = clength(bytesData[4:6])
        hour = clength(bytesData[6:8])
        minute = clength(bytesData[8:10])
        second = clength(bytesData[10:12])
        date = "{:0>4d}/{:0>2d}/{:0>2d} {:0>2d}:{:0>2d}:{:0>2d}".format(year, month, day, hour, minute, second)
        return date

    #
    @staticmethod
    def __s12_icc_primary_platform(bytesData: bytes) -> str:
        if bytesData == b'APPL':
            return 'Apple Computer, Inc.'
        elif bytesData == b'MSFT':
            return 'Microsoft Corporation'
        elif bytesData[0:3] == b'SGI':
            return 'Silicon Graphics, Inc.'
        elif bytesData == b'SUNW':
            return 'Sun Microsystems, Inc'
        elif bytesData == b'TGNT':
            return 'Taligent, Inc.'
        return ''

    #
    def __init__(self, bytesData: bytes):
        self.s0_app_marker = bytesData[0:2]
        self.s1_app_length = bytesData[2:4]
        self.s1_app_length_int = clength(data=self.s1_app_length)
        self.s2_icc_marker = bytesData[4:16]
        self.s2_icc_marker_str = 'ICC_PROFILE\\x00'
        self.s3_icc_starter = bytesData[16:18]
        self.s4_icc_profile_size = bytesData[18:22]
        self.s4_icc_profile_size_int = clength(data=self.s4_icc_profile_size)
        self.s5_icc_cmm_type = bytesData[22:26]
        self.s6_icc_profile_version_number = bytesData[26:30]
        self.s6_icc_profile_version_number_1major = '(Major Revision in BCD : ' + str(
            ord(self.s6_icc_profile_version_number[0:1])) + ')'
        self.s6_icc_profile_version_number_2minor = '(Minor Revision in BCD : ' + str(
            ord(self.s6_icc_profile_version_number[1:2])) + ')'
        self.s6_icc_profile_version_number_3reserved = '(Reserved : ' + str(
            ord(self.s6_icc_profile_version_number[2:3])) + ')'
        self.s6_icc_profile_version_number_4reserved = '(Reserved : ' + str(
            ord(self.s6_icc_profile_version_number[3:4])) + ')'
        self.s7_icc_profile_and_device_class = bytesData[30:34]
        self.s7_icc_profile_and_device_class_str = self.__s7_icc_profile_and_device_class(
            bytesData=self.s7_icc_profile_and_device_class)
        self.s8_icc_color_space_signatures = bytesData[34:38]
        self.s8_icc_color_space_signatures_str = self.__s8_icc_color_space_signatures(
            bytesData=self.s8_icc_color_space_signatures)
        self.s9_icc_profile_connection_space = bytesData[38:42]
        self.s9_icc_profile_connection_space_str = self.__s9_icc_profile_connection_space(
            bytesData=self.s9_icc_profile_connection_space)
        self.s10_icc_date_and_time = bytesData[42:54]
        self.s10_icc_date_and_time_str = self.s10_func_icc_date_and_time(bytesData=self.s10_icc_date_and_time)
        self.s11_icc_profile_file_signature = bytesData[54:58]
        self.s12_icc_primary_platform = bytesData[58:62]
        self.s12_icc_primary_platform_str = self.__s12_icc_primary_platform(bytesData=self.s12_icc_primary_platform)
        self.s13_icc_flag_options = bytesData[62:66]
        self.s14_icc_device_manufacturer = bytesData[66:70]
        self.s15_icc_device_model = bytesData[70:74]
        self.s16_icc_device_attributes = bytesData[74:82]
        self.s17_icc_rendering_intent = bytesData[82:86]
        self.s18_icc_xyz_number = bytesData[86:98]
        self.s19_icc_identifier_creator = bytesData[98:102]
        self.s20_icc_future = bytesData[102:146]
        self.s21_icc_body_tag_counts = bytesData[146:150]
        self.s21_icc_body_tag_counts_int = clength(self.s21_icc_body_tag_counts)
        self.s22_icc_body_tags = []
        for nn in range(0, self.s21_icc_body_tag_counts_int):
            nn_start = 150 + nn * 12
            nn_end = nn_start + 12
            nn_item = icc_tag(bytesData=bytesData[nn_start:nn_end], index=nn_start)
            nn_item.i4_data_obj = icc_tag_type.find_icc_data_type( data=bytesData[nn_item.i3_data_start:nn_item.i3_data_end] )
            self.s22_icc_body_tags.append(nn_item)
        self.s23_data = bytesData

    #
    def showHeader(self):
        txt1 = '\tApp Marker : ' +  self.s0_app_marker.hex(sep=' ') + "  '" + Kind.findType(self.s0_app_marker).shortname + "'"
        txt2 = '\tApp Length : ' +  self.s1_app_length.hex(sep=' ') + '  (' + str(self.s1_app_length_int) +' bayt)'
        txt3 = '\tIcc Profile Marker   : ' + self.s2_icc_marker.hex(sep=' ') + "  '" + self.s2_icc_marker_str +  "'"
        txt4 = '\tIcc Profile Starter  : ' + self.s3_icc_starter.hex(sep=' ')
        txt5 = '\tIcc Profile Length   : ' + self.s4_icc_profile_size.hex(sep=' ') + '  ('+ str(self.s4_icc_profile_size_int) + ' bayt)'
        txt6 = '\tIcc Profile CMM Type : ' + self.s5_icc_cmm_type.hex(sep=' ')
        txt7 = '\tIcc Profile Version  : ' + self.s6_icc_profile_version_number.hex(sep=' ')
        txt8 = '\t' + self.s6_icc_profile_version_number_1major + '  ' + self.s6_icc_profile_version_number_2minor +'  '+ self.s6_icc_profile_version_number_3reserved + '  ' + self.s6_icc_profile_version_number_4reserved
        txt9 = '\tIcc Profile and Device Class    : ' + self.s7_icc_profile_and_device_class.hex(sep=' ') + "  '"+self.s7_icc_profile_and_device_class_str+"'"
        txt10 = '\tIcc Profile Color Space         : ' + self.s8_icc_color_space_signatures.hex(sep=' ') +"  '"+self.s8_icc_color_space_signatures_str+"'"
        txt11 = '\tIcc Profile Connection Space    : ' + self.s9_icc_profile_connection_space.hex(sep=' ') + "  '"+self.s9_icc_profile_connection_space_str+"'"
        txt12 = '\tIcc Profile Date and Time       : ' + self.s10_icc_date_and_time.hex(sep=' ') + "  '"+ self.s10_icc_date_and_time_str +"'"
        txt13 = '\tIcc Profile File Signature      : ' + self.s11_icc_profile_file_signature.hex(sep=' ')
        txt14 = '\tIcc Profile Primary Platform    : '+self.s12_icc_primary_platform.hex(sep=' ')+"  '" + self.s12_icc_primary_platform_str + "'"
        txt15 = '\tIcc Profile Flag Options        : ' + self.s13_icc_flag_options.hex(sep=' ')
        txt16 = '\tIcc Profile Device Manufacturer : ' + self.s14_icc_device_manufacturer.hex(sep=' ')
        txt17 = '\tIcc Profile Device Model        : ' + self.s15_icc_device_model.hex(sep=' ')
        txt18 = '\tIcc Profile Device Attributes   : ' + self.s16_icc_device_attributes.hex(sep=' ')
        txt19 = '\tIcc Profile Rendering Intent    : ' + self.s17_icc_rendering_intent.hex(sep=' ')
        txt20 = '\tIcc Profile XYZ Number          : [CIE X] ' + self.s18_icc_xyz_number[0:4].hex(sep=' ') +' - [CIE Y] ' + self.s18_icc_xyz_number[4:8].hex(sep=' ') + ' - [CIE Z] ' + self.s18_icc_xyz_number[8:12].hex(sep=' ')
        txt21 = '\tIcc Profile Identifier Creator  : ' + self.s19_icc_identifier_creator.hex(sep=' ')
        txt22 = '\tIcc Profile Future              : ' + self.s20_icc_future[0:10].hex(sep=' ')
        txt23 = '\t                                : ' + self.s20_icc_future[10:20].hex(sep=' ')
        txt24 = '\t                                : ' + self.s20_icc_future[20:30].hex(sep=' ')
        txt25 = '\t                                : ' + self.s20_icc_future[30:40].hex(sep=' ')
        txt26 = '\t                                : ' + self.s20_icc_future[40:].hex(sep=' ')
        txt27 = '\tIcc Profile Body Tag Counts     : ' + self.s21_icc_body_tag_counts.hex(sep=' ') + '  (' +str(self.s21_icc_body_tag_counts_int) + ' adet)'
        print(txt1)
        print(txt2)
        print(txt3)
        print(txt4)
        print(txt5)
        print(txt6)
        print(txt7)
        print(txt8)
        print(txt9)
        print(txt10)
        print(txt11)
        print(txt12)
        print(txt13)
        print(txt14)
        print(txt15)
        print(txt16)
        print(txt17)
        print(txt18)
        print(txt19)
        print(txt20)
        print(txt21)
        print(txt22)
        print(txt23)
        print(txt24)
        print(txt25)
        print(txt26)
        print(txt27)

    #
    def header(self) -> str:
        txt1 = '\tApp Marker : ' +  self.s0_app_marker.hex(sep=' ') + "  '" + Kind.findType(self.s0_app_marker).shortname + "'"
        txt2 = '\tApp Length : ' +  self.s1_app_length.hex(sep=' ') + '  (' + str(self.s1_app_length_int) +' bayt)'
        txt3 = '\tIcc Profile Marker   : ' + self.s2_icc_marker.hex(sep=' ') + "  '" + self.s2_icc_marker_str +  "'"
        txt4 = '\tIcc Profile Starter  : ' + self.s3_icc_starter.hex(sep=' ')
        txt5 = '\tIcc Profile Length   : ' + self.s4_icc_profile_size.hex(sep=' ') + '  ('+ str(self.s4_icc_profile_size_int) + ' bayt)'
        txt6 = '\tIcc Profile CMM Type : ' + self.s5_icc_cmm_type.hex(sep=' ')
        txt7 = '\tIcc Profile Version  : ' + self.s6_icc_profile_version_number.hex(sep=' ')
        txt8 = '\t' + self.s6_icc_profile_version_number_1major + '  ' + self.s6_icc_profile_version_number_2minor +'  '+ self.s6_icc_profile_version_number_3reserved + '  ' + self.s6_icc_profile_version_number_4reserved
        txt9 = '\tIcc Profile and Device Class    : ' + self.s7_icc_profile_and_device_class.hex(sep=' ') + "  '"+self.s7_icc_profile_and_device_class_str+"'"
        txt10 = '\tIcc Profile Color Space         : ' + self.s8_icc_color_space_signatures.hex(sep=' ') +"  '"+self.s8_icc_color_space_signatures_str+"'"
        txt11 = '\tIcc Profile Connection Space    : ' + self.s9_icc_profile_connection_space.hex(sep=' ') + "  '"+self.s9_icc_profile_connection_space_str+"'"
        txt12 = '\tIcc Profile Date and Time       : ' + self.s10_icc_date_and_time.hex(sep=' ') + "  '"+ self.s10_icc_date_and_time_str +"'"
        txt13 = '\tIcc Profile File Signature      : ' + self.s11_icc_profile_file_signature.hex(sep=' ')
        txt14 = '\tIcc Profile Primary Platform    : '+self.s12_icc_primary_platform.hex(sep=' ')+"  '" + self.s12_icc_primary_platform_str + "'"
        txt15 = '\tIcc Profile Flag Options        : ' + self.s13_icc_flag_options.hex(sep=' ')
        txt16 = '\tIcc Profile Device Manufacturer : ' + self.s14_icc_device_manufacturer.hex(sep=' ')
        txt17 = '\tIcc Profile Device Model        : ' + self.s15_icc_device_model.hex(sep=' ')
        txt18 = '\tIcc Profile Device Attributes   : ' + self.s16_icc_device_attributes.hex(sep=' ')
        txt19 = '\tIcc Profile Rendering Intent    : ' + self.s17_icc_rendering_intent.hex(sep=' ')
        txt20 = '\tIcc Profile XYZ Number          : [CIE X] ' + self.s18_icc_xyz_number[0:4].hex(sep=' ') +' - [CIE Y] ' + self.s18_icc_xyz_number[4:8].hex(sep=' ') + ' - [CIE Z] ' + self.s18_icc_xyz_number[8:12].hex(sep=' ')
        txt21 = '\tIcc Profile Identifier Creator  : ' + self.s19_icc_identifier_creator.hex(sep=' ')
        txt22 = '\tIcc Profile Future              : ' + self.s20_icc_future[0:10].hex(sep=' ')
        txt23 = '\t                                : ' + self.s20_icc_future[10:20].hex(sep=' ')
        txt24 = '\t                                : ' + self.s20_icc_future[20:30].hex(sep=' ')
        txt25 = '\t                                : ' + self.s20_icc_future[30:40].hex(sep=' ')
        txt26 = '\t                                : ' + self.s20_icc_future[40:].hex(sep=' ')
        txt27 = '\tIcc Profile Body Tag Counts     : ' + self.s21_icc_body_tag_counts.hex(sep=' ') + '  (' +str(self.s21_icc_body_tag_counts_int) + ' adet)'
        result = txt1 + '\n' + txt2 + '\n' + txt3 + '\n' + txt4 + '\n' + txt5 + '\n' + txt6 + '\n' \
                 + txt7 + '\n' + txt8 + '\n' + txt9 + '\n' + txt10 + '\n' + txt11 + '\n' + txt12 + '\n' \
                 + txt13 + '\n' + txt14 + '\n' + txt15 + '\n' + txt16 + '\n' + txt17 + '\n' + txt18 + '\n' \
                 + txt19 + '\n' + txt20 + '\n' + txt21 + '\n' + txt22 + '\n' + txt23 + '\n' + txt24 + '\n' \
                 + txt25 + '\n' + txt26 + '\n' + txt27
        return  result

    #
    def showBodyTag(self, index:int):
        tag = self.s22_icc_body_tags[index-1]

        txt1 = '\t<<Tag Hex>>               || ' + self.s23_data[tag.i1_start:tag.i1_end].hex(sep=' ') + ' ||'
        txt2 = '\tTag Index                 : ' + str(index)
        txt3 = '\tTag Start/End Offset      : ' + str(tag.i1_start) + ' - ' + str(tag.i1_end) + '  ('+str(tag.i1_end - tag.i1_start)+' bayt)'
        txt4 = '\tTag Marker                : ' + tag.i2_header_1_signature.hex(sep=' ')
        txt5 = '\tTag Name                  : ' + tag.i2_header_0_type.t2_name
        txt6 = '\tTag Comment               : ' + tag.i2_header_0_type.t3_comment
        txt7 = '\tTag Data Start/End Offset : ' + str(tag.i3_data_start) +  ' - ' + str(tag.i3_data_end-1) + '  ('+str(tag.i2_header_3_size_int)+' bayt)'

        print("\t" + "#" * 83)
        print(txt1)
        print()
        print(txt2)
        print(txt3)
        print(txt4)
        print(txt5)
        print(txt6)
        print(txt7)
        print()
        tag.i4_data_obj.show()
        print()
        s2hex( dataBytes=self.s23_data[tag.i3_data_start:tag.i3_data_end], dataName='<< '+tag.i2_header_0_type.t2_name+' Data >>', columnSize=20)
        print("\t" + "#" * 83)

    #
    def showBodyTags(self):
        txt1 = '\t << Total {} Body Tags >>'.format(self.s21_icc_body_tag_counts_int)
        txt2 = "\tIndex: {:<3}  \tTag Marker: '{:<11}'  \tTag Name: {}"
        for ii in range(0,self.s21_icc_body_tag_counts_int):
            if ii==0:
                print(txt1)
                print('\t'+'-'*70)
            print( txt2.format(ii+1, self.s22_icc_body_tags[ii].i2_header_1_signature.hex(sep='-'),
                               self.s22_icc_body_tags[ii].i2_header_0_type.t2_name )  )

    #
    def bodyTags(self) -> str:
        txt1 = '\t << Total {} Body Tags >>'.format(self.s21_icc_body_tag_counts_int)
        txt_dash = '\t'+'-'*70
        txt2 = "\tIndex: {:<3}  \tTag Marker: '{:<11}'  \tTag Name: {}"
        result = ''
        for ii in range(0,self.s21_icc_body_tag_counts_int):
            if ii==0:
                result = txt1 + '\n' + txt_dash
            result += '\n' +txt2.format(ii+1, self.s22_icc_body_tags[ii].i2_header_1_signature.hex(sep='-'),
                               self.s22_icc_body_tags[ii].i2_header_0_type.t2_name )
        return result

# icc_tag
class icc_tag:
    #
    def __init__(self, bytesData: bytes, index: int):
        self.i1_start = index
        self.i1_end = index + 12
        self.i2_header_1_signature = bytesData[0:4]
        self.i2_header_0_type = icc_tag_type.find_icc_tag_type(headerSignature=self.i2_header_1_signature)
        self.i2_header_2_address = bytesData[4:8]
        self.i2_header_2_address_int = clength(data=self.i2_header_2_address)
        self.i2_header_3_size = bytesData[8:12]
        self.i2_header_3_size_int = clength(data=self.i2_header_3_size)
        self.i3_data_start = self.i2_header_2_address_int + 18
        self.i3_data_end = self.i3_data_start + self.i2_header_3_size_int
        self.i4_data_obj = icc_data_type()
    #


class icc_tag_type:
    #
    def __init__(self):
        self.t1_marker = b''
        self.t2_name = ''
        self.t3_comment = ''

    #
    @staticmethod
    def find_icc_tag_type(headerSignature: bytes):
        tag_type = icc_tag_type()
        if headerSignature == b'A2B0':  # 1
            tag_type.t1_marker = b'A2B0'
            tag_type.t2_name = 'AToB0Tag'
            tag_type.t3_comment = 'Multidimensional transformation structure'
        elif headerSignature == b'A2B1':  # 2
            tag_type.t1_marker = b'A2B1'
            tag_type.t2_name = 'AToB1Tag'
            tag_type.t3_comment = 'Multidimensional transformation structure'
        elif headerSignature == b'A2B2':  # 3
            tag_type.t1_marker = b'A2B2'
            tag_type.t2_name = 'AToB2Tag'
            tag_type.t3_comment = 'Relative XYZ values of blue phosphor or colorant'
        elif headerSignature == b'bXYZ':  # 4
            tag_type.t1_marker = b'bXYZ'
            tag_type.t2_name = 'blueColorantTag'
            tag_type.t3_comment = 'Multidimensional transformation structure'
        elif headerSignature == b'bTRC':  # 5
            tag_type.t1_marker = b'bTRC'
            tag_type.t2_name = 'blueTRCTag'
            tag_type.t3_comment = 'Blue channel tone reproduction curve'
        elif headerSignature == b'B2A0':  # 6
            tag_type.t1_marker = b'B2A0'
            tag_type.t2_name = 'BToA0Tag'
            tag_type.t3_comment = 'Multidimensional transformation structure'
        elif headerSignature == b'B2A1':  # 7
            tag_type.t1_marker = b'B2A1'
            tag_type.t2_name = 'BToA1Tag'
            tag_type.t3_comment = 'Multidimensional transformation structure'
        elif headerSignature == b'B2A2':  # 8
            tag_type.t1_marker = b'B2A2'
            tag_type.t2_name = 'BToA2Tag'
            tag_type.t3_comment = 'Multidimensional transformation structure'
        elif headerSignature == b'calt':  # 9
            tag_type.t1_marker = b'calt'
            tag_type.t2_name = 'calibrationDateTimeTag'
            tag_type.t3_comment = 'Profile calibration date and time'
        elif headerSignature == b'targ':  # 10
            tag_type.t1_marker = b'targ'
            tag_type.t2_name = 'charTargetTag'
            tag_type.t3_comment = 'Characterization target such as IT8/7.2'
        elif headerSignature == b'cprt':  # 11
            tag_type.t1_marker = b'cprt'
            tag_type.t2_name = 'copyrightTag'
            tag_type.t3_comment = 'An 8-bit byte containing one 7-bit ASCII code. The final byte is terminated with NULL'
        elif headerSignature == b'dmnd':  # 12
            tag_type.t1_marker = b'dmnd'
            tag_type.t2_name = 'deviceMfgDescTag'
            tag_type.t3_comment = 'Structure containing invariant and localizable versions of the device manufacturer for display.'
        elif headerSignature == b'dmdd':  # 13
            tag_type.t1_marker = b'dmdd'
            tag_type.t2_name = 'deviceModelDescTag'
            tag_type.t3_comment = 'Structure containing invariant and localizable versions of the device model for display'
        elif headerSignature == b'gamt':  # 14
            tag_type.t1_marker = b'gamt'
            tag_type.t2_name = 'gamutTag'
            tag_type.t3_comment = 'The CLUT tag'
        elif headerSignature == b'kTRC':  # 15
            tag_type.t1_marker = b'kTRC'
            tag_type.t2_name = 'grayTRCTag'
            tag_type.t3_comment = 'Gray tone reproduction curve'
        elif headerSignature == b'gXYZ':  # 16
            tag_type.t1_marker = b'gXYZ'
            tag_type.t2_name = 'greenColorantTag'
            tag_type.t3_comment = 'Relative XYZ values of green phosphor or colorant'
        elif headerSignature == b'gTRC':  # 17
            tag_type.t1_marker = b'gTRC'
            tag_type.t2_name = 'greenTRCTag'
            tag_type.t3_comment = 'Green channel tone reproduction curve'
        elif headerSignature == b'lumi':  # 18
            tag_type.t1_marker = b'lumi'
            tag_type.t2_name = 'luminanceTag'
            tag_type.t3_comment = 'Absolute luminance of devices is in candelas per meter squared as described by the Y channel.'
        elif headerSignature == b'meas':  # 19
            tag_type.t1_marker = b'meas'
            tag_type.t2_name = 'measurementTag'
            tag_type.t3_comment = 'Alternative measurement specification such as a D65 illuminant instead of the default D50'
        elif headerSignature == b'bkpt':  # 20
            tag_type.t1_marker = b'bkpt'
            tag_type.t2_name = 'mediaBlackPointTag'
            tag_type.t3_comment = 'This tag specifies the media black point and is used for generating absolute colorimetry.'
        elif headerSignature == b'wtpt':  # 21
            tag_type.t1_marker = b'wtpt'
            tag_type.t2_name = 'mediaWhitePointTag'
            tag_type.t3_comment = 'This tag specifies the media white point and is used for generating absolute colorimetry.'
        elif headerSignature == b'ncol':  # 22
            tag_type.t1_marker = b'ncol'
            tag_type.t2_name = 'namedColorTag'
            tag_type.t3_comment = 'Named color reference transformation for converting between named color sets and the profile connection space or device color spaces.'
        elif headerSignature == b'ncl2':  # 23
            tag_type.t1_marker = b'ncl2'
            tag_type.t2_name = 'namedColor2Tag'
            tag_type.t3_comment = 'Named color information providing a PCS and optional device representation for a list of named colors.'
        elif headerSignature == b'pre0':  # 24
            tag_type.t1_marker = b'pre0'
            tag_type.t2_name = 'preview0Tag'
            tag_type.t3_comment = 'Preview transformation from PCS to device space and back to the PCS: 8 bit or 16 bit data.'
        elif headerSignature == b'pre1':  # 25
            tag_type.t1_marker = b'pre1'
            tag_type.t2_name = 'preview1Tag'
            tag_type.t3_comment = 'Preview transformation from the PCS to device space and back to the PCS: 8 bit or 16 bit data.'
        elif headerSignature == b'pre2':  # 26
            tag_type.t1_marker = b'pre2'
            tag_type.t2_name = 'preview2Tag'
            tag_type.t3_comment = 'Preview transformation from PCS to device space and back to the PCS: 8 bit or 16 bit data.'
        elif headerSignature == b'desc':  # 27
            tag_type.t1_marker = b'desc'
            tag_type.t2_name = 'profileDescriptionTag'
            tag_type.t3_comment = 'Structure containing invariant and localizable versions of the profile description for display.'
        elif headerSignature == b'pseq':  # 28
            tag_type.t1_marker = b'pseq'
            tag_type.t2_name = 'profileSequenceDescTag'
            tag_type.t3_comment = 'Structure containing a description of the profile sequence from source to destination, typically used with the devicelink profile.'
        elif headerSignature == b'psd0':  # 29
            tag_type.t1_marker = b'psd0'
            tag_type.t2_name = 'ps2CRD0Tag'
            tag_type.t3_comment = 'PostScript Level 2 Type 1 color rendering dictionary (CRD) for the Perceptual rendering intent'
        elif headerSignature == b'psd1':  # 30
            tag_type.t1_marker = b'psd1'
            tag_type.t2_name = 'ps2CRD1Tag'
            tag_type.t3_comment = 'PostScript Level 2 Type 1 CRD for the RelativeColorimetric rendering intent.'
        elif headerSignature == b'psd2':  # 31
            tag_type.t1_marker = b'psd2'
            tag_type.t2_name = 'ps2CRD2Tag'
            tag_type.t3_comment = 'PostScript Level 2 Type 1 CRD for the Saturation rendering intent.'
        elif headerSignature == b'psd3':  # 32
            tag_type.t1_marker = b'psd3'
            tag_type.t2_name = 'ps2CRD3Tag'
            tag_type.t3_comment = 'PostScript Level 2 Type 1 CRD for the AbsoluteColorimetric rendering intent.'
        elif headerSignature == b'ps2s':  # 33
            tag_type.t1_marker = b'ps2s'
            tag_type.t2_name = 'ps2CSATag'
            tag_type.t3_comment = 'PostScript Level 2 color space array.'
        elif headerSignature == b'ps2i':  # 34
            tag_type.t1_marker = b'ps2i'
            tag_type.t2_name = 'ps2RenderingIntentTag'
            tag_type.t3_comment = 'PostScript Level 2 rendering intent.'
        elif headerSignature == b'rXYZ':  # 35
            tag_type.t1_marker = b'rXYZ'
            tag_type.t2_name = 'redColorantTag'
            tag_type.t3_comment = 'Relative XYZ values of red phosphor or colorant'
        elif headerSignature == b'rTRC':  # 36
            tag_type.t1_marker = b'rTRC'
            tag_type.t2_name = 'redTRCTag'
            tag_type.t3_comment = 'Red channel tone reproduction curve.'
        elif headerSignature == b'scrd':  # 37
            tag_type.t1_marker = b'scrd'
            tag_type.t2_name = 'screeningDescTag'
            tag_type.t3_comment = 'Structure containing invariant and localizable versions of the screening conditions'
        elif headerSignature == b'scrn':  # 38
            tag_type.t1_marker = b'scrn'
            tag_type.t2_name = 'screeningTag'
            tag_type.t3_comment = 'This tag contains screening information for a variable number of channels.'
        elif headerSignature == b'tech':  # 39
            tag_type.t1_marker = b'tech'
            tag_type.t2_name = 'technologyTag'
            tag_type.t3_comment = 'Device technology information such as CRT, Dye Sublimation, etc.'
        elif headerSignature == b'bfd ':  # 40
            tag_type.t1_marker = b'bfd '
            tag_type.t2_name = 'ucrbgTag'
            tag_type.t3_comment = 'Under color removal and black generation specification'
        elif headerSignature == b'vued':  # 41
            tag_type.t1_marker = b'vued'
            tag_type.t2_name = 'viewingCondDescTag'
            tag_type.t3_comment = 'Structure containing invariant and localizable versions of the viewing conditions'
        elif headerSignature == b'view':  # 42
            tag_type.t1_marker = b'view'
            tag_type.t2_name = 'viewingConditionsTag'
            tag_type.t3_comment = 'Viewing conditions parameters.'
        elif headerSignature == b'chad':  # 43
            tag_type.t1_marker = b'chad'
            tag_type.t2_name = 'chadTag'
            tag_type.t3_comment = 'Chadtag for conversion of D65 to D50 for use in profiles'
        else:
            tag_type.t2_name = 'Unknown'
            tag_type.t3_comment = 'has been not found the tag'
        return tag_type


    #
    @staticmethod
    def find_icc_data_type(data:bytes):
        if type1_curv.check(data):
            return type1_curv(bytesData=data)
        elif type2_data.check(data):
            return type2_data(bytesData=data)
        elif type3_datetime.check(data):
            return  type3_datetime(bytesData=data)
        elif type4_lut16.check(data):
            return type4_lut16(bytesData=data)
        elif type5_lut8.check(data):
            return type5_lut8(bytesData=data)
        elif type6_measurement.check(data):
            return type6_measurement(bytesData=data)
        elif type7_namedcolor.check(data):
            return type7_namedcolor(bytesData=data)
        elif type8_pseq.check(data):
            return type8_pseq(bytesData=data)
        elif type9_screening.check(data):
            return type9_screening(bytesData=data)
        elif type10_signature.check(data):
            return type10_signature(bytesData=data)
        elif type11_s15Fixed16Array.check(data):
            return type11_s15Fixed16Array(bytesData=data)
        elif type12_textDescription.check(data):
            return  type12_textDescription(bytesData=data)
        elif type13_text.check(data):
            return type13_text(bytesData=data)
        elif type14_u16Fixed16Array.check(data):
            return type14_u16Fixed16Array(bytesData=data)
        elif type15_ucrbg.check(data):
            return type15_ucrbg(bytesData=data)
        elif type16_uInt16Array.check(data):
            return  type16_uInt16Array(bytesData=data)
        elif type17_uInt32Array.check(data):
            return  type17_uInt32Array(bytesData=data)
        elif type18_uInt64Array.check(data):
            return type18_uInt64Array(bytesData=data)
        elif type19_uInt8Array.check(data):
            return type19_uInt8Array(bytesData=data)
        elif type20_viewingConditions.check(data):
            return type20_viewingConditions(bytesData=data)
        elif type21_XYZ.check(data):
            return type21_XYZ(bytesData=data)
        else:
            return icc_data_type()




class icc_data_type:
    #
    def __init__(self):
        self.t1_no = -1
        self.t2_marker = b''
        self.t3_name = 'Unknown'
        self.t4_data_start_offset = -1

    #
    def show(self):
        txt1 = '\tData Type No     : {:<2}'.format(self.t1_no)
        txt2 = '\tData Type Name   : {}'.format(self.t3_name)
        txt3 = '\tData Type Marker : {}'.format(self.t2_marker.hex(sep=' '))
        txt4 = '\tData Start Offset Index : {}'.format(self.t4_data_start_offset)
        print(txt1)
        print(txt2)
        print(txt3)
        print(txt4)

    #
    def all(self) -> str:
        txt1 = '\tData Type No     : {:<2}'.format(self.t1_no)
        txt2 = '\tData Type Name   : {}'.format(self.t3_name)
        txt3 = '\tData Type Marker : {}'.format(self.t2_marker.hex(sep=' '))
        txt4 = '\tData Start Offset Index : {}'.format(self.t4_data_start_offset)
        result = txt1 + '\n' + txt2 + '\n' + txt3 + '\n' + txt4
        return result


# (1) curv type
class type1_curv(icc_data_type):
    #
    @staticmethod
    def check(bytesData: bytes) -> bool:
        if len(bytesData) >= 12:
            return bytesData[0:4] == b'curv'
        else:
            return False

    #
    def __init__(self, bytesData: bytes):
        super().__init__()
        self.t1_no = 1
        self.t2_marker = bytesData[0:4]
        self.t3_name = 'curveType'
        self.t4_data_start_offset = 12
        self.t5_reserved = bytesData[4:8]
        self.t6_count = bytesData[8:12]
        self.t6_count_int = clength(self.t6_count)

    #
    def show(self):
        txt1 = '\tData Type No     : {:<2}'.format(self.t1_no)
        txt2 = '\tData Type Name   : {}'.format(self.t3_name)
        txt3 = '\tData Type Marker : {}'.format(self.t2_marker.hex(sep=' '))
        txt4 = '\tData Type Reserved      : {}'.format(self.t5_reserved.hex(sep=' '))
        txt5 = '\tData Type Count         : {}'.format(self.t6_count_int)
        txt6 = '\tData Start Offset Index : {}'.format(self.t4_data_start_offset)
        print(txt1)
        print(txt2)
        print(txt3)
        print(txt4)
        print(txt5)
        print(txt6)

    #
    def all(self) -> str:
        txt1 = '\tData Type No     : {:<2}'.format(self.t1_no)
        txt2 = '\tData Type Name   : {}'.format(self.t3_name)
        txt3 = '\tData Type Marker : {}'.format(self.t2_marker.hex(sep=' '))
        txt4 = '\tData Type Reserved      : {}'.format(self.t5_reserved.hex(sep=' '))
        txt5 = '\tData Type Count         : {}'.format(self.t6_count_int)
        txt6 = '\tData Start Offset Index : {}'.format(self.t4_data_start_offset)
        result = txt1 + '\n' + txt2 + '\n' + txt3 + '\n' + txt4 + '\n' + txt5 + '\n' + txt6
        return result


# (2) dataType
class type2_data(icc_data_type):
    #
    @staticmethod
    def check(bytesData: bytes) -> bool:
        if len(bytesData) >= 12:
            return bytesData[0:4] == b'data'
        else:
            return False

    #
    def __init__(self, bytesData: bytes):
        super().__init__()
        self.t1_no = 2
        self.t2_marker = bytesData[0:4]
        self.t3_name = 'dataType'
        self.t4_data_start_offset = 12
        self.t5_reserved = bytesData[4:8]
        self.t6_type_flag = bytesData[8:12]
        if self.t6_type_flag == b'\x00\x00\x00\x00':
            self.t6_type_flag_str = 'ASCII Data'
        elif self.t6_type_flag == b'\x00\x00\x00\x01':
            self.t6_type_flag_str = 'Binary Data'
        else:
            self.t6_type_flag_str = ''

    #
    def show(self):
        txt1 = '\tData Type No     : {:<2}'.format(self.t1_no)
        txt2 = '\tData Type Name   : {}'.format(self.t3_name)
        txt3 = '\tData Type Marker : {}'.format(self.t2_marker.hex(sep=' '))
        txt4 = '\tData Type Reserved      : {}'.format(self.t5_reserved.hex(sep=' '))
        txt5 = '\tData Type Flag          : {}'.format(self.t6_type_flag_str)
        txt6 = '\tData Start Offset Index : {}'.format(self.t4_data_start_offset)
        print(txt1)
        print(txt2)
        print(txt3)
        print(txt4)
        print(txt5)
        print(txt6)

    #
    def all(self):
        txt1 = '\tData Type No     : {:<2}'.format(self.t1_no)
        txt2 = '\tData Type Name   : {}'.format(self.t3_name)
        txt3 = '\tData Type Marker : {}'.format(self.t2_marker.hex(sep=' '))
        txt4 = '\tData Type Reserved      : {}'.format(self.t5_reserved.hex(sep=' '))
        txt5 = '\tData Type Flag          : {}'.format(self.t6_type_flag_str)
        txt6 = '\tData Start Offset Index : {}'.format(self.t4_data_start_offset)
        result = txt1 + '\n' + txt2 + '\n' + txt3 + '\n' + txt4 + '\n' + txt5 + '\n' + txt6
        return result


# (3) dateTimeType
class type3_datetime(icc_data_type):
    #
    @staticmethod
    def check(bytesData: bytes) -> bool:
        if len(bytesData) >= 12:
            return bytesData[0:4] == b'dtim'
        else:
            return False

    #
    def __init__(self, bytesData: bytes):
        super().__init__()
        self.t1_no = 3
        self.t2_marker = bytesData[0:4]
        self.t3_name = 'dateTimeType'
        self.t4_data_start_offset = 8
        self.t5_reserved = bytesData[4:8]
        self.t6_datetime = bytesData[8:20]
        self.t6_datetime_str = ICC_PROFILE.s10_func_icc_date_and_time(self.t6_datetime)

    #
    def show(self):
        txt1 = '\tData Type No     : {:<2}'.format(self.t1_no)
        txt2 = '\tData Type Name   : {}'.format(self.t3_name)
        txt3 = '\tData Type Marker : {}'.format(self.t2_marker.hex(sep=' '))
        txt4 = '\tData Type Reserved      : {}'.format(self.t5_reserved.hex(sep=' '))
        txt5 = '\tData Type Date and Type : {}'.format(self.t6_datetime_str)
        print(txt1)
        print(txt2)
        print(txt3)
        print(txt4)
        print(txt5)

    #
    def all(self):
        txt1 = '\tData Type No     : {:<2}'.format(self.t1_no)
        txt2 = '\tData Type Name   : {}'.format(self.t3_name)
        txt3 = '\tData Type Marker : {}'.format(self.t2_marker.hex(sep=' '))
        txt4 = '\tData Type Reserved      : {}'.format(self.t5_reserved.hex(sep=' '))
        txt5 = '\tData Type Date and Type : {}'.format(self.t6_datetime_str)
        result = txt1 + '\n' + txt2 + '\n' + txt3 + '\n' + txt4 + '\n' + txt5
        return result

# (4) lut16Type
class type4_lut16(icc_data_type):
    #
    @staticmethod
    def check(bytesData:bytes) -> bool:
        if len(bytesData) >= 12:
            return bytesData[0:4] == b'mft2'
        else:
            return False
    #
    def __init__(self, bytesData: bytes):
        super().__init__()
        self.t1_no = 4
        self.t2_marker = bytesData[0:4]
        self.t3_name =  'lut16Type'
        self.t4_data_start_offset = 12
        self.t5_reserved = bytesData[4:8]
        self.t6_input_channel = bytesData[8:9]
        self.t7_output_channel = bytesData[9:10]
        self.t8_clut_grid_points = bytesData[10:11]
        self.t9_type_padding = bytesData[11:12]

    #
    def show(self):
        txt1 = '\tData Type No     : {:<2}'.format(self.t1_no)
        txt2 = '\tData Type Name   : {}'.format(self.t3_name)
        txt3 = '\tData Type Marker : {}'.format(self.t2_marker.hex(sep=' '))
        txt4 = '\tData Type Reserved      : {}'.format( self.t5_reserved.hex(sep=' ') )
        txt5 = '\tData Input Channel      : {}'.format( self.t6_input_channel.hex(sep=' ') )
        txt6 = '\tData Output Channel     : {}'.format(self.t7_output_channel.hex(sep=' '))
        txt7 = '\tData Clut Grid Points   : {}'.format(self.t8_clut_grid_points.hex(sep=' '))
        txt8 = '\tData Padding            : {}'.format(self.t9_type_padding.hex(sep=' '))
        txt9 = '\tData Start Offset Index : {}'.format(self.t4_data_start_offset)
        print(txt1)
        print(txt2)
        print(txt3)
        print(txt4)
        print(txt5)
        print(txt6)
        print(txt7)
        print(txt8)
        print(txt9)

    #
    def all(self):
        txt1 = '\tData Type No     : {:<2}'.format(self.t1_no)
        txt2 = '\tData Type Name   : {}'.format(self.t3_name)
        txt3 = '\tData Type Marker : {}'.format(self.t2_marker.hex(sep=' '))
        txt4 = '\tData Type Reserved      : {}'.format( self.t5_reserved.hex(sep=' ') )
        txt5 = '\tData Input Channel      : {}'.format( self.t6_input_channel.hex(sep=' ') )
        txt6 = '\tData Output Channel     : {}'.format(self.t7_output_channel.hex(sep=' '))
        txt7 = '\tData Clut Grid Points   : {}'.format(self.t8_clut_grid_points.hex(sep=' '))
        txt8 = '\tData Padding            : {}'.format(self.t9_type_padding.hex(sep=' '))
        txt9 = '\tData Start Offset Index : {}'.format(self.t4_data_start_offset)
        result = txt1 + '\n' + txt2 + '\n' + txt3 + '\n' + txt4 + '\n' + txt5 + '\n' + txt6 + '\n' + txt7 + '\n' + txt8 + '\n' + txt9
        return result

# (5) lut8Type
class type5_lut8(icc_data_type):
    #
    @staticmethod
    def check(bytesData:bytes) -> bool:
        if len(bytesData) >= 12:
            return bytesData[0:4] == b'mft2'
        else:
            return False
    #
    def __init__(self, bytesData: bytes):
        super().__init__()
        self.t1_no = 5
        self.t2_marker = bytesData[0:4]
        self.t3_name =  'lut8Type'
        self.t4_data_start_offset = 12
        self.t5_reserved = bytesData[4:8]
        self.t6_input_channel = bytesData[8:9]
        self.t7_output_channel = bytesData[9:10]
        self.t8_clut_grid_points = bytesData[10:11]
        self.t9_type_padding = bytesData[11:12]

    #
    def show(self):
        txt1 = '\tData Type No     : {:<2}'.format(self.t1_no)
        txt2 = '\tData Type Name   : {}'.format(self.t3_name)
        txt3 = '\tData Type Marker : {}'.format(self.t2_marker.hex(sep=' '))
        txt4 = '\tData Type Reserved      : {}'.format( self.t5_reserved.hex(sep=' ') )
        txt5 = '\tData Input Channel      : {}'.format( self.t6_input_channel.hex(sep=' ') )
        txt6 = '\tData Output Channel     : {}'.format(self.t7_output_channel.hex(sep=' '))
        txt7 = '\tData Clut Grid Points   : {}'.format(self.t8_clut_grid_points.hex(sep=' '))
        txt8 = '\tData Padding            : {}'.format(self.t9_type_padding.hex(sep=' '))
        txt9 = '\tData Start Offset Index : {}'.format(self.t4_data_start_offset)
        print(txt1)
        print(txt2)
        print(txt3)
        print(txt4)
        print(txt5)
        print(txt6)
        print(txt7)
        print(txt8)
        print(txt9)

    #
    def all(self):
        txt1 = '\tData Type No     : {:<2}'.format(self.t1_no)
        txt2 = '\tData Type Name   : {}'.format(self.t3_name)
        txt3 = '\tData Type Marker : {}'.format(self.t2_marker.hex(sep=' '))
        txt4 = '\tData Type Reserved      : {}'.format( self.t5_reserved.hex(sep=' ') )
        txt5 = '\tData Input Channel      : {}'.format( self.t6_input_channel.hex(sep=' ') )
        txt6 = '\tData Output Channel     : {}'.format(self.t7_output_channel.hex(sep=' '))
        txt7 = '\tData Clut Grid Points   : {}'.format(self.t8_clut_grid_points.hex(sep=' '))
        txt8 = '\tData Padding            : {}'.format(self.t9_type_padding.hex(sep=' '))
        txt9 = '\tData Start Offset Index : {}'.format(self.t4_data_start_offset)
        result = txt1 + '\n' + txt2 + '\n' + txt3 + '\n' + txt4 + '\n' + txt5 + '\n' + txt6 + '\n' + txt7 + '\n' + txt8 + '\n' + txt9
        return result

# (6) measurementType
class type6_measurement(icc_data_type):
    #
    @staticmethod
    def check(bytesData:bytes) -> bool:
        if len(bytesData) >= 12:
            return bytesData[0:4] == b'meas'
        else:
            return False
    #
    def __init__(self, bytesData: bytes):
        super().__init__()
        self.t1_no = 6
        self.t2_marker = bytesData[0:4]
        self.t3_name = 'measurementType'
        self.t4_data_start_offset = 12
        self.t5_reserved = bytesData[4:8]
        self.t6_observer = bytesData[8:12]
        if self.t6_observer == b'\x00\x00\x00\x01':
            self.t6_observer_str = '1931 2 degree Observer'
        elif self.t6_observer == b'\x00\x00\x00\x02':
            self.t6_observer_str = '1964 10 degree Observer'
        else:
            self.t6_observer_str = 'unknown'

    #
    def show(self):
        txt1 = '\tData Type No     : {:<2}'.format(self.t1_no)
        txt2 = '\tData Type Name   : {}'.format(self.t3_name)
        txt3 = '\tData Type Marker : {}'.format(self.t2_marker.hex(sep=' '))
        txt4 = '\tData Type Reserved      : {}'.format( self.t5_reserved.hex(sep=' ') )
        txt5 = '\tData Observer (hex)     : {}'.format( self.t6_observer.hex(sep=' ') )
        txt6 = '\tData Observer (str)     : {}'.format(self.t6_observer_str  )
        txt7 = '\tData Start Offset Index : {}'.format(self.t4_data_start_offset)
        print(txt1)
        print(txt2)
        print(txt3)
        print(txt4)
        print(txt5)
        print(txt6)
        print(txt7)

    #
    def all(self):
        txt1 = '\tData Type No     : {:<2}'.format(self.t1_no)
        txt2 = '\tData Type Name   : {}'.format(self.t3_name)
        txt3 = '\tData Type Marker : {}'.format(self.t2_marker.hex(sep=' '))
        txt4 = '\tData Type Reserved      : {}'.format( self.t5_reserved.hex(sep=' ') )
        txt5 = '\tData Observer (hex)     : {}'.format( self.t6_observer.hex(sep=' ') )
        txt6 = '\tData Observer (str)     : {}'.format(self.t6_observer_str  )
        txt7 = '\tData Start Offset Index : {}'.format(self.t4_data_start_offset)
        result = txt1 + '\n' + txt2 + '\n' + txt3 + '\n' + txt4 + '\n' + txt5 + '\n' + txt6 + '\n' + txt7
        return result

# (7) namedColorType
class type7_namedcolor(icc_data_type):
    #
    @staticmethod
    def check(bytesData:bytes) -> bool:
        if len(bytesData) >= 12:
            return bytesData[0:4] == b'ncol'
        else:
            return False
    #
    def __init__(self, bytesData: bytes):
        super().__init__()
        self.t1_no = 7
        self.t2_marker = bytesData[0:4]
        self.t3_name =  'namedColorType'
        self.t4_data_start_offset = 8
        self.t5_reserved = bytesData[4:8]

    #
    def show(self):
        txt1 = '\tData Type No     : {:<2}'.format(self.t1_no)
        txt2 = '\tData Type Name   : {}'.format(self.t3_name)
        txt3 = '\tData Type Marker : {}'.format(self.t2_marker.hex(sep=' '))
        txt4 = '\tData Type Reserved      : {}'.format( self.t5_reserved.hex(sep=' ') )
        txt5 = '\tData Start Offset Index : {}'.format(self.t4_data_start_offset)
        print(txt1)
        print(txt2)
        print(txt3)
        print(txt4)
        print(txt5)

    #
    def all(self):
        txt1 = '\tData Type No     : {:<2}'.format(self.t1_no)
        txt2 = '\tData Type Name   : {}'.format(self.t3_name)
        txt3 = '\tData Type Marker : {}'.format(self.t2_marker.hex(sep=' '))
        txt4 = '\tData Type Reserved      : {}'.format( self.t5_reserved.hex(sep=' ') )
        txt5 = '\tData Start Offset Index : {}'.format(self.t4_data_start_offset)
        result = txt1 + '\n' + txt2 + '\n' + txt3 + '\n' + txt4 + '\n' + txt5
        return result

# (8) profileSequenceDescType
class  type8_pseq(icc_data_type):
    #
    @staticmethod
    def check(bytesData:bytes) -> bool:
        if len(bytesData) >= 12:
            return bytesData[0:4] == b'pseq'
        else:
            return False
    #
    def __init__(self, bytesData: bytes):
        super().__init__()
        self.t1_no = 8
        self.t2_marker = bytesData[0:4]
        self.t3_name = 'profileSequenceDescType'
        self.t4_data_start_offset = 12
        self.t5_reserved = bytesData[4:8]
        self.t6_count = bytesData[8:12]
        self.t6_count_int = clength(self.t6_count)

    #
    def show(self):
        txt1 = '\tData Type No     : {:<2}'.format(self.t1_no)
        txt2 = '\tData Type Name   : {}'.format(self.t3_name)
        txt3 = '\tData Type Marker : {}'.format(self.t2_marker.hex(sep=' '))
        txt4 = '\tData Type Reserved      : {}'.format(self.t5_reserved.hex(sep=' '))
        txt5 = '\tData Type Count         : {}'.format(self.t6_count_int)
        txt6 = '\tData Start Offset Index : {}'.format(self.t4_data_start_offset)
        print(txt1)
        print(txt2)
        print(txt3)
        print(txt4)
        print(txt5)
        print(txt6)

    #
    def all(self) -> str:
        txt1 = '\tData Type No     : {:<2}'.format(self.t1_no)
        txt2 = '\tData Type Name   : {}'.format(self.t3_name)
        txt3 = '\tData Type Marker : {}'.format(self.t2_marker.hex(sep=' '))
        txt4 = '\tData Type Reserved      : {}'.format(self.t5_reserved.hex(sep=' '))
        txt5 = '\tData Type Count         : {}'.format(self.t6_count_int)
        txt6 = '\tData Start Offset Index : {}'.format(self.t4_data_start_offset)
        result = txt1 + '\n' + txt2 + '\n' + txt3 + '\n' + txt4 + '\n' + txt5 + '\n' + txt6
        return result

# (9) screeningType
class  type9_screening(icc_data_type):
    #
    @staticmethod
    def check(bytesData:bytes) -> bool:
        if len(bytesData) >= 12:
            return bytesData[0:4] == b'scrn'
        else:
            return False
    #
    def __init__(self, bytesData: bytes):
        super().__init__()
        self.t1_no = 9
        self.t2_marker = bytesData[0:4]
        self.t3_name = 'screeningType'
        self.t4_data_start_offset = 8
        self.t5_reserved = bytesData[4:8]

    #
    def show(self):
        txt1 = '\tData Type No     : {:<2}'.format(self.t1_no)
        txt2 = '\tData Type Name   : {}'.format(self.t3_name)
        txt3 = '\tData Type Marker : {}'.format(self.t2_marker.hex(sep=' '))
        txt4 = '\tData Type Reserved      : {}'.format(self.t5_reserved.hex(sep=' '))
        txt5 = '\tData Start Offset Index : {}'.format(self.t4_data_start_offset)
        print(txt1)
        print(txt2)
        print(txt3)
        print(txt4)
        print(txt5)


    #
    def all(self) -> str:
        txt1 = '\tData Type No     : {:<2}'.format(self.t1_no)
        txt2 = '\tData Type Name   : {}'.format(self.t3_name)
        txt3 = '\tData Type Marker : {}'.format(self.t2_marker.hex(sep=' '))
        txt4 = '\tData Type Reserved      : {}'.format(self.t5_reserved.hex(sep=' '))
        txt5 = '\tData Start Offset Index : {}'.format(self.t4_data_start_offset)
        result = txt1 + '\n' + txt2 + '\n' + txt3 + '\n' + txt4 + '\n' + txt5
        return result


#
# (10) signatureType
class  type10_signature(icc_data_type):
    #
    @staticmethod
    def check(bytesData:bytes) -> bool:
        if len(bytesData) >= 12:
            return bytesData[0:4] == b'sig '
        else:
            return False
    #
    def __init__(self, bytesData: bytes):
        super().__init__()
        self.t1_no = 10
        self.t2_marker = bytesData[0:4]
        self.t3_name = 'signatureType'
        self.t4_data_start_offset = 8
        self.t5_reserved = bytesData[4:8]
        self.t6_data = bytesData[8:12]
        if self.t6_data == b'fscn':
            self.t6_data_str = 'Film Scanner'
        elif self.t6_data == b'dcam':
            self.t6_data_str = 'Digital Camera'
        elif self.t6_data== b'rscn':
            self.t6_data_str = 'Reflective Scanner'
        elif self.t6_data== b'ijet':
            self.t6_data_str = 'Ink Jet Printer'
        elif self.t6_data== b'twax':
            self.t6_data_str = 'Thermal Wax Printer'
        elif self.t6_data== b'epho':
            self.t6_data_str = 'Electrophotographic Printer'
        elif self.t6_data== b'esta':
            self.t6_data_str = 'Electrostatic Printer'
        elif self.t6_data== b'dsub':
            self.t6_data_str = 'Dye Sublimation Printer'
        elif self.t6_data== b'rpho':
            self.t6_data_str = 'Photographic Paper Printer'
        elif self.t6_data== b'fprn':
            self.t6_data_str = 'Film Writer'
        elif self.t6_data== b'vidm':
            self.t6_data_str = 'Video Monitor'
        elif self.t6_data== b'vidc':
            self.t6_data_str = 'Video Camera'
        elif self.t6_data== b'pjtv':
            self.t6_data_str = 'Projection Television'
        elif self.t6_data== b'CRT ':
            self.t6_data_str = 'Cathode Ray Tube Display'
        elif self.t6_data== b'PMD ':
            self.t6_data_str = 'Passive Matrix Display'
        elif self.t6_data== b'AMD ':
            self.t6_data_str = 'Active Matrix Display'
        elif self.t6_data== b'KPCD':
            self.t6_data_str = 'Photo CD'
        elif self.t6_data== b'imgs':
            self.t6_data_str = 'PhotoImageSetter'
        elif self.t6_data== b'grav':
            self.t6_data_str = 'Gravure'
        elif self.t6_data== b'offs':
            self.t6_data_str = 'Offset Lithography'
        elif self.t6_data== b'silk':
            self.t6_data_str = 'Silkscreen'
        elif self.t6_data== b'flex':
            self.t6_data_str = 'Flexography'
        else:
            self.t6_data_str = ''

    #
    def show(self):
        txt1 = '\tData Type No     : {:<2}'.format(self.t1_no)
        txt2 = '\tData Type Name   : {}'.format(self.t3_name)
        txt3 = '\tData Type Marker : {}'.format(self.t2_marker.hex(sep=' '))
        txt4 = '\tData Type Reserved      : {}'.format(self.t5_reserved.hex(sep=' '))
        txt5 = '\tData Type Data (hex)    : {}'.format( self.t6_data.hex(sep=' ') )
        txt6 = '\tData Type Data (str)    : {}'.format( self.t6_data_str )
        print(txt1)
        print(txt2)
        print(txt3)
        print(txt4)
        print(txt5)
        print(txt6)

    def all(self):
        txt1 = '\tData Type No     : {:<2}'.format(self.t1_no)
        txt2 = '\tData Type Name   : {}'.format(self.t3_name)
        txt3 = '\tData Type Marker : {}'.format(self.t2_marker.hex(sep=' '))
        txt4 = '\tData Type Reserved      : {}'.format(self.t5_reserved.hex(sep=' '))
        txt5 = '\tData Type Data (hex)    : {}'.format( self.t6_data.hex(sep=' ') )
        txt6 = '\tData Type Data (str)    : {}'.format( self.t6_data_str )
        result = txt1 + '\n' + txt2 + '\n' + txt3 + '\n' + txt4 + '\n' + txt5 + '\n' + txt6
        return result


# (11) s15Fixed16ArrayType
class type11_s15Fixed16Array(icc_data_type):
    #
    @staticmethod
    def check(bytesData: bytes) -> bool:
        if len(bytesData) >= 12:
            return bytesData[0:4] == b'sf32'
        else:
            return False

    #
    def __init__(self, bytesData: bytes):
        super().__init__()
        self.t1_no = 11
        self.t2_marker = bytesData[0:4]
        self.t3_name = 's15Fixed16ArrayType'
        self.t4_data_start_offset = 8
        self.t5_reserved = bytesData[4:8]

    #
    def show(self):
        txt1 = '\tData Type No     : {:<2}'.format(self.t1_no)
        txt2 = '\tData Type Name   : {}'.format(self.t3_name)
        txt3 = '\tData Type Marker : {}'.format(self.t2_marker.hex(sep=' '))
        txt4 = '\tData Type Reserved      : {}'.format(self.t5_reserved.hex(sep=' '))
        txt5 = '\tData Start Offset Index : {}'.format(self.t4_data_start_offset)
        print(txt1)
        print(txt2)
        print(txt3)
        print(txt4)
        print(txt5)

    #
    def all(self) -> str:
        txt1 = '\tData Type No     : {:<2}'.format(self.t1_no)
        txt2 = '\tData Type Name   : {}'.format(self.t3_name)
        txt3 = '\tData Type Marker : {}'.format(self.t2_marker.hex(sep=' '))
        txt4 = '\tData Type Reserved      : {}'.format(self.t5_reserved.hex(sep=' '))
        txt5 = '\tData Start Offset Index : {}'.format(self.t4_data_start_offset)
        result = txt1 + '\n' + txt2 + '\n' + txt3 + '\n' + txt4 + '\n' + txt5
        return result


# (12) textDescriptionType
class type12_textDescription(icc_data_type):
    #
    @staticmethod
    def check(bytesData: bytes) -> bool:
        if len(bytesData) >= 12:
            return bytesData[0:4] == b'desc'
        else:
            return False

    #
    def __init__(self, bytesData: bytes):
        super().__init__()
        self.t1_no = 12
        self.t2_marker = bytesData[0:4]
        self.t3_name = 'textDescriptionType'
        self.t4_data_start_offset = 12
        self.t5_reserved = bytesData[4:8]
        self.t6_description_length = bytesData[8:12]
        self.t6_description_length_int = clength(self.t6_description_length)

    #
    def show(self):
        txt1 = '\tData Type No     : {:<2}'.format(self.t1_no)
        txt2 = '\tData Type Name   : {}'.format(self.t3_name)
        txt3 = '\tData Type Marker : {}'.format(self.t2_marker.hex(sep=' '))
        txt4 = '\tData Type Reserved                 : {}'.format(self.t5_reserved.hex(sep=' '))
        txt5 = '\tData Start Offset Index            : {}'.format(self.t4_data_start_offset)
        txt6 = '\tData Type Description Length (hex) : {}'.format(self.t6_description_length.hex(sep=' '))
        txt7 = '\tData Type Description Length (str) : {}'.format(self.t6_description_length_int )
        txt8 = '\tData End Offset Index              : {}'.format( self.t6_description_length_int+self.t4_data_start_offset )
        print(txt1)
        print(txt2)
        print(txt3)
        print(txt4)
        print(txt5)
        print(txt6)
        print(txt7)
        print(txt8)

    #
    def all(self) -> str:
        txt1 = '\tData Type No     : {:<2}'.format(self.t1_no)
        txt2 = '\tData Type Name   : {}'.format(self.t3_name)
        txt3 = '\tData Type Marker : {}'.format(self.t2_marker.hex(sep=' '))
        txt4 = '\tData Type Reserved                 : {}'.format(self.t5_reserved.hex(sep=' '))
        txt5 = '\tData Start Offset Index            : {}'.format(self.t4_data_start_offset)
        txt6 = '\tData Type Description Length (hex) : {}'.format(self.t6_description_length.hex(sep=' '))
        txt7 = '\tData Type Description Length (str) : {}'.format(self.t6_description_length_int )
        txt8 = '\tData End Offset Index (str)        : {}'.format( self.t6_description_length_int+self.t4_data_start_offset )
        result = txt1 + '\n' + txt2 + '\n' + txt3 + '\n' + txt4 + '\n' + txt5 + '\n' + txt6 + '\n' + txt7 + '\n' + txt8
        return result

# (13) textType
class type13_text(icc_data_type):
    #
    @staticmethod
    def check(bytesData: bytes) -> bool:
        if len(bytesData) >= 12:
            return bytesData[0:4] == b'text'
        else:
            return False

    #
    def __init__(self, bytesData: bytes):
        super().__init__()
        self.t1_no = 13
        self.t2_marker = bytesData[0:4]
        self.t3_name = 'textType'
        self.t4_data_start_offset = 8
        self.t5_reserved = bytesData[4:8]

    #
    def show(self):
        txt1 = '\tData Type No     : {:<2}'.format(self.t1_no)
        txt2 = '\tData Type Name   : {}'.format(self.t3_name)
        txt3 = '\tData Type Marker : {}'.format(self.t2_marker.hex(sep=' '))
        txt4 = '\tData Type Reserved      : {}'.format(self.t5_reserved.hex(sep=' '))
        txt5 = '\tData Start Offset Index : {}'.format(self.t4_data_start_offset)
        print(txt1)
        print(txt2)
        print(txt3)
        print(txt4)
        print(txt5)

    #
    def all(self) -> str:
        txt1 = '\tData Type No     : {:<2}'.format(self.t1_no)
        txt2 = '\tData Type Name   : {}'.format(self.t3_name)
        txt3 = '\tData Type Marker : {}'.format(self.t2_marker.hex(sep=' '))
        txt4 = '\tData Type Reserved      : {}'.format(self.t5_reserved.hex(sep=' '))
        txt5 = '\tData Start Offset Index : {}'.format(self.t4_data_start_offset)
        result = txt1 + '\n' + txt2 + '\n' + txt3 + '\n' + txt4 + '\n' + txt5
        return result

# (14) u16Fixed16ArrayType
class type14_u16Fixed16Array(icc_data_type):
    #
    @staticmethod
    def check(bytesData: bytes) -> bool:
        if len(bytesData) >= 12:
            return bytesData[0:4] == b'uf32'
        else:
            return False

    #
    def __init__(self, bytesData: bytes):
        super().__init__()
        self.t1_no = 14
        self.t2_marker = bytesData[0:4]
        self.t3_name = 'u16Fixed16ArrayType'
        self.t4_data_start_offset = 8
        self.t5_reserved = bytesData[4:8]

    def show(self):
        txt1 = '\tData Type No     : {:<2}'.format(self.t1_no)
        txt2 = '\tData Type Name   : {}'.format(self.t3_name)
        txt3 = '\tData Type Marker : {}'.format(self.t2_marker.hex(sep=' '))
        txt4 = '\tData Type Reserved      : {}'.format(self.t5_reserved.hex(sep=' '))
        txt5 = '\tData Start Offset Index : {}'.format(self.t4_data_start_offset)
        print(txt1)
        print(txt2)
        print(txt3)
        print(txt4)
        print(txt5)

    #
    def all(self) -> str:
        txt1 = '\tData Type No     : {:<2}'.format(self.t1_no)
        txt2 = '\tData Type Name   : {}'.format(self.t3_name)
        txt3 = '\tData Type Marker : {}'.format(self.t2_marker.hex(sep=' '))
        txt4 = '\tData Type Reserved      : {}'.format(self.t5_reserved.hex(sep=' '))
        txt5 = '\tData Start Offset Index : {}'.format(self.t4_data_start_offset)
        result = txt1 + '\n' + txt2 + '\n' + txt3 + '\n' + txt4 + '\n' + txt5
        return result




#
# (15) ucrbgType
class type15_ucrbg(icc_data_type):
    #
    @staticmethod
    def check(bytesData: bytes) -> bool:
        if len(bytesData) >= 12:
            return bytesData[0:4] == b'bfd '
        else:
            return False

    #
    def __init__(self, bytesData: bytes):
        super().__init__()
        self.t1_no = 15
        self.t2_marker = bytesData[0:4]
        self.t3_name = 'ucrbgType'
        self.t4_data_start_offset = 12
        self.t5_reserved = bytesData[4:8]
        self.t6_count = bytesData[8:12]
        self.t6_count_int = clength(self.t6_count)

    #
    def show(self):
        txt1 = '\tData Type No     : {:<2}'.format(self.t1_no)
        txt2 = '\tData Type Name   : {}'.format(self.t3_name)
        txt3 = '\tData Type Marker : {}'.format(self.t2_marker.hex(sep=' '))
        txt4 = '\tData Type Reserved      : {}'.format(self.t5_reserved.hex(sep=' '))
        txt5 = '\tData Type Count         : {}'.format(self.t6_count_int)
        txt6 = '\tData Start Offset Index : {}'.format(self.t4_data_start_offset)
        print(txt1)
        print(txt2)
        print(txt3)
        print(txt4)
        print(txt5)
        print(txt6)

    #
    def all(self) -> str:
        txt1 = '\tData Type No     : {:<2}'.format(self.t1_no)
        txt2 = '\tData Type Name   : {}'.format(self.t3_name)
        txt3 = '\tData Type Marker : {}'.format(self.t2_marker.hex(sep=' '))
        txt4 = '\tData Type Reserved      : {}'.format(self.t5_reserved.hex(sep=' '))
        txt5 = '\tData Type Count         : {}'.format(self.t6_count_int)
        txt6 = '\tData Start Offset Index : {}'.format(self.t4_data_start_offset)
        result = txt1 + '\n' + txt2 + '\n' + txt3 + '\n' + txt4 + '\n' + txt5 + '\n' + txt6
        return result

#
# (16) uInt16ArrayType
class type16_uInt16Array(icc_data_type):
    #
    @staticmethod
    def check(bytesData: bytes) -> bool:
        if len(bytesData) >= 12:
            return bytesData[0:4] == b'ui16'
        else:
            return False

    #
    def __init__(self, bytesData: bytes):
        super().__init__()
        self.t1_no = 16
        self.t2_marker = bytesData[0:4]
        self.t3_name = 'uInt16ArrayType'
        self.t4_data_start_offset = 8
        self.t5_reserved = bytesData[4:8]


    def show(self):
        txt1 = '\tData Type No     : {:<2}'.format(self.t1_no)
        txt2 = '\tData Type Name   : {}'.format(self.t3_name)
        txt3 = '\tData Type Marker : {}'.format(self.t2_marker.hex(sep=' '))
        txt4 = '\tData Type Reserved      : {}'.format(self.t5_reserved.hex(sep=' '))
        txt5 = '\tData Start Offset Index : {}'.format(self.t4_data_start_offset)
        print(txt1)
        print(txt2)
        print(txt3)
        print(txt4)
        print(txt5)

    #
    def all(self) -> str:
        txt1 = '\tData Type No     : {:<2}'.format(self.t1_no)
        txt2 = '\tData Type Name   : {}'.format(self.t3_name)
        txt3 = '\tData Type Marker : {}'.format(self.t2_marker.hex(sep=' '))
        txt4 = '\tData Type Reserved      : {}'.format(self.t5_reserved.hex(sep=' '))
        txt5 = '\tData Start Offset Index : {}'.format(self.t4_data_start_offset)
        result = txt1 + '\n' + txt2 + '\n' + txt3 + '\n' + txt4 + '\n' + txt5
        return result

#
# (17) uInt32ArrayType
class type17_uInt32Array(icc_data_type):
    #
    @staticmethod
    def check(bytesData: bytes) -> bool:
        if len(bytesData) >= 12:
            return bytesData[0:4] == b'ui32'
        else:
            return False

    #
    def __init__(self, bytesData: bytes):
        super().__init__()
        self.t1_no = 17
        self.t2_marker = bytesData[0:4]
        self.t3_name = 'uInt32ArrayType'
        self.t4_data_start_offset = 8
        self.t5_reserved = bytesData[4:8]

    def show(self):
        txt1 = '\tData Type No     : {:<2}'.format(self.t1_no)
        txt2 = '\tData Type Name   : {}'.format(self.t3_name)
        txt3 = '\tData Type Marker : {}'.format(self.t2_marker.hex(sep=' '))
        txt4 = '\tData Type Reserved      : {}'.format(self.t5_reserved.hex(sep=' '))
        txt5 = '\tData Start Offset Index : {}'.format(self.t4_data_start_offset)
        print(txt1)
        print(txt2)
        print(txt3)
        print(txt4)
        print(txt5)

    #
    def all(self) -> str:
        txt1 = '\tData Type No     : {:<2}'.format(self.t1_no)
        txt2 = '\tData Type Name   : {}'.format(self.t3_name)
        txt3 = '\tData Type Marker : {}'.format(self.t2_marker.hex(sep=' '))
        txt4 = '\tData Type Reserved      : {}'.format(self.t5_reserved.hex(sep=' '))
        txt5 = '\tData Start Offset Index : {}'.format(self.t4_data_start_offset)
        result = txt1 + '\n' + txt2 + '\n' + txt3 + '\n' + txt4 + '\n' + txt5
        return result


# (18) uInt64ArrayType
class type18_uInt64Array(icc_data_type):
    #
    @staticmethod
    def check(bytesData: bytes) -> bool:
        if len(bytesData) >= 12:
            return bytesData[0:4] == b'ui64'
        else:
            return False

    #
    def __init__(self, bytesData: bytes):
        super().__init__()
        self.t1_no = 18
        self.t2_marker = bytesData[0:4]
        self.t3_name = 'uInt64ArrayType'
        self.t4_data_start_offset = 8
        self.t5_reserved = bytesData[4:8]

    def show(self):
        txt1 = '\tData Type No     : {:<2}'.format(self.t1_no)
        txt2 = '\tData Type Name   : {}'.format(self.t3_name)
        txt3 = '\tData Type Marker : {}'.format(self.t2_marker.hex(sep=' '))
        txt4 = '\tData Type Reserved      : {}'.format(self.t5_reserved.hex(sep=' '))
        txt5 = '\tData Start Offset Index : {}'.format(self.t4_data_start_offset)
        print(txt1)
        print(txt2)
        print(txt3)
        print(txt4)
        print(txt5)

    #
    def all(self) -> str:
        txt1 = '\tData Type No     : {:<2}'.format(self.t1_no)
        txt2 = '\tData Type Name   : {}'.format(self.t3_name)
        txt3 = '\tData Type Marker : {}'.format(self.t2_marker.hex(sep=' '))
        txt4 = '\tData Type Reserved      : {}'.format(self.t5_reserved.hex(sep=' '))
        txt5 = '\tData Start Offset Index : {}'.format(self.t4_data_start_offset)
        result = txt1 + '\n' + txt2 + '\n' + txt3 + '\n' + txt4 + '\n' + txt5
        return result

#
# (19) uInt8ArrayType
class type19_uInt8Array(icc_data_type):
    #
    @staticmethod
    def check(bytesData: bytes) -> bool:
        if len(bytesData) >= 12:
            return bytesData[0:4] == b'ui08'
        else:
            return False

    #
    def __init__(self, bytesData: bytes):
        super().__init__()
        self.t1_no = 19
        self.t2_marker = bytesData[0:4]
        self.t3_name = 'uInt8ArrayType'
        self.t4_data_start_offset = 8
        self.t5_reserved = bytesData[4:8]

    #
    def show(self):
        txt1 = '\tData Type No     : {:<2}'.format(self.t1_no)
        txt2 = '\tData Type Name   : {}'.format(self.t3_name)
        txt3 = '\tData Type Marker : {}'.format(self.t2_marker.hex(sep=' '))
        txt4 = '\tData Type Reserved      : {}'.format(self.t5_reserved.hex(sep=' '))
        txt5 = '\tData Start Offset Index : {}'.format(self.t4_data_start_offset)
        print(txt1)
        print(txt2)
        print(txt3)
        print(txt4)
        print(txt5)

    #
    def all(self) -> str:
        txt1 = '\tData Type No     : {:<2}'.format(self.t1_no)
        txt2 = '\tData Type Name   : {}'.format(self.t3_name)
        txt3 = '\tData Type Marker : {}'.format(self.t2_marker.hex(sep=' '))
        txt4 = '\tData Type Reserved      : {}'.format(self.t5_reserved.hex(sep=' '))
        txt5 = '\tData Start Offset Index : {}'.format(self.t4_data_start_offset)
        result = txt1 + '\n' + txt2 + '\n' + txt3 + '\n' + txt4 + '\n' + txt5
        return result

# (20) viewingConditionsType
class type20_viewingConditions(icc_data_type):
    #
    @staticmethod
    def check(bytesData: bytes) -> bool:
        if len(bytesData) >= 12:
            return bytesData[0:4] == b'view'
        else:
            return False

    #
    def __init__(self, bytesData: bytes):
        super().__init__()
        self.t1_no = 20
        self.t2_marker = bytesData[0:4]
        self.t3_name = 'viewingConditionsType'
        self.t4_data_start_offset = 8
        self.t5_reserved = bytesData[4:8]

    #
    def show(self):
        txt1 = '\tData Type No     : {:<2}'.format(self.t1_no)
        txt2 = '\tData Type Name   : {}'.format(self.t3_name)
        txt3 = '\tData Type Marker : {}'.format(self.t2_marker.hex(sep=' '))
        txt4 = '\tData Type Reserved      : {}'.format(self.t5_reserved.hex(sep=' '))
        txt5 = '\tData Start Offset Index : {}'.format(self.t4_data_start_offset)
        print(txt1)
        print(txt2)
        print(txt3)
        print(txt4)
        print(txt5)

    #
    def all(self) -> str:
        txt1 = '\tData Type No     : {:<2}'.format(self.t1_no)
        txt2 = '\tData Type Name   : {}'.format(self.t3_name)
        txt3 = '\tData Type Marker : {}'.format(self.t2_marker.hex(sep=' '))
        txt4 = '\tData Type Reserved      : {}'.format(self.t5_reserved.hex(sep=' '))
        txt5 = '\tData Start Offset Index : {}'.format(self.t4_data_start_offset)
        result = txt1 + '\n' + txt2 + '\n' + txt3 + '\n' + txt4 + '\n' + txt5
        return result

#
# (21) XYZType
class type21_XYZ(icc_data_type):
    #
    @staticmethod
    def check(bytesData: bytes) -> bool:
        if len(bytesData) >= 12:
            return bytesData[0:4] == b'XYZ '
        else:
            return False

    #
    def __init__(self, bytesData: bytes):
        super().__init__()
        self.t1_no = 21
        self.t2_marker = bytesData[0:4]
        self.t3_name = 'XYZType'
        self.t4_data_start_offset = 8
        self.t5_reserved = bytesData[4:8]

    #
    def show(self):
        txt1 = '\tData Type No     : {:<2}'.format(self.t1_no)
        txt2 = '\tData Type Name   : {}'.format(self.t3_name)
        txt3 = '\tData Type Marker : {}'.format(self.t2_marker.hex(sep=' '))
        txt4 = '\tData Type Reserved      : {}'.format(self.t5_reserved.hex(sep=' '))
        txt5 = '\tData Start Offset Index : {}'.format(self.t4_data_start_offset)
        print(txt1)
        print(txt2)
        print(txt3)
        print(txt4)
        print(txt5)

    #
    def all(self) -> str:
        txt1 = '\tData Type No     : {:<2}'.format(self.t1_no)
        txt2 = '\tData Type Name   : {}'.format(self.t3_name)
        txt3 = '\tData Type Marker : {}'.format(self.t2_marker.hex(sep=' '))
        txt4 = '\tData Type Reserved      : {}'.format(self.t5_reserved.hex(sep=' '))
        txt5 = '\tData Start Offset Index : {}'.format(self.t4_data_start_offset)
        result = txt1 + '\n' + txt2 + '\n' + txt3 + '\n' + txt4 + '\n' + txt5
        return result