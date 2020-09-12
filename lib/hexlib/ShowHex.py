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
from lib.hexlib.ReadBinaryFileWithABuffer import ReadBinaryFileWithABuffer

# Dosyayı okur. En baştan sırayla hex olarak gösterir.
def showHexFile(readFile: ReadBinaryFileWithABuffer, columnSize: int = 10, linesHalt: int = -1):
    readFile.resetRead()
    line_format = '\tNo:{:0>6d}-{:0>6d}\t <Ascii>||{:<}||\t <Hex>||{:<}||'
    line_index = 0
    line_old_index = 0
    counter = 0
    counter_old = 0
    turn = True
    while turn:
        if readFile.getCurrent() < readFile.file_seek_end:
            read_bytes = readFile.read()
        else:
            break
        read_bytes_length = len(read_bytes)
        if read_bytes_length < 1:
            break
        for r_index in range(0, read_bytes_length):
            if counter % columnSize == 0:
                if counter != 0:
                    print(line_format.format(counter_old, counter, ascii_line, hex_line))
                    line_index += 1
                else:
                    nameTmp = "\t|| Filename: '{}' - Size: {} (bayt) ||".format(readFile.filename,
                                                                                readFile.file_seek_end)
                    dashTmp1 = '\t' + '-' * ((len(nameTmp)) - 1)
                    dashTmp2 = dashTmp1 + '\n'
                    print(dashTmp1)
                    print(nameTmp)
                    print(dashTmp2)
                counter_old = counter + 1
                bayt = read_bytes[r_index:r_index + 1]
                hex_line = bayt.hex()
                char = bayt.decode(encoding="ascii", errors='replace')
                if char.isprintable() and char != '�':
                    ascii_line = char
                else:
                    ascii_line = "."
            else:
                bayt = read_bytes[r_index:r_index + 1]
                hex_line += ' ' + bayt.hex()
                char = bayt.decode(encoding="ascii", errors='replace')
                if char.isprintable() and char != '�':
                    ascii_line += char
                else:
                    ascii_line += "."
            if counter == readFile.file_seek_end - 1:
                if line_index == 0:
                    print(line_format.format(counter_old, (counter + 1), ascii_line, hex_line))
                else:
                    addSpace = columnSize - len(ascii_line)
                    ascii_line += ' ' * addSpace
                    addSpace = (columnSize * 2) + (columnSize - 1) - len(hex_line)
                    hex_line += ' ' * addSpace
                    print(line_format.format(counter_old, (counter + 1), ascii_line, hex_line))
            if linesHalt != -1 and counter != readFile.file_seek_end - 1:
                if line_index != line_old_index and line_index % linesHalt == 0:
                    calculate = int((r_index / readFile.file_seek_end) * 10000)
                    percent = int((r_index / readFile.file_seek_end) * 100)
                    percent_point = calculate - (percent * 100)
                    print()
                    print("\t%{:0>2d}.{:0>2d} has completed".format(percent, percent_point))
                    input_char = input("\t[Hex-Editor] Continue <<enter>> or quit <<q>> :")
                    print()
                    if input_char.lower() == 'q':
                        turn = False
                        break
                    line_old_index = line_index
            counter += 1

# Dosyayı okur. Index 'ten sırayla hex olarak gösterir.
def showIndexHexFile(readFile: ReadBinaryFileWithABuffer, columnSize: int = 10, linesHalt: int = -1, index = 0):
    readFile.resetRead()
    line_format = '\tNo:{:0>6d}-{:0>6d}\t <Ascii>||{:<}||\t <Hex>||{:<}||'
    line_index = 0
    line_old_index = 0
    if index > 0:
        index_start = (index-1)
        counter = index_start
        counter_old = counter
        check_rest = counter % columnSize
    else:
        index_start = 0
        counter = 0
        counter_old = 0
        check_rest = 0
    turn = True
    while turn:
        if readFile.getCurrent() < readFile.file_seek_end:
            if index_start == counter:
                read_bytes = readFile.readIndex(index=index_start)
            else:
                read_bytes = readFile.read()
        else:
            break
        read_bytes_length = len(read_bytes)
        if read_bytes_length < 1:
            break
        for r_index in range(0, read_bytes_length):
            if counter % columnSize == check_rest:
                if counter != index_start:
                    print(line_format.format(counter_old, counter, ascii_line, hex_line))
                    line_index += 1
                else:
                    nameTmp = "\t|| Filename: '{}' - Size: {} (bayt) ||".format(readFile.filename,
                                                                                readFile.file_seek_end)
                    dashTmp1 = '\t' + '-' * ((len(nameTmp)) - 1)
                    dashTmp2 = dashTmp1 + '\n'
                    print(dashTmp1)
                    print(nameTmp)
                    print(dashTmp2)
                counter_old = counter + 1
                bayt = read_bytes[r_index:r_index + 1]
                hex_line = bayt.hex()
                char = bayt.decode(encoding="ascii", errors='replace')
                if char.isprintable() and char != '�':
                    ascii_line = char
                else:
                    ascii_line = "."
            else:
                bayt = read_bytes[r_index:r_index + 1]
                hex_line += ' ' + bayt.hex()
                char = bayt.decode(encoding="ascii", errors='replace')
                if char.isprintable() and char != '�':
                    ascii_line += char
                else:
                    ascii_line += "."
            if counter == readFile.file_seek_end - 1:
                if line_index == 0:
                    print(line_format.format(counter_old, (counter + 1), ascii_line, hex_line))
                else:
                    addSpace = columnSize - len(ascii_line)
                    ascii_line += ' ' * addSpace
                    addSpace = (columnSize * 2) + (columnSize - 1) - len(hex_line)
                    hex_line += ' ' * addSpace
                    print(line_format.format(counter_old, (counter + 1), ascii_line, hex_line))
            if linesHalt != -1 and counter != readFile.file_seek_end - 1:
                if line_index != line_old_index and line_index % linesHalt == 0:
                    calculate = int((counter / readFile.file_seek_end) * 10000)
                    percent = int((counter / readFile.file_seek_end) * 100)
                    percent_point = calculate - (percent * 100)
                    print()
                    print("\t%{:0>2d}.{:0>2d} has completed".format(percent, percent_point))
                    input_char = input("\t[Hex-Editor] Continue <<enter>> or quit <<q>> :")
                    print()
                    if input_char.lower() == 'q':
                        turn = False
                        break
                    line_old_index = line_index
            counter += 1

# Gönderilen datayı hex olarak gösterir.
def showHexBytes( dataBytes=bytes, columnSize: int = 10, linesHalt: int = -1, index=0, dataName:str=''):
    line_format = '\tNo:{:0>6d}-{:0>6d}\t <Ascii>||{:<}||\t <Hex>||{:<}||'
    dataBytes_length = len(dataBytes)
    line_index = 0
    line_old_index = 0
    if index > 0:
        counter = index-1
        counter_old = counter
    else:
        counter = 0
        counter_old = 0
    for r_index in range(0, dataBytes_length):
        if r_index % columnSize == 0:
            if r_index != 0:
                print(line_format.format(counter_old, counter, ascii_line, hex_line))
                line_index += 1
            else:
                if dataName == '':
                    nameTmp = "\t|| Size: {} (bayt) ||".format(dataBytes_length)
                else:
                    nameTmp = "\t|| {} - Size: {} (bayt) ||".format(dataName,dataBytes_length)
                dashTmp1 = '\t' + '-' * ((len(nameTmp)) - 1)
                dashTmp2 = dashTmp1 + '\n'
                print(dashTmp1)
                print(nameTmp)
                print(dashTmp2)
            counter_old = counter + 1
            bayt = dataBytes[r_index:r_index + 1]
            hex_line = bayt.hex()
            char = bayt.decode(encoding="ascii", errors='replace')
            if char.isprintable() and char != '�':
                ascii_line = char
            else:
                ascii_line = "."
        else:
            bayt = dataBytes[r_index:r_index + 1]
            hex_line += ' ' + bayt.hex()
            char = bayt.decode(encoding="ascii", errors='replace')
            if char.isprintable() and char != '�':
                ascii_line += char
            else:
                ascii_line += "."
        if r_index == dataBytes_length - 1:
            if line_index == 0:
                print(line_format.format(counter_old, (counter + 1), ascii_line, hex_line))
            else:
                addSpace = columnSize - len(ascii_line)
                ascii_line += ' ' * addSpace
                addSpace = (columnSize * 2) + (columnSize - 1) - len(hex_line)
                hex_line += ' ' * addSpace
                print(line_format.format(counter_old, (counter + 1), ascii_line, hex_line))
        if linesHalt != -1 and counter != dataBytes_length - 1:
            if line_index != line_old_index and line_index % linesHalt == 0:
                calculate = int((r_index / dataBytes_length) * 10000)
                percent = int((r_index / dataBytes_length) * 100)
                percent_point = calculate - (percent * 100)
                print()
                print("\t%{:0>2d}.{:0>2d} has completed".format(percent, percent_point))
                input_char = input("\t[Hex-Editor] Continue <<enter>> or quit <<q>> :")
                print()
                if input_char.lower() == 'q':
                    break
                line_old_index = line_index
        counter += 1

# Gönderilen datayı hex olarak gösterir.
def show2HexBytes( dataBytes=bytes, columnSize: int = 10, linesHalt: int = -1, index=0, dataName:str=''):
    line_format = '\tNo:{:0>6d}-{:0>6d}\t <Ascii>||{:<}||\t <Hex>||{:<}||'
    dataBytes_length = len(dataBytes)
    line_index = 0
    line_old_index = 0
    if index > 0:
        counter = index-1
        counter_old = counter
    else:
        counter = 0
        counter_old = 0
    for r_index in range(0, dataBytes_length):
        if r_index % columnSize == 0:
            if r_index != 0:
                print(line_format.format(counter_old, counter, ascii_line, hex_line))
                line_index += 1
            else:
                if dataName == '':
                    nameTmp = "\t|| Size: {} (bayt) ||".format(dataBytes_length)
                else:
                    nameTmp = "\t|| {} - Size: {} (bayt) ||".format(dataName,dataBytes_length)
                dashTmp1 = '\t' + '-' * ((len(nameTmp)) - 1)
                dashTmp2 = dashTmp1
                print(dashTmp1)
                print(nameTmp)
                print(dashTmp2)
            counter_old = counter + 1
            bayt = dataBytes[r_index:r_index + 1]
            hex_line = bayt.hex()
            char = bayt.decode(encoding="ascii", errors='replace')
            if char.isprintable() and char != '�':
                ascii_line = char
            else:
                ascii_line = "."
        else:
            bayt = dataBytes[r_index:r_index + 1]
            hex_line += ' ' + bayt.hex()
            char = bayt.decode(encoding="ascii", errors='replace')
            if char.isprintable() and char != '�':
                ascii_line += char
            else:
                ascii_line += "."
        if r_index == dataBytes_length - 1:
            if line_index == 0:
                print(line_format.format(counter_old, (counter + 1), ascii_line, hex_line))
            else:
                addSpace = columnSize - len(ascii_line)
                ascii_line += ' ' * addSpace
                addSpace = (columnSize * 2) + (columnSize - 1) - len(hex_line)
                hex_line += ' ' * addSpace
                print(line_format.format(counter_old, (counter + 1), ascii_line, hex_line))
        if linesHalt != -1 and counter != dataBytes_length - 1:
            if line_index != line_old_index and line_index % linesHalt == 0:
                calculate = int((r_index / dataBytes_length) * 10000)
                percent = int((r_index / dataBytes_length) * 100)
                percent_point = calculate - (percent * 100)
                print()
                print("\t%{:0>2d}.{:0>2d} has completed".format(percent, percent_point))
                input_char = input("\t[Hex-Editor] Continue <<enter>> or quit <<q>> :")
                print()
                if input_char.lower() == 'q':
                    break
                line_old_index = line_index
        counter += 1

# Gönderilen datayı hex olarak gösterir.
def show3HexBytes( dataBytes=bytes, columnSize: int = 10, linesHalt: int = -1, index=0):
    line_format = '\tNo:{:0>6d}-{:0>6d}\t <Ascii>||{:<}||\t <Hex>||{:<}||'
    dataBytes_length = len(dataBytes)
    line_index = 0
    line_old_index = 0
    if index > 0:
        counter = index-1
        counter_old = counter
    else:
        counter = 0
        counter_old = 0
    for r_index in range(0, dataBytes_length):
        if r_index % columnSize == 0:
            if r_index != 0:
                print(line_format.format(counter_old, counter, ascii_line, hex_line))
                line_index += 1
            counter_old = counter + 1
            bayt = dataBytes[r_index:r_index + 1]
            hex_line = bayt.hex()
            char = bayt.decode(encoding="ascii", errors='replace')
            if char.isprintable() and char != '�':
                ascii_line = char
            else:
                ascii_line = "."
        else:
            bayt = dataBytes[r_index:r_index + 1]
            hex_line += ' ' + bayt.hex()
            char = bayt.decode(encoding="ascii", errors='replace')
            if char.isprintable() and char != '�':
                ascii_line += char
            else:
                ascii_line += "."
        if r_index == dataBytes_length - 1:
            if line_index == 0:
                print(line_format.format(counter_old, (counter + 1), ascii_line, hex_line))
            else:
                addSpace = columnSize - len(ascii_line)
                ascii_line += ' ' * addSpace
                addSpace = (columnSize * 2) + (columnSize - 1) - len(hex_line)
                hex_line += ' ' * addSpace
                print(line_format.format(counter_old, (counter + 1), ascii_line, hex_line))
        if linesHalt != -1 and counter != dataBytes_length - 1:
            if line_index != line_old_index and line_index % linesHalt == 0:
                calculate = int((r_index / dataBytes_length) * 10000)
                percent = int((r_index / dataBytes_length) * 100)
                percent_point = calculate - (percent * 100)
                print()
                print("\t%{:0>2d}.{:0>2d} has completed".format(percent, percent_point))
                input_char = input("\t[Hex-Editor] Continue <<enter>> or quit <<q>> :")
                print()
                if input_char.lower() == 'q':
                    break
                line_old_index = line_index
        counter += 1

# Gönderilen datayı hex olarak gösterir.
def show4HexBytes( dataBytes=bytes, columnSize: int = 10, linesHalt: int = -1):
    line_format = '\t<Ascii>||{:<}||\t <Hex>||{:<}||'
    dataBytes_length = len(dataBytes)
    line_index = 0
    line_old_index = 0
    counter = 0
    for r_index in range(0, dataBytes_length):
        if r_index % columnSize == 0:
            if r_index != 0:
                print(line_format.format( ascii_line, hex_line) )
                line_index += 1
            bayt = dataBytes[r_index:r_index + 1]
            hex_line = bayt.hex()
            char = bayt.decode(encoding="ascii", errors='replace')
            if char.isprintable() and char != '�':
                ascii_line = char
            else:
                ascii_line = "."
        else:
            bayt = dataBytes[r_index:r_index + 1]
            hex_line += ' ' + bayt.hex()
            char = bayt.decode(encoding="ascii", errors='replace')
            if char.isprintable() and char != '�':
                ascii_line += char
            else:
                ascii_line += "."
        if r_index == dataBytes_length - 1:
            if line_index == 0:
                print(line_format.format(ascii_line, hex_line))
            else:
                addSpace = columnSize - len(ascii_line)
                ascii_line += ' ' * addSpace
                addSpace = (columnSize * 2) + (columnSize - 1) - len(hex_line)
                hex_line += ' ' * addSpace
                print(line_format.format(ascii_line, hex_line))
        if linesHalt != -1 and counter != dataBytes_length - 1:
            if line_index != line_old_index and line_index % linesHalt == 0:
                calculate = int((r_index / dataBytes_length) * 10000)
                percent = int((r_index / dataBytes_length) * 100)
                percent_point = calculate - (percent * 100)
                print()
                print("\t%{:0>2d}.{:0>2d} has completed".format(percent, percent_point))
                input_char = input("\t[Hex-Editor] Continue <<enter>> or quit <<q>> :")
                print()
                if input_char.lower() == 'q':
                    break
                line_old_index = line_index
        counter += 1