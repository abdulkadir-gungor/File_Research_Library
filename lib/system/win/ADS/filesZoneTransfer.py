# Only for Windows 10 / 64 bits
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
def strFilesZoneTransfer(path:str='') -> str:
    from lib.system.win.ADS.dir import dir
    from lib.hexlib.ReadBinaryFile import readBytes as rb
    #
    files, curDir = dir(path=path)
    result = ''
    count = 1
    txt1_format = '\n\t{}'
    #
    if curDir != None:
        if curDir != '':
            txt1   = '"'+curDir+'"'
            result  = txt1_format.format( txt1 )
            result += txt1_format.format( '#'*len(txt1) )
            result += '\n'
    #
    if files != None:
        txt2_format = '{}) "{}" [{}]'
        for tmp_file in files:
            if tmp_file.r2_ads_data == 'Zone.Identifier' :
                txt2 = txt2_format.format(count, tmp_file.r1_file, tmp_file.r2_ads_data)
                count += 1
                result += txt1_format.format(txt2)
                #
                read_file_path = curDir + '\\' + tmp_file.r1_file + ':' + tmp_file.r2_ads_data
                try:
                    file_bytes = rb(filename=read_file_path)
                    if file_bytes != None:
                        file_str = file_bytes.decode(encoding='utf-8', errors='replace')
                        if file_str.strip() != '':
                            result += txt1_format.format( '-'*len(txt2) )
                            for line in file_str.split(sep='\r\n'):
                                result += txt1_format.format(line)
                    else:
                        result += txt1_format.format('-' * len(txt2))
                        result += txt1_format.format('[None]')
                except:
                    result += txt1_format.format('[Error]')
                    result += '\n'
    #
    return result

#
#
#
def showFilesZoneTransfer(path:str='') :
    from lib.system.win.ADS.dir import dir
    from lib.hexlib.ReadBinaryFile import readBytes as rb
    #
    files, curDir = dir(path=path)
    count = 1
    txt1_format = '\t{}'
    #
    if curDir != None:
        if curDir != '':
            txt1   = '"'+curDir+'"'
            print( txt1_format.format( txt1 ) )
            print( txt1_format.format( '#'*len(txt1) ) )
            print()
    #
    if files != None:
        txt2_format = '{}) "{}" [{}]'
        for tmp_file in files:
            if tmp_file.r2_ads_data == 'Zone.Identifier' :
                txt2 = txt2_format.format(count, tmp_file.r1_file, tmp_file.r2_ads_data)
                count += 1
                print( txt1_format.format(txt2) )
                #
                read_file_path = curDir + '\\' + tmp_file.r1_file + ':' + tmp_file.r2_ads_data
                try:
                    file_bytes = rb(filename=read_file_path)
                    if file_bytes != None:
                        file_str = file_bytes.decode(encoding='utf-8', errors='replace')
                        if file_str.strip() != '':
                            print( txt1_format.format( '-'*len(txt2)) )
                            for line in file_str.split(sep='\r\n'):
                                print( txt1_format.format(line) )
                    else:
                        print( txt1_format.format('-' * len(txt2)) )
                        print( txt1_format.format('[None]') )
                except:
                    print(txt1_format.format('[Error]\n'))
    #

#
#
#
def delFilesZoneTransfer(path:str='') :
    from lib.system.win.ADS.dir import dir
    from lib.hexlib.WriteFile import WriteFile as wfile
    import os
    #
    files, curDir = dir(path=path)
    count = 1
    #
    if files != None and curDir != None:
        txt1 = '"' + curDir + '"'
        print('\t{}'.format(txt1))
        print('\t{}'.format('#' * len(txt1)))
        print()
        for tmp_file in files:
            if tmp_file.r2_ads_data == 'Zone.Identifier' :
                zone_file = curDir + '\\' + tmp_file.r1_file + ':' +tmp_file.r2_ads_data
                #
                try:
                    remove_obj = wfile(filename=zone_file)
                    remove_obj.writeByte(data=b'')
                    del remove_obj
                    print('\t{}) "{}:{}"  (+) [Content was deleted]'.format(count,tmp_file.r1_file,tmp_file.r2_ads_data))
                except:
                    print('\t{}) "{}:{}"  (-) [Couldn\'t delete content]'.format(count,tmp_file.r1_file,tmp_file.r2_ads_data))
                #
                try:
                    os.remove(zone_file)
                    print('\t{}) "{}:{}"  (+) [File was deleted]'.format(count, tmp_file.r1_file, tmp_file.r2_ads_data))
                except:
                    print('\t{}) "{}:{}"  (-) [Couldn\'t delete file]'.format(count, tmp_file.r1_file, tmp_file.r2_ads_data))
                #
                count += 1
    #

#
#
#
def writeFilesZoneTransfer(writefilename:str, path:str=''):
    from lib.hexlib.WriteFile import WriteFile as wfile
    #
    str_write = strFilesZoneTransfer(path=path)
    if str_write != None:
        if str_write != '':
            filewrite = wfile(filename=writefilename)
            filewrite.writeStr(data=str_write)
    #
#