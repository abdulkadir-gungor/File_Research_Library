# Only for Windows 10 / 64 bits
############################################################################
#
#   Microsoft Office File Inspector
#   © 2020 ABDULKADİR GÜNGÖR All Rights Reserved
#   Contact email address: abdulkadir_gungor@outlook.com
#
#	Developper:	Abdulkadir GÜNGÖR (abdulkadir_gungor@outlook.com)
#	Date:	08/2020
#	All Rights Reserved (Tüm Hakları Saklıdır)
#
############################################################################

#
import os
from lib.microsoft_office.Office import Office
#

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
        print('\t#**||       Microsoft Office File Inspector     ||**#')
        print('\t#**||      (Docx, Xlsx, Pptx, Docm, Xlsm vs.)   ||**#')
        print('\t#**||                09/2020                    ||**#')	
        print('\t#**||                                           ||**#')		
        print('\t#**||       Developer: Abdulkadir GÜNGÖR        ||**#')
        print('\t#**||       (abdulkadir_gungor@outlook.com)     ||**#')
        print('\t#**||                                           ||**#')
        print('\t#**||~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~||**#')
        print('\t#\*************************************************/#')
        print('\t#####################################################')
        print()
        print()
        print('\t               MENU')
        print('\t----------------------------------------')
        print('\t1) Microsoft Office File Inspector')
        print('\t2) Microsoft Office File Extract')
        print('\t3) Microsoft Office File Package')
        print()
        print()
        print( '\tÇıkış (Exit) <<e>>' )
        tmp=input('\tSeçim (Selection) : ')
        if tmp.strip().lower() == 'e' :
            exit(0)
        elif tmp.strip().isdigit():
            slc = int(tmp.strip())
            if  0< slc <4:
                return slc

#
def menu2():
    screenClear()
    print()
    print()
    filename  = input('\tOffice file name  : ').strip()
    directory = input('\tExtract Directory : ').strip()
    print()
    #
    val = Office.Extract(officeFile=filename, extractDirectory=directory)
    if type(val) == type(True):
        if val:
            print('\tİşlem başarılı. (Successful operation)')
    print()
    print()
    input('\tDevam (Continue) <<enter>> : ')

#
def menu3():
    screenClear()
    print()
    print()
    #
    directory = input('\tPackage Directory : ').strip()
    filename  = input('\tOffice File Name  : ').strip()
    print()
    #
    val = Office.Package(officeFile=filename, packageDirectory=directory)
    if type(val) == type(True):
        if val:
            print('\tİşlem başarılı. (Successful operation)')
    print()
    print()
    input('\tDevam (Continue) <<enter>> : ')

#
def menu1():
    #
    office = sub_menu1()
    if type(office) == type(None):
        return
    #
    if type(office) == type( Office(officeFile='?') ):
        while True:
            sub_menu2(fileaname=office.getOfficeFileName())
            print()
            print()
            print('\tGeri (Back) <<b>> , Çıkış (Exit) <<e>>')
            tmp = input('\tSeçim (Selection) : ').strip()
            if tmp.lower() == 'e':
                exit(0)
            elif tmp.lower() == 'b':
                return
            elif tmp.isdigit():
                slc = int(tmp)
                if slc == 1:
                    screenClear()
                    print()
                    print()
                    print('\tFile Name : "{}" '.format( office.getOfficeFileName() ) )
                    print()
                    print()
                    print('\tBulunan Uzantılar')
                    print('\t------------------')
                    office.showExtensions()
                    print()
                    print()
                    input('\tDevam (Continue) <<enter>> : ').strip()
                elif slc == 2:
                    screenClear()
                    print()
                    print()
                    print('\tFile Name : "{}" '.format( office.getOfficeFileName() ) )
                    print()
                    office.showExtensionsFiles()
                    print()
                    print()
                    input('\tDevam (Continue) <<enter>> : ').strip()
                elif slc == 3:
                    sub_menu7(office=office)
                elif slc == 4:
                    sub_menu3(office=office)
                elif slc == 5:
                    sub_menu4(office=office)
                elif slc == 6:
                    sub_menu5(office=office)
                elif slc == 7:
                    sub_menu6(office=office)
                elif slc == 8:
                    ext_name = (office.getOfficeObj().file.f1_name.split(sep='.')[-1]).upper()
                    dir_name = office.getOfficeObj().current_directory + '\\[' + ext_name + ']_' + office.getOfficeObj().file.f1_name
                    screenClear()
                    print()
                    print()
                    print('\tOffice file name   : "'+office.getOfficeObj().file.f3_fullpath+'"')
                    print('\tExtract Directory  : (Default) "' + dir_name + '"')
                    print()
                    print()
                    directory = input('\tDefault <<enter>> , New Extract Directory : ').strip()
                    if directory == '':
                        res = office.extractAllFiles()
                    else:
                        res = office.extractAllFiles(directory)
                    if res:
                        print('\tİşlem başarılı. (Operation successful)')
                    print()
                    print()
                    input('\tDevam (Continue) <<enter>> : ').strip()

#
def sub_menu1():
    while True:
        screenClear()
        print()
        print()
        #
        filename = input('\tOffice File : ').strip()
        if filename != '':
            try:
                office_obj = Office(officeFile=filename)
                if office_obj.getOfficeObj().checkFile:
                    return office_obj
            except:
                pass
            print('\tDosya bulunamadı. (File not found)')
        print()
        print()
        val = input('\tGeri (Back) <<b>> , Devam (Continue) <<enter>> : ').strip()
        if val.lower() == 'b':
            return None
#
def sub_menu2(fileaname:str) :
    screenClear()
    print()
    print()
    print('\t File name : "{}" '.format(fileaname))
    print()
    print()
    print('\t     **** MENU ****    ')
    print('\t-----------------------')
    print('\t1) Uzantıları göster. (Show extensions) ')
    print('\t2) Dosyaları göster. (Show files name)')
    print('\t3) "Office" dosyasına ait metadata bilgileri. (Metadata infos in the office file)')
    print('\t4) Dosyaların imzasını kontrol et. (Check files signature)')
    print('\t5) JPEG/JPG dosyaları "JPGInspector" ile aç. (Open jpeg/jpg files with "JPGInspector")')
    print('\t6) Dosyaları "HexEditor" ile aç. (Open files with "HexEditor")')
    print('\t7) Seçilen dosyayı çıkart. (The file extract)')
    print('\t8) Tüm dosyaları çıkart. (All files extract)')

#
def sub_menu3(office:Office):
    while True:
        screenClear()
        print()
        print()
        print('\t File name : "{}" '.format(office.getOfficeFileName()))
        print()
        print()
        print('\t     **** MENU ****    ')
        print('\t-----------------------')
        print('\t1) Tek tek dosya imzalarını kontrol et. (Check one file signature)')
        print('\t2) Bütün dosyaların imzalarını kontrol et. (Check all files signature)')
        print()
        print()
        print('\tGeri (Back) <<b>> , Çıkış (Exit) <<e>>')
        tmp = input('\tSeçim (Selection) : ').strip()
        if tmp.lower() == 'e':
            exit(0)
        elif tmp.lower() == 'b':
            return
        elif tmp.isdigit():
            slc= int(tmp)
            if slc ==  1:
                while True:
                    screenClear()
                    print()
                    print()
                    print('\t File name : "{}" '.format(office.getOfficeFileName()))
                    print()
                    print()
                    office.showFiles()
                    print()
                    print()
                    print()
                    print()
                    print('\tGeri (Back) <<b>> , Çıkış (Exit) <<e>>')
                    tmp2 = input('\tSeçim (Selection) : ').strip()
                    if tmp2.lower() == 'e':
                        exit(0)
                    elif tmp2.lower() == 'b':
                        break
                    elif tmp2.isdigit():
                        slc = int(tmp2)
                        screenClear()
                        print()
                        print()
                        print()
                        office.showCheckFile(index=slc)
                        print()
                        print()
                        print()
                        input('\tDevam (Continue) << enter >> : ')
            if slc == 2:
                screenClear()
                print()
                print()
                print('\t File name : "{}" '.format(office.getOfficeFileName()))
                print()
                office.showCheckAllFiles()
                print()
                print()
                input('\tDevam (Continue) << enter >> : ')

#
def sub_menu4(office:Office):
    while True:
        screenClear()
        print()
        print()
        print('\t File name : "{}" '.format(office.getOfficeFileName()))
        print()
        office.showJPGjpegFiles()
        print()
        print()
        print('\tGeri (Back) <<b>> , Çıkış (Exit) <<e>>')
        tmp = input('\tSeçim (Selection) : ').strip()
        if tmp.lower() == 'e':
            exit(0)
        elif tmp.lower() == 'b':
            return
        elif tmp.isdigit():
            slc= int(tmp)
            screenClear()
            office.showJPGjpegFile(index=slc)

#
def sub_menu5(office:Office):
    while True:
        screenClear()
        print()
        print()
        print('\t File name : "{}" '.format(office.getOfficeFileName()))
        print()
        print()
        print('\t     **** MENU ****    ')
        print('\t-----------------------')
        print('\t1) Dosyanın ilk satırlarını "hex editor"de aç.(Show first line of the file with "hex editor") ')
        print('\t2) Dosyayı "hex editor"de aç. (Open file with "hex editor") ')
        print('\t3) Tüm dosyaların ilk satırlarını "hex editor"de aç. (Show first line of the files with "hex editor")')
        print('\t4) Tüm dosyaları sırayla "hex editor"de aç. (Open files in order with "hex editor" )')
        print()
        print()
        print('\tGeri (Back) <<b>> , Çıkış (Exit) <<e>>')
        tmp = input('\tSeçim (Selection) : ').strip()
        if tmp.lower() == 'e':
            exit(0)
        elif tmp.lower() == 'b':
            return
        elif tmp.isdigit():
            slc = int(tmp)
            if slc == 1:
                while True:
                    screenClear()
                    print()
                    print()
                    print('\t File name : "{}" '.format(office.getOfficeFileName()))
                    print()
                    office.showFiles()
                    print()
                    print()
                    print('\tGeri (Back) <<b>> , Çıkış (Exit) <<e>>')
                    tmp2 = input('\tSeçim (Selection) : ').strip()
                    if tmp2.lower() == 'e':
                        exit(0)
                    elif tmp2.lower() == 'b':
                        break
                    elif tmp2.isdigit():
                        slc2 = int(tmp2)
                        screenClear()
                        print()
                        print()
                        print('\t File name : "{}" '.format(office.getOfficeFileName()))
                        print()
                        office.showSummaryFileHexEditor(index=slc2)
                        print()
                        print()
                        input('\tDevam (Continue) << enter >> : ')
            #
            elif slc == 2:
                while True:
                    screenClear()
                    print()
                    print()
                    print('\t File name : "{}" '.format(office.getOfficeFileName()))
                    print()
                    office.showFiles()
                    print()
                    print()
                    print('\tGeri (Back) <<b>> , Çıkış (Exit) <<e>>')
                    tmp2 = input('\tSeçim (Selection) : ').strip()
                    if tmp2.lower() == 'e':
                        exit(0)
                    elif tmp2.lower() == 'b':
                        break
                    elif tmp2.isdigit():
                        slc2 = int(tmp2)
                        screenClear()
                        print()
                        print()
                        print('\t File name : "{}" '.format(office.getOfficeFileName()))
                        print()
                        office.showFileHexEditor(index=slc2)
                        print()
                        print()
                        input('\tDevam (Continue) << enter >> : ')
            #
            elif slc == 3:
                screenClear()
                print()
                print()
                print('\t File name : "{}" '.format(office.getOfficeFileName()))
                print()
                office.showSummaryHexAllFiles()
                print()
                print()
                input('\tDevam (Continue) << enter >> : ')
            #
            elif slc == 4:
                screenClear()
                office.showHexAllFiles()
            #


def sub_menu6(office:Office):
    while True:
        screenClear()
        print()
        print()
        print('\t File name : "{}" '.format(office.getOfficeFileName()))
        print()
        print()
        office.showFiles()
        print()
        print()
        print('\tGeri (Back) <<b>> , Çıkış (Exit) <<e>>')
        tmp2 = input('\tSeçim (Selection) : ').strip()
        if tmp2.lower() == 'e':
            exit(0)
        elif tmp2.lower() == 'b':
            return
        elif tmp2.isdigit():
            slc2 = int(tmp2)
            screenClear()
            print()
            print()
            print('\t File name : "{}" '.format(office.getOfficeFileName()))
            print()
            print()
            office.saveFile(index=slc2)
            print()
            print()
            input('\tDevam (Continue) << enter >> : ')

def sub_menu7(office:Office):
    while True:
        screenClear()
        print()
        print()
        print('\t File name : "{}" '.format(office.getOfficeFileName()))
        print()
        print()
        print('\t     **** MENU ****    ')
        print('\t-----------------------')
        print('\t1) Metadata bilgilerini göster. (Show metadata infos)')
        print('\t2) Metadata bilgilerini sil. (Delete metadata infos)')
        print()
        print()
        print('\tGeri (Back) <<b>> , Çıkış (Exit) <<e>>')
        tmp = input('\tSeçim (Selection) : ').strip()
        if tmp.lower() == 'e':
            exit(0)
        elif tmp.lower() == 'b':
            return
        elif tmp.isdigit():
            slc= int(tmp)
            if slc ==  1:
                screenClear()
                print()
                print()
                print('\t File name : "{}" '.format(office.getOfficeFileName()))
                print()
                print()
                office.showMetadata()
                print()
                print()
                input('\tDevam (Continue) << enter >> : ')
            elif slc == 2:
                screenClear()
                print()
                print()
                print('\t File name : "{}" '.format(office.getOfficeFileName()))
                print()
                print()
                res, name =office.deleteMetaData()
                if res:
                    print('\t"{}" dosya kaydedildi. (Save the file)'.format(name))
                    print('\tİşlem başarılı. (Successful operation)')
                print()
                print()
                input('\tDevam (Continue) << enter >> : ')


##### main func #####
def main():
    while True:
        slc1 = menu0()
        if slc1 == 1:
            menu1()
        elif slc1 == 2:
            menu2()
        elif slc1 == 3:
            menu3()
##### #####

main()
