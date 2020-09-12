# Only for Windows 10 / 64 bits
############################################################################
#
#   Alternative Data Stream  [ Main Program ]
#   © 2020 ABDULKADİR GÜNGÖR All Rights Reserved
#   Contact email address: abdulkadir_gungor@outlook.com
#
#	Developper:	Abdulkadir GÜNGÖR (abdulkadir_gungor@outlook.com)
#	Date:	09/2020
#	All Rights Reserved (Tüm Hakları Saklıdır)
#
############################################################################
import os
from lib.system.win.ADS.filesZoneTransfer import showFilesZoneTransfer as showZone
from lib.system.win.ADS.filesZoneTransfer import writeFilesZoneTransfer as writeZone
from lib.system.win.ADS.filesZoneTransfer import delFilesZoneTransfer as delZone
from lib.system.win.ADS.dir import currentDirectory as curDir
from lib.system.win.ADS.AlternativeDataStream import AlternativeDataStream as ADS

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
        print('\t#**||        (Alternative Data Stream)          ||**#')
        print('\t#**||             ADS Editor V1.4               ||**#')
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
        print('\t       MENU')
        print('\t--------------------------------')
        print('\t1) Zone Identifier')
        print('\t2) Alternative Data Stream (ADS)')
        print()
        print()
        print( '\tÇıkış (Exit) <<e>>' )
        tmp=input('\tSeçim (Selection) : ')
        if tmp.strip().lower() == 'e' :
            exit(0)
        elif tmp.strip().isdigit():
            slc = int(tmp.strip())
            if  0< slc <3:
                return slc
#
def menu1():
    path = ''
    while True:
        result, path = curDir(path)
        if not result:
            path = '<<Error>>'
        screenClear()
        print()
        print('\tCurrent Directory: "' + path + '"' )
        print()
        print()
        print('\t             MENU')
        print('\t--------------------------------')
        print('\t1) Klasor yolunu değiştir. [Set path]')
        print('\t2) Bilgileri göster. [Show info(s)]')
        print('\t3) Bilgileri dosyaya kaydet. [Save info(s)]')
        print('\t4) Bilgileri sil. [Delete info(s)]')
        print()
        print()
        print('\tÇıkış (Exit) <<e>> , Geri (Back) <<b>>')
        tmp = input('\tSeçim (Selection) : ')
        #
        if tmp.strip().lower() == 'e':
            exit(0)
        elif tmp.strip().lower() == 'b':
            return
        elif tmp.strip().isdigit():
            slc = int(tmp.strip())
            if slc == 1:
                screenClear()
                print()
                print()
                print('\tKlasor Yolu (Directory Path) : (Available) '+ path )
                value = input('\tKlasor Yolu (Directory Path) : ')
                if value.strip() != '':
                    path = value.strip()
            elif slc == 2:
                screenClear()
                print()
                showZone(path=path)
                print()
                print()
                input('\tDevam (Continue) <<enter>>')
            elif slc == 3:
                screenClear()
                print()
                print()
                file_name_tmp = input('\tDosya ismi (File name) : ')
                if file_name_tmp.strip() != '':
                    file_name = path + '\\' + file_name_tmp
                    writeZone(writefilename=file_name, path=path)
                    print()
                    print()
                    print('\tDosyaya kaydedildi.(Save file)')
                    input('\tDevam (Continue) <<enter>>')
                else:
                    print()
                    print()
                    print('\tDosyaya kaydedilemedi.(Couldn\'t save file)')
                    input('\tDevam (Continue) <<enter>>')
            elif slc == 4:
                screenClear()
                print()
                delZone(path=path)
                print()
                print()
                input('\tDevam (Continue) <<enter>>')



def menu2():
    ads_obj = ADS()
    while True:
        screenClear()
        print()
        print('\tCurrent Directory: "' + ads_obj.a1_currenDirectory + '"')
        print()
        print()
        print('\t             MENU')
        print('\t--------------------------------')
        print('\t1) Klasor yolunu değiştir. [Set path]')
        print('\t2) ADS İşlemleri. [ADS Operations]')
        print('\t3) Dosyayı ADS\'e kopyala. [Copy file to ADS]')
        print('\t4) Güncelle! [Update]')
        print()
        print()
        print('\tÇıkış (Exit) <<e>> , Geri (Back) <<b>>')
        tmp = input('\tSeçim (Selection) : ')
        #
        if tmp.strip().lower() == 'e':
            exit(0)
        elif tmp.strip().lower() == 'b':
            return
        elif tmp.strip().isdigit():
            slc = int(tmp.strip())
            if 0 < slc < 5:
                if slc == 1:
                    screenClear()
                    print()
                    print()
                    print('\tKlasor Yolu (Directory Path) : (Available) ' + ads_obj.a1_currenDirectory )
                    value = input('\tKlasor Yolu (Directory Path) : ')
                    if value.strip() != '':
                         ads_obj.update( new_path=value.strip() )
                elif slc == 2:
                    while True:
                        screenClear()
                        print()
                        ads_obj.showADSFile()
                        print()
                        print()
                        print('\tÇıkış (Exit) <<e>> , Geri (Back) <<b>>')
                        tmp2 = input('\tSeçim (Selection) : ')
                        #
                        if tmp2.strip().lower() == 'e':
                            exit(0)
                        elif tmp2.strip().lower() == 'b' :
                            break
                        elif tmp2.strip().isdigit():
                            slc2 = int(tmp2.strip())
                            index2 = slc2 - 1
                            if  -1 < index2 < len( ads_obj.a2_ads_files ):
                                file_obj = ads_obj.a2_ads_files[index2]
                                txt_tmp  = '\t{} : {} \t\t ADS File: "{}"'.format( file_obj.r3_type, file_obj.r1_file, file_obj.r2_ads_data )
                                while True:
                                    screenClear()
                                    print()
                                    print(txt_tmp)
                                    print()
                                    print()
                                    print('\tSil (Delete) <<d>> , Kopyala (Copy) <<c>>')
                                    print('\tÇıkış (Exit) <<e>> , Geri (Back) <<b>>')
                                    print()
                                    print()
                                    tmp3 = input('\tSeçim (Selection) : ')
                                    if tmp3.strip().lower() == 'e':
                                        exit(0)
                                    elif tmp3.strip().lower() == 'b':
                                        break
                                    elif tmp3.strip().lower() == 'd' :
                                        print()
                                        ads_obj.delADSFile(index=slc2)
                                        print()
                                        print()
                                        input('\tDevam (Continue) <<enter>>')
                                        break
                                    elif tmp3.strip().lower() == 'c' :
                                        while True:
                                            screenClear()
                                            print()
                                            tmp4 = input('\tDosya adı (File name) : ')
                                            if tmp4.strip() == '':
                                                print()
                                                print()
                                                print('\tÇıkış (Exit) <<e>> , Geri (Back) <<b>>')
                                                tmp7 = input('\tDevam (Continue) <<enter>>').strip()
                                                if tmp7.lower() == 'e':
                                                    exit(0)
                                                elif tmp7.lower() == 'b':
                                                    break
                                            else:
                                                print()
                                                ads_obj.copyADSFile_To_Disk( index=slc2, filename=tmp4.strip() )
                                                print()
                                                print()
                                                input('\tDevam (Continue) <<enter>>')
                                                break
                                        #
                                        break
                elif slc == 3:
                    while True:
                        screenClear()
                        print()
                        print('\tCurrent Directory: "' + ads_obj.a1_currenDirectory + '"')
                        print()
                        print()
                        copy_file = input('\tKopyalanacak dosya adı (Copy file name) : ').strip()
                        ads_file  = input('\tADS dosya/klasor adı (ADS file/directory name) : ').strip()
                        ads_data  = input('\tADS data adı (ADS data name) : ').strip()
                        if copy_file != '' and ads_file != '' and ads_data != '':
                            print()
                            ads_obj.copyDisk_To_ADSFile(DiskFile=copy_file, ADSFile=ads_file, ADSDataName=ads_data)
                            print()
                            print()
                            input('\tDevam (Continue) <<enter>>')
                            break
                        print()
                        print()
                        print('\tÇıkış (Exit) <<e>> , Geri (Back) <<b>>')
                        tmp5 = input('\tDevam (Continue) <<enter>>').strip()
                        if tmp5.lower() == 'e':
                            exit(0)
                        elif tmp5.lower() == 'b':
                            break
                #
                elif slc == 4:
                    screenClear()
                    print()
                    print('\tCurrent Directory: "' + ads_obj.a1_currenDirectory + '"')
                    print()
                    print()
                    print('\t...')
                    ads_obj.update()
                    print('\tADS içeriği güncellendi. (ADS content has updated!)')
                    print()
                    print()
                    print('\tÇıkış (Exit) <<e>> ')
                    tmp5 = input('\tGeri (Back) <<enter>>').strip()
                    if tmp5.lower() == 'e':
                        exit(0)


###
def main():
    while True:
        selection = menu0()
        if selection == 1:
            menu1()
        elif selection == 2:
            menu2()


###
###
main()
###
###










