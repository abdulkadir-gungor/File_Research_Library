#!/usr/bin/python3
############################################################################
#
#	Pdf Inspector  [ Main Program ]
#   © 2020 ABDULKADİR GÜNGÖR All Rights Reserved
#   Contact email address: abdulkadir_gungor@outlook.com
#
#	Developper:	Abdulkadir GÜNGÖR (abdulkadir_gungor@outlook.com)
#	Date:	08/2020
#	All Rights Reserved (Tüm Hakları Saklıdır)
#
############################################################################
from lib.pdf.PdfFile import PdfFile as pdfFile
from lib.pdf.pdfshow.PdfShow import PdfShow as pdfShow
from lib.pdf.pdfanalyze.CheckObjBetik import checkObjBetik as pdfBetik
from lib.hexlib.ShowHex import show2HexBytes as s2hex
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
def menu0() -> str:
    while True:
        screenClear()
        print()
        print('\t#####################################################')
        print('\t#/*************************************************\#')
        print('\t#**||~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~||**#')
        print('\t#**||                                           ||**#')
        print('\t#**||           Pdf Inspector V2.3              ||**#')
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
        print( '\tÇıkış (Exit) <<e>>' )
        tmp=input('\tFile Name : ')
        if len(tmp.strip()) > 3:
            return tmp.strip()
        elif tmp.strip().lower() == 'e' :
            exit(0)

# Ön yükleme menüsü
def menu1(Filename:str) -> pdfFile:
    screenClear()
    pdffile = pdfFile(filename=Filename)
    pdffile.process()
    print()
    if pdffile.c1_checkNormal:
        return pdffile
    else:
        print()
        print()
        input('\tGeri (Back) <<enter>> : ')
        return pdffile

#
def menu2() -> int:
    while True:
        #
        screenClear()
        txt1_format = '\t{:<25}'
        txt2_format = '\t{:^25}'
        print('')
        print( txt2_format.format('MENU') )
        print( txt1_format.format( '-'*25 ) )
        print( txt1_format.format('1) Pdf Summary') )
        print( txt1_format.format('2) Check Pdf Tags'))
        print( txt1_format.format('3) * Show Object (Normal - use Obj Header)') )
        print( txt1_format.format('4) Show Object (Stream Summary)'))
        print(txt1_format.format( '5) Show Object (Normal)'))
        print( txt1_format.format('6) Show Object (Hex)') )
        print( txt1_format.format('7) Show Stream (Normal)') )
        print( txt1_format.format('8) Show Stream (Hex)') )
        print( txt1_format.format('9) Write Stream '))
        print( txt1_format.format('10) Show Xref (Hex)' ) )
        print( txt1_format.format('11) Show Trailer (Hex)') )
        print( txt1_format.format('12) Show StartXref (Hex)'))
        print()
        print()
        print('\tÇıkış (Exit) <<e>> , Geri (Back) <<b>>')
        selection = input('\tSeçim (Selection) : ')
        if selection.strip().lower() == 'e' :
            exit(0)
        elif selection.strip().lower() == 'b' :
            return -1
        elif selection.strip().isdigit():
            result = int(selection.strip())
            if  0 < result < 13:
                return result
#
#
def menu3( file:pdfFile ) :
    screenClear()
    file.show()
    print()
    print()
    input('\tDevam (Continue) <<enter>> : ')


def menu4( fileshow: pdfShow):
    objs_length = len(fileshow.o1_pdffile.p4_objs)
    selection = ''
    while True:
        screenClear()
        if  objs_length == 0:
            print()
            print('\t<<obj-endobj>> bulunamadı.')
            print()
            print()
            input('\tGeri (Back) <<enter>> : ')
            break
        elif objs_length == 1:
            print()
            print('\t<<obj-endobj>> 1 adet bulundu.')
            print('\t No : 0 ')
            print()
            print()
            print( '\tGeri (Back) <<b>>, Çıkıs (Exit) <<e>>' )
            selection = input('\t(Seçim) Selection No : ')
        elif objs_length > 1:
            print()
            print('\t<<obj-endobj>> {} adet bulundu.'.format(objs_length))
            print('\t No : 0 - {}'.format(objs_length-1) )
            print()
            print()
            print( '\tGeri (Back) <<b>>, Çıkıs (Exit) <<e>>' )
            selection = input('\t(Seçim) Selection No : ')
        #
        if selection.strip().lower() == 'e':
            exit(0)
        elif selection.strip().lower() == 'b':
            break
        elif selection.strip().isdigit():
            slc = int(selection.strip())
            if  -1 < slc < objs_length:
                screenClear()
                fileshow.objShow(index=slc)
                print()
                print()
                input('\tDevam (Continue) <<enter>> : ')

#
def menu5( fileshow: pdfShow):
    objs_length = len(fileshow.o1_pdffile.p4_objs)
    selection = ''
    while True:
        screenClear()
        if  objs_length == 0:
            print()
            print('\t<<obj-endobj>> bulunamadı.')
            print()
            print()
            input('\tGeri (Back) <<enter>> : ')
            break
        elif objs_length == 1:
            print()
            print('\t<<obj-endobj>> 1 adet bulundu.')
            print('\t No : 0 ')
            print()
            print()
            print( '\tGeri (Back) <<b>>, Çıkıs (Exit) <<e>>' )
            selection = input('\t(Seçim) Selection No : ')
        elif objs_length > 1:
            print()
            print('\t<<obj-endobj>> {} adet bulundu.'.format(objs_length))
            print('\t No : 0 - {}'.format(objs_length-1) )
            print()
            print()
            print( '\tGeri (Back) <<b>>, Çıkıs (Exit) <<e>>' )
            selection = input('\t(Seçim) Selection No : ')
        #
        if selection.strip().lower() == 'e':
            exit(0)
        elif selection.strip().lower() == 'b':
            break
        elif selection.strip().isdigit():
            slc = int(selection.strip())
            if  -1 < slc < objs_length:
                screenClear()
                s2hex(
                    dataBytes= fileshow.o1_pdffile.p2_pdf_bytes[fileshow.o1_pdffile.p4_objs[slc].i1_out_start:fileshow.o1_pdffile.p4_objs[slc].i1_out_end]
                  , dataName= 'Obj (index:'+str(slc)+')',
                    columnSize= 20,
                    index=fileshow.o1_pdffile.p4_objs[slc].i1_out_start
                       )
                print()
                print()
                input('\tDevam (Continue) <<enter>> : ')

def menu6( fileshow: pdfShow):
    streams_length = len(fileshow.o1_pdffile.p5_streams)
    selection = ''
    while True:
        screenClear()
        if  streams_length == 0:
            print()
            print('\t<<stream-endstream>> bulunamadı.')
            print()
            print()
            input('\tGeri (Back) <<enter>> : ')
            break
        elif streams_length == 1:
            print()
            print('\t<<stream-endstream>> 1 adet bulundu.')
            print('\t No : 0 ')
            print()
            print()
            print( '\tGeri (Back) <<b>>, Çıkıs (Exit) <<e>>' )
            selection = input('\t(Seçim) Selection No : ')
        elif streams_length > 1:
            print()
            print('\t<<stream-endstream>> {} adet bulundu.'.format(streams_length))
            print('\t No : 0 - {}'.format(streams_length-1) )
            print()
            print()
            print( '\tGeri (Back) <<b>>, Çıkıs (Exit) <<e>>' )
            selection = input('\t(Seçim) Selection No : ')
        #
        if selection.strip().lower() == 'e':
            exit(0)
        elif selection.strip().lower() == 'b':
            break
        elif selection.strip().isdigit():
            slc = int(selection.strip())
            if  -1 < slc < streams_length:
                screenClear()
                fileshow.streamShow(index=slc)
                print()
                print()
                input('\tDevam (Continue) <<enter>> : ')

def menu7( fileshow: pdfShow):
    streams_length = len(fileshow.o1_pdffile.p5_streams)
    selection = ''
    while True:
        screenClear()
        if  streams_length == 0:
            print()
            print('\t<<stream-endstream>> bulunamadı.')
            print()
            print()
            input('\tGeri (Back) <<enter>> : ')
            break
        elif streams_length == 1:
            print()
            print('\t<<stream-endstream>> 1 adet bulundu.')
            print('\t No : 0 ')
            print()
            print()
            print( '\tGeri (Back) <<b>>, Çıkıs (Exit) <<e>>' )
            selection = input('\t(Seçim) Selection No : ')
        elif streams_length > 1:
            print()
            print('\t<<stream-endstream>> {} adet bulundu.'.format(streams_length))
            print('\t No : 0 - {}'.format(streams_length-1) )
            print()
            print()
            print( '\tGeri (Back) <<b>>, Çıkıs (Exit) <<e>>' )
            selection = input('\t(Seçim) Selection No : ')
        #
        if selection.strip().lower() == 'e':
            exit(0)
        elif selection.strip().lower() == 'b':
            break
        elif selection.strip().isdigit():
            slc = int(selection.strip())
            if  -1 < slc < streams_length:
                screenClear()
                s2hex(
                    dataBytes= fileshow.o1_pdffile.p2_pdf_bytes[fileshow.o1_pdffile.p5_streams[slc].i1_out_start:fileshow.o1_pdffile.p5_streams[slc].i1_out_end]
                  , dataName= 'Stream (index:'+str(slc)+')',
                    columnSize= 20,
                    index=fileshow.o1_pdffile.p5_streams[slc].i1_out_start
                       )
                print()
                print()
                input('\tDevam (Continue) <<enter>> : ')


def menu8( fileshow: pdfShow):
    xrefs_length = len(fileshow.o1_pdffile.p6_xrefs)
    selection = ''
    while True:
        screenClear()
        if  xrefs_length == 0:
            print()
            print('\t<<xref>> bulunamadı.')
            print()
            print()
            input('\tGeri (Back) <<enter>> : ')
            break
        elif xrefs_length == 1:
            print()
            print('\t<<xref>> 1 adet bulundu.')
            print('\t No : 0 ')
            print()
            print()
            print( '\tGeri (Back) <<b>>, Çıkıs (Exit) <<e>>' )
            selection = input('\t(Seçim) Selection No : ')
        elif xrefs_length > 1:
            print()
            print('\t<<xref>> {} adet bulundu.'.format(xrefs_length))
            print('\t No : 0 - {}'.format(xrefs_length-1) )
            print()
            print()
            print( '\tGeri (Back) <<b>>, Çıkıs (Exit) <<e>>' )
            selection = input('\t(Seçim) Selection No : ')
        #
        if selection.strip().lower() == 'e':
            exit(0)
        elif selection.strip().lower() == 'b':
            break
        elif selection.strip().isdigit():
            slc = int(selection.strip())
            if  -1 < slc < xrefs_length:
                screenClear()
                fileshow.xrefShow(index=slc)
                print()
                print()
                input('\tDevam (Continue) <<enter>> : ')

def menu9( fileshow: pdfShow):
    trailers_length = len(fileshow.o1_pdffile.p7_trailers)
    selection = ''
    while True:
        screenClear()
        if  trailers_length == 0:
            print()
            print('\t<<trailer>> bulunamadı.')
            print()
            print()
            input('\tGeri (Back) <<enter>> : ')
            break
        elif trailers_length == 1:
            print()
            print('\t<<trailer>> 1 adet bulundu.')
            print('\t No : 0 ')
            print()
            print()
            print( '\tGeri (Back) <<b>>, Çıkıs (Exit) <<e>>' )
            selection = input('\t(Seçim) Selection No : ')
        elif trailers_length > 1:
            print()
            print('\t<<trailer>> {} adet bulundu.'.format(trailers_length))
            print('\t No : 0 - {}'.format(trailers_length-1) )
            print()
            print()
            print( '\tGeri (Back) <<b>>, Çıkıs (Exit) <<e>>' )
            selection = input('\t(Seçim) Selection No : ')
        #
        if selection.strip().lower() == 'e':
            exit(0)
        elif selection.strip().lower() == 'b':
            break
        elif selection.strip().isdigit():
            slc = int(selection.strip())
            if  -1 < slc < trailers_length:
                screenClear()
                fileshow.trailerShow(index=slc)
                print()
                print()
                input('\tDevam (Continue) <<enter>> : ')

def menu10( fileshow: pdfShow):
    startxref_length = len(fileshow.o1_pdffile.p8_startxrefs)
    selection = ''
    while True:
        screenClear()
        if  startxref_length == 0:
            print()
            print('\t<<startxref>> bulunamadı.')
            print()
            print()
            input('\tGeri (Back) <<enter>> : ')
            break
        elif startxref_length == 1:
            print()
            print('\t<<startxref>> 1 adet bulundu.')
            print('\t No : 0 ')
            print()
            print()
            print( '\tGeri (Back) <<b>>, Çıkıs (Exit) <<e>>' )
            selection = input('\t(Seçim) Selection No : ')
        elif startxref_length > 1:
            print()
            print('\t<<startxref>> {} adet bulundu.'.format(startxref_length))
            print('\t No : 0 - {}'.format(startxref_length-1) )
            print()
            print()
            print( '\tGeri (Back) <<b>>, Çıkıs (Exit) <<e>>' )
            selection = input('\t(Seçim) Selection No : ')
        #
        if selection.strip().lower() == 'e':
            exit(0)
        elif selection.strip().lower() == 'b':
            break
        elif selection.strip().isdigit():
            slc = int(selection.strip())
            if  -1 < slc < startxref_length:
                screenClear()
                fileshow.startXrefShow(index=slc)
                print()
                print()
                input('\tDevam (Continue) <<enter>> : ')
#
def menu11(betik:pdfBetik, fileshow:pdfShow):
    screenClear()
    print()
    print('\tPdf Analiz Ediliyor!...')
    betik.findPdfBetik()
    betik.findObjBetik()
    turn = True
    while turn:
        screenClear()
        print()
        betik.show()
        print()
        print()
        print('\tGeri (Back) <<b>>, Çıkıs (Exit) <<e>>')
        selection = input('\t(Seçim) Selection No : ')
        if selection.strip().lower() == 'e':
            exit(0)
        elif selection.strip().lower() == 'b':
            turn = False
            break
        elif selection.strip().isdigit():
            slc = int(selection.strip())
            if 0 < slc < 54:
                index_list = betik.selection(index=slc)
                if len(index_list) > 0:
                    for ii in index_list:
                        screenClear()
                        print()
                        fileshow.objShow(index=ii)
                        print()
                        print()
                        print('\tGeri (Back) <<b>>, Çıkıs (Exit) <<e>>')
                        selection2 = input('\tDevam (Continue) <<enter>> : ')
                        if selection2.strip().lower() == 'e':
                            exit(0)
                        elif selection2.strip().lower() == 'b':
                            turn = True
                            break
                else:
                    screenClear()
                    print()
                    print('\tTag bulunamadı. (Tag not found)')
                    print()
                    print()
                    input('\tDevam (Continue) <<enter>> : ')
#
def menu12( pdffile : pdfFile , fileshow : pdfShow):
    objs_length = len(fileshow.o1_pdffile.p4_objs)
    selection = ''
    while True:
        screenClear()
        if  objs_length == 0:
            print()
            print('\t<<obj-endobj>> bulunamadı.')
            print()
            print()
            input('\tGeri (Back) <<enter>> : ')
            break
        elif objs_length > 0:
            print()
            print('\t<<obj-endobj>> {} adet bulundu.'.format(objs_length))
            print()
            print()
            print( '\tGeri (Back) <<b>>, Çıkıs (Exit) <<e>>' )
            selection = input('\tObj Header (First No) : ')
        #
        if selection.strip().lower() == 'e':
            exit(0)
        elif selection.strip().lower() == 'b':
            break
        elif selection.strip().isdigit():
            slc = int(selection.strip())
            screenClear()
            tmp_obj = pdffile.objFirstNo( index=slc )
            if tmp_obj.i0_no != -1 and tmp_obj.i0_check:
                fileshow.objShow(index=tmp_obj.i0_no)
                print()
                print()
                input('\tDevam (Continue) <<enter>> : ')
#
#
def  menu13( fileshow:pdfShow ):
    from lib.hexlib.WriteFile import WriteFile as writefile
    #
    stream_len = len( fileshow.o1_pdffile.p5_streams )
    #
    while True:
        screenClear()
        if stream_len == 0:
            print()
            print('\tYazılacak stream dosyası yok.')
            print()
            print()
            input('\tDevam (Continue) <<enter>> : ')
            return
        elif stream_len == 1:
            print()
            print('\t<<stream-endstream>> 1 adet bulundu.')
            print('\tNo: 0')
        elif stream_len > 1:
            print()
            print('\t<<stream-endstream>> {} adet bulundu.'.format(stream_len))
            print('\tNo: 0 - {}'.format(stream_len-1))
        print()
        print()
        print('\tGeri (Back) <<b>>, Çıkıs (Exit) <<e>>')
        selection = input('\t(Seçim) Selection No : ')
        if selection.strip().lower() == 'b':
            break
        elif selection.strip().lower() == 'e':
            exit(0)
        elif selection.strip().isdigit():
            slc = int(selection.strip())
            if -1 < slc < stream_len:
                res = fileshow.detect_stream(index=slc)
                if res['result']:
                    screenClear()
                    print()
                    print()
                    print("\tDafult file name '{}' <<enter>> ".format( ('stream_'+str(slc)) ))
                    select_name = input('\tNew File Name : ')
                    if select_name.strip() == '':
                        file_name = 'stream_'+str(slc)
                    else:
                        file_name = select_name.strip()
                    try:
                        wf = writefile(filename=file_name)
                        wf.writeByte(data=res['bytes'])
                        screenClear()
                        print()
                        print()
                        print("\t'{}' yazıldı. ('{}' was written)".format(file_name,file_name) )
                        print()
                        print()
                        input('\tDevam (Continue) <<enter>> : ')
                    except:
                        screenClear()
                        print()
                        print()
                        print('\tDosya yazılırken hata oluştu.')
                        print('\t(Dosya adını ya da yazma izinlerini kontrol ediniz!)')
                        print()
                        print()
                        input('\tDevam (Continue) <<enter>> : ')
            else:
                screenClear()
                print()
                print()
                print('\tStream datası tanımlanamadı.')
                print()
                print()
                input('\tDevam (Continue) <<enter>> : ')
#
#
def menu14( fileshow: pdfShow):
    objs_length = len(fileshow.o1_pdffile.p4_objs)
    selection = ''
    while True:
        screenClear()
        if  objs_length == 0:
            print()
            print('\t<<obj-endobj>> bulunamadı.')
            print()
            print()
            input('\tGeri (Back) <<enter>> : ')
            break
        elif objs_length == 1:
            print()
            print('\t<<obj-endobj>> 1 adet bulundu.')
            print('\t No : 0 ')
            print()
            print()
            print( '\tGeri (Back) <<b>>, Çıkıs (Exit) <<e>>' )
            selection = input('\t(Seçim) Selection No : ')
        elif objs_length > 1:
            print()
            print('\t<<obj-endobj>> {} adet bulundu.'.format(objs_length))
            print('\t No : 0 - {}'.format(objs_length-1) )
            print()
            print()
            print( '\tGeri (Back) <<b>>, Çıkıs (Exit) <<e>>' )
            selection = input('\t(Seçim) Selection No : ')
        #
        if selection.strip().lower() == 'e':
            exit(0)
        elif selection.strip().lower() == 'b':
            break
        elif selection.strip().isdigit():
            slc = int(selection.strip())
            if  -1 < slc < objs_length:
                screenClear()
                fileshow.objSummaryShow(index=slc)
                print()
                print()
                input('\tDevam (Continue) <<enter>> : ')

#
def main():
    while True:
        filename = menu0()
        filepdf  = menu1(Filename=filename)
        fileshow = pdfShow(pdffile=filepdf)
        if filepdf.c1_checkNormal:
            while True:
                selection = menu2()
                if selection != -1:
                    if selection == 1:
                        menu3(file=filepdf)
                    elif selection == 2:
                        betikpdf = pdfBetik(pdffile=filepdf)
                        menu11(betik=betikpdf, fileshow=fileshow)
                    elif selection == 3:
                        menu12(pdffile=filepdf ,fileshow=fileshow)
                    elif selection == 4:
                        menu14(fileshow=fileshow)
                    elif selection == 5:
                        menu4(fileshow=fileshow)
                    elif selection == 6:
                        menu5(fileshow=fileshow)
                    elif selection == 7:
                        menu6(fileshow=fileshow)
                    elif selection == 8:
                        menu7(fileshow=fileshow)
                    elif selection == 9:
                        menu13(fileshow=fileshow)
                    elif selection == 10:
                        menu8(fileshow=fileshow)
                    elif selection == 11:
                        menu9(fileshow=fileshow)
                    elif selection == 12:
                        menu10(fileshow=fileshow)
                else:
                    break
#

# Main Program Start
main()

