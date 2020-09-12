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
# (Type) Data Store
class Kind:
    # data (type) kind store
    def __init__(self, item:object=None):
        if item == None:
            self.no = 0
            self.marker = b''
            self.name = ''
            self.shortname = ''
        else:
            self.no = item.no
            self.marker = item.marker
            self.name = item.name
            self.shortname = item.shortname

    #
    # (1)
    @staticmethod
    def SOI():
        obj = Kind()
        obj.no = 1
        obj.marker = b'\xff\xd8'
        obj.shortname = 'SOI'
        obj.name = 'Start Of Image'
        return obj

    #
    # (2)
    @staticmethod
    def APP0():
        obj = Kind()
        obj.no = 2
        obj.marker = b'\xff\xe0'
        obj.shortname = 'APP0'
        obj.name = 'Application Specific (0)'
        return obj

    #
    # (3)
    @staticmethod
    def APP1():
        obj = Kind()
        obj.no = 3
        obj.marker = b'\xff\xe1'
        obj.shortname = 'APP1'
        obj.name = 'Application Specific (1)'
        return obj

    #
    # (4)
    @staticmethod
    def APP2():
        obj = Kind()
        obj.no = 4
        obj.marker = b'\xff\xe2'
        obj.shortname = 'APP2'
        obj.name = 'Application Specific (2)'
        return obj

    #
    # (5)
    @staticmethod
    def APP3():
        obj = Kind()
        obj.no = 5
        obj.marker = b'\xff\xe3'
        obj.shortname = 'APP3'
        obj.name = 'Application Specific (3)'
        return obj

    #
    # (6)
    @staticmethod
    def APP4():
        obj = Kind()
        obj.no = 6
        obj.marker = b'\xff\xe4'
        obj.shortname = 'APP4'
        obj.name = 'Application Specific (4)'
        return obj

    #
    # (7)
    @staticmethod
    def APP5():
        obj = Kind()
        obj.no = 7
        obj.marker = b'\xff\xe5'
        obj.shortname = 'APP5'
        obj.name = 'Application Specific (5)'
        return obj

    #
    # (8)
    @staticmethod
    def APP6():
        obj = Kind()
        obj.no = 8
        obj.marker = b'\xff\xe6'
        obj.shortname = 'APP6'
        obj.name = 'Application Specific (6)'
        return obj

    #
    # (9)
    @staticmethod
    def APP7():
        obj = Kind()
        obj.no = 9
        obj.marker = b'\xff\xe7'
        obj.shortname = 'APP7'
        obj.name = 'Application Specific (7)'
        return obj

    #
    # (10)
    @staticmethod
    def APP8():
        obj = Kind()
        obj.no = 10
        obj.marker = b'\xff\xe8'
        obj.shortname = 'APP8'
        obj.name = 'Application Specific (8)'
        return obj

    #
    # (11)
    @staticmethod
    def APP9():
        obj = Kind()
        obj.no = 11
        obj.marker = b'\xff\xe9'
        obj.shortname = 'APP9'
        obj.name = 'Application Specific (9)'
        return obj

    #
    # (12)
    @staticmethod
    def APPA():
        obj = Kind()
        obj.no = 12
        obj.marker = b'\xff\xea'
        obj.shortname = 'APPA'
        obj.name = 'Application Specific (10)'
        return obj

    #
    # (13)
    @staticmethod
    def APPB():
        obj = Kind()
        obj.no = 13
        obj.marker = b'\xff\xeb'
        obj.shortname = 'APPB'
        obj.name = 'Application Specific (11)'
        return obj

    #
    # (14)
    @staticmethod
    def APPC():
        obj = Kind()
        obj.no = 14
        obj.marker = b'\xff\xec'
        obj.shortname = 'APPC'
        obj.name = 'Application Specific (12)'
        return obj

    #
    # (15)
    @staticmethod
    def APPD():
        obj = Kind()
        obj.no = 15
        obj.marker = b'\xff\xed'
        obj.shortname = 'APPD'
        obj.name = 'Application Specific (13)'
        return obj

    #
    # (16)
    @staticmethod
    def APPE():
        obj = Kind()
        obj.no = 16
        obj.marker = b'\xff\xee'
        obj.shortname = 'APPE'
        obj.name = 'Application Specific (14)'
        return obj

    #
    # (17)
    @staticmethod
    def APPF():
        obj = Kind()
        obj.no = 17
        obj.marker = b'\xff\xef'
        obj.shortname = 'APPF'
        obj.name = 'Application Specific (15)'
        return obj

    #
    # (18)
    @staticmethod
    def COM():
        obj = Kind()
        obj.no = 18
        obj.marker = b'\xff\xfe'
        obj.shortname = 'COM'
        obj.name = 'Comment'
        return obj

    #
    # (19)
    @staticmethod
    def SOF0():
        obj = Kind()
        obj.no = 19
        obj.marker = b'\xff\xc0'
        obj.shortname = 'SOF0'
        obj.name = 'Start Of Frame (Baseline DCT)'
        return obj

    #
    # (20)
    @staticmethod
    def SOF2():
        obj = Kind()
        obj.no = 20
        obj.marker = b'\xff\xc2'
        obj.shortname = 'SOF2'
        obj.name = 'Start Of Frame (Progressive DCT)'
        return obj

    #
    # (21)
    @staticmethod
    def DHT():
        obj = Kind()
        obj.no = 21
        obj.marker = b'\xff\xc4'
        obj.shortname = 'DHT'
        obj.name = 'Define Huffman Table(s)'
        return obj

    #
    # (22)
    @staticmethod
    def DQT():
        obj = Kind()
        obj.no = 22
        obj.marker = b'\xff\xdb'
        obj.shortname = 'DQT'
        obj.name = 'Define Quantization Table(s)'
        return obj

    #
    # (23)
    @staticmethod
    def DRI():
        obj = Kind()
        obj.no = 23
        obj.marker = b'\xff\xdd'
        obj.shortname = 'DRI'
        obj.name = 'Define Restart Interval'
        return obj

    #
    # (24)
    @staticmethod
    def SOS():
        obj = Kind()
        obj.no = 24
        obj.marker = b'\xff\xda'
        obj.shortname = 'SOS'
        obj.name = 'Start Of Scan'
        return obj

    #
    # (25)
    @staticmethod
    def RST0():
        obj = Kind()
        obj.no = 25
        obj.marker = b'\xff\xd0'
        obj.shortname = 'RST0'
        obj.name = 'Restart (r0 macroblock)'
        return obj

    #
    # (26)
    @staticmethod
    def RST1():
        obj = Kind()
        obj.no = 26
        obj.marker = b'\xff\xd1'
        obj.shortname = 'RST1'
        obj.name = 'Restart (r1 macroblock)'
        return obj

    #
    # (27)
    @staticmethod
    def RST2():
        obj = Kind()
        obj.no = 27
        obj.marker = b'\xff\xd2'
        obj.shortname = 'RST2'
        obj.name = 'Restart (r2 macroblock)'
        return obj

    #
    # (28)
    @staticmethod
    def RST3():
        obj = Kind()
        obj.no = 28
        obj.marker = b'\xff\xd3'
        obj.shortname = 'RST3'
        obj.name = 'Restart (r3 macroblock)'
        return obj

    #
    # (29)
    @staticmethod
    def RST4():
        obj = Kind()
        obj.no = 29
        obj.marker = b'\xff\xd4'
        obj.shortname = 'RST4'
        obj.name = 'Restart (r4 macroblock)'
        return obj

    #
    # (30)
    @staticmethod
    def RST5():
        obj = Kind()
        obj.no = 30
        obj.marker = b'\xff\xd5'
        obj.shortname = 'RST5'
        obj.name = 'Restart (r5 macroblock)'
        return obj

    #
    # (31)
    @staticmethod
    def RST6():
        obj = Kind()
        obj.no = 31
        obj.marker = b'\xff\xd6'
        obj.shortname = 'RST6'
        obj.name = 'Restart (r6 macroblock)'
        return obj

    #
    # (32)
    @staticmethod
    def RST7():
        obj = Kind()
        obj.no = 32
        obj.marker = b'\xff\xd7'
        obj.shortname = 'RST7'
        obj.name = 'Restart (r7 macroblock)'
        return obj

    #
    # (33)
    @staticmethod
    def EOI():
        obj = Kind()
        obj.no = 33
        obj.marker = b'\xff\xd9'
        obj.shortname = 'EOI'
        obj.name = 'End Of Image'
        return obj

    #
    # find Type
    # Only [-> APP0-APPF and COM <-]
    def findType( bytesData:bytes ):
        if bytesData == Kind.APP0().marker:
            return Kind.APP0()
        elif bytesData == Kind.APP1().marker:
            return Kind.APP1()
        elif bytesData == Kind.APP2().marker:
            return Kind.APP2()
        elif bytesData == Kind.APP3().marker:
            return  Kind.APP3()
        elif bytesData == Kind.APP4().marker:
            return Kind.APP4()
        elif bytesData == Kind.APP5().marker:
            return  Kind.APP5()
        elif bytesData == Kind.APP6().marker:
            return Kind.APP6()
        elif bytesData == Kind.APP7().marker:
            return Kind.APP7()
        elif bytesData == Kind.APP8().marker:
            return Kind.APP8()
        elif bytesData == Kind.APP9().marker:
            return  Kind.APP9()
        elif bytesData == Kind.APPA().marker:
            return  Kind.APPA()
        elif bytesData == Kind.APPB().marker:
            return Kind.APPB()
        elif bytesData == Kind.APPC().marker:
            return Kind.APPC()
        elif bytesData == Kind.APPD().marker:
            return Kind.APPD()
        elif bytesData == Kind.APPE().marker:
            return Kind.APPE()
        elif bytesData == Kind.APPF().marker:
            return Kind.APPF()
        elif bytesData == Kind.COM().marker:
            return Kind.COM()
