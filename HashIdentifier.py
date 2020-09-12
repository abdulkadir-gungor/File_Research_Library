#!/usr/bin/python3
############################################################################
#
#   Hash Identifier [ Main Program ]
#   © 2020 ABDULKADİR GÜNGÖR All Rights Reserved
#   Contact email address: abdulkadir_gungor@outlook.com
#
#	Developper:	Abdulkadir GÜNGÖR (abdulkadir_gungor@outlook.com)
#	Date:	09/2020
#	All Rights Reserved (Tüm Hakları Saklıdır)
#
############################################################################
import os
from lib.cryptography.hash.Hash import detectHash
from lib.hexlib.ReadBinaryFile import readBytes as rbytes

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
        print('\t#**||          Hash Identifier V1.1             ||**#')
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
        print('\t1) Copy the hash from file')
        print('\t2) Input the hash (String)')
        print('\t3) Input the hash (Hex)')
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

def menu1(slc:int):
    while True:
        if 0< slc <4:
            if slc == 1:
                while True:
                    screenClear()
                    print()
                    print('\tDosya utf-8 göre kodlanmalıdır.')
                    print('\tFile must be encoded according to utf-8')
                    print()
                    tmp_file = input('\tFile name : ').strip()
                    if tmp_file != '':
                        try:
                            file_bytes = rbytes(filename=tmp_file)
                            file_str = file_bytes.decode(encoding='utf-8', errors='strict')
                            result_list = detectHash( hashStr=file_str.strip() )
                            showresult(result_list, hash=file_str.strip() )
                        except:
                            print('\tHata meydana geldi.(Error has occured)')
                    print()
                    print()
                    print('\tÇıkış (Exit) <<e>>, Geri (Back) <<b>>')
                    tmp = input('\tDevam (Enter) : ').strip()
                    if tmp.lower() == 'e':
                        exit(0)
                    if tmp.lower() == 'b':
                        slc = -1
                        break
            if slc == 2:
                while True:
                    screenClear()
                    print()
                    hash_str = input('\tHash : ').strip()
                    if hash_str != '':
                        result_list = detectHash(hashStr=hash_str)
                        showresult(result_list, hash=hash_str)
                    print()
                    print()
                    print('\tÇıkış (Exit) <<e>>, Geri (Back) <<b>>')
                    tmp = input('\tDevam (Enter) : ').strip()
                    if tmp.lower() == 'e':
                        exit(0)
                    if tmp.lower() == 'b':
                        slc = -1
                        break
            if slc == 3:
                while True:
                    screenClear()
                    print()
                    print('\tKarakter dönüşümü utf-8 göre yapılacaktır.')
                    print('\tCharacter conversion is going to be done according to utf-8.')
                    print()
                    print('\tHash (Hex) : 33 64 30 38   ...(Example)')
                    hash_str_hex = input('\tHash (Hex) : ').strip()
                    try:
                        hash_str = ((bytes.fromhex( hash_str_hex )).decode(encoding='utf-8', errors='strict')).strip()
                        result_list = detectHash(hashStr=hash_str)
                        showresult(result_list, hash=hash_str)
                    except:
                        print('\tHata meydana geldi.(Error has occured)')
                    print()
                    print()
                    print('\tÇıkış (Exit) <<e>>, Geri (Back) <<b>>')
                    tmp = input('\tDevam (Enter) : ').strip()
                    if tmp.lower() == 'e':
                        exit(0)
                    if tmp.lower() == 'b':
                        slc = -1
                        break
        else:
            break

def showresult(res:list, hash:str):
    if res != None:
        result_total = len(res)
        screenClear()
        print()
        print( '\tHash (Str)  : "{}"'.format(hash) )
        print( '\tHash Length : {}'.format(len(hash)) )
        print( '\tIsDigit     : {:<5} \t IsAlpha : {:<5} \t IsAlphaNumeric : {:<5}'.format( str(hash.isdigit()) , str(hash.isalpha()) , str(hash.isalnum())  )  )
        print( '\tIsLower     : {:<5} \t IsUpper : {:<5} \t IsPrintable    : {:<5}'.format(str(hash.islower()), str(hash.isupper()), str(hash.isprintable())  ) )
        print()
        if result_total == 0:
            print('\tBulunamadı! (Not found!)')
        elif result_total == 1:
            print('\tMuhtemel Sonuç (Possible Hash)')
            print('\t[+] '+res[0].name )
        elif result_total == 2:
            print('\tMuhtemel Sonuçlar (Possible Hashes)')
            print('\t[+] '+res[0].name )
            print('\t[+] '+res[1].name )
        elif result_total > 2:
            print('\tMuhtemel Sonuçlar (Possible Hashes)')
            print('\t[+] '+res[0].name )
            print('\t[+] '+res[1].name )
            print()
            print('\tDiğer Muhtemel Sonuçlar (Other Possible Hashes)')
            for jj in range(2,result_total):
                print('\t[+] ' + res[jj].name)

###
###
###### Ana Fonksiyon (Main Function)
def main():
    while True:
        menu1( menu0() )
######
###
###

# Program Start
main()