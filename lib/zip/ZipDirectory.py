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
import zipfile
import os
from lib.zip.win.Directory import File as ZipFile
from lib.zip.win.Directory import Directory as ZipDirectory
from lib.hexlib.ReadBinaryFile import readBytes as rb
#
#
def zip_Extract(zipFile:str, extractDirectory:str):
    try:
        zipfile_obj = ZipFile(path=zipFile)
        zipextract_obj = ZipFile(path=extractDirectory)
    except:
        print('\tGirilen yolları kontrol ediniz. Yanlış girdi.')
        print('\t(Check the entered paths. Wrong path)')
        return
    #
    if zipfile_obj.checkFile and not zipfile_obj.checkDirectory:
        if not zipextract_obj.checkFile:
            if  not zipextract_obj.checkDirectory:
                with zipfile.ZipFile(zipfile_obj.file.f3_fullpath) as zipdata:
                    print('\t    ***FILE(S)***')
                    print('\t-----------------------')
                    for info in zipdata.infolist():
                        print('\t[-] '+info.filename)
                    zipdata.extractall( path=zipextract_obj.file.f3_fullpath )
            else:
                try:
                    os.rmdir(zipextract_obj.current_directory)
                    with zipfile.ZipFile(zipfile_obj.file.f3_fullpath) as zipdata:
                        print('\t    ***FILE(S)***')
                        print('\t-----------------------')
                        for info in zipdata.infolist():
                            print('\t[-] ' + info.filename)
                        zipdata.extractall(path=zipextract_obj.current_directory)
                except:
                    print('\tHedef klasorde dosyalar var!')
                    print('\t(There are files in the destination folder!)')
        else:
            print('\tOluşturulacak klasor ile aynı isme sahip bir dosya var!')
            print('\t(There is a file with the same name as the folder to be created!)')
    else:
        print('\tDosya bulunamadı! (File not found!)')

#
#
def zip_Package(zipFile:str, zipPackageDirectory:str):
    try:
        zipfile_obj = ZipFile(path=zipFile)
        zipdirectory_obj = ZipDirectory(path=zipPackageDirectory)
    except:
        print('\tGirilen yolları kontrol ediniz. Yanlış girdi.')
        print('\t(Check the entered paths. Wrong path)')
        return
    #
    if not zipfile_obj.checkFile and not zipfile_obj.checkDirectory:
        with zipfile.ZipFile(zipfile_obj.file.f3_fullpath, 'w') as zipdata:
            if len(zipdirectory_obj.files) > 0 :
                print('\t    ***FILE(S)***')
                print('\t-----------------------')
                for file_obj in zipdirectory_obj.files:
                    tmp_data_read = rb(filename=file_obj.f3_fullpath)
                    if tmp_data_read == None:
                        tmp_data_read = b''
                    zipdata.writestr(file_obj.f2_relativepath, tmp_data_read)
                    print( '\t[+] '+file_obj.f2_relativepath )
            else:
                print('\tKlasor bulunamadı.(Directory not found)')
            zipdata.close()
    elif zipfile_obj.checkFile:
        try:
            os.remove(zipfile_obj.file.f3_fullpath)
            with zipfile.ZipFile(zipfile_obj.file.f3_fullpath, 'w') as zipdata:
                if len(zipdirectory_obj.files) > 0:
                    print('\t    ***FILE(S)***')
                    print('\t-----------------------')
                    for file_obj in zipdirectory_obj.files:
                        tmp_data_read = rb(filename=file_obj.f3_fullpath)
                        if tmp_data_read == None:
                            tmp_data_read = b''
                        zipdata.writestr(file_obj.f2_relativepath, tmp_data_read)
                        print('\t[+] ' + file_obj.f2_relativepath)
                else:
                    print('\tKlasor bulunamadı.(Directory not found)')
                zipdata.close()

        except:
            print('\tOluşturulacak dosya adı ile aynı isme sahip bir dosya var. Dosya kullanımda!')
            print('\t(There is a file with the same name as the file to be created. The file is in use!)')
    else:
        print('\tOluşturulacak dosya adı ile aynı isme sahip klasor var!')
        print('\t(There is a directory with the same name as the file to be created!)')
