# Only for Windows 10 / 64 bits
############################################################################
#
#   © 2020 ABDULKADİR GÜNGÖR All Rights Reserved
#   Contact email address: abdulkadir_gungor@outlook.com
#
#	Developper:	Abdulkadir GÜNGÖR (abdulkadir_gungor@outlook.com)
#	Date:	09/2020
#	All Rights Reserved (Tüm Hakları Saklıdır)
#
############################################################################

#
#
import zipfile
import os
from  lib.hexlib.ShowHex import show2HexBytes as s2hex
from lib.filesignature.DetectFileSignature import detect_File_Signature as DSignature
from lib.zip.win.Directory import File as ZipFile
from lib.zip.win.Directory import Directory as ZipDirectory
from lib.hexlib.ReadBinaryFile import readBytes as rb
from lib.hexlib.WriteFile import WriteFile as wfile
from lib.microsoft_office.JPG_Inspector.JPG_Inspector import jpgInspector as jpg

#
class Office:
    #
    @classmethod
    def Extract( cls, officeFile:str, extractDirectory:str, showFiles:bool=False ):
        try:
            zipfile_obj = ZipFile(path=officeFile)
            zipextract_obj = ZipFile(path=extractDirectory)
        except:
            print('\tGirilen yolları kontrol ediniz. Yanlış girdi.')
            print('\t(Check the entered paths. Wrong path)')
            return False
        #
        if zipfile_obj.checkFile and not zipfile_obj.checkDirectory:
            if not zipextract_obj.checkFile:
                if not zipextract_obj.checkDirectory:
                    with zipfile.ZipFile(zipfile_obj.file.f3_fullpath) as zipdata:
                        #
                        if showFiles:
                            print('\t    ***FILE(S)***')
                            print('\t-----------------------')
                            for info in zipdata.infolist():
                                print('\t[-] ' + info.filename)
                        #
                        zipdata.extractall(path=zipextract_obj.file.f3_fullpath)
                        return True
                else:
                    try:
                        os.rmdir(zipextract_obj.current_directory)
                        with zipfile.ZipFile(zipfile_obj.file.f3_fullpath) as zipdata:
                            #
                            if showFiles:
                                print('\t    ***FILE(S)***')
                                print('\t-----------------------')
                                for info in zipdata.infolist():
                                    print('\t[-] ' + info.filename)
                            #
                            zipdata.extractall(path=zipextract_obj.current_directory)
                            return True
                    except:
                        print('\tHedef klasorde dosyalar var!')
                        print('\t(There are files in the destination folder!)')
            else:
                print('\tOluşturulacak klasor ile aynı isme sahip bir dosya var!')
                print('\t(There is a file with the same name as the folder to be created!)')
        else:
            print('\tDosya bulunamadı! (File not found!)')
        return False
    #
    @classmethod
    def Package(cls, officeFile:str, packageDirectory:str, showFiles:bool=False ):
        res = False
        try:
            zipfile_obj = ZipFile(path=officeFile)
            zipdirectory_obj = ZipDirectory(path=packageDirectory)
        except:
            print('\tGirilen yolları kontrol ediniz. Yanlış girdi.')
            print('\t(Check the entered paths. Wrong path)')
            return False
        #
        if not zipfile_obj.checkFile and not zipfile_obj.checkDirectory:
            with zipfile.ZipFile(zipfile_obj.file.f3_fullpath, 'w') as zipdata:
                if len(zipdirectory_obj.files) > 0:
                    #
                    if showFiles:
                        print('\t    ***FILE(S)***')
                        print('\t-----------------------')
                    #
                    for file_obj in zipdirectory_obj.files:
                        tmp_data_read = rb(filename=file_obj.f3_fullpath)
                        if tmp_data_read == None:
                            tmp_data_read = b''
                        zipdata.writestr(file_obj.f2_relativepath, tmp_data_read)
                        #
                        if showFiles:
                            print('\t[+] ' + file_obj.f2_relativepath)
                        #
                    res= True
                else:
                    print('\tKlasor bulunamadı.(Directory not found)')
                zipdata.close()
        elif zipfile_obj.checkFile:
            try:
                os.remove(zipfile_obj.file.f3_fullpath)
                with zipfile.ZipFile(zipfile_obj.file.f3_fullpath, 'w') as zipdata:
                    if len(zipdirectory_obj.files) > 0:
                        #
                        if showFiles:
                            print('\t    ***FILE(S)***')
                            print('\t-----------------------')
                        #
                        for file_obj in zipdirectory_obj.files:
                            tmp_data_read = rb(filename=file_obj.f3_fullpath)
                            if tmp_data_read == None:
                                tmp_data_read = b''
                            zipdata.writestr(file_obj.f2_relativepath, tmp_data_read)
                            #
                            if showFiles:
                                print('\t[+] ' + file_obj.f2_relativepath)
                            #
                        res = True
                    else:
                        print('\tKlasor bulunamadı.(Directory not found)')
                    zipdata.close()

            except:
                print('\tOluşturulacak dosya adı ile aynı isme sahip bir dosya var. Dosya kullanımda!')
                print('\t(There is a file with the same name as the file to be created. The file is in use!)')
        else:
            print('\tOluşturulacak dosya adı ile aynı isme sahip klasor var!')
            print('\t(There is a directory with the same name as the file to be created!)')
        #
        return res

    #
    def __init__(self, officeFile:str):
        self.__file_obj   = ZipFile(path=officeFile)
        self.files      = []
        self.extensions = {}
        self.__findExtensions()

    #
    def __findExtensions(self):
        self.__file_obj.update()
        if self.__file_obj.checkFile:
            with zipfile.ZipFile(self.__file_obj.file.f3_fullpath) as office:
                for file in office.infolist():
                    extension = (file.filename.split(sep='.')[-1]).strip().lower()
                    if extension  not in  self.extensions.keys():
                        self.extensions[extension] = []
                    self.extensions[extension].append(file.filename)
                    self.files.append(file.filename)
    #
    def showExtensionsFiles(self):
        with zipfile.ZipFile(self.__file_obj.file.f3_fullpath) as office:
            txt_extension_format = '\t [-] {} [{}]'
            txt_filename_format  = '\t  |------ {:<40}\t {:<7}\t {}'
            for extension in self.extensions.keys():
                print()
                print( txt_extension_format.format(extension.upper(), len(self.extensions[extension]) ) )
                for filename in sorted(self.extensions[extension]):
                    info = office.getinfo(name=filename)
                    tmp_size = str(info.file_size) + ' Bayts'
                    tmp_system = '-'
                    if info.create_system == 0:
                        tmp_system = 'Windows'
                    elif info.create_system == 3:
                        tmp_system = 'Unix'
                    print( txt_filename_format.format(filename, tmp_system, tmp_size ) )
    #
    def showExtensions(self):
            txt_extension_format = '\t [+] {} [{}]'
            if len(self.extensions.keys()) > 0:
                print()
                for extension in self.extensions.keys():
                    print( txt_extension_format.format(extension.upper(), len(self.extensions[extension])) )
    #
    def showCheckAllFiles(self):
        txt_filename_format = '\t [-] {}'
        txt_sig_format =  '\t  |------ Hex : "{}"\t Extension : "{}"\t Description : "{}"'
        with zipfile.ZipFile(self.__file_obj.file.f3_fullpath) as office:
            for filename in self.files:
                file_bytes = office.read(filename)
                signature_list = DSignature(bytesData=file_bytes)
                print()
                print( txt_filename_format.format(filename) )
                for sig in signature_list:
                    print( txt_sig_format.format(sig.f1_signature.hex(sep=' ') ,sig.f2_extension, sig.f3_description) )

    #
    def showHexAllFiles(self):
        files_len = len(self.files)
        count = 1
        txt_filename_format = '\t{}'
        with zipfile.ZipFile(self.__file_obj.file.f3_fullpath) as office:
            for filename in self.files:
                file_bytes = office.read(filename)
                print()
                s2hex(dataBytes=file_bytes , dataName=filename,columnSize=15, linesHalt=2000)
                if count != files_len:
                    print()
                    print()
                    val = input('\tGeri (Back) <<b>> , Devam (Continue) <<enter>> : ').strip()
                    print()
                    if val.lower() == 'b':
                        break
                count += 1
    #
    def showFiles(self):
        txt_officefile_format = '\t [-] {} [{}]'
        txt_filename_format     = '\t  |------ ({}) {:<40}\t {:<6}\t {:<7}\t {}'
        count = 1
        with zipfile.ZipFile(self.__file_obj.file.f3_fullpath) as office:
            print()
            print(txt_officefile_format.format(self.__file_obj.file.f1_name, len(self.files)))
            for extension in self.extensions:
                for filename in self.extensions[extension]:
                    info = office.getinfo(name=filename)
                    tmp_size = str(info.file_size) + ' Bayts'
                    tmp_system = '-'
                    if info.create_system == 0:
                        tmp_system = 'Windows'
                    elif info.create_system == 3:
                        tmp_system = 'Unix'
                    print(txt_filename_format.format(count,filename, extension.upper(),tmp_system, tmp_size))
                    count += 1
    #
    def getFile(self, index:int) :
        if 0 < index < len(self.files)+1:
            count = 1
            with zipfile.ZipFile(self.__file_obj.file.f3_fullpath) as office:
                for ext in self.extensions:
                    for name in self.extensions[ext]:
                        if count==index:
                            return name, office.read(name)
                        count += 1
        else:
            return None,None
    #
    def getOfficeFileName(self) ->str:
        return self.__file_obj.file.f3_fullpath
    #
    def getOfficeObj(self) -> ZipFile :
        return self.__file_obj
    #

    def saveFile(self,index:int) -> bool:
        if 0 < index < len(self.files)+1:
            count = 1
            with zipfile.ZipFile(self.__file_obj.file.f3_fullpath) as office:
                for ext in self.extensions:
                    for name in self.extensions[ext]:
                        if count==index:
                            try:
                                byte = office.read(name)
                                filename = name.split(sep='/')[-1]
                                writepath = self.__file_obj.current_directory + '\\' + filename
                                wr = wfile(filename=writepath)
                                wr.writeByte(byte)
                                print('\t"{}" Dosya yazıldı. (The file was written)'.format(writepath))
                                return True
                            except:
                                print('\tHata oluştu.(Error has occurred)')
                                return False
                        count += 1
                        #
        return False

    #
    def showFileHexEditor(self, index:int):
        if 0 < index < len(self.files)+1:
            count = 1
            with zipfile.ZipFile(self.__file_obj.file.f3_fullpath) as office:
                for ext in self.extensions:
                    for name in self.extensions[ext]:
                        if count==index:
                            byte = office.read(name)
                            s2hex(dataName='"'+name+'"', dataBytes=byte,columnSize=15, linesHalt=2000)
                            return
                        count += 1
    #
    def showSummaryFileHexEditor(self, index:int):
        if 0 < index < len(self.files)+1:
            count = 1
            with zipfile.ZipFile(self.__file_obj.file.f3_fullpath) as office:
                for ext in self.extensions:
                    for name in self.extensions[ext]:
                        if count==index:
                            byte = office.read(name)
                            if len(byte) > 45:
                                s2hex(dataName='"'+name+'"', dataBytes=byte[:45],columnSize=15)
                            else:
                                s2hex(dataName='"' + name + '"', dataBytes=byte, columnSize=15)
                            return
                        count += 1
    #
    def showSummaryHexAllFiles(self):
        with zipfile.ZipFile(self.__file_obj.file.f3_fullpath) as office:
            for filename in self.files:
                file_bytes = office.read(filename)
                print()
                if len(file_bytes) > 45:
                    s2hex(dataName='"' + filename + '"', dataBytes=file_bytes[:45], columnSize=15)
                else:
                    s2hex(dataName='"' + filename + '"', dataBytes=file_bytes, columnSize=15)


    #
    def showCheckFile(self, index:int):
        txt_filename_format = '\t [-] {}'
        txt_sig_format =  '\t  |------ Hex : "{}"\t Extension : "{}"\t Description : "{}"'
        if 0 < index < len(self.files)+1:
            count = 1
            with zipfile.ZipFile(self.__file_obj.file.f3_fullpath) as office:
                for ext in self.extensions:
                    for name in self.extensions[ext]:
                        if count==index:
                            file_bytes = office.read(name)
                            signature_list = DSignature(bytesData=file_bytes)
                            print()
                            print(txt_filename_format.format(name))
                            for sig in signature_list:
                                print(txt_sig_format.format(sig.f1_signature.hex(sep=' '), sig.f2_extension, sig.f3_description))
                            return
                        count += 1
    #
    def showJPGjpegFiles(self):
        with zipfile.ZipFile(self.__file_obj.file.f3_fullpath) as office:
            txt_extension_format = '\t [-] {} '
            txt_filename_format  = '\t  |------ {}) {:<40}\t {:<7}\t {}'
            count = 1
            for extension in self.extensions.keys():
                extension_check = extension.strip().lower()
                if  extension_check == 'jpg' or extension_check == 'jpeg':
                    print()
                    print( txt_extension_format.format(extension.upper() ) )
                    for filename in sorted(self.extensions[extension]):
                        info = office.getinfo(name=filename)
                        tmp_size = str(info.file_size) + ' Bayts'
                        tmp_system = '-'
                        if info.create_system == 0:
                            tmp_system = 'Windows'
                        elif info.create_system == 3:
                            tmp_system = 'Unix'
                        print( txt_filename_format.format(count,filename, tmp_system, tmp_size ) )
                        count += 1
    #
    def showJPGjpegFile(self, index: int):
        if 0 < index < len(self.files) + 1:
            with zipfile.ZipFile(self.__file_obj.file.f3_fullpath) as office:
                count = 1
                for extension in self.extensions.keys():
                    extension_check = extension.strip().lower()
                    if extension_check == 'jpg' or extension_check == 'jpeg':
                        for filename in sorted(self.extensions[extension]):
                            if count == index:
                                file_bytes = office.read(name=filename)
                                jpg(filename=filename, jpgBytes=file_bytes)
                            count += 1
    #
    def deleteMetaData(self):
        try:
            w_file = self.__file_obj.current_directory + '\\[NoMetadata]_' + self.__file_obj.file.f1_name
            with zipfile.ZipFile(self.__file_obj.file.f3_fullpath,mode='r') as office:
                with zipfile.ZipFile(w_file, mode='w') as newoffice:
                    for file in office.infolist():
                        if file.filename.find('docProps/') == -1:
                            newoffice.writestr(file.filename, office.read(file.filename) )
                    newoffice.close()
                    return True, w_file
        except:
            return False, ''
    #
    def showMetadata(self):
        import xml.etree.ElementTree as ET
        with zipfile.ZipFile(self.__file_obj.file.f3_fullpath, mode='r') as office:
            check_file = 'docProps/core.xml'
            if check_file in self.files:
                core_info_bytes = office.read(name=check_file)
                core_info_str = core_info_bytes.decode(encoding='utf-8', errors='strict')
                del core_info_bytes
                xml_tree = ET.fromstring(core_info_str)
                print('\tMetadata Bilgileri (Metadata Infos)')
                print('\t-----------------------------------')
                txt_tmp = '\t{:<20} : {}'
                for child in xml_tree:
                    sTag = child.tag.split(sep='}')[-1]
                    if child.text == None:
                        sText = '-'
                    elif child.text == '' or child.text.strip() == '':
                        sText = '-'
                    else:
                        sText = child.text
                    print(txt_tmp.format(sTag, sText))
            else:
                print('\tMetadata bilgileri bulunamadı. (Metadata infos not found)')

    def extractAllFiles(self, directoryPath:str=''):
        if directoryPath == '' or directoryPath.strip() == '':
            ext_name = (self.__file_obj.file.f1_name.split(sep='.')[-1]).upper()
            dir_name = self.__file_obj.current_directory + '\\['+ext_name+']_' + self.__file_obj.file.f1_name
        else:
            dir_name = directoryPath.strip()
        return Office.Extract(officeFile=self.__file_obj.file.f3_fullpath, extractDirectory=dir_name)