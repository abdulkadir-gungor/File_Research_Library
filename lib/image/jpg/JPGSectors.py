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
from typing import List
from lib.image.jpg.sector import Sector
from lib.image.jpg.kind import Kind
from lib.image.jpg.data_calculate.BigUnsignedLength import BigUnsignedLength as appLength

def findSectors(jpgBytes: bytes) -> List[Sector]:
    #
    jpgSectors_tmp = []
    jpgDataLength = len(jpgBytes)
    checkLength = jpgDataLength - 1
    itemCount = 1
    #

    # 1) SOI 'Start Of Image'   - 2 bayt
    startIndex = 0
    tmp_kind = Kind.SOI()
    while True:
        tmp_index = jpgBytes[startIndex:].find(tmp_kind.marker)
        if tmp_index == -1:
            break
        startIndex += tmp_index
        #
        item = Sector()
        item.no = itemCount
        item.start = startIndex
        item.end = startIndex + 2
        item.root = 0
        item.type = tmp_kind
        jpgSectors_tmp.append(item)
        #
        itemCount += 1
        startIndex += 2
        #
        if startIndex > checkLength:
            break
        #

    # 2) EOI 'End Of Image'    - 2 bayt
    startIndex = 0
    tmp_kind = Kind.EOI()
    while True:
        tmp_index = jpgBytes[startIndex:].find(tmp_kind.marker)
        if tmp_index == -1:
            break
        startIndex += tmp_index
        #
        item = Sector()
        item.no = itemCount
        item.start = startIndex
        item.end = startIndex + 2
        item.root = 0
        item.type = tmp_kind
        jpgSectors_tmp.append(item)
        #
        itemCount += 1
        startIndex += 2
        #
        if startIndex > checkLength:
            break
        #

    # 3) DRI 'Define Restart Interval'    - 4 bayt
    startIndex = 0
    tmp_kind = Kind.DRI()
    while True:
        tmp_index = jpgBytes[startIndex:].find(tmp_kind.marker)
        if tmp_index == -1:
            break
        startIndex += tmp_index
        #
        item = Sector()
        item.no = itemCount
        item.start = startIndex
        item.end = startIndex + 4
        item.root = 0
        item.type = tmp_kind
        jpgSectors_tmp.append(item)
        #
        itemCount += 1
        startIndex += 4
        #
        if startIndex > checkLength:
            break
        #

    # 4) APP0 'Application Specific'
    startIndex = 0
    tmp_kind = Kind.APP0()
    while True:
        tmp_index = jpgBytes[startIndex:].find(tmp_kind.marker)
        if tmp_index == -1:
            break
        startIndex += tmp_index
        #
        if startIndex + 4 > checkLength:
            break
        applength = appLength(data=jpgBytes[startIndex + 2:startIndex + 4])
        tmp_end = startIndex + 2 + applength
        if applength > -1 and tmp_end < checkLength:
            item = Sector()
            item.no = itemCount
            item.start = startIndex
            item.end = tmp_end
            item.root = 0
            item.type = tmp_kind
            jpgSectors_tmp.append(item)
            #
            itemCount += 1
        #
        startIndex += 2

    # 5) APP1 'Application Specific'
    startIndex = 0
    tmp_kind = Kind.APP1()
    while True:
        tmp_index = jpgBytes[startIndex:].find(tmp_kind.marker)
        if tmp_index == -1:
            break
        startIndex += tmp_index
        #
        if startIndex + 4 > checkLength:
            break
        applength = appLength(data=jpgBytes[startIndex + 2:startIndex + 4])
        tmp_end = startIndex + 2 + applength
        if applength > -1 and tmp_end < checkLength:
            item = Sector()
            item.no = itemCount
            item.start = startIndex
            item.end = tmp_end
            item.root = 0
            item.type = tmp_kind
            jpgSectors_tmp.append(item)
            #
            itemCount += 1
        #
        startIndex += 2

    # 6) APP2 'Application Specific'
    startIndex = 0
    tmp_kind = Kind.APP2()
    while True:
        tmp_index = jpgBytes[startIndex:].find(tmp_kind.marker)
        if tmp_index == -1:
            break
        startIndex += tmp_index
        #
        if startIndex + 4 > checkLength:
            break
        applength = appLength(data=jpgBytes[startIndex + 2:startIndex + 4])
        tmp_end = startIndex + 2 + applength
        if applength > -1 and tmp_end < checkLength:
            item = Sector()
            item.no = itemCount
            item.start = startIndex
            item.end = tmp_end
            item.root = 0
            item.type = tmp_kind
            jpgSectors_tmp.append(item)
            #
            itemCount += 1
        #
        startIndex += 2

    # 7) APP3 'Application Specific'
    startIndex = 0
    tmp_kind = Kind.APP3()
    while True:
        tmp_index = jpgBytes[startIndex:].find(tmp_kind.marker)
        if tmp_index == -1:
            break
        startIndex += tmp_index
        #
        if startIndex + 4 > checkLength:
            break
        applength = appLength(data=jpgBytes[startIndex + 2:startIndex + 4])
        tmp_end = startIndex + 2 + applength
        if applength > -1 and tmp_end < checkLength:
            item = Sector()
            item.no = itemCount
            item.start = startIndex
            item.end = tmp_end
            item.root = 0
            item.type = tmp_kind
            jpgSectors_tmp.append(item)
            #
            itemCount += 1
        #
        startIndex += 2

    # 8) APP4 'Application Specific'
    startIndex = 0
    tmp_kind = Kind.APP4()
    while True:
        tmp_index = jpgBytes[startIndex:].find(tmp_kind.marker)
        if tmp_index == -1:
            break
        startIndex += tmp_index
        #
        if startIndex + 4 > checkLength:
            break
        applength = appLength(data=jpgBytes[startIndex + 2:startIndex + 4])
        tmp_end = startIndex + 2 + applength
        if applength > -1 and tmp_end < checkLength:
            item = Sector()
            item.no = itemCount
            item.start = startIndex
            item.end = tmp_end
            item.root = 0
            item.type = tmp_kind
            jpgSectors_tmp.append(item)
            #
            itemCount += 1
        #
        startIndex += 22

    # 9) APP5 'Application Specific'
    startIndex = 0
    tmp_kind = Kind.APP5()
    while True:
        tmp_index = jpgBytes[startIndex:].find(tmp_kind.marker)
        if tmp_index == -1:
            break
        startIndex += tmp_index
        #
        if startIndex + 4 > checkLength:
            break
        applength = appLength(data=jpgBytes[startIndex + 2:startIndex + 4])
        tmp_end = startIndex + 2 + applength
        if applength > -1 and tmp_end < checkLength:
            item = Sector()
            item.no = itemCount
            item.start = startIndex
            item.end = tmp_end
            item.root = 0
            item.type = tmp_kind
            jpgSectors_tmp.append(item)
            #
            itemCount += 1
        #
        startIndex += 2

    # 10) APP6 'Application Specific'
    startIndex = 0
    tmp_kind = Kind.APP6()
    while True:
        tmp_index = jpgBytes[startIndex:].find(tmp_kind.marker)
        if tmp_index == -1:
            break
        startIndex += tmp_index
        #
        if startIndex + 4 > checkLength:
            break
        applength = appLength(data=jpgBytes[startIndex + 2:startIndex + 4])
        tmp_end = startIndex + 2 + applength
        if applength > -1 and tmp_end < checkLength:
            item = Sector()
            item.no = itemCount
            item.start = startIndex
            item.end = tmp_end
            item.root = 0
            item.type = tmp_kind
            jpgSectors_tmp.append(item)
            #
            itemCount += 1
        #
        startIndex += 2

    # 11) APP7 'Application Specific'
    startIndex = 0
    tmp_kind = Kind.APP7()
    while True:
        tmp_index = jpgBytes[startIndex:].find(tmp_kind.marker)
        if tmp_index == -1:
            break
        startIndex += tmp_index
        #
        if startIndex + 4 > checkLength:
            break
        applength = appLength(data=jpgBytes[startIndex + 2:startIndex + 4])
        tmp_end = startIndex + 2 + applength
        if applength > -1 and tmp_end < checkLength:
            item = Sector()
            item.no = itemCount
            item.start = startIndex
            item.end = tmp_end
            item.root = 0
            item.type = tmp_kind
            jpgSectors_tmp.append(item)
            #
            itemCount += 1
        #
        startIndex += 2

    # 12) APP8 'Application Specific'
    startIndex = 0
    tmp_kind = Kind.APP8()
    while True:
        tmp_index = jpgBytes[startIndex:].find(tmp_kind.marker)
        if tmp_index == -1:
            break
        startIndex += tmp_index
        #
        if startIndex + 4 > checkLength:
            break
        applength = appLength(data=jpgBytes[startIndex + 2:startIndex + 4])
        tmp_end = startIndex + 2 + applength
        if applength > -1 and tmp_end < checkLength:
            item = Sector()
            item.no = itemCount
            item.start = startIndex
            item.end = tmp_end
            item.root = 0
            item.type = tmp_kind
            jpgSectors_tmp.append(item)
            #
            itemCount += 1
        #
        startIndex += 2

    # 13) APP9 'Application Specific'
    startIndex = 0
    tmp_kind = Kind.APP9()
    while True:
        tmp_index = jpgBytes[startIndex:].find(tmp_kind.marker)
        if tmp_index == -1:
            break
        startIndex += tmp_index
        #
        if startIndex + 4 > checkLength:
            break
        applength = appLength(data=jpgBytes[startIndex + 2:startIndex + 4])
        tmp_end = startIndex + 2 + applength
        if applength > -1 and tmp_end < checkLength:
            item = Sector()
            item.no = itemCount
            item.start = startIndex
            item.end = tmp_end
            item.root = 0
            item.type = tmp_kind
            jpgSectors_tmp.append(item)
            #
            itemCount += 1
        #
        startIndex += 2

    # 14) APPA 'Application Specific'
    startIndex = 0
    tmp_kind = Kind.APPA()
    while True:
        tmp_index = jpgBytes[startIndex:].find(tmp_kind.marker)
        if tmp_index == -1:
            break
        startIndex += tmp_index
        #
        if startIndex + 4 > checkLength:
            break
        applength = appLength(data=jpgBytes[startIndex + 2:startIndex + 4])
        tmp_end = startIndex + 2 + applength
        if applength > -1 and tmp_end < checkLength:
            item = Sector()
            item.no = itemCount
            item.start = startIndex
            item.end = tmp_end
            item.root = 0
            item.type = tmp_kind
            jpgSectors_tmp.append(item)
            #
            itemCount += 1
        #
        startIndex += 2

    # 15) APPB 'Application Specific'
    startIndex = 0
    tmp_kind = Kind.APPB()
    while True:
        tmp_index = jpgBytes[startIndex:].find(tmp_kind.marker)
        if tmp_index == -1:
            break
        startIndex += tmp_index
        #
        if startIndex + 4 > checkLength:
            break
        applength = appLength(data=jpgBytes[startIndex + 2:startIndex + 4])
        tmp_end = startIndex + 2 + applength
        if applength > -1 and tmp_end < checkLength:
            item = Sector()
            item.no = itemCount
            item.start = startIndex
            item.end = tmp_end
            item.root = 0
            item.type = tmp_kind
            jpgSectors_tmp.append(item)
            #
            itemCount += 1
        #
        startIndex += 2

    # 16) APPC 'Application Specific'
    startIndex = 0
    tmp_kind = Kind.APPC()
    while True:
        tmp_index = jpgBytes[startIndex:].find(tmp_kind.marker)
        if tmp_index == -1:
            break
        startIndex += tmp_index
        #
        if startIndex + 4 > checkLength:
            break
        applength = appLength(data=jpgBytes[startIndex + 2:startIndex + 4])
        tmp_end = startIndex + 2 + applength
        if applength > -1 and tmp_end < checkLength:
            item = Sector()
            item.no = itemCount
            item.start = startIndex
            item.end = tmp_end
            item.root = 0
            item.type = tmp_kind
            jpgSectors_tmp.append(item)
            #
            itemCount += 1
        #
        startIndex += 2

    # 17) APPD 'Application Specific'
    startIndex = 0
    tmp_kind = Kind.APPD()
    while True:
        tmp_index = jpgBytes[startIndex:].find(tmp_kind.marker)
        if tmp_index == -1:
            break
        startIndex += tmp_index
        #
        if startIndex + 4 > checkLength:
            break
        applength = appLength(data=jpgBytes[startIndex + 2:startIndex + 4])
        tmp_end = startIndex + 2 + applength
        if applength > -1 and tmp_end < checkLength:
            item = Sector()
            item.no = itemCount
            item.start = startIndex
            item.end = tmp_end
            item.root = 0
            item.type = tmp_kind
            jpgSectors_tmp.append(item)
            #
            itemCount += 1
        #
        startIndex += 2

    # 18) APPE 'Application Specific'
    startIndex = 0
    tmp_kind = Kind.APPE()
    while True:
        tmp_index = jpgBytes[startIndex:].find(tmp_kind.marker)
        if tmp_index == -1:
            break
        startIndex += tmp_index
        #
        if startIndex + 4 > checkLength:
            break
        applength = appLength(data=jpgBytes[startIndex + 2:startIndex + 4])
        tmp_end = startIndex + 2 + applength
        if applength > -1 and tmp_end < checkLength:
            item = Sector()
            item.no = itemCount
            item.start = startIndex
            item.end = tmp_end
            item.root = 0
            item.type = tmp_kind
            jpgSectors_tmp.append(item)
            #
            itemCount += 1
        #
        startIndex += 2

    # 19) APPF 'Application Specific'
    startIndex = 0
    tmp_kind = Kind.APPF()
    while True:
        tmp_index = jpgBytes[startIndex:].find(tmp_kind.marker)
        if tmp_index == -1:
            break
        startIndex += tmp_index
        #
        if startIndex + 4 > checkLength:
            break
        applength = appLength(data=jpgBytes[startIndex + 2:startIndex + 4])
        tmp_end = startIndex + 2 + applength
        if applength > -1 and tmp_end < checkLength:
            item = Sector()
            item.no = itemCount
            item.start = startIndex
            item.end = tmp_end
            item.root = 0
            item.type = tmp_kind
            jpgSectors_tmp.append(item)
            #
            itemCount += 1
        #
        startIndex += 2

    # 20) SOF0 'Start Of Frame (Baseline DCT)'
    startIndex = 0
    tmp_kind = Kind.SOF0()
    while True:
        tmp_index = jpgBytes[startIndex:].find(tmp_kind.marker)
        if tmp_index == -1:
            break
        startIndex += tmp_index
        #
        if startIndex + 4 > checkLength:
            break
        applength = appLength(data=jpgBytes[startIndex + 2:startIndex + 4])
        tmp_end = startIndex + 2 + applength
        if applength > -1 and tmp_end < checkLength:
            item = Sector()
            item.no = itemCount
            item.start = startIndex
            item.end = tmp_end
            item.root = 0
            item.type = tmp_kind
            jpgSectors_tmp.append(item)
            #
            itemCount += 1
        #
        startIndex += 2

    # 21) SOF2 'Start Of Frame (Progressive DCT)'
    startIndex = 0
    tmp_kind = Kind.SOF2()
    while True:
        tmp_index = jpgBytes[startIndex:].find(tmp_kind.marker)
        if tmp_index == -1:
            break
        startIndex += tmp_index
        #
        if startIndex + 4 > checkLength:
            break
        applength = appLength(data=jpgBytes[startIndex + 2:startIndex + 4])
        tmp_end = startIndex + 2 + applength
        if applength > -1 and tmp_end < checkLength:
            item = Sector()
            item.no = itemCount
            item.start = startIndex
            item.end = tmp_end
            item.root = 0
            item.type = tmp_kind
            jpgSectors_tmp.append(item)
            #
            itemCount += 1
        #
        startIndex += 2

    # 22) DHT 'Define Huffman Table(s)'
    startIndex = 0
    tmp_kind = Kind.DHT()
    while True:
        tmp_index = jpgBytes[startIndex:].find(tmp_kind.marker)
        if tmp_index == -1:
            break
        startIndex += tmp_index
        #
        if startIndex + 4 > checkLength:
            break
        applength = appLength(data=jpgBytes[startIndex + 2:startIndex + 4])
        tmp_end = startIndex + 2 + applength
        if applength > -1 and tmp_end < checkLength:
            item = Sector()
            item.no = itemCount
            item.start = startIndex
            item.end = tmp_end
            item.root = 0
            item.type = tmp_kind
            jpgSectors_tmp.append(item)
            #
            itemCount += 1
        #
        startIndex += 2

    # 23) DQT 'Define Quantization Table(s)'
    startIndex = 0
    tmp_kind = Kind.DQT()
    while True:
        tmp_index = jpgBytes[startIndex:].find(tmp_kind.marker)
        if tmp_index == -1:
            break
        startIndex += tmp_index
        #
        if startIndex + 4 > checkLength:
            break
        applength = appLength(data=jpgBytes[startIndex + 2:startIndex + 4])
        tmp_end = startIndex + 2 + applength
        if applength > -1 and tmp_end < checkLength:
            item = Sector()
            item.no = itemCount
            item.start = startIndex
            item.end = tmp_end
            item.root = 0
            item.type = tmp_kind
            jpgSectors_tmp.append(item)
            #
            itemCount += 1
        #
        startIndex += 2

    # 24) SOS 'Start Of Scan'
    startIndex = 0
    tmp_kind = Kind.SOS()
    while True:
        tmp_index = jpgBytes[startIndex:].find(tmp_kind.marker)
        if tmp_index == -1:
            break
        startIndex += tmp_index
        #
        if startIndex + 4 > checkLength:
            break
        applength = appLength(data=jpgBytes[startIndex + 2:startIndex + 4])
        tmp_end = startIndex + 2 + applength
        if applength > -1 and tmp_end < checkLength:
            item = Sector()
            item.no = itemCount
            item.start = startIndex
            item.end = tmp_end
            item.root = 0
            item.type = tmp_kind
            jpgSectors_tmp.append(item)
            #
            itemCount += 1
        #
        startIndex += 2

    # 25) COM 'Comment'
    startIndex = 0
    tmp_kind = Kind.COM()
    while True:
        tmp_index = jpgBytes[startIndex:].find(tmp_kind.marker)
        if tmp_index == -1:
            break
        startIndex += tmp_index
        #
        if startIndex + 4 > checkLength:
            break
        applength = appLength(data=jpgBytes[startIndex + 2:startIndex + 4])
        tmp_end = startIndex + 2 + applength
        if applength > -1 and tmp_end < checkLength:
            item = Sector()
            item.no = itemCount
            item.start = startIndex
            item.end = tmp_end
            item.root = 0
            item.type = tmp_kind
            jpgSectors_tmp.append(item)
            #
            itemCount += 1
        #
        startIndex += 2

    # 26) RST0 'Restart'   - 2 bayt
    startIndex = 0
    tmp_kind = Kind.RST0()
    while True:
        tmp_index = jpgBytes[startIndex:].find(tmp_kind.marker)
        if tmp_index == -1:
            break
        startIndex += tmp_index
        #
        item = Sector()
        item.no = itemCount
        item.start = startIndex
        item.end = startIndex + 2
        item.root = 0
        item.type = tmp_kind
        jpgSectors_tmp.append(item)
        #
        itemCount += 1
        startIndex += 2
        #
        if startIndex > checkLength:
            break
        #

    # 27) RST1 'Restart'   - 2 bayt
    startIndex = 0
    tmp_kind = Kind.RST1()
    while True:
        tmp_index = jpgBytes[startIndex:].find(tmp_kind.marker)
        if tmp_index == -1:
            break
        startIndex += tmp_index
        #
        item = Sector()
        item.no = itemCount
        item.start = startIndex
        item.end = startIndex + 2
        item.root = 0
        item.type = tmp_kind
        jpgSectors_tmp.append(item)
        #
        itemCount += 1
        startIndex += 2
        #
        if startIndex > checkLength:
            break
        #

    # 28) RST2 'Restart'   - 2 bayt
    startIndex = 0
    tmp_kind = Kind.RST2()
    while True:
        tmp_index = jpgBytes[startIndex:].find(tmp_kind.marker)
        if tmp_index == -1:
            break
        startIndex += tmp_index
        #
        item = Sector()
        item.no = itemCount
        item.start = startIndex
        item.end = startIndex + 2
        item.root = 0
        item.type = tmp_kind
        jpgSectors_tmp.append(item)
        #
        itemCount += 1
        startIndex += 2
        #
        if startIndex > checkLength:
            break
        #

    # 29) RST3 'Restart'   - 2 bayt
    startIndex = 0
    tmp_kind = Kind.RST3()
    while True:
        tmp_index = jpgBytes[startIndex:].find(tmp_kind.marker)
        if tmp_index == -1:
            break
        startIndex += tmp_index
        #
        item = Sector()
        item.no = itemCount
        item.start = startIndex
        item.end = startIndex + 2
        item.root = 0
        item.type = tmp_kind
        jpgSectors_tmp.append(item)
        #
        itemCount += 1
        startIndex += 2
        #
        if startIndex > checkLength:
            break
        #

    # 30) RST4 'Restart'   - 2 bayt
    startIndex = 0
    tmp_kind = Kind.RST4()
    while True:
        tmp_index = jpgBytes[startIndex:].find(tmp_kind.marker)
        if tmp_index == -1:
            break
        startIndex += tmp_index
        #
        item = Sector()
        item.no = itemCount
        item.start = startIndex
        item.end = startIndex + 2
        item.root = 0
        item.type = tmp_kind
        jpgSectors_tmp.append(item)
        #
        itemCount += 1
        startIndex += 2
        #
        if startIndex > checkLength:
            break
        #

    # 31) RST5 'Restart'   - 2 bayt
    startIndex = 0
    tmp_kind = Kind.RST5()
    while True:
        tmp_index = jpgBytes[startIndex:].find(tmp_kind.marker)
        if tmp_index == -1:
            break
        startIndex += tmp_index
        #
        item = Sector()
        item.no = itemCount
        item.start = startIndex
        item.end = startIndex + 2
        item.root = 0
        item.type = tmp_kind
        jpgSectors_tmp.append(item)
        #
        itemCount += 1
        startIndex += 2
        #
        if startIndex > checkLength:
            break
        #

    # 32) RST6 'Restart'   - 2 bayt
    startIndex = 0
    tmp_kind = Kind.RST6()
    while True:
        tmp_index = jpgBytes[startIndex:].find(tmp_kind.marker)
        if tmp_index == -1:
            break
        startIndex += tmp_index
        #
        item = Sector()
        item.no = itemCount
        item.start = startIndex
        item.end = startIndex + 2
        item.root = 0
        item.type = tmp_kind
        jpgSectors_tmp.append(item)
        #
        itemCount += 1
        startIndex += 2
        #
        if startIndex > checkLength:
            break
        #

    # 33) RST7 'Restart'   - 2 bayt
    startIndex = 0
    tmp_kind = Kind.RST7()
    while True:
        tmp_index = jpgBytes[startIndex:].find(tmp_kind.marker)
        if tmp_index == -1:
            break
        startIndex += tmp_index
        #
        item = Sector()
        item.no = itemCount
        item.start = startIndex
        item.end = startIndex + 2
        item.root = 0
        item.type = tmp_kind
        jpgSectors_tmp.append(item)
        #
        itemCount += 1
        startIndex += 2
        #
        if startIndex > checkLength:
            break
        #
    #
    # Detect Root Child
    jpgSectors = []
    #
    sort_jpgSectors_tmp = sorted(jpgSectors_tmp, key=lambda x:x.start)
    number_find = len(sort_jpgSectors_tmp)
    #
    for ii in range(0,number_find):
        main_item = sort_jpgSectors_tmp[ii]
        if ii > 0:
            for jj in range ( (ii-1), -1, -1):
                check_item = sort_jpgSectors_tmp[jj]
                if check_item.start <= main_item.start <= check_item.end:
                    if check_item.start <= main_item.end <= check_item.end:
                        main_item.root = check_item.no
                        break
        jpgSectors.append(main_item)
    #
    #
    return jpgSectors
