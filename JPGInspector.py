#!/usr/bin/python3
############################################################################
#
#   JPG/JPEG Inspector [ Main Program ]
#   © 2020 ABDULKADİR GÜNGÖR All Rights Reserved
#   Contact email address: abdulkadir_gungor@outlook.com
#
#	Developper:	Abdulkadir GÜNGÖR (abdulkadir_gungor@outlook.com)
#	Date:	08/2020
#	All Rights Reserved (Tüm Hakları Saklıdır)
#
############################################################################
from  lib.image.jpg.JPGFile import JPGFile as jpg
import os
#

#
class element:
    def __init__(self):
        from lib.image.jpg.sector import Sector
        from lib.image.jpg.app.APPTAG import APPTAG as App
        self.e1_sector_check = False
        self.e1_sector = Sector()
        self.e2_app_check = False
        self.e2_app = App( Sector(),b'' )
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


# screen_1
def screen_1():
    #
    txt0_tmp  = '\t   *****  MENU  *****     '
    txt1_tmp  = '\t ------------------------ '
    txt1  = "\t 1) Detail 'APPn and COM'  ----."
    txt2  = "\t                               | "
    txt3  = "\t 2) Normal 'APPn and COM'  ----+ -------  ***{ Application and Comment Segments }***"
    txt4  = "\t                               | "
    txt5  = "\t 3) Summary 'APPn and COM' ----. "
    txt6  = "\t 4) Detail Segment ----. "
    txt7  = "\t                       | "
    txt8  = "\t 5) Normal Segment ----+ ------  ***{ All Segments (Except RST) }***"
    txt9  = "\t                       | "
    txt10 = "\t 6) Summary Segment ---. "
    txt11 = "\t 7) Detail All Segment ----. "
    txt12 = "\t                           | "
    txt13 = "\t 8) Normal All Segment ----+ ------  ***{ All Segments }***"
    txt14 = "\t                           | "
    txt15 = "\t 9) Summary All Segment ---. "
    txt16 = "\t 10) Application and Comment Segments --. "
    txt17 = "\t                                        | "
    txt18 = "\t 11) All Segments (Except RST) ---------+ ------- ***{ Use Element Index }***"
    txt19 = "\t                                        | "
    txt20 = "\t 12) All Segment -----------------------. "
    #
    print()
    print( txt1_tmp )
    print( txt0_tmp )
    print( txt1_tmp )
    print()
    print()
    print( txt1 )
    print( txt2 )
    print( txt3 )
    print( txt4 )
    print( txt5 )
    print()
    print()
    print( txt6 )
    print( txt7 )
    print( txt8 )
    print( txt9 )
    print( txt10 )
    print()
    print()
    print( txt11 )
    print( txt12 )
    print( txt13 )
    print( txt14 )
    print( txt15 )
    print()
    print()
    print( txt16 )
    print( txt17 )
    print( txt18 )
    print( txt19 )
    print( txt20 )


# Giriş Menüsü
def menu_0() -> str:
    screenClear()
    print()
    print('\t#####################################################')
    print('\t#/*************************************************\#')
    print('\t#**||~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~||**#')
    print('\t#**||                                           ||**#')
    print('\t#**||         JPG/JPEG Inspector V1.1           ||**#')
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
        return file
    return ''

# Ana Menü
def menu_1() -> int:
    while True:
        screenClear()
        screen_1()
        print()
        print()
        print('\tÇıkış (Exit) <<e>> , Geri (Back) <<b>> ')
        selection = input('\tSeçim (Selection) : ').strip()
        if selection.isdigit():
            val = int(selection)
            if 0 < val < 13:
                return val
        else:
            if selection.lower() == 'e':
                exit(0)
            elif selection.lower() == 'b':
                return -1
# Menu 2
def menu_2( file:jpg, selection:int) -> int:
    while True:
        sub_menu_1(file, selection)
        if 0 < selection < 10:
            selection2 = input('\n\n\tGeri (Back) <<b>> , Seçim (Selection) : ')
        else:
            selection2 = input('\n\n\tGeri (Back) <<b>> , Seçim (Selection -Element Index-) : ')
        if selection2.isdigit():
            return int(selection2)
        else:
            if selection2.lower() == 'b':
                return -1
#
# Menu 3
def menu_3 ( file:jpg, ee:element, colSize:int=20, linesHalt:int=-1) -> int:
    #
    while True:
        screenClear()
        selection3 = ' '
        if ee.e1_sector_check and ee.e2_app_check:
            if ee.e2_app.a1_tag_no == 1: # JFIF
                txt1 = '\tSegment Type Name : {} '.format(ee.e1_sector.type.shortname)
                txt2 = '\tSegment Index     : {} '.format(ee.e1_sector.no)
                txt3 = '\tSegment Size      : {} bayt'.format((ee.e1_sector.end - ee.e1_sector.start))
                txt4 = '\tApp Name          : {} '.format(ee.e2_app.a2_tag_name )
                #
                print(txt1)
                print(txt2)
                print(txt3)
                print(txt4)
                print()
                print('\t     Menu')
                print('\t' + ('-' * 20))
                print('\t1) Hex Editor')
                print('\t2) Show JFIF ')
                print('\t3) Show JFIF (Not include thumbnail)')
                print()
                selection3 = input('\n\n\tGeri (Back) <<b>> , Seçim (Selection) : ')
                if selection3.strip().isdigit():
                    if int(selection3.strip()) == 1:
                        sub_menu_2(file=file, ee=ee, func_no=1, colSize=colSize, linesHalt=linesHalt)
                        print()
                        print()
                        input('\n\n\tDevam (Continue) <<Enter>>  : ')
                    elif int(selection3.strip()) == 2:
                        sub_menu_2(file=file, ee=ee, func_no=3, colSize=colSize, linesHalt=linesHalt)
                        print()
                        print()
                        input('\n\n\tDevam (Continue) <<Enter>>  : ')
                    elif int(selection3.strip()) == 3:
                        sub_menu_2(file=file, ee=ee, func_no=2, colSize=colSize, linesHalt=linesHalt)
                        print()
                        print()
                        input('\n\n\tDevam (Continue) <<Enter>>  : ')
            #
            elif ee.e2_app.a1_tag_no == 2:  # JFXX
                txt1 = '\tSegment Type Name : {} '.format(ee.e1_sector.type.shortname)
                txt2 = '\tSegment Index     : {} '.format(ee.e1_sector.no)
                txt3 = '\tSegment Size      : {} bayt'.format((ee.e1_sector.end - ee.e1_sector.start))
                txt4 = '\tApp Name          : {} '.format(ee.e2_app.a2_tag_name )
                #
                print(txt1)
                print(txt2)
                print(txt3)
                print(txt4)
                print()
                print('\t     Menu')
                print('\t' + ('-' * 20))
                print('\t1) Hex Editor')
                print('\t2) Show JFXX ')
                print('\t3) Show JFXX (Not include thumbnail)')
                print()
                selection3 = input('\n\n\tGeri (Back) <<b>> , Seçim (Selection) : ')
                if selection3.strip().isdigit():
                    if int(selection3.strip()) == 1:
                        sub_menu_2(file=file, ee=ee, func_no=1, colSize=colSize, linesHalt=linesHalt)
                        print()
                        print()
                        input('\n\n\tDevam (Continue) <<Enter>>  : ')
                    elif int(selection3.strip()) == 2:
                        sub_menu_2(file=file, ee=ee, func_no=3, colSize=colSize, linesHalt=linesHalt)
                        print()
                        print()
                        input('\n\n\tDevam (Continue) <<Enter>>  : ')
                    elif int(selection3.strip()) == 3:
                        sub_menu_2(file=file, ee=ee, func_no=2, colSize=colSize, linesHalt=linesHalt)
                        print()
                        print()
                        input('\n\n\tDevam (Continue) <<Enter>>  : ')
            elif ee.e2_app.a1_tag_no == 3:  # Exif
                #
                txt1 = '\tSegment Type Name : {} '.format(ee.e1_sector.type.shortname)
                txt2 = '\tSegment Index     : {} '.format(ee.e1_sector.no)
                txt3 = '\tSegment Size      : {} bayt'.format((ee.e1_sector.end - ee.e1_sector.start))
                txt4 = '\tApp Name          : {} '.format(ee.e2_app.a2_tag_name )
                #
                print(txt1)
                print(txt2)
                print(txt3)
                print(txt4)
                print()
                print('\t     Menu')
                print('\t' + ('-' * 20))
                print('\t1) Hex Editor')
                print('\t2) Show <<Exif>> Header  ')
                print("\t3) Show <<Exif>> '0IFD' Tag Names")
                print("\t4) Show <<Exif>> 'ExifIFD' Tag Names")
                print("\t5) Show <<Exif>> 'InterOperabilityIFD' Tag Names")
                print("\t6) Show <<Exif>> 'GpsIFD' Tag Names")
                print("\t7) Show <<Exif>> '1IFD' Tag Names")
                #
                print()
                selection3 = input('\n\n\tGeri (Back) <<b>> , Seçim (Selection) : ')
                if selection3.strip().isdigit():
                    if int(selection3.strip()) == 1:
                        sub_menu_2(file=file, ee=ee, func_no=1, colSize=colSize, linesHalt=linesHalt)
                        print()
                        print()
                        input('\n\n\tDevam (Continue) <<Enter>>  : ')
                    elif  int(selection3.strip()) == 2:
                        sub_menu_2(file=file, ee=ee, func_no=3, colSize=colSize, linesHalt=linesHalt)
                        print()
                        print()
                        input('\n\n\tDevam (Continue) <<Enter>>  : ')
                    elif  int(selection3.strip()) == 3:
                    #
                        while True:
                            sub_menu_2(file=file, ee=ee, func_no=5, colSize=colSize, linesHalt=linesHalt)
                            print()
                            print()
                            selection4 = input('\n\n\tGeri (Back) <<b>> , Seçim (Selection) : ')
                            if selection4.strip().lower() == 'b':
                                break
                            elif selection4.strip().isdigit():
                                val4 = int( selection4.strip() )
                                if ee.e2_app_check:
                                    screenClear()
                                    ee.e2_app.no3_exif_show0IFDTag(index=val4)
                                    print()
                                    print()
                                    input('\n\n\tDevam (Continue) <<Enter>>  : ')
                    #
                    elif  int(selection3.strip()) == 4:
                    #
                        while True:
                            sub_menu_2(file=file, ee=ee, func_no=6, colSize=colSize, linesHalt=linesHalt)
                            print()
                            print()
                            selection4 = input('\n\n\tGeri (Back) <<b>> , Seçim (Selection) : ')
                            if selection4.strip().lower() == 'b':
                                break
                            elif selection4.strip().isdigit():
                                val4 = int( selection4.strip() )
                                if ee.e2_app_check:
                                    screenClear()
                                    ee.e2_app.no3_exif_showExifIFDTag(index=val4)
                                    print()
                                    print()
                                    input('\n\n\tDevam (Continue) <<Enter>>  : ')
                    #
                    elif  int(selection3.strip()) == 5:
                        #
                        while True:
                            sub_menu_2(file=file, ee=ee, func_no=7, colSize=colSize, linesHalt=linesHalt)
                            print()
                            print()
                            selection4 = input('\n\n\tGeri (Back) <<b>> , Seçim (Selection) : ')
                            if selection4.strip().lower() == 'b':
                                break
                            elif selection4.strip().isdigit():
                                val4 = int( selection4.strip() )
                                if ee.e2_app_check:
                                    screenClear()
                                    ee.e2_app.no3_exif_showInterOperabilityIFDTag(index=val4)
                                    print()
                                    print()
                                    input('\n\n\tDevam (Continue) <<Enter>>  : ')
                        #
                    elif  int(selection3.strip()) == 6:
                        #
                        while True:
                            sub_menu_2(file=file, ee=ee, func_no=8, colSize=colSize, linesHalt=linesHalt)
                            print()
                            print()
                            selection4 = input('\n\n\tGeri (Back) <<b>> , Seçim (Selection) : ')
                            if selection4.strip().lower() == 'b':
                                break
                            elif selection4.strip().isdigit():
                                val4 = int(selection4.strip())
                                if ee.e2_app_check:
                                    screenClear()
                                    ee.e2_app.no3_exif_showGpsIFDTag(index=val4)
                                    print()
                                    print()
                                    input('\n\n\tDevam (Continue) <<Enter>>  : ')
                        #
                    elif  int(selection3.strip()) == 7:
                        #
                        while True:
                            sub_menu_2(file=file, ee=ee, func_no=9, colSize=colSize, linesHalt=linesHalt)
                            print()
                            print()
                            selection4 = input('\n\n\tGeri (Back) <<b>> , Seçim (Selection) : ')
                            if selection4.strip().lower() == 'b':
                                break
                            elif selection4.strip().isdigit():
                                val4 = int( selection4.strip() )
                                if ee.e2_app_check:
                                    screenClear()
                                    ee.e2_app.no3_exif_show1IFDTag(index=val4)
                                    print()
                                    print()
                                    input('\n\n\tDevam (Continue) <<Enter>>  : ')
                #
            elif ee.e2_app.a1_tag_no == 4:  # ICC_PROFILE
                #
                txt1 = '\tSegment Type Name : {} '.format(ee.e1_sector.type.shortname)
                txt2 = '\tSegment Index     : {} '.format(ee.e1_sector.no)
                txt3 = '\tSegment Size      : {} bayt'.format((ee.e1_sector.end - ee.e1_sector.start))
                txt4 = '\tApp Name          : {} '.format(ee.e2_app.a2_tag_name )
                #
                print(txt1)
                print(txt2)
                print(txt3)
                print(txt4)
                print()
                print('\t     Menu')
                print('\t' + ('-' * 20))
                print('\t1) Hex Editor')
                print('\t2) Show ICC_PROFILE Header')
                print("\t3) Show ICC_PROFILE Body Tags Name")
                #
                print()
                selection3 = input('\n\n\tGeri (Back) <<b>> , Seçim (Selection) : ')
                if selection3.strip().isdigit():
                    if int(selection3.strip()) == 1:
                        sub_menu_2(file=file, ee=ee, func_no=1, colSize=colSize, linesHalt=linesHalt)
                        print()
                        print()
                        input('\n\n\tDevam (Continue) <<Enter>>  : ')
                    elif int(selection3.strip()) == 2:
                        sub_menu_2(file=file, ee=ee, func_no=3, colSize=colSize, linesHalt=linesHalt)
                        print()
                        print()
                        input('\n\n\tDevam (Continue) <<Enter>>  : ')
                    elif int(selection3.strip()) == 3:
                        #
                        while True:
                            sub_menu_2(file=file, ee=ee, func_no=11, colSize=colSize, linesHalt=linesHalt)
                            print()
                            print()
                            selection4 = input('\n\n\tGeri (Back) <<b>> , Seçim (Selection) : ')
                            if selection4.strip().lower() == 'b':
                                break
                            elif selection4.strip().isdigit():
                                val4 = int(selection4.strip())
                                if ee.e2_app_check:
                                    screenClear()
                                    ee.e2_app.showBodyTag(index=val4)
                                    print()
                                    print()
                                    input('\n\n\tDevam (Continue) <<Enter>>  : ')
                    #
            elif ee.e2_app.a1_tag_no == 5:  # XMP
                #
                txt1 = '\tSegment Type Name : {} '.format(ee.e1_sector.type.shortname)
                txt2 = '\tSegment Index     : {} '.format(ee.e1_sector.no)
                txt3 = '\tSegment Size      : {} bayt'.format((ee.e1_sector.end - ee.e1_sector.start))
                txt4 = '\tApp Name          : {} '.format(ee.e2_app.a2_tag_name )
                #
                print(txt1)
                print(txt2)
                print(txt3)
                print(txt4)
                print()
                print('\t     Menu')
                print('\t' + ('-' * 20))
                print('\t1) Hex Editor')
                print('\t2) Show XMP Header')
                print("\t3) Show XMP ")
                #
                print()
                selection3 = input('\n\n\tGeri (Back) <<b>> , Seçim (Selection) : ')
                if selection3.strip().isdigit():
                    if int(selection3.strip()) == 1:
                        sub_menu_2(file=file, ee=ee, func_no=1, colSize=colSize, linesHalt=linesHalt)
                        print()
                        print()
                        input('\n\n\tDevam (Continue) <<Enter>>  : ')
                    elif int(selection3.strip()) == 2:
                        sub_menu_2(file=file, ee=ee, func_no=2, colSize=colSize, linesHalt=linesHalt)
                        print()
                        print()
                        input('\n\n\tDevam (Continue) <<Enter>>  : ')
                    elif int(selection3.strip()) == 3:
                        sub_menu_2(file=file, ee=ee, func_no=3, colSize=colSize, linesHalt=linesHalt)
                        print()
                        print()
                        input('\n\n\tDevam (Continue) <<Enter>>  : ')
            #
            elif ee.e2_app.a1_tag_no == 6:  # MPF
                #
                txt1 = '\tSegment Type Name : {} '.format(ee.e1_sector.type.shortname)
                txt2 = '\tSegment Index     : {} '.format(ee.e1_sector.no)
                txt3 = '\tSegment Size      : {} bayt'.format((ee.e1_sector.end - ee.e1_sector.start))
                txt4 = '\tApp Name          : {} '.format(ee.e2_app.a2_tag_name )
                #
                print(txt1)
                print(txt2)
                print(txt3)
                print(txt4)
                print()
                print('\t     Menu')
                print('\t' + ('-' * 20))
                print('\t1) Hex Editor')
                print('\t2) Show MPF Header')
                print("\t3) Show MPF Body Tags Name")
                #
                print()
                selection3 = input('\n\n\tGeri (Back) <<b>> , Seçim (Selection) : ')
                if selection3.strip().isdigit():
                    if int(selection3.strip()) == 1:
                        sub_menu_2(file=file, ee=ee, func_no=1, colSize=colSize, linesHalt=linesHalt)
                        print()
                        print()
                        input('\n\n\tDevam (Continue) <<Enter>>  : ')
                    elif int(selection3.strip()) == 2:
                        sub_menu_2(file=file, ee=ee, func_no=2, colSize=colSize, linesHalt=linesHalt)
                        print()
                        print()
                        input('\n\n\tDevam (Continue) <<Enter>>  : ')
                    elif int(selection3.strip()) == 3:
                        #
                        while True:
                            sub_menu_2(file=file, ee=ee, func_no=11, colSize=colSize, linesHalt=linesHalt)
                            print()
                            print()
                            selection4 = input('\n\n\tGeri (Back) <<b>> , Seçim (Selection) : ')
                            if selection4.strip().lower() == 'b':
                                break
                            elif selection4.strip().isdigit():
                                val4 = int(selection4.strip())
                                if ee.e2_app_check:
                                    screenClear()
                                    ee.e2_app.showBodyTag(index=val4)
                                    print()
                                    print()
                                    input('\n\n\tDevam (Continue) <<Enter>>  : ')
            elif ee.e2_app.a1_tag_no == 7:  # Photoshop
                #
                txt1 = '\tSegment Type Name : {} '.format(ee.e1_sector.type.shortname)
                txt2 = '\tSegment Index     : {} '.format(ee.e1_sector.no)
                txt3 = '\tSegment Size      : {} bayt'.format((ee.e1_sector.end - ee.e1_sector.start))
                txt4 = '\tApp Name          : {} '.format(ee.e2_app.a2_tag_name )
                #
                print(txt1)
                print(txt2)
                print(txt3)
                print(txt4)
                print()
                print('\t     Menu')
                print('\t' + ('-' * 20))
                print('\t1) Hex Editor')
                print('\t2) Show Photoshop Header')
                print("\t3) Show Photoshop Body Tags Name")
                #
                print()
                selection3 = input('\n\n\tGeri (Back) <<b>> , Seçim (Selection) : ')
                if selection3.strip().isdigit():
                    if int(selection3.strip()) == 1:
                        sub_menu_2(file=file, ee=ee, func_no=1, colSize=colSize, linesHalt=linesHalt)
                        print()
                        print()
                        input('\n\n\tDevam (Continue) <<Enter>>  : ')
                    elif int(selection3.strip()) == 2:
                        sub_menu_2(file=file, ee=ee, func_no=2, colSize=colSize, linesHalt=linesHalt)
                        print()
                        print()
                        input('\n\n\tDevam (Continue) <<Enter>>  : ')
                    elif int(selection3.strip()) == 3:
                        #
                        while True:
                            sub_menu_2(file=file, ee=ee, func_no=11, colSize=colSize, linesHalt=linesHalt)
                            print()
                            print()
                            selection4 = input('\n\n\tGeri (Back) <<b>> , Seçim (Selection) : ')
                            if selection4.strip().lower() == 'b':
                                break
                            elif selection4.strip().isdigit():
                                val4 = int(selection4.strip())
                                if ee.e2_app_check:
                                    screenClear()
                                    ee.e2_app.showBodyTag(index=val4)
                                    print()
                                    print()
                                    input('\n\n\tDevam (Continue) <<Enter>>  : ')
                #
            elif ee.e2_app.a1_tag_no == 8:  # Adobe
                #
                txt1 = '\tSegment Type Name : {} '.format(ee.e1_sector.type.shortname)
                txt2 = '\tSegment Index     : {} '.format(ee.e1_sector.no)
                txt3 = '\tSegment Size      : {} bayt'.format((ee.e1_sector.end - ee.e1_sector.start))
                txt4 = '\tApp Name          : {} '.format(ee.e2_app.a2_tag_name )
                #
                print(txt1)
                print(txt2)
                print(txt3)
                print(txt4)
                print()
                print('\t     Menu')
                print('\t' + ('-' * 20))
                print('\t1) Hex Editor')
                print("\t2) Show 'Adobe' Header")
                print("\t3) Show 'Adobe' ")
                #
                print()
                selection3 = input('\n\n\tGeri (Back) <<b>> , Seçim (Selection) : ')
                if selection3.strip().isdigit():
                    if int(selection3.strip()) == 1:
                        sub_menu_2(file=file, ee=ee, func_no=1, colSize=colSize, linesHalt=linesHalt)
                        print()
                        print()
                        input('\n\n\tDevam (Continue) <<Enter>>  : ')
                    elif int(selection3.strip()) == 2:
                        sub_menu_2(file=file, ee=ee, func_no=2, colSize=colSize, linesHalt=linesHalt)
                        print()
                        print()
                        input('\n\n\tDevam (Continue) <<Enter>>  : ')
                    elif int(selection3.strip()) == 3:
                        sub_menu_2(file=file, ee=ee, func_no=3, colSize=colSize, linesHalt=linesHalt)
                        print()
                        print()
                        input('\n\n\tDevam (Continue) <<Enter>>  : ')
                #
            elif ee.e2_app.a1_tag_no == 9:  # Adobe_CM
                #
                txt1 = '\tSegment Type Name : {} '.format(ee.e1_sector.type.shortname)
                txt2 = '\tSegment Index     : {} '.format(ee.e1_sector.no)
                txt3 = '\tSegment Size      : {} bayt'.format((ee.e1_sector.end - ee.e1_sector.start))
                txt4 = '\tApp Name          : {} '.format(ee.e2_app.a2_tag_name )
                #
                print(txt1)
                print(txt2)
                print(txt3)
                print(txt4)
                print()
                print('\t     Menu')
                print('\t' + ('-' * 20))
                print('\t1) Hex Editor')
                print("\t2) Show 'Adobe_CM' Header")
                print("\t3) Show 'Adobe_CM' ")
                #
                print()
                selection3 = input('\n\n\tGeri (Back) <<b>> , Seçim (Selection) : ')
                if selection3.strip().isdigit():
                    if int(selection3.strip()) == 1:
                        sub_menu_2(file=file, ee=ee, func_no=1, colSize=colSize, linesHalt=linesHalt)
                        print()
                        print()
                        input('\n\n\tDevam (Continue) <<Enter>>  : ')
                    elif int(selection3.strip()) == 2:
                        sub_menu_2(file=file, ee=ee, func_no=2, colSize=colSize, linesHalt=linesHalt)
                        print()
                        print()
                        input('\n\n\tDevam (Continue) <<Enter>>  : ')
                    elif int(selection3.strip()) == 3:
                        sub_menu_2(file=file, ee=ee, func_no=3, colSize=colSize, linesHalt=linesHalt)
                        print()
                        print()
                        input('\n\n\tDevam (Continue) <<Enter>>  : ')
            #
        elif ee.e1_sector_check and  not ee.e2_app_check:
            txt1 = '\tSegment Type Name : {} '.format(ee.e1_sector.type.shortname)
            txt2 = '\tSegment Index     : {} '.format(ee.e1_sector.no)
            txt3 = '\tSegment Size      : {} bayt'.format((ee.e1_sector.end - ee.e1_sector.start))
            #
            print(txt1)
            print(txt2)
            print(txt3)
            print()
            print('\t     Menu')
            print('\t' + ('-' * 20))
            print('\t1) Hex Editor')
            print()
            selection3 = input('\n\n\tGeri (Back) <<b>> , Seçim (Selection) : ')
            if selection3.strip().isdigit():
                if int(selection3.strip()) == 1:
                    sub_menu_2(file=file, ee=ee, func_no=1, colSize=colSize, linesHalt=linesHalt)
                    print()
                    print()
                    input('\n\n\tDevam (Continue) <<Enter>>  : ')
        else:
            print()
            print()
            print('\tSegment bulunamadı. (Segment could not found)"')
            print()
            print()
            input('\n\n\tGeri (Back) <<Enter>>  : ')
            return 0
        #
        if selection3.strip().lower() == 'b':
            return 0
#


# Alt Menu 1files
def sub_menu_1( file:jpg, selection:int):
    screenClear()
    if selection == 1:
        file.func3_showAllAppsDetails()
    elif selection == 2:
        file.func3_showAllApps()
    elif selection == 3:
        file.func3_showAllAppsSummary()
    elif selection == 4:
        file.func4_showSegmentsDetails()
    elif selection == 5:
        file.func4_showSegments()
    elif selection == 6:
        file.func4_showSegmentsSummary()
    elif selection == 7:
        file.func5_showAllSegmentsDetails()
    elif selection == 8:
        file.func5_showAllSegments()
    elif selection == 9:
        file.func5_showAllSegmentsSummary()
    elif selection == 10:
        file.graph_apps()
    elif selection == 11:
        file.graph_segments()
    elif selection == 12:
        file.graph_allsegments()

# Alt Menu 2
def sub_menu_2( file:jpg, ee:element , func_no:int, colSize=20, linesHalt=-1 ):
    from lib.hexlib.ShowHex import show2HexBytes as s2hex
    screenClear()
    if  ee.e1_sector_check and func_no == 1:
        s2hex(  dataBytes= file.bytes[ee.e1_sector.start:ee.e1_sector.end],
                dataName = ee.e1_sector.type.shortname,
                index=ee.e1_sector.start+1,
                columnSize=colSize,
                linesHalt=linesHalt
                )
    elif ee.e2_app_check and func_no == 2:
        ee.e2_app.showHeader()
    elif ee.e2_app_check and func_no == 3:
        ee.e2_app.show()
    elif ee.e2_app_check and func_no == 4:
        ee.e2_app.no3_exif_showAllTagsNames()
    elif ee.e2_app_check and func_no == 5:
        ee.e2_app.no3_exif_show0IFDTagsNames()
    elif ee.e2_app_check and func_no == 6:
        ee.e2_app.no3_exif_showExifIFDTagsNames()
    elif ee.e2_app_check and func_no == 7:
        ee.e2_app.no3_exif_showInteroperabilityIFDTagsNames()
    elif ee.e2_app_check and func_no == 8:
        ee.e2_app.no3_exif_showGpsIFDTagsNames()
    elif ee.e2_app_check and func_no == 9:
        ee.e2_app.no3_exif_show1IFDTagNames()
    elif ee.e2_app_check and func_no == 10:
        ee.e2_app.no6_mpf_showHex()
    elif ee.e2_app_check and func_no == 11:
        ee.e2_app.showBodyTagsNames()


    else:
        txt1 = "\n\n\tSegment bulunamadı. (Segment could not found)"
        print( txt1 )
#

# check sub menu 2
def check_menu_2(file:jpg, selection1:int, selection2:int) -> element:
    re = element()
    if 0 < selection1 < 4:
        tmp_app = file.func3_findAllApp(index=selection2)
        if 0 < tmp_app.a1_tag_no:
            re.e2_app_check = True
            re.e2_app = tmp_app
        if 0 < tmp_app.a0_sector.no:
            re.e1_sector_check =  True
            re.e1_sector = tmp_app.a0_sector
    elif 3 < selection1 < 13:
        if  3 < selection1 < 7:
            tmp_sector = file.func4_findSegment(index=selection2)
        elif 6 < selection1 < 10:
            tmp_sector = file.func5_findAllSegment(index=selection2)
        else:
            tmp_sector = file.findSectorUsingElementIndex(index=selection2)
        #Sector
        if 0 < tmp_sector.no:
            re.e1_sector_check = True
            re.e1_sector = tmp_sector
        if 0 <= tmp_sector.applistno:
            tmp_app = file.apps[tmp_sector.applistno]
            if 0 < tmp_app.a1_tag_no:
                re.e2_app_check = True
                re.e2_app = tmp_app
    return re

##### Main Program #####
def jpgInspector():
    while True:
        while True:
            try:
                file=menu_0()
                jpg_info = jpg(filename=file)
                break
            except:
                pass
        while True:
            selection =  menu_1()
            if selection != -1:
                selection2 = menu_2(jpg_info, selection)
                if selection2 != -1:
                    while True:
                        val1 = menu_3(file=jpg_info, ee=check_menu_2(jpg_info, selection, selection2),colSize=20, linesHalt=-1 )
                        if val1 == 0:
                            selection2 = menu_2(jpg_info, selection)
                            if selection2 == -1:
                                break
                        elif val1 == -1:
                            break
            elif selection == -1:
                break
#####   #####


# Program Start
jpgInspector()