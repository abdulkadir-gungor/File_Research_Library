#!/usr/bin/python3
############################################################################
#
#	File Signature  [ Main Program ]
#   © 2020 ABDULKADİR GÜNGÖR All Rights Reserved
#   Contact email address: abdulkadir_gungor@outlook.com
#
#	Developper:	Abdulkadir GÜNGÖR (abdulkadir_gungor@outlook.com)
#	Date:	08/2020
#	All Rights Reserved (Tüm Hakları Saklıdır)
#
############################################################################
from lib.filesignature.DetectFileSignature import detect_File_Signature as detectsig
from lib.hexlib.ReadBinaryFile import readBytes as rfile
import os

# Ekranı Temizlemek için
def screenClear():
    print("\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n") # Konsol dışı kullanımda ekranı temizlemek için
    # clear screen
    # ********************
    # Windows
    if os.name=='nt':
        os.system('cls')
    # Linux or MAC
    elif os.name=='posix':
        os.system('clear')
    # ********************
    print("")

# Giriş Menüsü
def menu0() -> int:
    while True:
        screenClear()
        print()
        print('\t#####################################################')
        print('\t#/*************************************************\#')
        print('\t#**||~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~||**#')
        print('\t#**||                                           ||**#')
        print('\t#**||          File Signature V1.3              ||**#')
        print('\t#**||                08/2020                    ||**#')
        print('\t#**||                                           ||**#')
        print('\t#**||       Developer: Abdulkadir GÜNGÖR        ||**#')
        print('\t#**||       (abdulkadir_gungor@outlook.com)     ||**#')
        print('\t#**||                                           ||**#')
        print('\t#**||~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~||**#')
        print('\t#\*************************************************/#')
        print('\t#####################################################')
        print()
        print()
        print('\t1) Check File')
        print('\t2) Check Input (Hex)')
        print('\t3) Directory (Check all files in directory)')
        print()
        print()
        tmp=input('\tÇıkış (Exit) <<e>> , Seçim (Selection) : ').strip()
        if tmp.isdigit():
            val = int(tmp)
            if 0 < val < 4:
                return val
        elif tmp.lower() == 'e' :
            exit(0)
#
def menu1():
    while True:
        screenClear()
        print()
        print("\tKontrol edilecek dosya adını giriniz!")
        print("\t(Enter the file name to be checked!)")
        print()
        print()
        tmp=input('\tFile : ')
        val = tmp.strip()
        try:
            result = rfile(filename=val)
            if result == None:
                result = b''
            return result
        except:
            print("\tDosya bulunamadı.(File not found)")
            print()
            print()
            print('\tÇıkış (Exit) <<e>> , Geri (Back) <<b>> ')
            ii = input('\tDevam (Continue) <<enter>> : ').strip()
            if ii.lower() == 'e':
                exit(0)
            elif ii.lower() == 'b':
                return None
#
def menu2():
    while True:
        screenClear()
        print()
        print("\tKontrol edilecek hex degerini giriniz!")
        print("\t(Enter the hex value to be checked!)")
        print("\tExample 'ff ee 23 e4' ")
        print()
        print()
        tmp=input('\tHex : ')
        val = tmp.strip().lower()
        try:
            result = bytearray.fromhex(val)
            return  result
        except:
            print("\tYanlıs giris yapildi. (Wrong entry)")
            print()
            print()
            print('\tÇıkış (Exit) <<e>> , Geri (Back) <<b>> ')
            ii = input('\tDevam (Continue) <<enter>> : ').strip()
            if ii.lower() == 'e':
                exit(0)
            elif ii.lower() == 'b':
                return None

def menu3():
    from lib.zip.win.Directory import Directory as Dir
    screenClear()
    print()
    print("\tKontrol edilecek dosyaları içeren klasor yolunu giriniz!")
    print("\t(Enter the path to the folder containing the files to check!)")
    print()
    print()
    print('\tGeri (Back) <<*>> ')
    tmp_directory = input('\tDirectory path : ').strip()
    if tmp_directory == '*':
        return None
    try:
        files = Dir(tmp_directory)
        return files
    except:
        print()
        print()
        print('\tYanlış klasor yolu.(Wrong directory path)')
        print()
        print('\tÇıkış (Exit) <<e>> , Geri (Back) <<b>> ')
        ii = input('\tDevam (Continue) <<enter>> : ').strip()
        if ii.lower() == 'e':
            exit(0)
        elif ii.lower() == 'b':
            return None

def main():
    while True:
        #
        selection = menu0()
        #
        if  0<selection <3:
            if selection == 1:
                data = menu1()
            elif selection == 2:
                data = menu2()
            else:
                data  = None
            if data != None:
                result = detectsig(bytesData=data)
                #
                if len(result) < 1:
                    print()
                    print()
                    print('\tSonuç bulunamadı.(No results)')
                else:
                    #
                    count = 1
                    txt_format = "\t{:<2} \tHex: '{}' \tExtension: '{}' \tDescription: '{}'"
                    #
                    for ii in result:
                        if count == 1:
                            print()
                            if len(result) == 1:
                                print('\t{:^60}'.format('The File Signature (1)'))
                            else:
                                txt_header = 'The File Signatures ({})'.format(len(result))
                                print('\t{:^60}'.format(txt_header))
                            print('\t' + '-' * 60)
                        print(
                            txt_format.format(count, ii.f1_signature.hex(sep=' '), ii.f2_extension, ii.f3_description))
                        count += 1
                    #
                print('')
                print('')
                print('')
                jj = input('\tExit <<e>> Start <<enter>>')
                if jj.strip().lower() == 'e':
                    exit(0)
        #
        elif selection == 3:
            while   True:
                files = menu3()
                if files == None:
                    break
                else:
                    if len(files.files) > 0:
                        for file_ in  files.files:
                            screenClear()
                            print()
                            print('\tCurrent Directory : ' + files.current_directory )
                            print('\tFile              : ' + file_.f2_relativepath )
                            print()
                            print()
                            check_continue = False
                            try:
                                result_data = rfile(filename=file_.f3_fullpath)
                                if result_data == None:
                                    result_data = b''
                                check_continue = True
                            except:
                                print('\tDosya okunurken hata oluştu.')
                                print('\t(An error occurred while reading the file.)')
                            #
                            if check_continue:
                                result = detectsig(bytesData=result_data)
                                #
                                if len(result) < 1:
                                    print()
                                    print()
                                    print('\tSonuç bulunamadı.(No results)')
                                else:
                                    #
                                    count = 1
                                    txt_format = "\t{:<2} \tHex: '{}' \tExtension: '{}' \tDescription: '{}'"
                                    #
                                    for ii in result:
                                        if count == 1:
                                            print()
                                            if len(result) == 1:
                                                print('\t{:^60}'.format('The File Signature (1)'))
                                            else:
                                                txt_header = 'The File Signatures ({})'.format(len(result))
                                                print('\t{:^60}'.format(txt_header))
                                            print('\t' + '-' * 60)
                                        print(txt_format.format(count, ii.f1_signature.hex(sep=' '), ii.f2_extension,
                                                                ii.f3_description))
                                        count += 1
                                #
                                print()
                                print()
                                print('\tÇıkış (Exit) <<e>> , Geri (Back) <<b>>')
                                jj = input('\tDevam (Continue) <<enter>> : ').strip()
                                if jj.lower() == 'e':
                                    exit(0)
                                elif jj.lower() == 'b':
                                    break
                                #
                    else:
                        print()
                        print()
                        print('\tÇıkış (Exit) <<e>> , Geri (Back) <<b>>')
                        jj = input('\tDevam (Continue) <<enter>> : ').strip()
                        if jj.lower() == 'e':
                            exit(0)
                        elif jj.lower() == 'b':
                            break

#
#
#
main()