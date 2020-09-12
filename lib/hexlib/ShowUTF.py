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

# UTF-8
def showUTF8Bytes( bytesData:bytes, columnSize: int = 25, linesHalt: int = -1):
    #
    line_format   = '\t<<UTF-8>> \t||{:.<'+str(columnSize)+'}||\t <<UTF-8>>'
    ###
    bytes_tmp0 = bytesData.replace(b'\r\n', b'  ')
    del bytesData
    bytes_tmp1 = bytes_tmp0.replace(b'\n', b' ')
    del bytes_tmp0
    bytes_tmp2 = bytes_tmp1.replace( b'\r', b' ' )
    del bytes_tmp1
    bytes_tmp3 = bytes_tmp2.replace(b'\t', b' ')
    del bytes_tmp2
    data_str = bytes_tmp3.decode(encoding='utf-8',errors='ignore')
    del bytes_tmp3
    ###
    data_str_len  = len(data_str)
    data_turn_int     = data_str_len / columnSize
    data_continue = True
    #
    if int(data_turn_int) == data_turn_int:
        data_turn_end=False
    else:
        data_turn_end=True
    #
    if linesHalt > 0:
        data_halt = True
    else:
        data_halt = False
    #
    counter = 0
    for ii in range(0, int(data_turn_int)):
        ii_start = ii * columnSize
        ii_end   = ii_start + columnSize
        #
        counter = ii
        if data_halt and ii!=0 and ii%linesHalt==0 :
            calculate = ( (ii*columnSize) / data_str_len)
            percent = int(calculate * 100)
            percent_point = int(calculate * 10000) - (percent * 100)
            print()
            print("\t%{:0>2d}.{:0>2d} has completed".format(percent, percent_point))
            input_char = input("\t[UTF-8 Editor] Continue <<enter>> or quit <<q>> :")
            print()
            if input_char.lower() == 'q':
                data_continue = False
                break
        #
        print( line_format.format(data_str[ii_start:ii_end] )  )
    #
    #
    if data_halt and data_continue and data_turn_end and counter != 0 and (counter+1)%linesHalt == 0:
        calculate = ( ((counter+1) * columnSize) / data_str_len )
        percent = int(calculate * 100)
        percent_point = int(calculate * 10000) - (percent * 100)
        print()
        print("\t%{:0>2d}.{:0>2d} has completed".format(percent, percent_point))
        input_char = input("\t[UTF-8 Editor] Continue <<enter>> or quit <<q>> :")
        print()
        if input_char.lower() == 'q':
            data_continue = False
    #
    if data_turn_end and data_continue:
        ii_start = columnSize * int(data_turn_int)
        print( line_format.format(data_str[ii_start:] ) )

# UTF16 (BE)
def showUTF16BEBytes( bytesData:bytes, columnSize: int = 25, linesHalt: int = -1):
    #
    line_format   = '\t<<UTF-16BE>> \t||{:.<'+str(columnSize)+'}||\t <<UTF-16BE>>'
    ###
    bytes_tmp0 = bytesData.replace(b'\r\n', b'  ')
    del bytesData
    bytes_tmp1 = bytes_tmp0.replace(b'\n', b' ')
    del bytes_tmp0
    bytes_tmp2 = bytes_tmp1.replace( b'\r', b' ' )
    del bytes_tmp1
    bytes_tmp3 = bytes_tmp2.replace(b'\t', b' ')
    del bytes_tmp2
    data_str = bytes_tmp3.decode(encoding='utf-16BE',errors='ignore')
    del bytes_tmp3
    ###
    data_str_len  = len(data_str)
    data_turn_int     = data_str_len / columnSize
    data_continue = True
    #
    if int(data_turn_int) == data_turn_int:
        data_turn_end=False
    else:
        data_turn_end=True
    #
    if linesHalt > 0:
        data_halt = True
    else:
        data_halt = False
    #
    counter = 0
    for ii in range(0, int(data_turn_int)):
        ii_start = ii * columnSize
        ii_end   = ii_start + columnSize
        #
        counter = ii
        if data_halt and ii!=0 and ii%linesHalt==0 :
            calculate = ( (ii*columnSize) / data_str_len)
            percent = int(calculate * 100)
            percent_point = int(calculate * 10000) - (percent * 100)
            print()
            print("\t%{:0>2d}.{:0>2d} has completed".format(percent, percent_point))
            input_char = input("\t[UTF-8 Editor] Continue <<enter>> or quit <<q>> :")
            print()
            if input_char.lower() == 'q':
                data_continue = False
                break
        #
        print( line_format.format(data_str[ii_start:ii_end] )  )
    #
    #
    if data_halt and data_continue and data_turn_end and counter != 0 and (counter+1)%linesHalt == 0:
        calculate = ( ((counter+1) * columnSize) / data_str_len )
        percent = int(calculate * 100)
        percent_point = int(calculate * 10000) - (percent * 100)
        print()
        print("\t%{:0>2d}.{:0>2d} has completed".format(percent, percent_point))
        input_char = input("\t[UTF-8 Editor] Continue <<enter>> or quit <<q>> :")
        print()
        if input_char.lower() == 'q':
            data_continue = False
    #
    if data_turn_end and data_continue:
        ii_start = columnSize * int(data_turn_int)
        print( line_format.format(data_str[ii_start:] ) )

# UTF16 (LE)
def showUTF16LEBytes( bytesData:bytes, columnSize: int = 25, linesHalt: int = -1):
    #
    line_format   = '\t<<UTF-16LE>> \t||{:.<'+str(columnSize)+'}||\t <<UTF-16LE>>'
    ###
    bytes_tmp0 = bytesData.replace(b'\r\n', b'  ')
    del bytesData
    bytes_tmp1 = bytes_tmp0.replace(b'\n', b' ')
    del bytes_tmp0
    bytes_tmp2 = bytes_tmp1.replace( b'\r', b' ' )
    del bytes_tmp1
    bytes_tmp3 = bytes_tmp2.replace(b'\t', b' ')
    del bytes_tmp2
    data_str = bytes_tmp3.decode(encoding='utf-16LE',errors='ignore')
    del bytes_tmp3
    ###
    data_str_len  = len(data_str)
    data_turn_int     = data_str_len / columnSize
    data_continue = True
    #
    if int(data_turn_int) == data_turn_int:
        data_turn_end=False
    else:
        data_turn_end=True
    #
    if linesHalt > 0:
        data_halt = True
    else:
        data_halt = False
    #
    counter = 0
    for ii in range(0, int(data_turn_int)):
        ii_start = ii * columnSize
        ii_end   = ii_start + columnSize
        #
        counter = ii
        if data_halt and ii!=0 and ii%linesHalt==0 :
            calculate = ( (ii*columnSize) / data_str_len)
            percent = int(calculate * 100)
            percent_point = int(calculate * 10000) - (percent * 100)
            print()
            print("\t%{:0>2d}.{:0>2d} has completed".format(percent, percent_point))
            input_char = input("\t[UTF-8 Editor] Continue <<enter>> or quit <<q>> :")
            print()
            if input_char.lower() == 'q':
                data_continue = False
                break
        #
        print( line_format.format(data_str[ii_start:ii_end] )  )
    #
    #
    if data_halt and data_continue and data_turn_end and counter != 0 and (counter+1)%linesHalt == 0:
        calculate = ( ((counter+1) * columnSize) / data_str_len )
        percent = int(calculate * 100)
        percent_point = int(calculate * 10000) - (percent * 100)
        print()
        print("\t%{:0>2d}.{:0>2d} has completed".format(percent, percent_point))
        input_char = input("\t[UTF-8 Editor] Continue <<enter>> or quit <<q>> :")
        print()
        if input_char.lower() == 'q':
            data_continue = False
    #
    if data_turn_end and data_continue:
        ii_start = columnSize * int(data_turn_int)
        print( line_format.format(data_str[ii_start:] ) )

# UTF32 (BE)
def showUTF32BEBytes( bytesData:bytes, columnSize: int = 25, linesHalt: int = -1):
    #
    line_format   = '\t<<UTF-32BE>> \t||{:.<'+str(columnSize)+'}||\t <<UTF-32BE>>'
    ###
    bytes_tmp0 = bytesData.replace(b'\r\n', b'  ')
    del bytesData
    bytes_tmp1 = bytes_tmp0.replace(b'\n', b' ')
    del bytes_tmp0
    bytes_tmp2 = bytes_tmp1.replace( b'\r', b' ' )
    del bytes_tmp1
    bytes_tmp3 = bytes_tmp2.replace(b'\t', b' ')
    del bytes_tmp2
    data_str = bytes_tmp3.decode(encoding='utf-32BE',errors='ignore')
    del bytes_tmp3
    ###
    data_str_len  = len(data_str)
    data_turn_int     = data_str_len / columnSize
    data_continue = True
    #
    if int(data_turn_int) == data_turn_int:
        data_turn_end=False
    else:
        data_turn_end=True
    #
    if linesHalt > 0:
        data_halt = True
    else:
        data_halt = False
    #
    counter = 0
    for ii in range(0, int(data_turn_int)):
        ii_start = ii * columnSize
        ii_end   = ii_start + columnSize
        #
        counter = ii
        if data_halt and ii!=0 and ii%linesHalt==0 :
            calculate = ( (ii*columnSize) / data_str_len)
            percent = int(calculate * 100)
            percent_point = int(calculate * 10000) - (percent * 100)
            print()
            print("\t%{:0>2d}.{:0>2d} has completed".format(percent, percent_point))
            input_char = input("\t[UTF-8 Editor] Continue <<enter>> or quit <<q>> :")
            print()
            if input_char.lower() == 'q':
                data_continue = False
                break
        #
        print( line_format.format(data_str[ii_start:ii_end] )  )
    #
    #
    if data_halt and data_continue and data_turn_end and counter != 0 and (counter+1)%linesHalt == 0:
        calculate = ( ((counter+1) * columnSize) / data_str_len )
        percent = int(calculate * 100)
        percent_point = int(calculate * 10000) - (percent * 100)
        print()
        print("\t%{:0>2d}.{:0>2d} has completed".format(percent, percent_point))
        input_char = input("\t[UTF-8 Editor] Continue <<enter>> or quit <<q>> :")
        print()
        if input_char.lower() == 'q':
            data_continue = False
    #
    if data_turn_end and data_continue:
        ii_start = columnSize * int(data_turn_int)
        print( line_format.format(data_str[ii_start:] ) )

# UTF32 (LE)
def showUTF32LEBytes( bytesData:bytes, columnSize: int = 25, linesHalt: int = -1):
    #
    line_format   = '\t<<UTF-32LE>> \t||{:.<'+str(columnSize)+'}||\t <<UTF-32LE>>'
    ###
    bytes_tmp0 = bytesData.replace(b'\r\n', b'  ')
    del bytesData
    bytes_tmp1 = bytes_tmp0.replace(b'\n', b' ')
    del bytes_tmp0
    bytes_tmp2 = bytes_tmp1.replace( b'\r', b' ' )
    del bytes_tmp1
    bytes_tmp3 = bytes_tmp2.replace(b'\t', b' ')
    del bytes_tmp2
    data_str = bytes_tmp3.decode(encoding='utf-32LE',errors='ignore')
    del bytes_tmp3
    ###
    data_str_len  = len(data_str)
    data_turn_int     = data_str_len / columnSize
    data_continue = True
    #
    if int(data_turn_int) == data_turn_int:
        data_turn_end=False
    else:
        data_turn_end=True
    #
    if linesHalt > 0:
        data_halt = True
    else:
        data_halt = False
    #
    counter = 0
    for ii in range(0, int(data_turn_int)):
        ii_start = ii * columnSize
        ii_end   = ii_start + columnSize
        #
        counter = ii
        if data_halt and ii!=0 and ii%linesHalt==0 :
            calculate = ( (ii*columnSize) / data_str_len)
            percent = int(calculate * 100)
            percent_point = int(calculate * 10000) - (percent * 100)
            print()
            print("\t%{:0>2d}.{:0>2d} has completed".format(percent, percent_point))
            input_char = input("\t[UTF-8 Editor] Continue <<enter>> or quit <<q>> :")
            print()
            if input_char.lower() == 'q':
                data_continue = False
                break
        #
        print( line_format.format(data_str[ii_start:ii_end] )  )
    #
    #
    if data_halt and data_continue and data_turn_end and counter != 0 and (counter+1)%linesHalt == 0:
        calculate = ( ((counter+1) * columnSize) / data_str_len )
        percent = int(calculate * 100)
        percent_point = int(calculate * 10000) - (percent * 100)
        print()
        print("\t%{:0>2d}.{:0>2d} has completed".format(percent, percent_point))
        input_char = input("\t[UTF-8 Editor] Continue <<enter>> or quit <<q>> :")
        print()
        if input_char.lower() == 'q':
            data_continue = False
    #
    if data_turn_end and data_continue:
        ii_start = columnSize * int(data_turn_int)
        print( line_format.format(data_str[ii_start:] ) )