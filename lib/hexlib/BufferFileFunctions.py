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
from lib.hexlib.ReadBinaryFile import readIndexBytes
from lib.hexlib.WriteFile import WriteFile
# Functions
# searchBuffer, replaceOne, deleteOneIndex, replaceBuffer, replaceBuffer_slow1, replaceBuffer_slow2
# replaceDelBuffer, delBuffer, searchOneBuffer

# Dosyadan "buffer" özelliğini kullanarak
# ilgili aramayı yapar. Bir adet sonuç döndürür.
def searchOneBuffer(file:ReadBinaryFileWithABuffer, searchData:bytes) -> int:
    searchData_length= len(searchData)
    search_counter=0
    counter=0
    file.resetRead()
    while True:
        bufferData=file.read()
        if bufferData == b'':
            break
        for ii in range(0, len(bufferData)):
            if bufferData[ii:ii+1] == searchData[search_counter:search_counter+1]:
                if search_counter == searchData_length-1:
                    return (counter-search_counter)
                else:
                    search_counter += 1
            else:
                search_counter = 0
            counter += 1
    return -1

# Dosyadan "buffer" özelliğini kullanarak
# replace işlemini yapar.
def replaceOne(rfile:ReadBinaryFileWithABuffer, wfile:WriteFile, startIndex:int , stopIndex:int ,replaceData:bytes) :
    rfile.resetRead()
    while True:
        if rfile.getCurrent() >= rfile.file_seek_end:
            break
        if startIndex > rfile.getCurrent()+rfile.buffer or  rfile.getCurrent() >= stopIndex:
            wfile.appendByte( data=rfile.read() )
        else:
            if rfile.getCurrent() < startIndex:
                wfile.appendByte(data=readIndexBytes(filename=rfile.filename, startIndex=rfile.getCurrent(), stopIndex=startIndex))
            wfile.appendByte(data=replaceData)
            wfile.appendByte(data=rfile.readIndex(stopIndex))

# Dosyadan "buffer" özelliğini kullanarak
# delete işlemini yapar
def deleteOneIndex(rfile:ReadBinaryFileWithABuffer, wfile:WriteFile, startIndex:int , stopIndex:int) :
    rfile.resetRead()
    while True:
        if rfile.getCurrent() >= rfile.file_seek_end:
            break
        if startIndex > rfile.getCurrent()+rfile.buffer or  rfile.getCurrent() >= stopIndex:
            wfile.appendByte( data=rfile.read() )
        else:
            if rfile.getCurrent() < startIndex:
                wfile.appendByte(data=readIndexBytes(filename=rfile.filename, startIndex=rfile.getCurrent(), stopIndex=startIndex))
            wfile.appendByte(data=rfile.readIndex(stopIndex))

# Dosyadan "buffer" özelliğini kullanarak
# ilgili aramayı yapar. Tüm sonuçları döndürür.
def searchBuffer(file:ReadBinaryFileWithABuffer, searchData:bytes) -> list:
    result=[]
    searchData_length= len(searchData)
    search_counter=0
    counter=0
    file.resetRead()
    while True:
        bufferData=file.read()
        if bufferData == b'':
            break
        for ii in range(0, len(bufferData)):
            if bufferData[ii:ii+1] == searchData[search_counter:search_counter+1]:
                if search_counter == searchData_length-1:
                    result.append( counter-search_counter )
                    search_counter = 0
                else:
                    search_counter += 1
            else:
                search_counter = 0
            counter += 1
    return result

# Dosyadan "buffer" özelliğini kullanarak
# ilgili değerleri siler.
def replaceDelBuffer(rfile:ReadBinaryFileWithABuffer, wfile:WriteFile, searchData:bytes):
    result=[]
    searchData_length= len(searchData)
    search_counter=0
    counter=0
    rfile.resetRead()
    while True:
        bufferData=rfile.read()
        if bufferData == b'':
            break
        for ii in range(0, len(bufferData)):
            if bufferData[ii:ii+1] == searchData[search_counter:search_counter+1]:
                if search_counter == searchData_length-1:
                    result.append( counter-search_counter )
                    search_counter = 0
                else:
                    search_counter += 1
            else:
                search_counter = 0
            counter += 1
    if len(result) > 0:
        rfile.resetRead()
        startIndex  = result.pop(0)
        stopIndex = startIndex + searchData_length
        while True:
            if rfile.getCurrent() >= rfile.file_seek_end:
                break
            if startIndex > rfile.getCurrent() + rfile.buffer or rfile.getCurrent() >= stopIndex:
                wfile.appendByte(data=rfile.read())
            else:
                if rfile.getCurrent() < startIndex:
                    wfile.appendByte(data=readIndexBytes(filename=rfile.filename, startIndex=rfile.getCurrent(),
                                                         stopIndex=startIndex))
                rfile.setCurrent(seek=stopIndex)
                if len(result)>0:
                    startIndex = result.pop(0)
                    stopIndex = startIndex + searchData_length
                else:
                    wfile.appendByte(data=rfile.readIndex(stopIndex))
    else:
        rfile.resetRead()
        while True:
            bufferData=rfile.read()
            if bufferData == b'':
                break
            wfile.writeByte(bufferData)

# Dosyadan "buffer" özelliğini kullanarak
# Silme işlemi yapar
# delist = [ [0, 1], [0, 2], [3, 5], [7, 8] ... ]
def delBuffer(rfile:ReadBinaryFileWithABuffer, wfile:WriteFile, delList:list) :
    rfile.resetRead()
    if len(delList) > 0:
        rfile.resetRead()
        startStopIndex  = delList.pop(0)
        startIndex = startStopIndex[0]
        stopIndex = startStopIndex[1]
        while True:
            if rfile.getCurrent() >= rfile.file_seek_end:
                break
            if startIndex > rfile.getCurrent() + rfile.buffer or rfile.getCurrent() >= stopIndex:
                wfile.appendByte(data=rfile.read())
            else:
                if rfile.getCurrent() < startIndex:
                    wfile.appendByte(data=readIndexBytes(filename=rfile.filename, startIndex=rfile.getCurrent(),
                                                         stopIndex=startIndex))
                rfile.setCurrent(seek=stopIndex)
                if len(delList) > 0:
                    startStopIndex = delList.pop(0)
                    startIndex = startStopIndex[0]
                    stopIndex = startStopIndex[1]
                else:
                    wfile.appendByte(data=rfile.readIndex(stopIndex))
    else:
        rfile.resetRead()
        while True:
            bufferData=rfile.read()
            if bufferData == b'':
                break
            wfile.writeByte(bufferData)

# Dosyadan "buffer" özelliğini kullanarak
# replace yapar
def replaceBuffer(rfile:ReadBinaryFileWithABuffer, wfile:WriteFile, searchData:bytes, replaceData:bytes) :
    result=[]
    searchData_length= len(searchData)
    search_counter=0
    counter=0
    rfile.resetRead()
    while True:
        bufferData=rfile.read()
        if bufferData == b'':
            break
        for ii in range(0, len(bufferData)):
            if bufferData[ii:ii+1] == searchData[search_counter:search_counter+1]:
                if search_counter == searchData_length-1:
                    result.append( counter-search_counter )
                    search_counter = 0
                else:
                    search_counter += 1
            else:
                search_counter = 0
            counter += 1
    if len(result) > 0:
        rfile.resetRead()
        startIndex  = result.pop(0)
        stopIndex = startIndex + searchData_length
        while True:
            if rfile.getCurrent() >= rfile.file_seek_end:
                break
            if startIndex > rfile.getCurrent() + rfile.buffer or rfile.getCurrent() >= stopIndex:
                wfile.appendByte(data=rfile.read())
            else:
                if rfile.getCurrent() < startIndex:
                    wfile.appendByte(data=readIndexBytes(filename=rfile.filename, startIndex=rfile.getCurrent(),
                                                         stopIndex=startIndex))
                wfile.appendByte(data=replaceData)
                rfile.setCurrent(seek=stopIndex)
                if len(result)>0:
                    startIndex = result.pop(0)
                    stopIndex = startIndex + searchData_length
                else:
                    wfile.appendByte(data=rfile.readIndex(stopIndex))
    else:
        rfile.resetRead()
        while True:
            bufferData=rfile.read()
            if bufferData == b'':
                break
            wfile.writeByte(bufferData)

# Dosyadan "buffer" özelliğini kullanarak
# replace yapar.
# Byte byte kontrol ve yazma yaptığı için çok yavaş
def replaceBuffer_slow1(rfile:ReadBinaryFileWithABuffer, wfile:WriteFile, searchData:bytes, replaceData:bytes) :
    result=[]
    searchData_length= len(searchData)
    search_counter=0
    counter=0
    rfile.resetRead()
    while True:
        bufferData=rfile.read()
        if bufferData == b'':
            break
        for ii in range(0, len(bufferData)):
            if bufferData[ii:ii+1] == searchData[search_counter:search_counter+1]:
                if search_counter == searchData_length-1:
                    result.append( counter-search_counter )
                    search_counter = 0
                else:
                    search_counter += 1
            else:
                search_counter = 0
            counter += 1
    if len(result) > 0:
        rfile.resetRead()
        counter = 0
        add_bool = True
        add_bytes = b''
        pop_first = result.pop(0)
        pop_end  = pop_first + searchData_length
        while True:
            bufferData = rfile.read()
            if bufferData == b'':
                break
            #
            for jj in range(0, len(bufferData)):
                if counter == pop_first:
                    add_bool= False
                    add_bytes += replaceData
                elif counter == pop_end:
                    add_bool=True
                    if len(result) > 0:
                        pop_first = result.pop(0)
                        pop_end = pop_first + searchData_length
                        if counter == pop_first:
                            add_bool = False
                            add_bytes += replaceData
                if add_bool:
                    add_bytes += bufferData[jj:jj+1]
                counter += 1
            #
            if len( add_bytes ) > 0:
                wfile.appendByte(add_bytes)
            add_bytes = b''
    else:
        rfile.resetRead()
        while True:
            bufferData=rfile.read()
            if bufferData == b'':
                break
            wfile.writeByte(bufferData)

# Dosyadan "buffer" özelliğini kullanarak
# replace yapar.
# Byte byte kontrol ve yazma yaptığı için çok yavaş
def replaceBuffer_slow2(rfile:ReadBinaryFileWithABuffer, wfile:WriteFile, searchData:bytes, replaceData:bytes) :
    result=[]
    searchData_length= len(searchData)
    search_counter=0
    counter=0
    rfile.resetRead()
    while True:
        bufferData=rfile.read()
        if bufferData == b'':
            break
        for ii in range(0, len(bufferData)):
            if bufferData[ii:ii+1] == searchData[search_counter:search_counter+1]:
                if search_counter == searchData_length-1:
                    result.append( counter-search_counter )
                    search_counter = 0
                else:
                    search_counter += 1
            else:
                search_counter = 0
            counter += 1
    if len(result) > 0:
        pop_first = result.pop(0)
        pop_end = pop_first+searchData_length
        counter=0
        write_bool=True
        with open(file=rfile.filename, mode='rb') as readfile:
            with open(file=wfile.filename, mode='ab') as writefile:
                read_file_end = readfile.seek(0, 2)
                readfile.seek(0, 0)
                while True:
                    if counter >= read_file_end:
                        break
                    if counter == pop_first:
                        write_bool=False
                        writefile.write(replaceData)
                        writefile.flush()
                    elif counter == pop_end:
                        write_bool=True
                        if len(result) > 0:
                            pop_first = result.pop(0)
                            pop_end = pop_first + searchData_length
                            if counter == pop_first:
                                write_bool=True
                                writefile.write(replaceData)
                                writefile.flush()
                    bayt = readfile.read(1)
                    if bayt:
                        if write_bool:
                            writefile.write(bayt)
                            writefile.flush()
                    else:
                        break
                    counter += 1
    else:
        rfile.resetRead()
        while True:
            bufferData=rfile.read()
            if bufferData == b'':
                break
            wfile.appendByte(bufferData)
