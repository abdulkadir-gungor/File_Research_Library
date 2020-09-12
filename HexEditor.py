#!/usr/bin/python3
############################################################################
#
#	HexEditor  [ Main Program ]
#   © 2020 ABDULKADİR GÜNGÖR All Rights Reserved
#   Contact email address: abdulkadir_gungor@outlook.com
#
#	Developper:	Abdulkadir GÜNGÖR (abdulkadir_gungor@outlook.com)
#	Date:	08/2020
#	All Rights Reserved (Tüm Hakları Saklıdır)
#
############################################################################
from  lib.hexlib.ReadBinaryFileWithABuffer import ReadBinaryFileWithABuffer as rfile
from  lib.hexlib.ShowHex import showIndexHexFile
import os

settings = dict(    # <<Start Settings>>
                    file='',        # Başlangıçta tanımlı dosya adı (YOK)
                    index=1,
                    columnsize=10,  # Hex Editorde 10 karakter Uzunluk
                    lineshalt=-1,   # Satır Sonu Yok
                    buffer=1024     # 1024 bayt, 1024 bayt okuyacak
                )   # <</Start Settings>>

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
def menu0(settings:dict)->dict:
    screenClear()
    print()
    print('\t#####################################################')
    print('\t#/*************************************************\#')
    print('\t#**||~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~||**#')
    print('\t#**||                                           ||**#')
    print('\t#**||            Hex Editor V2.1                ||**#')
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
    tmp=input('\tFile : ')
    file = tmp.strip()
    if file.isprintable():
        settings['file']=file
    return settings

# Ayar Menüsü
def menu1(settings:dict)->dict:
    while True:
        screenClear()
        print()
        print("\tAyarlar (Settings)")
        print("\t"+'-'*30)
        print("\t1) File : '{}'".format(settings['file']))
        print("\t2) Hex Editor Start Index : {}".format(settings['index']))
        print("\t3) Hex Editor Column Size : {}".format(settings['columnsize']))
        print("\t4) Hex Editor Line Halt : {}".format(settings['lineshalt']))
        print("\t5) Hex Editor Buffer Size : {}".format(settings['buffer']))
        print()
        print()
        if settings['lineshalt'] != -1:
            suggestion_val = settings['columnsize'] * settings['lineshalt']
            if settings['buffer'] < suggestion_val:
                print("\tHex Editor için minimum buffer size '{}'\n"
                      "\tdeğerinden büyük olması önerilmektedir.".format(suggestion_val))
        print()
        print()
        selection=input('\n\tSelection (Continue <<Enter>> , Exit <<e>>) : ')
        if selection.isdigit():
            if selection == "1":
                selection=input("\tFile :")
                if selection.strip().isprintable():
                    settings['file'] = selection.strip()
            elif selection == "2":
                selection=input("\tStart Index : ")
                if selection.strip().isdigit():
                    settings['index'] = int(selection.strip())
            elif selection == "3":
                selection=input("\tColumn Size : ")
                if selection.strip().isdigit():
                    settings['columnsize'] = int(selection.strip())
            elif selection == "4":
                selection = input("\tLine Halt : ")
                if selection.strip().isdigit():
                    if int(selection.strip()) > 0:
                        settings['lineshalt'] = int(selection.strip())
                elif selection.strip() == "-1":
                    settings['lineshalt'] = -1
            elif selection == "5":
                selection = input("\tBuffer Size : ")
                if selection.strip().isdigit():
                    if int(selection.strip()) > 0:
                        settings['buffer'] = int(selection.strip())
        elif selection.lower() == 'e':
            exit(0)
        elif len(selection) == 0:
            break
    return  settings

# <<Programın Akışı>>
settings=menu0(settings=settings)
while True:
    settings=menu1(settings=settings)
    try:
        screenClear()
        print()
        rfile_tmp = rfile(filename=settings['file'], buffer=settings['buffer'])
        showIndexHexFile (readFile=rfile_tmp, columnSize=settings['columnsize'],linesHalt=settings['lineshalt'],index=settings['index'] )
        selection=input('\n\t[Program] Ayarlar (Settings) <<Enter>> , Çıkış (Exit) <<e>> : ')
        if selection.strip().lower() == 'e':
            break
    except IOError:
        screenClear()
        print()
        print("\t'{}' adlı bir dosya okunurken hata oluştu.".format(settings['file']))
        print()
        print()
        selection = input('\n\t[Program] Ayarlar (Settings) <<Enter>> , Çıkış (Exit) <<e>> : ')
        if selection.strip().lower() == 'e':
            break
# <</Program Akışı>>