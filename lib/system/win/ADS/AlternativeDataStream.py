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
class AlternativeDataStream:
    #
    def __init__( self, path:str='' ):
        self.a0_input = path
        self.a2_ads_files, self.a1_currenDirectory =  self.__dir()

    #
    def __dir(self):
        from lib.system.win.ADS.dir import dir
        return dir(path=self.a0_input)

    #
    def update(self, new_path:str=None):
        if new_path == None:
            self.a2_ads_files, self.a1_currenDirectory = self.__dir()
        else:
            self.a0_input = new_path
            self.a2_ads_files, self.a1_currenDirectory = self.__dir()

    #
    def showADSFile(self):
        print( '\tCurrent Directory: "'+self.a1_currenDirectory + '"')
        if self.a2_ads_files != None:
            if len( self.a2_ads_files ) > 0:
                print()
                print( '\tAlternative Data Stream File(s)' )
                print( '\t'+'-'*31 )
                txt_tmp = '\t{:>2}) {} : {} \t\t ADS File: "{}"'
                count = 1
                for file in self.a2_ads_files:
                    fd_name = '"{}"'.format( file.r1_file )
                    print( txt_tmp.format(count, file.r3_type ,fd_name, file.r2_ads_data) )
                    count += 1
            else:
                print('\tADS dosyaları bulunamadı. (ADS files not found)')
    #
    def delADSFile(self, index:int):
        import os
        slc = index - 1
        if -1 < slc < len(self.a2_ads_files):
            file = self.a1_currenDirectory + '\\' + self.a2_ads_files[slc].r1_file + ':' + self.a2_ads_files[slc].r2_ads_data
            try:
                os.remove(file)
                print( '\t[{} : "{}"] \tADS file "{}" silindi. (ADS file was deleted)'.format( self.a2_ads_files[slc].r3_type ,self.a2_ads_files[slc].r1_file , self.a2_ads_files[slc].r2_ads_data ) )
            except:
                print('\tHata meydana geldi.[{} "{}"] \tADS file "{}" silinemedi. (Error! Couldn\'t delete ADS file)'.format( self.a2_ads_files[slc].r3_type , self.a2_ads_files[slc].r1_file, self.a2_ads_files[slc].r2_ads_data))
            print('\n\t...')
            self.update()
            print('\tADS içeriği güncellendi. (ADS content has updated!)')

    #
    def copyADSFile_To_Disk(self, index:int ,filename:str, filepath:str=None ):
        from lib.hexlib.ReadBinaryFileWithABuffer import ReadBinaryFileWithABuffer as rfile
        from lib.hexlib.WriteFile import WriteFile as wfile
        slc = index - 1
        buffer = 5120
        if -1 < slc < len(self.a2_ads_files):
            read_file_name = self.a1_currenDirectory + '\\' + self.a2_ads_files[slc].r1_file + ':' + self.a2_ads_files[slc].r2_ads_data
            if filepath == None:
                write_file_name = self.a1_currenDirectory + '\\' + filename
            else:
                if filepath.strip() != '':
                    write_file_name = filepath + '\\' + filename
                else:
                    write_file_name = filename
            try:
                read_obj = rfile(filename=read_file_name, buffer=buffer)
                write_obj = wfile(filename=write_file_name)
                read_obj.resetRead()
                write_obj.writeByte(data=b'')
                while True:
                    if read_obj.getCurrent() >= read_obj.file_seek_end:
                        break
                    tmp_bytes = read_obj.read()
                    if tmp_bytes != None:
                        if tmp_bytes != b'':
                            write_obj.appendByte(data=tmp_bytes)
                        else:
                            break
                    else:
                        break
                print('\t...')
                print( '\tADS dosyası "{}" dosyasına kopyalandı.'.format(filename) )
                print( '\t[Copied ADS file to "{}" file]'.format(filename) )
            except:
                print('\tHata meydana geldi. [Error has occurred]')
                print('\tDosyanın varlığını ve izinleri kontrol ediniz. [Check file and permissions]')
        #
        print('\n\t...')
        self.update()
        print('\tADS içeriği güncellendi. (ADS content has updated!)')

    #
    def copyDisk_To_ADSFile(self , DiskFile:str, ADSFile:str, ADSDataName:str, DiskFilePath:str=None, ADSFilePath:str=None ):
        from lib.hexlib.ReadBinaryFileWithABuffer import ReadBinaryFileWithABuffer as rfile
        from lib.hexlib.WriteFile import WriteFile as wfile
        buffer = 5120
        #
        if ADSFilePath == None:
            writefile_name = self.a1_currenDirectory + '\\' + ADSFile + ':' + ADSDataName
        else:
            if ADSFilePath.strip() != '':
                writefile_name = ADSFilePath + '\\' + ADSFile + ':' + ADSDataName
            else:
                writefile_name = ADSFile + ':' + ADSDataName
        #
        if DiskFilePath == None:
            readfile_name = self.a1_currenDirectory + '\\' + DiskFile
        else:
            if DiskFilePath.strip() != '':
                readfile_name = DiskFilePath + '\\' + DiskFile
            else:
                readfile_name = DiskFile
                #
        try:
            print('\t...')
            read_obj = rfile(filename=readfile_name, buffer=buffer)
            write_obj = wfile(filename=writefile_name)
            read_obj.resetRead()
            write_obj.writeByte(data=b'')
            while True:
                if read_obj.getCurrent() >= read_obj.file_seek_end:
                    break
                tmp_bytes = read_obj.read()
                if tmp_bytes != None:
                    if tmp_bytes != b'':
                        write_obj.appendByte(data=tmp_bytes)
                    else:
                        break
                else:
                    break
            print('\tADS dosyası oluşturuldu. [ADS file has created]')
        except:
            print('\tHata meydana geldi. [Error has occurred]')
            print('\tDosyanın varlığını ve izinleri kontrol ediniz. [Check file and permissions]')
        #
        print('\n\t...')
        self.update()
        print('\tADS içeriği güncellendi. (ADS content has updated!)')
