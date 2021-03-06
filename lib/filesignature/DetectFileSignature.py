#!/usr/bin/python3
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
class FileSignature:
    #
    def __init__(self):
        self.f1_signature = b''
        self.f2_extension = ''
        self.f3_description = ''
#
#
#
def detect_File_Signature( bytesData:bytes ) -> list:
    #
    #
    sig_list = []
    #
    #

    #
    if bytesData[0:4] == b'\x41\x43\x53\x44':
        filesig = FileSignature()
        filesig.f1_signature = b'\x41\x43\x53\x44'
        filesig.f2_extension = '*'
        filesig.f3_description = 'AOL Parameter (Info Files)'
        sig_list.append(filesig)
    #
    if bytesData[0:6] == b'\x62\x70\x6c\x69\x73\x74':
        filesig = FileSignature()
        filesig.f1_signature = b'\x62\x70\x6c\x69\x73\x74'
        filesig.f2_extension = '*'
        filesig.f3_description = 'Binary Property List (plist)'
        sig_list.append(filesig)
    #
    if bytesData[0:6] == b'\x00\x14\x00\x00\x01\x02':
        filesig = FileSignature()
        filesig.f1_signature= b'\x62\x70\x6c\x69\x73\x74'
        filesig.f2_extension = '*'
        filesig.f3_description= 'BIOS Details in RAM'
        sig_list.append(filesig)
    #
    if bytesData[0:5] == b'\x30\x37\x30\x37\x30':
        filesig = FileSignature()
        filesig.f1_signature =  b'\x30\x37\x30\x37\x30'
        filesig.f2_extension = '*'
        filesig.f3_description = 'Cpio Archive'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x7f\x45\x4c\x46':
        filesig = FileSignature()
        filesig.f1_signature =  b'\x7f\x45\x4c\x46'
        filesig.f2_extension = '*'
        filesig.f3_description = 'ELF Executable'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\xa1\xb2\xcd\x34':
        filesig = FileSignature()
        filesig.f1_signature= b'\xa1\xb2\xcd\x34'
        filesig.f2_extension = '*'
        filesig.f3_description = 'Extended tcpdump (libpcap) Capture File'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x04\x00\x00\x00':
        filesig = FileSignature()
        filesig.f1_signature = b'\x04\x00\x00\x00'
        filesig.f2_extension = '*'
        filesig.f3_description = 'INFO2 Windows Recycle bin_1'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x05\x00\x00\x00':
        filesig = FileSignature()
        filesig.f1_signature = b'\x05\x00\x00\x00'
        filesig.f2_extension = '*'
        filesig.f3_description = 'INFO2 Windows Recycle bin_2'
        sig_list.append(filesig)
    #
    if bytesData[0:2] == b'\xac\xed':
        filesig = FileSignature()
        filesig.f1_signature =  b'\xac\xed'
        filesig.f2_extension = '*'
        filesig.f3_description = 'Java Serialization Data'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\x4b\x57\x41\x4a\x88\xf0\x27\xd1':
        filesig = FileSignature()
        filesig.f1_signature = b'\x4b\x57\x41\x4a\x88\xf0\x27\xd1'
        filesig.f2_extension = '*'
        filesig.f3_description = 'KWAJ (Compressed) File'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\xcd\x20\xaa\xaa\x02\x00\x00\x00':
        filesig = FileSignature()
        filesig.f1_signature= b'\xcd\x20\xaa\xaa\x02\x00\x00\x00'
        filesig.f2_extension = '*'
        filesig.f3_description = 'NAV Quarantined Virus File'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\x53\x5a\x20\x88\xf0\x27\x33\xd1':
        filesig = FileSignature()
        filesig.f1_signature = b'\x53\x5a\x20\x88\xf0\x27\x33\xd1'
        filesig.f2_extension = '*'
        filesig.f3_description = 'QBASIC SZDD File'
        sig_list.append(filesig)
    #
    if bytesData[0:2] == b'\x6f\x3c':
        filesig = FileSignature()
        filesig.f1_signature = b'\x6f\x3c'
        filesig.f2_extension = '*'
        filesig.f3_description = 'SMS Text (SIM)'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\x53\x5a\x44\x44\x88\xf0\x27\x33':
        filesig = FileSignature()
        filesig.f1_signature = b'\x53\x5a\x44\x44\x88\xf0\x27\x33'
        filesig.f2_extension = '*'
        filesig.f3_description = 'SZDD File Format'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\xa1\xb2\xc3\xd4':
        filesig = FileSignature()
        filesig.f1_signature = b'\xa1\xb2\xc3\xd4'
        filesig.f2_extension = '*'
        filesig.f3_description = 'tcpdump (libpcap) Capture File'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x34\xcd\xb2\xa1' :
        filesig = FileSignature()
        filesig.f1_signature =  b'\x34\xcd\xb2\xa1'
        filesig.f2_extension = '*'
        filesig.f3_description = 'Tcpdump Capture File'
        sig_list.append(filesig)
    #
    if bytesData[0:3] == b'\xef\xbb\xbf' :
        filesig = FileSignature()
        filesig.f1_signature = b'\xef\xbb\xbf'
        filesig.f2_extension = '*'
        filesig.f3_description = 'UTF8 File'
        sig_list.append(filesig)
    #
    if bytesData[0:2] == b'\xfe\xff' :
        filesig = FileSignature()
        filesig.f1_signature = b'\xfe\xff'
        filesig.f2_extension = '*'
        filesig.f3_description = 'UTF-16 (UCS-2 File)'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\xff\xfe\x00\x00' :
        filesig = FileSignature()
        filesig.f1_signature = b'\xff\xfe\x00\x00'
        filesig.f2_extension = '*'
        filesig.f3_description = 'UTF-32 (UCS-4 File)'
        sig_list.append(filesig)
    #
    if bytesData[0:5] == b'\x62\x65\x67\x69\x6e' :
        filesig = FileSignature()
        filesig.f1_signature =  b'\x62\x65\x67\x69\x6e'
        filesig.f2_extension= '*'
        filesig.f3_description = 'UUencoded File'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\xd4\xc3\xb2\xa1' :
        filesig = FileSignature()
        filesig.f1_signature = b'\xd4\xc3\xb2\xa1'
        filesig.f2_extension = '*'
        filesig.f3_description = 'WinDump (winpcap) Capture File'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\x37\xe4\x53\x96\xc9\xdb\xd6\x07' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x37\xe4\x53\x96\xc9\xdb\xd6\x07'
        filesig.f2_extension = '*'
        filesig.f3_description = 'Zisofs Compressed File'
        sig_list.append(filesig)
    #
    if bytesData[0:7] == b'\x00\x00\x1a\x00\x05\x10\x04' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x00\x00\x1a\x00\x05\x10\x04'
        filesig.f2_extension = '123'
        filesig.f3_description = 'Lotus 1-2-3 (v9)'
        sig_list.append(filesig)
    #
    if bytesData[0:2] == b'\x4d\x5a':
        filesig = FileSignature()
        filesig.f1_signature = b'\x4d\x5a'
        filesig.f2_extension = '386'
        filesig.f3_description = 'Windows Virtual Device Drivers'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\x00\x00\x00\x14\x66\x74\x79\x70' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x00\x00\x00\x14\x66\x74\x79\x70'
        filesig.f2_extension = '3GP'
        filesig.f3_description = '3GPP Multimedia Files'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\x00\x00\x00\x20\x66\x74\x79\x70' :
        filesig = FileSignature()
        filesig.f1_signature =  b'\x00\x00\x00\x20\x66\x74\x79\x70'
        filesig.f2_extension = '3GP'
        filesig.f3_description  = '3GPP2 Multimedia Files'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\x00\x00\x00\x18\x66\x74\x79\x70':
        filesig = FileSignature()
        filesig.f1_signature = b'\x00\x00\x00\x18\x66\x74\x79\x70'
        filesig.f2_extension = '3GP5'
        filesig.f3_description = 'MPEG-4 Video Files'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x52\x49\x46\x46':
        filesig = FileSignature()
        filesig.f1_signature =  b'\x52\x49\x46\x46'
        filesig.f2_extension = '4XM'
        filesig.f3_description = '4X Movie Video'
        sig_list.append(filesig)
    #
    if bytesData[0:6] == b'\x37\x7a\xbc\xaf\x27\x1c' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x37\x7a\xbc\xaf\x27\x1c'
        filesig.f2_extension = '7Z'
        filesig.f3_description = '7-Zip Compressed File'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x00\x01\x42\x41' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x00\x01\x42\x41'
        filesig.f2_extension = 'ABA'
        filesig.f3_description = 'Palm Address Book Archive'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\x51\x57\x20\x56\x65\x72\x2e\x20' :
        filesig = FileSignature()
        filesig.f1_signature =  b'\x51\x57\x20\x56\x65\x72\x2e\x20'
        filesig.f2_extension = 'ABD'
        filesig.f3_description = 'ABD (QSD Quicken Data File)'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\x41\x4f\x4c\x49\x4e\x44\x45\x58' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x41\x4f\x4c\x49\x4e\x44\x45\x58'
        filesig.f2_extension = 'ABI'
        filesig.f3_description = 'AOL Address Book Index'
        sig_list.append(filesig)
    #
    if bytesData[0:3] == b'\x41\x4f\x4c' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x41\x4f\x4c'
        filesig.f2_extension = 'ABI/ABY'
        filesig.f3_description = 'AOL Config Files'
        sig_list.append(filesig)
    #
    if bytesData[0:5] == b'\x41\x4f\x4c\x44\x42' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x41\x4f\x4c\x44\x42'
        filesig.f2_extension = 'ABY'
        filesig.f3_description = 'AOL Address Book'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x72\x69\x66\x66' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x72\x69\x66\x66'
        filesig.f2_extension= 'AC'
        filesig.f3_description = 'Sonic Foundry Acid Music File'
        sig_list.append(filesig)
    #
    if bytesData[0:19] == b'\x00\x01\x00\x00\x53\x74\x61\x6e\x64\x61\x72\x64\x20\x41\x43\x45\x20\x44\x42' :
        filesig = FileSignature()
        filesig.f1_signature =  b'\x00\x01\x00\x00\x53\x74\x61\x6e\x64\x61\x72\x64\x20\x41\x43\x45\x20\x44\x42'
        filesig.f2_extension = 'ACCDB'
        filesig.f3_description = 'Microsoft Access 2007'
        sig_list.append(filesig)
    #
    if bytesData[0:2] == b'\x4d\x5a':
        filesig = FileSignature()
        filesig.f1_signature =  b'\x4d\x5a'
        filesig.f2_extension = 'ACM'
        filesig.f3_description = 'MS Audio Compression Manager Driver'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\xc3\xab\xcd\xab' :
        filesig = FileSignature()
        filesig.f1_signature = b'\xc3\xab\xcd\xab'
        filesig.f2_extension = 'ACS'
        filesig.f3_description = 'MS Agent Character File'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1' :
        filesig = FileSignature()
        filesig.f1_signature =  b'\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1'
        filesig.f2_extension = 'AC'
        filesig.f3_description = 'CaseWare Working Papers'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\x52\x45\x56\x4e\x55\x4d\x3a\x2c' :
        filesig = FileSignature()
        filesig.f1_signature  = b'\x52\x45\x56\x4e\x55\x4d\x3a\x2c'
        filesig.f2_extension = 'AD'
        filesig.f3_description = 'Antenna Data File'
        sig_list.append(filesig)
    #
    if bytesData[0:3] == b'\x44\x4f\x53' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x44\x4f\x53'
        filesig.f2_extension = 'ADF'
        filesig.f3_description = 'Amiga Disk File'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1' :
        filesig = FileSignature()
        filesig.f1_signature = b'\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1'
        filesig.f2_extension = 'ADP'
        filesig.f3_description = 'Access Project File'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\x03\x00\x00\x00\x41\x50\x50\x52' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x03\x00\x00\x00\x41\x50\x50\x52'
        filesig.f2_extension = 'ADX'
        filesig.f3_description = 'Approach Index File'
        sig_list.append(filesig)
    #
    if bytesData[0:7] == b'\x80\x00\x00\x20\x03\x12\x04' :
        filesig = FileSignature()
        filesig.f1_signature =  b'\x80\x00\x00\x20\x03\x12\x04'
        filesig.f2_extension = 'ADX'
        filesig.f3_description = 'Dreamcast Audio'
        sig_list.append(filesig)
    #
    if bytesData[0:5] == b'\x46\x4f\x52\x4d\x00' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x46\x4f\x52\x4d\x00'
        filesig.f2_extension = 'AIFF'
        filesig.f3_description = 'Audio Interchange File'
        sig_list.append(filesig)
    #
    if bytesData[0:2] == b'\x21\x12' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x21\x12'
        filesig.f2_extension = 'AIN'
        filesig.f3_description = 'AIN Compressed Archive'
        sig_list.append(filesig)
    #
    if bytesData[0:5]  == b'\x23\x21\x41\x4d\x52' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x23\x21\x41\x4d\x52'
        filesig.f2_extension = 'AMR'
        filesig.f3_description = "Adaptive Multi-Rate ACELP Codec (GSM)"
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x52\x49\x46\x46' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x52\x49\x46\x46'
        filesig.f2_extension = 'ANI'
        filesig.f3_description = 'Windows Animated Cursor'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\x4d\x5a\x90\x00\x03\x00\x00\x00' :
        filesig = FileSignature()
        filesig.f1_signature =  b'\x4d\x5a\x90\x00\x03\x00\x00\x00'
        filesig.f2_extension = 'API'
        filesig.f3_description  = 'Acrobat Plug-In'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1' :
        filesig = FileSignature()
        filesig.f1_signature = b'\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1'
        filesig.f2_extension = 'APR'
        filesig.f3_description = 'Lotus (IBM Approach 97 File)'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x41\x72\x43\x01' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x41\x72\x43\x01'
        filesig.f2_extension = 'ARC'
        filesig.f3_description = 'FreeArc Compressed File'
        sig_list.append(filesig)
    #
    if bytesData[0:2] == b'\x1a\x02' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x1a\x02'
        filesig.f2_extension = 'ARC'
        filesig.f3_description = 'LH Archive (Old Vers.|Type 1)'
        sig_list.append(filesig)
    #
    if bytesData[0:2] == b'\x1a\x03' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x1a\x03'
        filesig.f2_extension = 'ARC'
        filesig.f3_description = 'LH Archive (Old Vers.|Type 2)'
        sig_list.append(filesig)
    #
    if bytesData[0:2] == b'\x1a\x04' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x1a\x04'
        filesig.f2_extension = 'ARC'
        filesig.f3_description = 'LH Archive (Old Vers.|Type 3)'
        sig_list.append(filesig)
    #
    if bytesData[0:2] == b'\x1a\x08' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x1a\x08'
        filesig.f2_extension = 'ARC'
        filesig.f3_description = 'LH Archive (Old Vers.|Type 4)'
        sig_list.append(filesig)
    #
    if bytesData[0:2] == b'\x1a\x09' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x1a\x09'
        filesig.f2_extension = 'ARC'
        filesig.f3_description = 'LH Archive (Old Vers.|Type 5)'
        sig_list.append(filesig)
    #
    if bytesData[0:2] == b'\x60\xea' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x60\xea'
        filesig.f2_extension = 'ARJ'
        filesig.f3_description = 'ARJ Compressed Archive File'
        sig_list.append(filesig)
    #
    if bytesData[0:2] == b'\xd4\x2a' :
        filesig = FileSignature()
        filesig.f1_signature = b'\xd4\x2a'
        filesig.f2_extension = 'ARL'
        filesig.f3_description = 'AOL History (Typed URL Files)'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\x30\x26\xb2\x75\x8e\x66\xcf\x11' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x30\x26\xb2\x75\x8e\x66\xcf\x11'
        filesig.f2_extension = 'ASF'
        filesig.f3_description = 'Windows Media Audio/Video File'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x53\x43\x48\x6c' :
        filesig = FileSignature()
        filesig.f1_signature =  b'\x53\x43\x48\x6c'
        filesig.f2_extension= 'AST'
        filesig.f3_description = 'Underground Audio'
        sig_list.append(filesig)
    #
    if bytesData[0:1] == b'\x3c':
        filesig = FileSignature()
        filesig.f1_signature = b'\x3c'
        filesig.f2_extension = 'ASX'
        filesig.f3_description = 'Advanced Stream Redirector'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x64\x6e\x73\x2e' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x64\x6e\x73\x2e'
        filesig.f2_extension = 'AU'
        filesig.f3_description = 'Audacity Audio File'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x2e\x73\x6e\x64':
        filesig = FileSignature()
        filesig.f1_signature = b'\x2e\x73\x6e\x64'
        filesig.f2_extension = 'AU'
        filesig.f3_description = 'NeXT/Sun Microsystems Audio File'
        sig_list.append(filesig)
    #
    if bytesData[0:2] == b'\xd4\x2a':
        filesig = FileSignature()
        filesig.f1_signature = b'\xd4\x2a'
        filesig.f2_extension = 'AUT'
        filesig.f3_description = 'AOL History (Typed URL Files)'
        sig_list.append(filesig)
    #
    elif bytesData[0:4] == b'\x52\x49\x46\x46' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x52\x49\x46\x46'
        filesig.f2_extension = 'AVI'
        filesig.f3_description = 'Resource Interchange File Format'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\x8a\x01\x09\x00\x00\x00\xe1\x08' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x8a\x01\x09\x00\x00\x00\xe1\x08'
        filesig.f2_extension = 'AW'
        filesig.f3_description = 'MS Answer Wizard'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\x4d\x5a\x90\x00\x03\x00\x00\x00' :
        filesig = FileSignature()
        filesig.f1_signature  = b'\x4d\x5a\x90\x00\x03\x00\x00\x00'
        filesig.f2_extension = 'AX'
        filesig.f3_description = 'DirectShow Filter'
        sig_list.append(filesig)
    #
    if bytesData[0:2] == b'\x4d\x5a' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x4d\x5a'
        filesig.f2_extension = 'AX'
        filesig.f3_description = 'Library Cache File'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\x41\x4f\x4c\x20\x46\x65\x65\x64' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x41\x4f\x4c\x20\x46\x65\x65\x64'
        filesig.f2_extension = 'BAG'
        filesig.f3_description = 'AOL and AIM Buddy List'
        sig_list.append(filesig)
    #
    if bytesData[0:3] == b'\x41\x4f\x4c' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x41\x4f\x4c'
        filesig.f2_extension = 'BAG'
        filesig.f3_description = 'AOL Config Files'
        sig_list.append(filesig)
    #
    if bytesData[0:2] == b'\x58\x54' :
        filesig = FileSignature()
        filesig.f1_signature =  b'\x58\x54'
        filesig.f2_extension = 'BDR'
        filesig.f3_description = 'MS Publisher'
        sig_list.append(filesig)
    #
    if bytesData[0:7] == b'\x42\x4c\x49\x32\x32\x33\x51' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x42\x4c\x49\x32\x32\x33\x51'
        filesig.f2_extension = 'BIN'
        filesig.f3_description = 'Speedtouch Router Firmware'
        sig_list.append(filesig)
    #
    if bytesData[0:2] == b'\x42\x4d' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x42\x4d'
        filesig.f2_extension = 'BMP'
        filesig.f3_description = 'Bitmap Image'
        sig_list.append(filesig)
    #
    if bytesData[0:3] == b'\x42\x5a\x68' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x42\x5a\x68'
        filesig.f2_extension = 'BZ2'
        filesig.f3_description  = 'Bzip2 Compressed Archive'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x49\x53\x63\x28' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x49\x53\x63\x28'
        filesig.f2_extension = 'CAB'
        filesig.f3_description = 'Install Shield Compressed File'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x4d\x53\x43\x46' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x4d\x53\x43\x46'
        filesig.f2_extension = 'CAB'
        filesig.f3_description = 'Microsoft Cabinet File'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\x73\x72\x63\x64\x6f\x63\x69\x64' :
        filesig = FileSignature()
        filesig.f1_signature =  b'\x73\x72\x63\x64\x6f\x63\x69\x64'
        filesig.f2_extension = 'CAL'
        filesig.f3_description = 'CALS Raster Bitmap'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\x53\x75\x70\x65\x72\x43\x61\x6c' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x53\x75\x70\x65\x72\x43\x61\x6c'
        filesig.f2_extension = 'CAL'
        filesig.f3_description = 'SuperCalc Worksheet'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\xb5\xa2\xb0\xb3\xb3\xb0\xa5\xb5' :
        filesig = FileSignature()
        filesig.f1_signature = b'\xb5\xa2\xb0\xb3\xb3\xb0\xa5\xb5'
        filesig.f2_extension = 'CAL'
        filesig.f3_description = 'Windows Calendar'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x58\x43\x50\x00' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x58\x43\x50\x00'
        filesig.f2_extension = 'CAP'
        filesig.f3_description = 'Packet Sniffer Files'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x52\x54\x53\x53' :
        filesig = FileSignature()
        filesig.f1_signature =  b'\x52\x54\x53\x53'
        filesig.f2_extension = 'CAP'
        filesig.f3_description = 'WinNT Netmon Capture File'
        sig_list.append(filesig)
    #
    if bytesData[0:6] == b'\x5f\x43\x41\x53\x45\x5f' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x5f\x43\x41\x53\x45\x5f'
        filesig.f2_extension = 'CAS/CBK'
        filesig.f3_description = 'EnCase Case File'
        sig_list.append(filesig)
    #
    if bytesData[0:1] == b'\x30' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x30'
        filesig.f2_extension = 'CAT'
        filesig.f3_description ='MS Security Catalog File'
        sig_list.append(filesig)
    #
    if bytesData[0:6] == b'\x43\x42\x46\x49\x4c\x45' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x43\x42\x46\x49\x4c\x45'
        filesig.f2_extension = 'CBD'
        filesig.f3_description = 'WordPerfect Dictionary'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x52\x49\x46\x46' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x52\x49\x46\x46'
        filesig.f2_extension = 'CDA/CDR'
        filesig.f3_description = 'Resource Interchange File Format/CorelDraw Document'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\x45\x45\x49\x54\x45\x20\x43\x6f' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x45\x45\x49\x54\x45\x20\x43\x6f'
        filesig.f2_extension = 'CDR'
        filesig.f3_description = 'Elite Plus Commander Game File'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\x4d\x53\x5f\x56\x4f\x49\x43\x45' :
        filesig = FileSignature()
        filesig.f1_signature =  b'\x4d\x53\x5f\x56\x4f\x49\x43\x45'
        filesig.f2_extension = 'CDR'
        filesig.f3_description = 'Sony Compressed Voice File'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\x5b\x66\x6c\x74\x73\x69\x6d\x2e' :
        filesig = FileSignature()
        filesig.f1_signature =  b'\x5b\x66\x6c\x74\x73\x69\x6d\x2e'
        filesig.f2_extension = 'CFG'
        filesig.f3_description = 'Flight Simulator Aircraft Configuration'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x49\x54\x53\x46' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x49\x54\x53\x46'
        filesig.f2_extension = 'CHI/CHM'
        filesig.f3_description = 'MS Compiled HTML Help File'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\xca\xfe\xba\xbe' :
        filesig = FileSignature()
        filesig.f1_signature = b'\xca\xfe\xba\xbe'
        filesig.f2_extension = 'CLASS'
        filesig.f3_description = 'Java Bytecode'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x43\x4f\x4d\x2b' :
        filesig = FileSignature()
        filesig.f1_signature =  b'\x43\x4f\x4d\x2b'
        filesig.f2_extension = 'CLB'
        filesig.f3_description = 'COM+ Catalog'
        sig_list.append(filesig)
    #
    elif bytesData[0:4] == b'\x43\x4d\x58\x31' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x43\x4d\x58\x31'
        filesig.f2_extension = 'CLB'
        filesig.f3_description = 'Corel Binary Metafile'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x52\x49\x46\x46' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x52\x49\x46\x46'
        filesig.f2_extension = 'CMX'
        filesig.f3_description = 'Corel Presentation Exchange Metadata'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\x53\x51\x4c\x4f\x43\x4f\x4e\x56' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x53\x51\x4c\x4f\x43\x4f\x4e\x56'
        filesig.f2_extension = 'CNV'
        filesig.f3_description = 'DB2 Conversion File'
        sig_list.append(filesig)
    #
    if bytesData[0:6] == b'\x4e\x61\x6d\x65\x3a\x20' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x4e\x61\x6d\x65\x3a\x20'
        filesig.f2_extension = 'COD'
        filesig.f3_description = 'Agent Newsreader Character Map'
        sig_list.append(filesig)
    #
    if bytesData[0:2] == b'\x4d\x5a' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x4d\x5a'
        filesig.f2_extension = 'COM'
        filesig.f3_description = 'Windows/DOS Executable File'
        sig_list.append(filesig)
    #
    if bytesData[0:1] == b'\xe8' :
        filesig = FileSignature()
        filesig.f1_signature =  b'\xe8'
        filesig.f2_extension = 'COM'
        filesig.f3_description = 'Windows Executable file_1'
        sig_list.append(filesig)
    #
    if bytesData[0:1] == b'\xe9' :
        filesig = FileSignature()
        filesig.f1_signature = b'\xe9'
        filesig.f2_extension = 'COM'
        filesig.f3_description = 'Windows Executable file_2'
        sig_list.append(filesig)
    #
    if bytesData[0:1] == b'\xeb' :
        filesig = FileSignature()
        filesig.f1_signature = b'\xeb'
        filesig.f2_extension = 'COM'
        filesig.f3_description  = 'Windows Executable file_3'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\x46\x41\x58\x43\x4f\x56\x45\x52' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x46\x41\x58\x43\x4f\x56\x45\x52'
        filesig.f2_extension = 'CPE'
        filesig.f3_description = 'MS Fax Cover Sheet'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\x53\x49\x45\x54\x52\x4f\x4e\x49' :
        filesig = FileSignature()
        filesig.f1_signature= b'\x53\x49\x45\x54\x52\x4f\x4e\x49'
        filesig.f2_extension = 'CPI'
        filesig.f3_description = 'Sietronics CPI XRD Document'
        sig_list.append(filesig)
    #
    if bytesData[0:5] == b'\xff\x46\x4f\x4e\x54' :
        filesig = FileSignature()
        filesig.f1_signature = b'\xff\x46\x4f\x4e\x54'
        filesig.f2_extension = 'CPI'
        filesig.f3_description = 'Windows International Code Page'
        sig_list.append(filesig)
    #
    if bytesData[0:2] == b'\x4d\x5a' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x4d\x5a'
        filesig.f2_extension = 'CPL'
        filesig.f3_description = 'Control Panel Application'
        sig_list.append(filesig)
    #
    if bytesData[0:2] == b'\xdc\xdc' :
        filesig = FileSignature()
        filesig.f1_signature = b'\xdc\xdc'
        filesig.f2_extension = 'CPL'
        filesig.f3_description = 'Corel Color Palette'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\x43\x50\x54\x37\x46\x49\x4c\x45' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x43\x50\x54\x37\x46\x49\x4c\x45'
        filesig.f2_extension = 'CPT'
        filesig.f3_description = 'Corel Photopaint file_1'
        sig_list.append(filesig)
    #
    if bytesData[0:7] == b'\x43\x50\x54\x46\x49\x4c\x45' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x43\x50\x54\x46\x49\x4c\x45'
        filesig.f2_extension = 'CPT'
        filesig.f3_description = 'Corel Photopaint file_2'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\x5b\x57\x69\x6e\x64\x6f\x77\x73' :
        filesig = FileSignature()
        filesig.f1_signature =  b'\x5b\x57\x69\x6e\x64\x6f\x77\x73'
        filesig.f2_extension = 'CPX'
        filesig.f3_description = 'Microsoft Code Page Translation File'
        sig_list.append(filesig)
    #
    if bytesData[0:7] == b'\x43\x52\x55\x53\x48\x20\x76' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x43\x52\x55\x53\x48\x20\x76'
        filesig.f2_extension = 'CRU'
        filesig.f3_description = 'Crush Compressed Archive'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\x49\x49\x1a\x00\x00\x00\x48\x45' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x49\x49\x1a\x00\x00\x00\x48\x45'
        filesig.f2_extension = 'CRW'
        filesig.f3_description = 'Canon RAW File'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\x63\x75\x73\x68\x00\x00\x00\x02' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x63\x75\x73\x68\x00\x00\x00\x02'
        filesig.f2_extension = 'CSH'
        filesig.f3_description = 'Photoshop Custom Shape'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\x43\x61\x74\x61\x6c\x6f\x67\x20' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x43\x61\x74\x61\x6c\x6f\x67\x20'
        filesig.f2_extension= 'CTF'
        filesig.f3_description = 'WhereIsIt Catalog'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\x56\x45\x52\x53\x49\x4f\x4e\x20' :
        filesig = FileSignature()
        filesig.f1_signature =  b'\x56\x45\x52\x53\x49\x4f\x4e\x20'
        filesig.f2_extension = 'CTL'
        filesig.f3_description = 'Visual Basic User-Defined Control File'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x50\x48\x03\x04' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x50\x48\x03\x04'
        filesig.f2_extension = 'CUIX'
        filesig.f3_description = 'Customization Files'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x00\x00\x02\x00' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x00\x00\x02\x00'
        filesig.f2_extension = 'CUR'
        filesig.f3_description = 'Windows Cursor'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x52\x49\x49\x46' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x52\x49\x49\x46'
        filesig.f2_extension = 'DAT'
        filesig.f3_description = 'Video CD MPEG Movie'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\xa9\x0d\x00\x00\x00\x00\x00\x00' :
        filesig = FileSignature()
        filesig.f1_signature = b'\xa9\x0d\x00\x00\x00\x00\x00\x00'
        filesig.f2_extension = 'DAT'
        filesig.f3_description = 'Access Data FTK Evidence'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x73\x6c\x68\x21' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x73\x6c\x68\x21'
        filesig.f2_extension = 'DAT'
        filesig.f3_description = 'Allegro Generic Packfile (compressed)'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x73\x6c\x68\x2e' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x73\x6c\x68\x2e'
        filesig.f2_extension = 'DAT'
        filesig.f3_description = 'Allegro Generic Packfile (uncompressed)'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\x41\x56\x47\x36\x5f\x49\x6e\x74' :
        filesig = FileSignature()
        filesig.f1_signature= b'\x41\x56\x47\x36\x5f\x49\x6e\x74'
        filesig.f2_extension = 'DAT'
        filesig.f3_description = 'AVG6 Integrity database'
        sig_list.append(filesig)
    #
    if bytesData[0:1] == b'\x03' :
        filesig = FileSignature()
        filesig.f1_signature =  b'\x03'
        filesig.f2_extension = 'DAT'
        filesig.f3_description = 'MapInfo Native Data Format'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\x45\x52\x46\x53\x53\x41\x56\x45' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x45\x52\x46\x53\x53\x41\x56\x45'
        filesig.f2_extension = 'DAT'
        filesig.f3_description = 'EasyRecovery Saved State File'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\x43\x6c\x69\x65\x6e\x74\x20\x55' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x43\x6c\x69\x65\x6e\x74\x20\x55'
        filesig.f2_extension = 'DAT'
        filesig.f3_description = 'IE History File'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\x49\x6e\x6e\x6f\x20\x53\x65\x74' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x49\x6e\x6e\x6f\x20\x53\x65\x74'
        filesig.f2_extension = 'DAT'
        filesig.f3_description = 'Inno Setup Uninstall Log'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\x50\x4e\x43\x49\x55\x4e\x44\x4e' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x50\x4e\x43\x49\x55\x4e\x44\x4e'
        filesig.f2_extension = 'DAT'
        filesig.f3_description = 'Norton Disk Doctor Undo File'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x50\x45\x53\x54' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x50\x45\x53\x54'
        filesig.f2_extension = 'DAT'
        filesig.f3_description = 'PestPatrol Data (Scan Strings)'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\x1a\x52\x54\x53\x20\x43\x4f\x4d' :
        filesig = FileSignature()
        filesig.f1_signature  = b'\x1a\x52\x54\x53\x20\x43\x4f\x4d'
        filesig.f2_extension  = 'DAT'
        filesig.f3_description = 'Runtime Software Disk Image'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\x52\x41\x5a\x41\x54\x44\x42\x31' :
        filesig = FileSignature()
        filesig.f1_signature =  b'\x52\x41\x5a\x41\x54\x44\x42\x31'
        filesig.f2_extension = 'DAT'
        filesig.f3_description = 'Shareaza (P2P) Thumbnail'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\x4e\x41\x56\x54\x52\x41\x46\x46' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x4e\x41\x56\x54\x52\x41\x46\x46'
        filesig.f2_extension = 'DAT'
        filesig.f3_description = 'TomTom Traffic Data'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\x55\x46\x4f\x4f\x72\x62\x69\x74' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x55\x46\x4f\x4f\x72\x62\x69\x74'
        filesig.f2_extension = 'DAT'
        filesig.f3_description = 'UFO Capture Map File'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x57\x4d\x4d\x50' :
        filesig = FileSignature()
        filesig.f1_signature =  b'\x57\x4d\x4d\x50'
        filesig.f2_extension = 'DAT'
        filesig.f3_description  = 'Walkman MP3 File'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x43\x52\x45\x47' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x43\x52\x45\x47'
        filesig.f2_extension = 'DAT'
        filesig.f3_description = 'Win9x Registry Hive'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x72\x65\x67\x66' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x72\x65\x67\x66'
        filesig.f2_extension = 'DAT'
        filesig.f3_description = 'WinNT Registry File'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1' :
        filesig = FileSignature()
        filesig.f1_signature = b'\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1'
        filesig.f2_extension = 'DB'
        filesig.f3_description = 'MSWorks Database File'
        sig_list.append(filesig)
    #
    if bytesData[0:1]  == b'\x08':
        filesig = FileSignature()
        filesig.f1_signature = b'\x08'
        filesig.f2_extension = 'DB'
        filesig.f3_description = 'dBASE IV or dBFast Configuration File'
        sig_list.append(filesig)
    #
    if bytesData[0:16] == b'\x00\x06\x15\x61\x00\x00\x00\x02\x00\x00\x04\xd2\x00\x00\x10\x00' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x00\x06\x15\x61\x00\x00\x00\x02\x00\x00\x04\xd2\x00\x00\x10\x00'
        filesig.f2_extension = 'DB'
        filesig.f3_description = 'Netscape Navigator (v4) Database'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x44\x42\x46\x48' :
        filesig = FileSignature()
        filesig.f1_signature =  b'\x44\x42\x46\x48'
        filesig.f2_extension = 'DB'
        filesig.f3_description = 'Palm Zire Photo Database'
        sig_list.append(filesig)
    #
    if bytesData[0:16] == b'\x53\x51\x4c\x69\x74\x65\x20\x66\x6f\x72\x6d\x61\x74\x20\x33\x00' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x53\x51\x4c\x69\x74\x65\x20\x66\x6f\x72\x6d\x61\x74\x20\x33\x00'
        filesig.f2_extension = 'DB'
        filesig.f3_description = 'SQLite Database File'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\xfd\xff\xff\xff' :
        filesig = FileSignature()
        filesig.f1_signature = b'\xfd\xff\xff\xff'
        filesig.f2_extension = 'DB'
        filesig.f3_description = 'Thumbs.db Subheader'
        sig_list.append(filesig)
    #
    if bytesData[0:1] == b'\x03' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x03'
        filesig.f2_extension = 'DB3'
        filesig.f3_description = 'dBASE III File'
        sig_list.append(filesig)
    #
    if bytesData[0:1] == b'\x04' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x04'
        filesig.f2_extension = 'DB4'
        filesig.f3_description = 'dBASE IV File'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x00\x01\x42\x44' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x00\x01\x42\x44'
        filesig.f2_extension = 'DBA'
        filesig.f3_description = 'Palm DateBook Archive'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x6c\x33\x33\x6c' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x6c\x33\x33\x6c'
        filesig.f2_extension = 'DBB'
        filesig.f3_description = 'Skype User Data File'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\x4f\x50\x4c\x44\x61\x74\x61\x62' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x4f\x50\x4c\x44\x61\x74\x61\x62'
        filesig.f2_extension = 'DBF'
        filesig.f3_description = 'Psion Series 3 Database'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\xcf\xad\x12\xfe' :
        filesig = FileSignature()
        filesig.f1_signature =  b'\xcf\xad\x12\xfe'
        filesig.f2_extension = 'DBX'
        filesig.f3_description = 'Outlook Express E-mail Folder'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\x3c\x21\x64\x6f\x63\x74\x79\x70' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x3c\x21\x64\x6f\x63\x74\x79\x70'
        filesig.f2_extension = 'DCI'
        filesig.f3_description = 'AOL HTML Mail'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\xb1\x68\xde\x3a' :
        filesig = FileSignature()
        filesig.f1_signature = b'\xb1\x68\xde\x3a'
        filesig.f2_extension = 'DCX'
        filesig.f3_description = 'PCX Bitmap'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\x64\x65\x78\x0a\x30\x30\x39\x00' :
        filesig = FileSignature()
        filesig.f1_signature  = b'\x64\x65\x78\x0a\x30\x30\x39\x00'
        filesig.f2_extension = 'dex'
        filesig.f3_description = 'Dalvik (Android) Executable File'
        sig_list.append(filesig)
    #
    if bytesData[0:2] == b'\x42\x4d':
        filesig = FileSignature()
        filesig.f1_signature = b'\x42\x4d'
        filesig.f2_extension = 'DIB'
        filesig.f3_description = 'Bitmap Image'
        sig_list.append(filesig)
    #
    if bytesData[0:2] == b'\x4d\x5a' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x4d\x5a'
        filesig.f2_extension = 'DLL'
        filesig.f3_description = 'Windows/DOS Executable File'
        sig_list.append(filesig)
    #
    if bytesData[0:1] == b'\x78' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x78'
        filesig.f2_extension = 'DMG'
        filesig.f3_description = 'MacOS X Image File'
        sig_list.append(filesig)
    #
    if bytesData[0:6] == b'\x4d\x44\x4d\x50\x93\xa7' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x4d\x44\x4d\x50\x93\xa7'
        filesig.f2_extension = 'DMP'
        filesig.f3_description  = 'Windows Dump File'
        sig_list.append(filesig)
    #
    if bytesData[0:6] == b'\x50\x41\x47\x45\x44\x55' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x50\x41\x47\x45\x44\x55'
        filesig.f2_extension = 'DMP'
        filesig.f3_description = 'Windows Memory Dump'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x44\x4d\x53\x21' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x44\x4d\x53\x21'
        filesig.f2_extension = 'DMS'
        filesig.f3_description = 'Amiga DiskMasher Compressed Archive'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1' :
        filesig = FileSignature()
        filesig.f1_signature = b'\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1'
        filesig.f2_extension = 'doc'
        filesig.f3_description = 'Microsoft Office Document'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x0d\x44\x4f\x43' :
        filesig = FileSignature()
        filesig.f1_signature =  b'\x0d\x44\x4f\x43'
        filesig.f2_extension = 'doc'
        filesig.f3_description = 'DeskMate Document'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\xcf\x11\xe0\xa1\xb1\x1a\xe1\x00' :
        filesig = FileSignature()
        filesig.f1_signature = b'\xcf\x11\xe0\xa1\xb1\x1a\xe1\x00'
        filesig.f2_extension = 'doc'
        filesig.f3_description = 'Perfect Office Document'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\xdb\xa5\x2d\x00' :
        filesig = FileSignature()
        filesig.f1_signature = b'\xdb\xa5\x2d\x00'
        filesig.f2_extension = 'doc'
        filesig.f3_description = 'Word 2.0 File'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\xec\xa5\xc1\x00' :
        filesig = FileSignature()
        filesig.f1_signature = b'\xec\xa5\xc1\x00'
        filesig.f2_extension = 'doc'
        filesig.f3_description = 'Word Document Subheader'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x50\x4b\x03\x04' :
        filesig = FileSignature()
        filesig.f1_signature  =  b'\x50\x4b\x03\x04'
        filesig.f2_extension  = 'DOCX'
        filesig.f3_description = 'MS Office Open XML Format Document'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\x50\x4b\x03\x04\x14\x00\x06\x00' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x50\x4b\x03\x04\x14\x00\x06\x00'
        filesig.f2_extension = 'DOCX'
        filesig.f3_description = 'MS Office 2007 Documents'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1' :
        filesig = FileSignature()
        filesig.f1_signature = b'\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1'
        filesig.f2_extension  ='DOT'
        filesig.f3_description = 'Microsoft Office Document'
        sig_list.append(filesig)
    #
    if bytesData[0:2] == b'\x4d\x5a' :
        filesig = FileSignature()
        filesig.f1_signature =  b'\x4d\x5a'
        filesig.f2_extension = 'DRV'
        filesig.f3_description = 'Windows/DOS Executable File'
        sig_list.append(filesig)
    #
    if bytesData[0:1] == b'\x07' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x07'
        filesig.f2_extension = 'DRW'
        filesig.f3_description = 'Generic Drawing Programs'
        sig_list.append(filesig)
    #
    if bytesData[0:6] == b'\x01\xff\x02\x04\x03\x02' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x01\xff\x02\x04\x03\x02'
        filesig.f2_extension = 'DRW'
        filesig.f3_description = 'Micrografx Vector Graphic File'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x52\x49\x46\x46' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x52\x49\x46\x46'
        filesig.f2_extension = 'DS4'
        filesig.f3_description = 'Micrografx Designer Graphic'
        sig_list.append(filesig)
    #
    if bytesData[0:2] == b'\x4d\x56':
        filesig = FileSignature()
        filesig.f1_signature = b'\x4d\x56'
        filesig.f2_extension = 'DSN'
        filesig.f3_description = 'CD Stomper Pro Label File'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\x23\x20\x4d\x69\x63\x72\x6f\x73' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x23\x20\x4d\x69\x63\x72\x6f\x73'
        filesig.f2_extension = 'DSP'
        filesig.f3_description = 'MS Developer Studio Project File'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x02\x64\x73\x73' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x02\x64\x73\x73'
        filesig.f2_extension = 'DSS'
        filesig.f3_description = 'Digital Speech Standard File'
        sig_list.append(filesig)
    #
    if bytesData[0:7] == b'\x64\x73\x77\x66\x69\x6c\x65' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x64\x73\x77\x66\x69\x6c\x65'
        filesig.f2_extension = 'DSW'
        filesig.f3_description = 'MS Visual Studio Workspace File'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\x07\x64\x74\x32\x64\x64\x74\x64' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x07\x64\x74\x32\x64\x64\x74\x64'
        filesig.f2_extension = 'DTD'
        filesig.f3_description = 'DesignTools 2D Design file'
        sig_list.append(filesig)
    #
    if bytesData[0:7] == b'\x5b\x50\x68\x6f\x6e\x65\x5d' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x5b\x50\x68\x6f\x6e\x65\x5d'
        filesig.f2_extension = 'DUN'
        filesig.f3_description = 'Dial-up Networking File'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\x4d\x53\x5f\x56\x4f\x49\x43\x45' :
        filesig = FileSignature()
        filesig.f1_signature =  b'\x4d\x53\x5f\x56\x4f\x49\x43\x45'
        filesig.f2_extension = 'DVF'
        filesig.f3_description = 'Sony Compressed Voice File'
        sig_list.append(filesig)
    #
    if bytesData[0:3] == b'\x44\x56\x44' :
        filesig = FileSignature()
        filesig.f1_signature =  b'\x44\x56\x44'
        filesig.f2_extension = 'DVR'
        filesig.f3_description = 'DVR-Studio Stream File'
        sig_list.append(filesig)
    #
    if bytesData[0:2] == b'\x4f\x7b' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x4f\x7b'
        filesig.f2_extension = 'DW4'
        filesig.f3_description = 'Visio(DisplayWrite 4 Text File)'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x41\x43\x31\x30' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x41\x43\x31\x30'
        filesig.f2_extension = 'DWG'
        filesig.f3_description = 'Generic AutoCAD Drawing'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\x45\x56\x46\x09\x0d\x0a\xff\x00' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x45\x56\x46\x09\x0d\x0a\xff\x00'
        filesig.f2_extension = 'E01'
        filesig.f3_description = 'Expert Witness Compression Format'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\x4c\x56\x46\x09\x0d\x0a\xff\x00' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x4c\x56\x46\x09\x0d\x0a\xff\x00'
        filesig.f2_extension = 'EO1'
        filesig.f3_description = 'Logical File Evidence Format'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\x5b\x47\x65\x6e\x65\x72\x61\x6c' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x5b\x47\x65\x6e\x65\x72\x61\x6c'
        filesig.f2_extension = 'ECF'
        filesig.f3_description = 'MS Exchange Configuration File'
        sig_list.append(filesig)
    #
    if bytesData[0:2] == b'\xdc\xfe' :
        filesig = FileSignature()
        filesig.f1_signature = b'\xdc\xfe'
        filesig.f2_extension = 'EFX'
        filesig.f3_description = 'eFax File'
        sig_list.append(filesig)
    #
    if bytesData[0:2] == b'\x58\x2d':
        filesig = FileSignature()
        filesig.f1_signature = b'\x58\x2d'
        filesig.f2_extension ='EML'
        filesig.f3_description = 'Exchange E-mail'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\x52\x65\x74\x75\x72\x6e\x2d\x50' :
        filesig = FileSignature()
        filesig.f1_signature =  b'\x52\x65\x74\x75\x72\x6e\x2d\x50'
        filesig.f2_extension = 'EML'
        filesig.f3_description = 'Generic E-mail_1'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x46\x72\x6f\x6d' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x46\x72\x6f\x6d'
        filesig.f2_extension = 'EML'
        filesig.f3_description = 'Generic E-mail_2'
        sig_list.append(filesig)
    #
    if bytesData[0:10] == b'\x40\x40\40\x20\x00\x00\x40\x40\x40\x40':
        filesig = FileSignature()
        filesig.f1_signature = b'\x40\x40\40\x20\x00\x00\x40\x40\x40\x40'
        filesig.f2_extension  = 'ENL'
        filesig.f3_description = 'EndNote Library File'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\xc5\xd0\xd3\xc6' :
        filesig = FileSignature()
        filesig.f1_signature = b'\xc5\xd0\xd3\xc6'
        filesig.f2_extension = 'EPS'
        filesig.f3_description = 'Adobe Encapsulated PostScript'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\x25\x21\x50\x53\x2d\x41\x64\x6f' :
        filesig = FileSignature()
        filesig.f1_signature  = b'\x25\x21\x50\x53\x2d\x41\x64\x6f'
        filesig.f2_extension = 'EPS'
        filesig.f3_description = 'Encapsulated PostScript File'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x1a\x35\x01\x00' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x1a\x35\x01\x00'
        filesig.f2_extension = 'ETH'
        filesig.f3_description = 'WinPharoah Capture File'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\x30\x00\x00\x00\x4c\x66\x4c\x65' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x30\x00\x00\x00\x4c\x66\x4c\x65'
        filesig.f2_extension = 'EVT'
        filesig.f3_description = 'Windows Event Viewer File'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\x45\x6c\x66\x46\x69\x6c\x65\x00' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x45\x6c\x66\x46\x69\x6c\x65\x00'
        filesig.f2_extension = 'EVTX'
        filesig.f3_description = 'Windows Vista Event Log'
        sig_list.append(filesig)
    #
    if bytesData[0:2] == b'\x4d\x5a' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x4d\x5a'
        filesig.f2_extension = 'EXE'
        filesig.f3_description = 'Windows/DOS Executable File'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x25\x50\x44\x46' :
        filesig = FileSignature()
        filesig.f1_signature =  b'\x25\x50\x44\x46'
        filesig.f2_extension = 'FDF'
        filesig.f3_description = 'PDF File'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\x66\x4c\x61\x43\x00\x00\x00\x22':
        filesig = FileSignature()
        filesig.f1_signature = b'\x66\x4c\x61\x43\x00\x00\x00\x22'
        filesig.f2_extension = 'FLAC'
        filesig.f3_description = 'Free Lossless Audio Codec File'
        sig_list.append(filesig)
    #
    if bytesData[0:2] == b'\x00\x11' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x00\x11'
        filesig.f2_extension = 'FLI'
        filesig.f3_description = 'FLIC Animation'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\x4d\x5a\x90\x00\x03\x00\x00\x00' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x4d\x5a\x90\x00\x03\x00\x00\x00'
        filesig.f2_extension = 'FLT'
        filesig.f3_description = 'Audition Graphic Filter'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\x76\x32\x30\x30\x33\x2e\x31\x30' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x76\x32\x30\x30\x33\x2e\x31\x30'
        filesig.f2_extension = 'FLT'
        filesig.f3_description = 'Qimage Filter'
        sig_list.append(filesig)
    #
    if bytesData[0:3] == b'\x46\x4c\x56':
        filesig = FileSignature()
        filesig.f1_signature =  b'\x46\x4c\x56'
        filesig.f2_extension = 'FLV'
        filesig.f3_description = 'Flash Video File'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\x3c\x4d\x61\x6b\x65\x72\x46\x69':
        filesig = FileSignature()
        filesig.f1_signature = b'\x3c\x4d\x61\x6b\x65\x72\x46\x69'
        filesig.f2_extension = 'FM'
        filesig.f3_description = 'Adobe FrameMaker'
        sig_list.append(filesig)
    #
    if bytesData[0:2] == b'\x4d\x5a' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x4d\x5a'
        filesig.f2_extension = 'FON'
        filesig.f3_description = 'Font File'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\xd2\x0a\x00\x00' :
        filesig = FileSignature()
        filesig.f1_signature = b'\xd2\x0a\x00\x00'
        filesig.f2_extension = 'FTR'
        filesig.f3_description = 'WinPharoah Filter File'
        sig_list.append(filesig)
    #
    if bytesData[0:2] == b'\xfe\xef':
        filesig = FileSignature()
        filesig.f1_signature = b'\xfe\xef'
        filesig.f2_extension = 'GHO/GHS'
        filesig.f3_description = 'Symantex Ghost Image File'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x3f\x5f\x03\x00' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x3f\x5f\x03\x00'
        filesig.f2_extension = 'GID'
        filesig.f3_description = 'Windows Help file_2'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x4c\x4e\x02\x00' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x4c\x4e\x02\x00'
        filesig.f2_extension = 'GID'
        filesig.f3_description = 'Windows help file_3'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x47\x49\x46\x38' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x47\x49\x46\x38'
        filesig.f2_extension = 'GIF'
        filesig.f3_description = 'GIF File'
        sig_list.append(filesig)
    #
    if bytesData[0:1] == b'\x99' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x99'
        filesig.f2_extension = 'GPG'
        filesig.f3_description = 'GPG Public Keyring'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x50\x4d\x43\x43' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x50\x4d\x43\x43'
        filesig.f2_extension = 'GRP'
        filesig.f3_description  = 'Windows Program Manager Group File'
        sig_list.append(filesig)
    #
    if bytesData[0:3] == b'\x47\x58\x32' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x47\x58\x32'
        filesig.f2_extension = 'GX2'
        filesig.f3_description = 'Show Partner Graphics File'
        sig_list.append(filesig)
    #
    if bytesData[0:3] == b'\x1f\x8b\x08' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x1f\x8b\x08'
        filesig.f2_extension = 'GZ'
        filesig.f3_description = 'GZIP archive file'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x91\x33\x48\x46' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x91\x33\x48\x46'
        filesig.f2_extension = 'HAP'
        filesig.f3_description = 'Hamarsoft Compressed Archive'
        sig_list.append(filesig)
    #
    if bytesData[0:6] == b'\x4d\x44\x4d\x50\x93\xa7' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x4d\x44\x4d\x50\x93\xa7'
        filesig.f2_extension = 'HDMP'
        filesig.f3_description = 'Windows Dump File'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x49\x53\x63\x28':
        filesig = FileSignature()
        filesig.f1_signature = b'\x49\x53\x63\x28'
        filesig.f2_extension = 'HDR'
        filesig.f3_description = 'Install Shield Compressed File'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\x23\x3f\x52\x41\x44\x49\x41\x4e' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x23\x3f\x52\x41\x44\x49\x41\x4e'
        filesig.f2_extension = 'HDR'
        filesig.f3_description = 'Radiance High Dynamic Range Image File'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x48\x69\x50\x21' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x48\x69\x50\x21'
        filesig.f2_extension = 'hip'
        filesig.f3_description = 'Houdini Image File. Three-dimensional Modeling and Animation'
        sig_list.append(filesig)
    #
    if bytesData[0:6] == b'\x00\x00\xff\xff\xff\xff' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x00\x00\xff\xff\xff\xff'
        filesig.f2_extension = 'HLP'
        filesig.f3_description = 'Windows Help file_1'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x3f\x5f\x03\x00' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x3f\x5f\x03\x00'
        filesig.f2_extension = 'HLP'
        filesig.f3_description = 'Windows Help file_2'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x4c\x4e\x02\x00' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x4c\x4e\x02\x00'
        filesig.f2_extension = 'HLP'
        filesig.f3_description = 'Windows Help file_3'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\x28\x54\x68\x69\x73\x20\x66\x69' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x28\x54\x68\x69\x73\x20\x66\x69'
        filesig.f2_extension = 'HQX'
        filesig.f3_description = 'BinHex 4 Compressed Archive'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x00\x00\x01\x00':
        filesig = FileSignature()
        filesig.f1_signature =  b'\x00\x00\x01\x00'
        filesig.f2_extension = 'ICO'
        filesig.f3_description = 'Windows Icon (Printer Spool File)'
        sig_list.append(filesig)
    #
    if bytesData[0:5] == b'\x41\x4f\x4c\x44\x42' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x41\x4f\x4c\x44\x42'
        filesig.f2_extension = 'IDX'
        filesig.f3_description = 'AOL User Configuration'
        sig_list.append(filesig)
    #
    if bytesData[0:3] == b'\x41\x4f\x4c' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x41\x4f\x4c'
        filesig.f2_extension = 'IDX'
        filesig.f3_description = 'AOL Config Files'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\x50\x00\x00\x00\x20\x00\x00\x00' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x50\x00\x00\x00\x20\x00\x00\x00'
        filesig.f2_extension = 'IDX'
        filesig.f3_description = 'Quicken QuickFinder Information File'
        sig_list.append(filesig)
    #
    if bytesData[0:3] == b'\x44\x56\x44' :
        filesig = FileSignature()
        filesig.f1_signature  = b'\x44\x56\x44'
        filesig.f2_extension  = 'IFO'
        filesig.f3_description = 'DVD Info File'
        sig_list.append(filesig)
    #
    if bytesData[0:6] == b'\x50\x49\x43\x54\x00\x08' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x50\x49\x43\x54\x00\x08'
        filesig.f2_extension = 'IMG'
        filesig.f3_description = 'ChromaGraph Graphics Card Bitmap'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\xeb\x3c\x90\x2a' :
        filesig = FileSignature()
        filesig.f1_signature = b'\xeb\x3c\x90\x2a'
        filesig.f2_extension = 'IMG'
        filesig.f3_description = 'GEM Raster File'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x53\x43\x4d\x49' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x53\x43\x4d\x49'
        filesig.f2_extension = 'IMG'
        filesig.f3_description = 'Img Software Bitmap'
        sig_list.append(filesig)
    #
    if bytesData[0:6] == b'\x41\x4f\x4c\x49\x44\x58' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x41\x4f\x4c\x49\x44\x58'
        filesig.f2_extension = 'IND'
        filesig.f3_description = 'AOL Client Preferences(Settings) File'
        sig_list.append(filesig)
    #
    if bytesData[0:3] == b'\x41\x4f\x4c' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x41\x4f\x4c'
        filesig.f2_extension = 'IND'
        filesig.f3_description = 'AOL Config Files'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\xe3\x10\x00\x01\x00\x00\x00\x00' :
        filesig = FileSignature()
        filesig.f1_signature = b'\xe3\x10\x00\x01\x00\x00\x00\x00'
        filesig.f2_extension = 'INFO'
        filesig.f3_description = 'Amiga Icon'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\x54\x68\x69\x73\x20\x69\x73\x20' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x54\x68\x69\x73\x20\x69\x73\x20'
        filesig.f2_extension = 'INFO'
        filesig.f3_description = 'GNU Info Reader File'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x7a\x62\x65\x78' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x7a\x62\x65\x78'
        filesig.f2_extension = 'INFO'
        filesig.f3_description = 'ZoomBrowser Image Index'
        sig_list.append(filesig)
    #
    if bytesData[0:5] == b'\x43\x44\x30\x30\x31' :
        filesig = FileSignature()
        filesig.f1_signature =  b'\x43\x44\x30\x30\x31'
        filesig.f2_extension = 'ISO'
        filesig.f3_description = 'ISO-9660 CD Disc Image'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x2e\x52\x45\x43' :
        filesig = FileSignature()
        filesig.f1_signature =  b'\x2e\x52\x45\x43'
        filesig.f2_extension = 'IVR'
        filesig.f3_description = 'RealPlayer Video File (V11+)'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x50\x4b\x03\x04' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x50\x4b\x03\x04'
        filesig.f2_extension = 'JAR'
        filesig.f3_description = 'Java archive_1'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x5f\x27\xa8\x89' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x5f\x27\xa8\x89'
        filesig.f2_extension = 'JAR'
        filesig.f3_description  = 'Jar Archive'
        sig_list.append(filesig)
    #
    if bytesData[0:6] == b'\x4a\x41\x52\x43\x53\x00' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x4a\x41\x52\x43\x53\x00'
        filesig.f2_extension = 'JAR'
        filesig.f3_description = 'JARCS Compressed Archive'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\x50\x4b\x03\x04\x14\x00\x08\x00' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x50\x4b\x03\x04\x14\x00\x08\x00'
        filesig.f2_extension = 'JAR'
        filesig.f3_description = 'Java archive_2'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\xff\xd8\xff\xe0' :
        filesig = FileSignature()
        filesig.f1_signature = b'\xff\xd8\xff\xe0'
        filesig.f2_extension = 'JFIF/JPG/JPEG'
        filesig.f3_description = 'JPG/JPEG Image'
        sig_list.append(filesig)
    #
    if bytesData[0:2] == b'\xff\xd8' :
        filesig = FileSignature()
        filesig.f1_signature = b'\xff\xd8'
        filesig.f2_extension = 'JPG'
        filesig.f3_description = 'JPG Image'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x4a\x47\x03\x0e' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x4a\x47\x03\x0e'
        filesig.f2_extension = 'JG'
        filesig.f3_description = 'AOL ART file_1'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x4a\x47\x04\x0e' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x4a\x47\x04\x0e'
        filesig.f2_extension = 'JG'
        filesig.f3_description = 'AOL ART file_2'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x4e\x42\x2a\x00' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x4e\x42\x2a\x00'
        filesig.f2_extension = 'JNT'
        filesig.f3_description = 'MS Windows Journal'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\x00\x00\x00\x0c\x6a\x50\x20\x20' :
        filesig = FileSignature()
        filesig.f1_signature =  b'\x00\x00\x00\x0c\x6a\x50\x20\x20'
        filesig.f2_extension = 'JP2'
        filesig.f3_description = 'JPEG2000 Image Files'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\xff\xd8\xff\xe1' :
        filesig = FileSignature()
        filesig.f1_signature = b'\xff\xd8\xff\xe1'
        filesig.f2_extension = 'JPG'
        filesig.f3_description = 'Digital Camera JPG Using Exchangeable Image File Format (EXIF)'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\xff\xd8\xff\xe2' :
        filesig = FileSignature()
        filesig.f1_signature = b'\xff\xd8\xff\xe2'
        filesig.f2_extension = 'JPEG'
        filesig.f3_description = 'CANNON EOS JPEG FILE'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\xff\xd8\xff\xe3' :
        filesig = FileSignature()
        filesig.f1_signature = b'\xff\xd8\xff\xe3'
        filesig.f2_extension = 'JPEG'
        filesig.f3_description = 'SAMSUNG D500 JPEG FILE'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\xff\xd8\xff\xe8' :
        filesig = FileSignature()
        filesig.f1_signature = b'\xff\xd8\xff\xe8'
        filesig.f2_extension = 'JPG'
        filesig.f3_description = 'Still Picture Interchange File Format (SPIFF)'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x4e\x42\x2a\x00' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x4e\x42\x2a\x00'
        filesig.f2_extension  = 'JTP'
        filesig.f3_description = 'MS Windows Journal'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\x4b\x47\x42\x5f\x61\x72\x63\x68' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x4b\x47\x42\x5f\x61\x72\x63\x68'
        filesig.f2_extension = 'KGB'
        filesig.f3_description = 'KGB Archive'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\x49\x44\x33\x03\x00\x00\00' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x49\x44\x33\x03\x00\x00\00'
        filesig.f2_extension = 'KOZ'
        filesig.f3_description = 'Sprint Music Store Audio'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x50\x4b\x03\x04' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x50\x4b\x03\x04'
        filesig.f2_extension = 'KWD'
        filesig.f3_description = 'KWord Document'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\xc8\x00\x79\x00' :
        filesig = FileSignature()
        filesig.f1_signature = b'\xc8\x00\x79\x00'
        filesig.f2_extension = 'LBK'
        filesig.f3_description = 'Jeppesen FliteLog File'
        sig_list.append(filesig)
    #
    if bytesData[0:5] == b'\x7b\x0d\x0a\x6f\x20':
        filesig = FileSignature()
        filesig.f1_signature = b'\x7b\x0d\x0a\x6f\x20'
        filesig.f2_extension = 'LGC/LGD'
        filesig.f3_description = 'Windows Application Log'
        sig_list.append(filesig)
    #
    if bytesData[0:3] == b'\x2d\x6c\x68' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x2d\x6c\x68'
        filesig.f2_extension = 'LHA'
        filesig.f3_description = 'Compressed Archive'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\x21\x3c\x61\x72\x63\x68\x3e\x0a' :
        filesig = FileSignature()
        filesig.f1_signature =  b'\x21\x3c\x61\x72\x63\x68\x3e\x0a'
        filesig.f2_extension = 'LIB'
        filesig.f3_description = 'Unix Archiver (ar) [MS Program Library Common Object File Format (COFF)]'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\x49\x54\x4f\x4c\x49\x54\x4c\x53' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x49\x54\x4f\x4c\x49\x54\x4c\x53'
        filesig.f2_extension = 'LIT'
        filesig.f3_description  = 'MS Reader eBook'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\x4c\x00\x00\x00\x01\x14\x02\x00' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x4c\x00\x00\x00\x01\x14\x02\x00'
        filesig.f2_extension = 'LNK'
        filesig.f3_description = 'Windows Shortcut File'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\x2a\x2a\x2a\x20\x20\x49\x6e\x73' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x2a\x2a\x2a\x20\x20\x49\x6e\x73'
        filesig.f2_extension = 'LOG'
        filesig.f3_description = 'Symantec Wise Installer Log'
        sig_list.append(filesig)
    #
    if  bytesData[0:7] == b'\x57\x6f\x72\x64\x50\x72\x6f' :
        filesig = FileSignature()
        filesig.f1_signature  = b'\x57\x6f\x72\x64\x50\x72\x6f'
        filesig.f2_extension = 'LWP'
        filesig.f3_description = 'Lotus WordPro File'
        sig_list.append(filesig)
    #
    if bytesData[0:3] == b'\x2d\x6c\x68' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x2d\x6c\x68'
        filesig.f2_extension = 'LZH'
        filesig.f3_description = 'Compressed Archive'
        sig_list.append(filesig)
    #
    if bytesData[0:11] == b'\x00\x00\x00\x20\x66\x74\x79\x70\x4d\x34\x41' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x00\x00\x00\x20\x66\x74\x79\x70\x4d\x34\x41'
        filesig.f2_extension = 'M4A'
        filesig.f3_description = 'Apple Audio and Video Files'
        sig_list.append(filesig)
    #
    if bytesData[0:14] == b'\x3c\x3f\x78\x6d\x6c\x20\x76\x65\x72\x73\x69\x6f\x6e\x3d' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x3c\x3f\x78\x6d\x6c\x20\x76\x65\x72\x73\x69\x6f\x6e\x3d'
        filesig.f2_extension = 'MANIFEST'
        filesig.f3_description = 'Windows Visual Stylesheet'
        sig_list.append(filesig)
    #
    if bytesData[0:5] == b'\x4d\x41\x72\x30\x00' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x4d\x41\x72\x30\x00'
        filesig.f2_extension = 'MAR'
        filesig.f3_description = 'MAr Compressed Archive'
        sig_list.append(filesig)
    #
    elif bytesData[0:4] == b'\x4d\x41\x52\x43' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x4d\x41\x52\x43'
        filesig.f2_extension  ='MAR'
        filesig.f3_description = 'Microsoft/MSN MARC Archive'
        sig_list.append(filesig)
    #
    if bytesData[0:5] == b'\x4d\x41\x52\x31\x00' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x4d\x41\x52\x31\x00'
        filesig.f2_extension = 'MAR'
        filesig.f3_description = 'Mozilla Archive'
        sig_list.append(filesig)
    #
    if bytesData[0:19] == b'\x00\x01\x00\x00\x53\x74\x61\x6e\x64\x61\x72\x64\x20\x4a\x65\x74\x20\x44\x42' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x00\x01\x00\x00\x53\x74\x61\x6e\x64\x61\x72\x64\x20\x4a\x65\x74\x20\x44\x42'
        filesig.f2_extension = 'MDB'
        filesig.f3_description = 'Microsoft Access'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x01\x0f\x00\x00' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x01\x0f\x00\x00'
        filesig.f2_extension = 'MDF'
        filesig.f3_description = 'SQL Data Base'
        sig_list.append(filesig)
    #
    if bytesData[0:2] == b'\x45\x50' :
        filesig = FileSignature()
        filesig.f1_signature =  b'\x45\x50'
        filesig.f2_extension = 'MDI'
        filesig.f3_description = 'MS Document Imaging File'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x4d\x54\x68\x64' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x4d\x54\x68\x64'
        filesig.f2_extension = 'MID/MIDI'
        filesig.f3_description = 'MIDI Sound File'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\x3c\x4d\x61\x6b\x65\x72\x46\x69' :
        filesig = FileSignature()
        filesig.f1_signature =  b'\x3c\x4d\x61\x6b\x65\x72\x46\x69'
        filesig.f2_extension = 'MIF'
        filesig.f3_description = 'Adobe FrameMaker'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\x56\x65\x72\x73\x69\x6f\x6e\x20' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x56\x65\x72\x73\x69\x6f\x6e\x20'
        filesig.f2_extension = 'MIF'
        filesig.f3_description  = 'MapInfo Interchange Format File'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\x1a\x45\xdf\xa3\x93\x42\x82\x88' :
        filesig = FileSignature()
        filesig.f1_signature  = b'\x1a\x45\xdf\xa3\x93\x42\x82\x88'
        filesig.f2_extension  = 'MKV'
        filesig.f3_description = 'Matroska Stream File'
        sig_list.append(filesig)
    #
    if bytesData[0:5] == b'\x4d\x49\x4c\x45\x53' :
        filesig = FileSignature()
        filesig.f1_signature =  b'\x4d\x49\x4c\x45\x53'
        filesig.f2_extension = 'MLS'
        filesig.f3_description = 'Milestones Project Management File'
        sig_list.append(filesig)
    #
    if bytesData[0:5] == b'\x4d\x56\x32\x31\x34' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x4d\x56\x32\x31\x34'
        filesig.f2_extension = 'MLS'
        filesig.f3_description = 'Milestones Project Management file_1'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x4d\x56\x32\x43' :
        filesig = FileSignature()
        filesig.f1_signature  =  b'\x4d\x56\x32\x43'
        filesig.f2_extension = 'MLS'
        filesig.f3_description = 'Milestones Project Management file_2'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x4d\x4c\x53\x57' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x4d\x4c\x53\x57'
        filesig.f2_extension = 'MLS'
        filesig.f3_description = 'Skype Localization Data File'
        sig_list.append(filesig)
    #
    if bytesData[0:6] == b'\x4d\x4d\x4d\x44\x00\x00' :
        filesig = FileSignature()
        filesig.f1_signature =  b'\x4d\x4d\x4d\x44\x00\x00'
        filesig.f2_extension = 'MMF'
        filesig.f3_description = 'Yamaha Synthetic Music Mobile Application Format'
        sig_list.append(filesig)
    #
    if bytesData[0:19] == b'\x00\x01\x00\x00\x4d\x53\x49\x53\x41\x4d\x20\x44\x61\x74\x61\x62\x61\x73\x65' :
        filesig = FileSignature()
        filesig.f1_signature =  b'\x00\x01\x00\x00\x4d\x53\x49\x53\x41\x4d\x20\x44\x61\x74\x61\x62\x61\x73\x65'
        filesig.f2_extension = 'MNY'
        filesig.f3_description = 'Microsoft Money File'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\xff\xfe\x23\x00\x6c\x00\x69\x00':
        filesig = FileSignature()
        filesig.f1_signature = b'\xff\xfe\x23\x00\x6c\x00\x69\x00'
        filesig.f2_extension = 'MOF'
        filesig.f3_description  = 'MSinfo File'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x6d\x6f\x6f\x76' :
        filesig = FileSignature()
        filesig.f1_signature  = b'\x6d\x6f\x6f\x76'
        filesig.f2_extension = 'MOV'
        filesig.f3_description = 'QuickTime movie_1'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x66\x72\x65\x65' :
        filesig = FileSignature()
        filesig.f1_signature  = b'\x66\x72\x65\x65'
        filesig.f2_extension = 'MOV'
        filesig.f3_description = 'QuickTime movie_2'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x6d\x64\x61\x74' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x6d\x64\x61\x74'
        filesig.f2_extension = 'MOV'
        filesig.f3_description = 'QuickTime movie_3'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x77\x69\x64\x65' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x77\x69\x64\x65'
        filesig.f2_extension  = 'MOV'
        filesig.f3_description = 'QuickTime movie_4'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x70\x6e\x6f\x74' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x70\x6e\x6f\x74'
        filesig.f2_extension = 'MOV'
        filesig.f3_description = 'QuickTime movie_5'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x73\x6b\x69\x70' :
        filesig = FileSignature()
        filesig.f1_signature  =  b'\x73\x6b\x69\x70'
        filesig.f2_extension = 'MOV'
        filesig.f3_description = 'QuickTime movie_6'
        sig_list.append(filesig)
    #
    if bytesData[0:2] == b'\x0c\xed' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x0c\xed'
        filesig.f2_extension = 'MP'
        filesig.f3_description = 'Monochrome Picture TIFF Bitmap'
        sig_list.append(filesig)
    #
    elif bytesData[0:3] == b'\x49\x44\x33' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x49\x44\x33'
        filesig.f2_extension = 'MP3'
        filesig.f3_description = 'MP3 Audio File'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x00\x00\x01\xba' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x00\x00\x01\xba'
        filesig.f2_extension = 'MPG'
        filesig.f3_description = 'DVD Video File'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x00\x00\x01\xb3' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x00\x00\x01\xb3'
        filesig.f2_extension = 'MPG'
        filesig.f3_description = 'MPEG Video File'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1' :
        filesig = FileSignature()
        filesig.f1_signature = b'\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1'
        filesig.f2_extension = 'MSC'
        filesig.f3_description = 'Microsoft Common Console Document'
        sig_list.append(filesig)
    #
    if bytesData[0:50] == b'\x3c\x3f\x78\x6d\x6c\x20\x76\x65\x72\x73' \
                            b'\x69\x6f\x6e\x3d\x22\x31\x2e\x30\x22\x3f\x3e\x0d' \
                            b'\x0a\x3c\x4d\x4d\x43\x5f\x43\x6f\x6e\x73\x6f\x6c\x65' \
                            b'\x46\x69\x6c\x65\x20\x43\x6f\x6e\x73\x6f\x6c\x65\x46\x69\x6c' \
                            b'\x65\x20\x43\x6f\x6e\x73\x6f\x6c\x65\x56\x65\x72' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x3c\x3f\x78\x6d\x6c\x20\x76\x65\x72\x73' \
                            b'\x69\x6f\x6e\x3d\x22\x31\x2e\x30\x22\x3f\x3e\x0d' \
                            b'\x0a\x3c\x4d\x4d\x43\x5f\x43\x6f\x6e\x73\x6f\x6c\x65' \
                            b'\x46\x69\x6c\x65\x20\x43\x6f\x6e\x73\x6f\x6c\x65\x46\x69\x6c' \
                            b'\x65\x20\x43\x6f\x6e\x73\x6f\x6c\x65\x56\x65\x72'
        filesig.f2_extension = 'MSC'
        filesig.f3_description = 'MMC Snap-in Control File'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1' :
        filesig = FileSignature()
        filesig.f1_signature = b'\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1'
        filesig.f2_extension = 'MSI'
        filesig.f3_description  = 'Microsoft Installer Package'
        sig_list.append(filesig)
    #
    if bytesData[0:2] == b'\x23\x20' :
        filesig = FileSignature()
        filesig.f1_signature =  b'\x23\x20'
        filesig.f2_extension = 'MSI'
        filesig.f3_description = 'Cerius2 file'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\x4d\x53\x5f\x56\x4f\x49\x43\x45' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x4d\x53\x5f\x56\x4f\x49\x43\x45'
        filesig.f2_extension  ='MSV'
        filesig.f3_description = 'Sony Compressed Voice File'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1' :
        filesig = FileSignature()
        filesig.f1_signature = b'\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1'
        filesig.f2_extension = 'MTW'
        filesig.f3_description = 'Minitab Data File'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\x0e\x4e\x65\x72\x6f\x49\x53\x4f' :
        filesig = FileSignature()
        filesig.f1_signature =  b'\x0e\x4e\x65\x72\x6f\x49\x53\x4f'
        filesig.f2_extension = 'NRI'
        filesig.f3_description = 'Nero CD Compilation'
        sig_list.append(filesig)
    #
    if bytesData[0:6] == b'\x1a\x00\x00\x04\x00\x00' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x1a\x00\x00\x04\x00\x00'
        filesig.f2_extension = 'NSF'
        filesig.f3_description = 'Lotus Notes Database'
        sig_list.append(filesig)
    #
    if bytesData[0:6] == b'\x4e\x45\x53\x4d\x1a\x01' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x4e\x45\x53\x4d\x1a\x01'
        filesig.f2_extension = 'NSF'
        filesig.f3_description  = 'NES Sound File'
        sig_list.append(filesig)
    #
    if bytesData[0:3] == b'\x1a\x00\x00' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x1a\x00\x00'
        filesig.f2_extension = 'NTF'
        filesig.f3_description  = 'Lotus Notes Database Template'
        sig_list.append(filesig)
    #
    if bytesData[0:5] == b'\x4e\x49\x54\x46\x30' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x4e\x49\x54\x46\x30'
        filesig.f2_extension = 'NTF'
        filesig.f3_description = 'National Imagery Transmission Format File'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\x30\x31\x4f\x52\x44\x4e\x41\x4e' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x30\x31\x4f\x52\x44\x4e\x41\x4e'
        filesig.f2_extension = 'NTF'
        filesig.f3_description = 'National Transfer Format Map'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x4d\x52\x56\x4e' :
        filesig = FileSignature()
        filesig.f1_signature =  b'\x4d\x52\x56\x4e'
        filesig.f2_extension = 'NVRAM'
        filesig.f3_description = 'VMware BIOS State File'
        sig_list.append(filesig)
    #
    if bytesData[0:2] == b'\x4c\x01' :
        filesig = FileSignature()
        filesig.f1_signature =  b'\x4c\x01'
        filesig.f2_extension = 'OBJ'
        filesig.f3_description = 'MS COFF Relocatable Object Code'
        sig_list.append(filesig)
    #
    if bytesData[0:1] == b'\x80':
        filesig = FileSignature()
        filesig.f1_signature = b'\x80'
        filesig.f2_extension  ='OBJ'
        filesig.f3_description = 'Relocatable Object Code'
        sig_list.append(filesig)
    #
    if bytesData[0:2] == b'\x4d\x5a' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x4d\x5a'
        filesig.f2_extension = 'OCX'
        filesig.f3_description = 'ActiveX (OLE) Custom Control'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x50\x4b\x03\x04' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x50\x4b\x03\x04'
        filesig.f2_extension  = 'ODP/ODT'
        filesig.f3_description = 'OpenDocument Template'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\x4f\x67\x67\x53\x00\x02\x00\x00' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x4f\x67\x67\x53\x00\x02\x00\x00'
        filesig.f2_extension = 'OGA/OGG/OGV/OGX'
        filesig.f3_description = 'Ogg Vorbis Codec Compressed File'
        sig_list.append(filesig)
    #
    if bytesData[0:2] == b'\x4d\x5a' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x4d\x5a'
        filesig.f2_extension  = 'OLB'
        filesig.f3_description = 'OLE Object Library'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\xe4\x52\x5c\x7b\x8c\xd8\xa7\x4d' :
        filesig = FileSignature()
        filesig.f1_signature = b'\xe4\x52\x5c\x7b\x8c\xd8\xa7\x4d'
        filesig.f2_extension  ='ONE'
        filesig.f3_description = 'MS OneNote Note'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1' :
        filesig = FileSignature()
        filesig.f1_signature = b'\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1'
        filesig.f2_extension = 'OPT'
        filesig.f3_description = 'Developer Studio File Options File'
        sig_list.append(filesig)
    #
    if bytesData[0:5] == b'\xfd\xff\xff\xff\x20' :
        filesig = FileSignature()
        filesig.f1_signature = b'\xfd\xff\xff\xff\x20'
        filesig.f2_extension = 'OPT'
        filesig.f3_description = 'Developer Studio Subheader'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\x41\x4f\x4c\x56\x4d\x31\x30\x30' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x41\x4f\x4c\x56\x4d\x31\x30\x30'
        filesig.f2_extension = 'ORG'
        filesig.f3_description = 'AOL Personal File Cabinet'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x50\x4b\x03\x04' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x50\x4b\x03\x04'
        filesig.f2_extension = 'OTT'
        filesig.f3_description = 'OpenDocument Template'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x64\x00\x00\x00' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x64\x00\x00\x00'
        filesig.f2_extension = 'P10'
        filesig.f3_description = 'Intel PROset/Wireless Profile'
        sig_list.append(filesig)
    #
    if bytesData[0:2] == b'\x1a\x0b' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x1a\x0b'
        filesig.f2_extension = 'PAK'
        filesig.f3_description = 'PAK Compressed Archive File'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x50\x41\x43\x4b' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x50\x41\x43\x4b'
        filesig.f2_extension = 'PAK'
        filesig.f3_description = 'Quake Archive File'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x47\x50\x41\x54' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x47\x50\x41\x54'
        filesig.f2_extension = 'PAT'
        filesig.f3_description = 'GIMP Pattern File'
        sig_list.append(filesig)
    #
    if bytesData[0:3] == b'\x50\x41\x58' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x50\x41\x58'
        filesig.f2_extension = 'PAX'
        filesig.f3_description = 'PAX Password Protected Bitmap'
        sig_list.append(filesig)
    #
    if bytesData[0:6] == b'\x56\x43\x50\x43\x48\x30' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x56\x43\x50\x43\x48\x30'
        filesig.f2_extension = 'PCH'
        filesig.f3_description = 'Visual C PreCompiled Header'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x0a\x05\x01\x01' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x0a\x05\x01\x01'
        filesig.f2_extension = 'PCX'
        filesig.f3_description = 'ZSOFT Paintbrush file_3'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x0a\x03\x01\x01' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x0a\x03\x01\x01'
        filesig.f2_extension = 'PCX'
        filesig.f3_description = 'ZSOFT Paintbrush file_2'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x0a\x02\x01\x01' :
        filesig = FileSignature()
        filesig.f1_signature =  b'\x0a\x02\x01\x01'
        filesig.f2_extension = 'PCX'
        filesig.f3_description = 'ZSOFT Paintbrush file_1'
        sig_list.append(filesig)
    #
    if bytesData[0:16] == b'\x4d\x69\x63\x72\x6f\x73\x6f\x66\x74\x20\x43\x2f\x43\x2b\x2b\x20' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x4d\x69\x63\x72\x6f\x73\x6f\x66\x74\x20\x43\x2f\x43\x2b\x2b\x20'
        filesig.f2_extension = 'PDB'
        filesig.f3_description = 'MS C++ Debugging Symbols File'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\x4d\x2d\x57\x20\x50\x6f\x63\x6b' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x4d\x2d\x57\x20\x50\x6f\x63\x6b'
        filesig.f2_extension = 'PDB'
        filesig.f3_description = 'Merriam-Webster Pocket Dictionary'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\xac\xed\x00\x05\x73\x72\x00\x12' :
        filesig = FileSignature()
        filesig.f1_signature = b'\xac\xed\x00\x05\x73\x72\x00\x12'
        filesig.f2_extension = 'PDB'
        filesig.f3_description = 'BGBlitz Position Database File'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x73\x7a\x65\x7a' :
        filesig = FileSignature()
        filesig.f1_signature =  b'\x73\x7a\x65\x7a'
        filesig.f2_extension = 'PDB'
        filesig.f3_description = 'PowerBASIC Debugger Symbols'
        sig_list.append(filesig)
    #
    if bytesData[0:3] == b'\x73\x6d\x5f' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x73\x6d\x5f'
        filesig.f2_extension = 'PDB'
        filesig.f3_description = 'PalmOS SuperMemo'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x25\x50\x44\x46' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x25\x50\x44\x46'
        filesig.f2_extension = 'PDF'
        filesig.f3_description = 'PDF File'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\x11\x00\x00\x00\x53\x43\x43\x41' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x11\x00\x00\x00\x53\x43\x43\x41'
        filesig.f2_extension = 'PF'
        filesig.f3_description = 'Windows Prefetch File'
        sig_list.append(filesig)
    #
    if bytesData[0:3] == b'\x41\x4f\x4c'  :
        filesig = FileSignature()
        filesig.f1_signature = b'\x41\x4f\x4c'
        filesig.f2_extension = 'PFC'
        filesig.f3_description = 'AOL Config Files'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\x41\x4f\x4c\x56\x4d\x31\x30\x30' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x41\x4f\x4c\x56\x4d\x31\x30\x30'
        filesig.f2_extension = 'PFC'
        filesig.f3_description = 'AOL Personal File Cabinet'
        sig_list.append(filesig)
    #
    elif bytesData[0:8] == b'\x50\x47\x50\x64\x4d\x41\x49\x4e' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x50\x47\x50\x64\x4d\x41\x49\x4e'
        filesig.f2_extension = 'PGD'
        filesig.f3_description = 'PGP Disk Image'
        sig_list.append(filesig)
    #
    if bytesData[0:3] == b'\x50\x35\x0a' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x50\x35\x0a'
        filesig.f2_extension = 'PGM'
        filesig.f3_description = 'Portable Graymap Graphic'
        sig_list.append(filesig)
    #
    if bytesData[0:2] == b'\x4d\x5a' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x4d\x5a'
        filesig.f2_extension = 'PIF'
        filesig.f3_description = 'Windows/DOS Executable File'
        sig_list.append(filesig)
    #
    if bytesData[0:2] == b'\x99\x01' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x99\x01'
        filesig.f2_extension = 'PKR'
        filesig.f3_description = 'PGP Public Keyring'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\x89\x50\x4e\x47\x0d\x0a\x1a\x0a' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x89\x50\x4e\x47\x0d\x0a\x1a\x0a'
        filesig.f2_extension = 'PNG'
        filesig.f3_description =  'PNG Image'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1' :
        filesig = FileSignature()
        filesig.f1_signature = b'\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1'
        filesig.f2_extension = 'PPS'
        filesig.f3_description = 'Microsoft Office Document'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\xfd\xff\xff\xff\x43\x00\x00\x00' :
        filesig = FileSignature()
        filesig.f1_signature = b'\xfd\xff\xff\xff\x43\x00\x00\x00'
        filesig.f2_extension = 'PPT'
        filesig.f3_description = 'PowerPoint Presentation Subheader_6'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\xfd\xff\xff\xff\x1c\x00\x00\x00' :
        filesig = FileSignature()
        filesig.f1_signature =   b'\xfd\xff\xff\xff\x1c\x00\x00\x00'
        filesig.f2_extension = 'PPT'
        filesig.f3_description = 'PowerPoint Presentation Subheader_5'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1' :
        filesig = FileSignature()
        filesig.f1_signature = b'\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1'
        filesig.f2_extension = 'PPT'
        filesig.f3_description = 'Microsoft Office Document'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\xfd\xff\xff\xff\x0e\x00\x00\x00' :
        filesig = FileSignature()
        filesig.f1_signature =  b'\xfd\xff\xff\xff\x0e\x00\x00\x00'
        filesig.f2_extension = 'PPT'
        filesig.f3_description = 'PowerPoint Presentation Subheader_4'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\xa0\x46\x1d\xf0' :
        filesig = FileSignature()
        filesig.f1_signature = b'\xa0\x46\x1d\xf0'
        filesig.f2_extension = 'PPT'
        filesig.f3_description = 'PowerPoint Presentation Subheader_3'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x0f\x00\xe8\x03' :
        filesig = FileSignature()
        filesig.f1_signature =  b'\x0f\x00\xe8\x03'
        filesig.f2_extension = 'PPT'
        filesig.f3_description = 'PowerPoint Presentation Subheader_2'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x00\x6e\x1e\xf0' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x00\x6e\x1e\xf0'
        filesig.f2_extension = 'PPT'
        filesig.f3_description = 'PowerPoint Presentation Subheader_1'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x50\x4b\x03\x04' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x50\x4b\x03\x04'
        filesig.f2_extension = 'PPTX'
        filesig.f3_description = 'MS Office Open XML Format Document'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\x50\x4b\x03\x04\x14\x00\x06\x00' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x50\x4b\x03\x04\x14\x00\x06\x00'
        filesig.f2_extension = 'PPTX'
        filesig.f3_description = 'MS Office 2007 Documents'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x4d\x53\x43\x46' :
        filesig = FileSignature()
        filesig.f1_signature =  b'\x4d\x53\x43\x46'
        filesig.f2_extension = 'PPZ'
        filesig.f3_description  = 'Powerpoint Packaged Presentation'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\x74\x42\x4d\x50\x4b\x6e\x57\x72' :
        filesig = FileSignature()
        filesig.f1_signature =  b'\x74\x42\x4d\x50\x4b\x6e\x57\x72'
        filesig.f2_extension = 'PRC'
        filesig.f3_description = 'PathWay Map File'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\x42\x4f\x4f\x4b\x4d\x4f\x42\x49' :
        filesig = FileSignature()
        filesig.f1_signature  = b'\x42\x4f\x4f\x4b\x4d\x4f\x42\x49'
        filesig.f2_extension = 'PRC'
        filesig.f3_description = 'Palmpilot Resource File'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x38\x42\x50\x53' :
        filesig = FileSignature()
        filesig.f1_signature =  b'\x38\x42\x50\x53'
        filesig.f2_extension = 'PSD'
        filesig.f3_description = 'Photoshop Image'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x7e\x42\x4b\x00' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x7e\x42\x4b\x00'
        filesig.f2_extension = 'PSP'
        filesig.f3_description = 'Corel Paint Shop Pro Image'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1' :
        filesig = FileSignature()
        filesig.f1_signature = b'\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1'
        filesig.f2_extension = 'PUB'
        filesig.f3_description = 'MS Publisher File'
        sig_list.append(filesig)
    #
    if bytesData[0:5] == b'\x7b\x5c\x70\x77\x69' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x7b\x5c\x70\x77\x69'
        filesig.f2_extension = 'PWI'
        filesig.f3_description = 'MS WinMobile Personal Note'
        sig_list.append(filesig)
    #
    elif bytesData[0:4] == b'\xe3\x82\x85\x96' :
        filesig = FileSignature()
        filesig.f1_signature = b'\xe3\x82\x85\x96'
        filesig.f2_extension = 'PWL'
        filesig.f3_description = 'Win98 Password File'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\xb0\x4d\x46\x43' :
        filesig = FileSignature()
        filesig.f1_signature = b'\xb0\x4d\x46\x43'
        filesig.f2_extension = 'PWL'
        filesig.f3_description = 'Win95 Password File'
        sig_list.append(filesig)
    #
    if bytesData[0:6] == b'\x45\x86\x00\x00\x06\x00' :
        filesig = FileSignature()
        filesig.f1_signature =  b'\x45\x86\x00\x00\x06\x00'
        filesig.f2_extension = 'QBB'
        filesig.f3_description = 'QuickBooks Backup'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x52\x49\x46\x46' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x52\x49\x46\x46'
        filesig.f2_extension = 'QCP'
        filesig.f3_description = 'Resource Interchange File Format'
        sig_list.append(filesig)
    #
    if bytesData[0:6] == b'\xac\x9e\xbd\x8f\x00\x00' :
        filesig = FileSignature()
        filesig.f1_signature = b'\xac\x9e\xbd\x8f\x00\x00'
        filesig.f2_extension = 'QDF'
        filesig.f3_description = 'QDF Quicken Data'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x51\x45\x4c\x20' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x51\x45\x4c\x20'
        filesig.f2_extension = 'QEL'
        filesig.f3_description = 'QDL Quicken Data'
        sig_list.append(filesig)
    #
    if bytesData[0:3] == b'\x51\x46\x49' :
        filesig = FileSignature()
        filesig.f1_signature =  b'\x51\x46\x49'
        filesig.f2_extension = 'QEMU'
        filesig.f3_description = 'Qcow Disk Image'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x03\x00\x00\x00' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x03\x00\x00\x00'
        filesig.f2_extension = 'QPH'
        filesig.f3_description = 'Quicken Price History'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\x51\x57\x20\x56\x65\x72\x2e\x20' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x51\x57\x20\x56\x65\x72\x2e\x20'
        filesig.f2_extension = 'QSD'
        filesig.f3_description = 'ABD (QSD) Quicken Data File'
        sig_list.append(filesig)
    #
    if bytesData[0:2] == b'\x4d\x5a' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x4d\x5a'
        filesig.f2_extension = 'QTS/QTX'
        filesig.f3_description = 'Windows/DOS Executable File'
        sig_list.append(filesig)
    #
    if bytesData[0:7] == b'\x00\x00\x4d\x4d\x58\x50\x52' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x00\x00\x4d\x4d\x58\x50\x52'
        filesig.f2_extension = 'QXD'
        filesig.f3_description = 'Quark Express (Motorola)'
        sig_list.append(filesig)
    #
    if bytesData[0:7] == b'\x00\x00\x49\x49\x58\x50\x52' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x00\x00\x49\x49\x58\x50\x52'
        filesig.f2_extension = 'QXD'
        filesig.f3_description = 'Quark Express (Intel)'
        sig_list.append(filesig)
    #
    if bytesData[0:5] == b'\x2e\x72\x61\xfd\x00' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x2e\x72\x61\xfd\x00'
        filesig.f2_extension = 'RA'
        filesig.f3_description = 'RealAudio Streaming Media'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\x2e\x52\x4d\x46\x00\x00\x00\x12' :
        filesig = FileSignature()
        filesig.f1_signature =  b'\x2e\x52\x4d\x46\x00\x00\x00\x12'
        filesig.f2_extension = 'RA'
        filesig.f3_description = 'RealAudio File'
        sig_list.append(filesig)
    #
    if bytesData[0:7] == b'\x72\x74\x73\x70\x3a\x2f\x2f' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x72\x74\x73\x70\x3a\x2f\x2f'
        filesig.f2_extension = 'RAM'
        filesig.f3_description = 'RealMedia Metafile'
        sig_list.append(filesig)
    #
    if bytesData[0:7] == b'\x52\x61\x72\x21\x1a\x07\x00' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x52\x61\x72\x21\x1a\x07\x00'
        filesig.f2_extension = 'RAR'
        filesig.f3_description = 'WinRAR Compressed Archive'
        sig_list.append(filesig)
    #
    if bytesData[0:7] == b'\x52\x45\x47\x45\x44\x49\x54' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x52\x45\x47\x45\x44\x49\x54'
        filesig.f2_extension = 'REG'
        filesig.f3_description = 'WinNT Registry (Registry Undo) Files'
        sig_list.append(filesig)
    #
    if bytesData[0:2] == b'\xff\xfe' :
        filesig = FileSignature()
        filesig.f1_signature = b'\xff\xfe'
        filesig.f2_extension = 'REG'
        filesig.f3_description = 'Windows Registry File'
        sig_list.append(filesig)
    #
    if bytesData[0:6] == b'\x01\xda\x01\x01\x00\x03' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x01\xda\x01\x01\x00\x03'
        filesig.f2_extension = 'RGB'
        filesig.f3_description = 'Silicon Graphics RGB Bitmap'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x2e\x52\x4d\x46' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x2e\x52\x4d\x46'
        filesig.f2_extension = 'RM/RMVB'
        filesig.f3_description = 'RealMedia Streaming Media'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x52\x49\x46\x46' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x52\x49\x46\x46'
        filesig.f2_extension = 'RMI'
        filesig.f3_description = 'Resource Interchange File Format'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\xed\xab\xee\xdb' :
        filesig = FileSignature()
        filesig.f1_signature = b'\xed\xab\xee\xdb'
        filesig.f2_extension = 'RPM'
        filesig.f3_description = 'RedHat Package Manager'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\x43\x23\x2b\x44\xa4\x43\x4d\xa5' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x43\x23\x2b\x44\xa4\x43\x4d\xa5'
        filesig.f2_extension  ='RTD'
        filesig.f3_description = 'RagTime Document'
        sig_list.append(filesig)
    #
    if bytesData[0:6] == b'\x7b\x5c\x72\x74\x66\x31' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x7b\x5c\x72\x74\x66\x31'
        filesig.f2_extension = 'RTF'
        filesig.f3_description = 'RTF File'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1' :
        filesig = FileSignature()
        filesig.f1_signature = b'\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1'
        filesig.f2_extension = 'RVT'
        filesig.f3_description = 'Revit Project File'
        sig_list.append(filesig)
    #
    if bytesData[0:5] == b'\x5b\x76\x65\x72\x5d' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x5b\x76\x65\x72\x5d'
        filesig.f2_extension = 'SAM'
        filesig.f3_description = 'Lotus AMI Pro Document_2'
        sig_list.append(filesig)
    #
    if bytesData[0:5] == b'\x5b\x56\x45\x52\x5d' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x5b\x56\x45\x52\x5d'
        filesig.f2_extension = 'SAM'
        filesig.f3_description = 'Lotus AMI Pro Document_1'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\x24\x46\x4c\x32\x40\x28\x23\x29' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x24\x46\x4c\x32\x40\x28\x23\x29'
        filesig.f2_extension = 'SAV'
        filesig.f3_description = 'SPSS Data File'
        sig_list.append(filesig)
    #
    if bytesData[0:2] == b'\x4d\x5a' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x4d\x5a'
        filesig.f2_extension = 'SCR'
        filesig.f3_description = 'Screen Saver'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\x53\x4d\x41\x52\x54\x44\x52\x57' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x53\x4d\x41\x52\x54\x44\x52\x57'
        filesig.f2_extension = 'SDR'
        filesig.f3_description = 'SmartDraw Drawing File'
        sig_list.append(filesig)
    #
    if bytesData[0:5] == b'\x48\x48\x47\x42\x31' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x48\x48\x47\x42\x31'
        filesig.f2_extension =' SH3'
        filesig.f3_description = 'Harvard Graphics Presentation File'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x67\x49\x00\x00' :
        filesig = FileSignature()
        filesig.f1_signature =  b'\x67\x49\x00\x00'
        filesig.f2_extension = 'SHD'
        filesig.f3_description = 'Win2000/XP Printer Spool File'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x4b\x49\x00\x00' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x4b\x49\x00\x00'
        filesig.f2_extension = 'SHD'
        filesig.f3_description = 'Win9x Printer Spool File'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x66\x49\x00\x00' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x66\x49\x00\x00'
        filesig.f2_extension = 'SHD'
        filesig.f3_description = 'WinNT Printer Spool File'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x68\x49\x00\x00' :
        filesig = FileSignature()
        filesig.f1_signature =  b'\x68\x49\x00\x00'
        filesig.f2_extension = 'SHD'
        filesig.f3_description = 'Win Server 2003 Printer Spool File'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x53\x48\x4f\x57' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x53\x48\x4f\x57'
        filesig.f2_extension = 'SHW'
        filesig.f3_description = 'Harvard Graphics Presentation'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\x53\x74\x75\x66\x66\x49\x74\x20' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x53\x74\x75\x66\x66\x49\x74\x20'
        filesig.f2_extension ='SIT'
        filesig.f3_description = 'StuffIt Compressed Archive'
        sig_list.append(filesig)
    #
    if bytesData[0:5] == b'\x53\x49\x54\x21\x00' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x53\x49\x54\x21\x00'
        filesig.f2_extension = 'SIT'
        filesig.f3_description = 'StuffIt Archive'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x07\x53\x4b\x46' :
        filesig = FileSignature()
        filesig.f1_signature=  b'\x07\x53\x4b\x46'
        filesig.f2_extension = 'SKF'
        filesig.f3_description = 'SkinCrafter Skin'
        sig_list.append(filesig)
    #
    if bytesData[0:2] == b'\x95\x01' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x95\x01'
        filesig.f2_extension = 'SKR'
        filesig.f3_description = 'PGP Secret Keyring_2'
        sig_list.append(filesig)
    #
    if bytesData[0:2] == b'\x95\x00' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x95\x00'
        filesig.f2_extension = 'SKR'
        filesig.f3_description = 'PGP Secret Keyring_1'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\x3a\x56\x45\x52\x53\x49\x4f\x4e' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x3a\x56\x45\x52\x53\x49\x4f\x4e'
        filesig.f2_extension = 'SLE'
        filesig.f3_description = 'Surfplan Kite Project File'
        sig_list.append(filesig)
    #
    if bytesData[0:3] == b'\x41\x43\x76' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x41\x43\x76'
        filesig.f2_extension = 'SLE'
        filesig.f3_description = 'Steganos Virtual Secure Drive'
        sig_list.append(filesig)
    #
    if bytesData[0:16] == b'\x4d\x69\x63\x72\x6f\x73\x6f\x66\x74\x20\x56\x69\x73\x75\x61\x6c' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x4d\x69\x63\x72\x6f\x73\x6f\x66\x74\x20\x56\x69\x73\x75\x61\x6c'
        filesig.f2_extension = 'SLN'
        filesig.f3_description = 'Visual Studio .NET File'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\x00\x1e\x84\x90\x00\x00\x00\x00' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x00\x1e\x84\x90\x00\x00\x00\x00'
        filesig.f2_extension = 'SNM'
        filesig.f3_description = 'Netscape Communicator (v4) Mail Folder'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x4d\x53\x43\x46' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x4d\x53\x43\x46'
        filesig.f2_extension = 'SNP'
        filesig.f3_description = 'MS Access Snapshot Viewer File'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1' :
        filesig = FileSignature()
        filesig.f1_signature = b'\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1'
        filesig.f2_extension = 'SOU'
        filesig.f3_description = 'Visual Studio Solution User Options File'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x00\x00\x01\x00' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x00\x00\x01\x00'
        filesig.f2_extension = 'SPL'
        filesig.f3_description = 'Windows Icon / Printer Spool File'
        sig_list.append(filesig)
    #
    if bytesData[0:8] ==  b'\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1' :
        filesig = FileSignature()
        filesig.f1_signature = b'\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1'
        filesig.f2_extension = 'SPO'
        filesig.f3_description = 'SPSS Output File'
        sig_list.append(filesig)
    #
    if bytesData[0:7] == b'\x52\x45\x47\x45\x44\x49\x54' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x52\x45\x47\x45\x44\x49\x54'
        filesig.f2_extension = 'SUD'
        filesig.f3_description = 'WinNT Registry/Registry Undo Files'
        sig_list.append(filesig)
    #
    if bytesData[0:5] == b'\xfd\xff\xff\xff\x04' :
        filesig = FileSignature()
        filesig.f1_signature = b'\xfd\xff\xff\xff\x04'
        filesig.f2_extension = 'SUO'
        filesig.f3_description = 'Visual Studio Solution Subheader'
        sig_list.append(filesig)
    #
    if bytesData[0:3] == b'\x46\x57\x53' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x46\x57\x53'
        filesig.f2_extension = 'SWF'
        filesig.f3_description = 'Shockwave Flash Player'
        sig_list.append(filesig)
    #
    if bytesData[0:3] == b'\x43\x57\x53' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x43\x57\x53'
        filesig.f2_extension = 'SWF'
        filesig.f3_description = 'Shockwave Flash File'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x50\x4b\x03\x04' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x50\x4b\x03\x04'
        filesig.f2_extension = 'SXC/SXD/SXI/SXW'
        filesig.f3_description = 'StarOffice Spreadsheet/OpenOffice Documents'
        sig_list.append(filesig)
    #
    if bytesData[0:1] == b'\xff' :
        filesig = FileSignature()
        filesig.f1_signature = b'\xff'
        filesig.f2_extension = 'SYS'
        filesig.f3_description = 'Windows Executable'
        sig_list.append(filesig)
    #
    if bytesData[0:1] == b'\xeb' :
        filesig = FileSignature()
        filesig.f1_signature = b'\xeb'
        filesig.f2_extension = 'SYS'
        filesig.f3_description = 'Windows Executable file_3'
        sig_list.append(filesig)
    #
    if bytesData[0:1] == b'\xe9' :
        filesig = FileSignature()
        filesig.f1_signature = b'\xe9'
        filesig.f2_extension = 'SYS'
        filesig.f3_description = 'Windows Executable file_2'
        sig_list.append(filesig)
    #
    if bytesData[0:1] == b'\xe8' :
        filesig = FileSignature()
        filesig.f1_signature = b'\xe8'
        filesig.f2_extension = 'SYS'
        filesig.f3_description = 'Windows Executable File_1'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\xff\x4b\x45\x59\x42\x20\x20\x20' :
        filesig = FileSignature()
        filesig.f1_signature =  b'\xff\x4b\x45\x59\x42\x20\x20\x20'
        filesig.f2_extension = 'SYS'
        filesig.f3_description = 'Keyboard Driver File'
        sig_list.append(filesig)
    #
    if bytesData[0:2] == b'\x4d\x5a' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x4d\x5a'
        filesig.f2_extension = 'SYS'
        filesig.f3_description = 'Windows/DOS Executable File'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\xff\xff\xff\xff' :
        filesig = FileSignature()
        filesig.f1_signature = b'\xff\xff\xff\xff'
        filesig.f2_extension = 'SYS'
        filesig.f3_description = 'DOS System Driver'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x41\x4d\x59\x4f' :
        filesig = FileSignature()
        filesig.f1_signature =  b'\x41\x4d\x59\x4f'
        filesig.f2_extension = 'SYW'
        filesig.f3_description = 'Harvard Graphics Symbol Graphic'
        sig_list.append(filesig)
    #
    if bytesData[0:5] == b'\x75\x73\x74\x61\x72' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x75\x73\x74\x61\x72'
        filesig.f2_extension = 'TAR'
        filesig.f3_description = 'Tape Archive'
        sig_list.append(filesig)
    #
    if bytesData[0:3] == b'\x42\x5a\x68' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x42\x5a\x68'
        filesig.f2_extension = 'TAR.BZ2'
        filesig.f3_description = 'bzip2 Compressed Archive'
        sig_list.append(filesig)
    #
    if bytesData[0:2] == b'\x1f\xa0' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x1f\xa0'
        filesig.f2_extension = 'TAR.Z'
        filesig.f3_description = 'Compressed Tape Archive_2'
        sig_list.append(filesig)
    #
    if bytesData[0:3] == b'\x1f\x9d\x90' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x1f\x9d\x90'
        filesig.f2_extension = 'TAR.Z'
        filesig.f3_description = 'Compressed Tape Archive_1'
        sig_list.append(filesig)
    #
    if bytesData[0:3] == b'\x42\x5a\x68' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x42\x5a\x68'
        filesig.f2_extension = 'TB2/TBZ2'
        filesig.f3_description = 'bzip2 Compressed Archive'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\xb4\x6e\x68\x44' :
        filesig = FileSignature()
        filesig.f1_signature = b'\xb4\x6e\x68\x44'
        filesig.f2_extension = 'TIB'
        filesig.f3_description = 'Acronis True Image'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x4d\x4d\x00\x2a':
        filesig = FileSignature()
        filesig.f1_signature = b'\x4d\x4d\x00\x2a'
        filesig.f2_extension = 'TIF'
        filesig.f3_description = 'TIFF File_3'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x49\x49\x2a\x00' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x49\x49\x2a\x00'
        filesig.f2_extension = 'TIF'
        filesig.f3_description  = 'TIFF File_2'
        sig_list.append(filesig)
    #
    if bytesData[0:3] == b'\x49\x20\x49' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x49\x20\x49'
        filesig.f2_extension = 'TIF'
        filesig.f3_description = 'TIFF File_1'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x4d\x4d\x00\x2b' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x4d\x4d\x00\x2b'
        filesig.f2_extension = 'TIF'
        filesig.f3_description = 'TIFF File_4'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x49\x49\x2a\x00' :
        filesig = FileSignature()
        filesig.f1_signature =  b'\x49\x49\x2a\x00'
        filesig.f2_extension = 'TIFF'
        filesig.f3_description = 'TIFF File_2'
        sig_list.append(filesig)
    #
    if bytesData[0:3] == b'\x49\x20\x49' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x49\x20\x49'
        filesig.f2_extension = 'TIFF'
        filesig.f3_description = 'TIFF File_1'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x4d\x4d\x00\x2b':
        filesig = FileSignature()
        filesig.f1_signature = b'\x4d\x4d\x00\x2b'
        filesig.f2_extension = 'TIFF'
        filesig.f3_description = 'TIFF File_4'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x4d\x4d\x00\x2a' :
        filesig = FileSignature()
        filesig.f1_signature =  b'\x4d\x4d\x00\x2a'
        filesig.f2_extension = 'TIFF'
        filesig.f3_description = 'TIFF File_3'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\x4d\x53\x46\x54\x02\x00\x01\x00':
        filesig = FileSignature()
        filesig.f1_signature = b'\x4d\x53\x46\x54\x02\x00\x01\x00'
        filesig.f2_extension = 'TLB'
        filesig.f3_description = 'OLE/SPSS/Visual C++ library File'
        sig_list.append(filesig)
    #
    if bytesData[0:2] == b'\x01\x10' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x01\x10'
        filesig.f2_extension = 'TR1'
        filesig.f3_description = 'Novell LANalyzer Capture File'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x55\x43\x45\x58' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x55\x43\x45\x58'
        filesig.f2_extension = 'UCE'
        filesig.f3_description = 'Unicode Extensions'
        sig_list.append(filesig)
    #
    if bytesData[0:6] == b'\x55\x46\x41\xc6\xd2\xc1' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x55\x46\x41\xc6\xd2\xc1'
        filesig.f2_extension = 'UFA'
        filesig.f3_description = 'UFA Compressed Archive'
        sig_list.append(filesig)
    #
    if bytesData[0:2] == b'\x4d\x5a' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x4d\x5a'
        filesig.f2_extension = 'VBX'
        filesig.f3_description = 'VisualBASIC Application'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\x45\x4e\x54\x52\x59\x56\x43\x44' :
        filesig = FileSignature()
        filesig.f1_signature =  b'\x45\x4e\x54\x52\x59\x56\x43\x44'
        filesig.f2_extension = 'VCD'
        filesig.f3_description = 'VideoVCD/VCDImager File'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\x42\x45\x47\x49\x4e\x3a\x56\x43' :
        filesig = FileSignature()
        filesig.f1_signature =  b'\x42\x45\x47\x49\x4e\x3a\x56\x43'
        filesig.f2_extension = 'VCF'
        filesig.f3_description = 'vCard'
        sig_list.append(filesig)
    #
    if bytesData[0:5] == b'\x5b\x4d\x53\x56\x43' :
        filesig = FileSignature()
        filesig.f1_signature =  b'\x5b\x4d\x53\x56\x43'
        filesig.f2_extension = 'VCW'
        filesig.f3_description = 'Visual C++ Workbench Info File'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\x63\x6f\x6e\x65\x63\x74\x69\x78' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x63\x6f\x6e\x65\x63\x74\x69\x78'
        filesig.f2_extension = 'VHD'
        filesig.f3_description = 'Virtual PC HD Image'
        sig_list.append(filesig)
    #
    if bytesData[0:3] == b'\x4b\x44\x4d' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x4b\x44\x4d'
        filesig.f2_extension = 'VMDK'
        filesig.f3_description = 'VMware 4 Virtual Disk'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\x23\x20\x44\x69\x73\x6b\x20\x44' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x23\x20\x44\x69\x73\x6b\x20\x44'
        filesig.f2_extension = 'VMDK'
        filesig.f3_description = 'VMware 4 Virtual Disk Description'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == '\x43\x4f\x57\x44' :
        filesig = FileSignature()
        filesig.f1_signature = '\x43\x4f\x57\x44'
        filesig.f2_extension = 'VMDK'
        filesig.f3_description = 'VMware 3 Virtual Disk'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x00\x00\x01\xba' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x00\x00\x01\xba'
        filesig.f2_extension = 'VOB'
        filesig.f3_description = 'DVD Video File'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1' :
        filesig = FileSignature()
        filesig.f1_signature = b'\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1'
        filesig.f2_extension = 'VSD'
        filesig.f3_description = 'Visio File'
        sig_list.append(filesig)
    #
    if bytesData[0:2] == b'\x4d\x5a' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x4d\x5a'
        filesig.f2_extension = 'VXD'
        filesig.f3_description = 'Windows Virtual Device Drivers'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\x81\x32\x84\xc1\x85\x05\xd0\x11' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x81\x32\x84\xc1\x85\x05\xd0\x11'
        filesig.f2_extension = 'WAB'
        filesig.f3_description = 'Outlook Express Address Book (Win95)'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\x9c\xcb\xcb\x8d\x13\x75\xd2\x11' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x9c\xcb\xcb\x8d\x13\x75\xd2\x11'
        filesig.f2_extension = 'WAB'
        filesig.f3_description = 'Outlook Address File'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x52\x49\x46\x46' :
        filesig = FileSignature()
        filesig.f1_signature =  b'\x52\x49\x46\x46'
        filesig.f2_extension = 'WAV'
        filesig.f3_description = 'Resource Interchange File Format'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x00\x00\x02\x00' :
        filesig = FileSignature()
        filesig.f1_signature =  b'\x00\x00\x02\x00'
        filesig.f2_extension = 'WB2'
        filesig.f3_description = 'QuattroPro Spreadsheet'
        sig_list.append(filesig)
    #
    if bytesData[0:9] == b'\x3e\x00\x03\x00\xfe\xff\x09\x00\x06' :
        filesig = FileSignature()
        filesig.f1_signature =  b'\x3e\x00\x03\x00\xfe\xff\x09\x00\x06'
        filesig.f2_extension = 'WB3'
        filesig.f3_description = 'Quatro Pro For Windows 7.0'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1' :
        filesig = FileSignature()
        filesig.f1_signature = b'\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1'
        filesig.f2_extension = 'WIZ'
        filesig.f3_description = 'Microsoft Office Document'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\x00\x00\x02\x00\x06\x04\x06\x00' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x00\x00\x02\x00\x06\x04\x06\x00'
        filesig.f2_extension = 'WK1'
        filesig.f3_description = 'Lotus 1-2-3 (v1)'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\x00\x00\x1a\x00\x00\x10\x04\x00' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x00\x00\x1a\x00\x00\x10\x04\x00'
        filesig.f2_extension = 'WK3'
        filesig.f3_description = 'Lotus 1-2-3 (v3)'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\x00\x00\x1a\x00\x02\x10\x04\x00' :
        filesig = FileSignature()
        filesig.f1_signature =  b'\x00\x00\x1a\x00\x02\x10\x04\x00'
        filesig.f2_extension = 'WK4/WK5'
        filesig.f3_description = 'Lotus 1-2-3 (v4/v5)'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x0e\x57\x4b\x53' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x0e\x57\x4b\x53'
        filesig.f2_extension  = 'WKS'
        filesig.f3_description = 'DeskMate Worksheet'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\xff\x00\x02\x00\x04\x04\x05\x54' :
        filesig = FileSignature()
        filesig.f1_signature = b'\xff\x00\x02\x00\x04\x04\x05\x54'
        filesig.f2_extension = 'WKS'
        filesig.f3_description = 'Works For Windows Spreadsheet'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\x30\x26\xb2\x75\x8e\x66\xcf\x11' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x30\x26\xb2\x75\x8e\x66\xcf\x11'
        filesig.f2_extension = 'WMA'
        filesig.f3_description = 'Windows Media Audio/Video File'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\xd7\xcd\xc6\x9a' :
        filesig = FileSignature()
        filesig.f1_signature = b'\xd7\xcd\xc6\x9a'
        filesig.f2_extension = 'WMF'
        filesig.f3_description = 'Windows Graphics Metafile'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\x30\x26\xb2\x75\x8e\x66\xcf\x11' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x30\x26\xb2\x75\x8e\x66\xcf\x11'
        filesig.f2_extension = 'WMV'
        filesig.f3_description = 'Windows Media Audio/Video File'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x50\x4b\x03\x04' :
        filesig = FileSignature()
        filesig.f1_signature =  b'\x50\x4b\x03\x04'
        filesig.f2_extension = 'WMZ'
        filesig.f3_description = 'Windows Media Compressed Skin File'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\xff\x57\x50\x43' :
        filesig = FileSignature()
        filesig.f1_signature = b'\xff\x57\x50\x43'
        filesig.f2_extension = 'WP/WP5/WP6/WPD/WPP/WPG'
        filesig.f3_description = 'WordPerfect Text and Graphics'
        sig_list.append(filesig)
    #
    if bytesData[0:3] == b'\x81\xcd\xab' :
        filesig = FileSignature()
        filesig.f1_signature =  b'\x81\xcd\xab'
        filesig.f2_extension = 'WPF'
        filesig.f3_description = 'WordPerfect Text'
        sig_list.append(filesig)
    #
    if bytesData[0:34] == b'\x4d\x69\x63\x72\x6f\x73\x6f\x66\x74\x20\x57' \
                            b'\x69\x6e\x64\x6f\x77\x73\x20\x4d\x65\x64\x69' \
                            b'\x61\x20\x50\x6c\x61\x79\x65\x72\x20\x2d\x2d\x20'  :
        filesig = FileSignature()
        filesig.f1_signature = b'\x4d\x69\x63\x72\x6f\x73\x6f\x66\x74\x20\x57' \
                            b'\x69\x6e\x64\x6f\x77\x73\x20\x4d\x65\x64\x69' \
                            b'\x61\x20\x50\x6c\x61\x79\x65\x72\x20\x2d\x2d\x20'
        filesig.f2_extension = 'WPL'
        filesig.f3_description = 'Windows Media Player Playlist'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1' :
        filesig = FileSignature()
        filesig.f1_signature = b'\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1'
        filesig.f2_extension = 'WPS'
        filesig.f3_description = 'MSWorks Text Document'
        sig_list.append(filesig)
    #
    if bytesData[0:5] == b'\xbe\x00\x00\x00\xab' :
        filesig = FileSignature()
        filesig.f1_signature = b'\xbe\x00\x00\x00\xab'
        filesig.f2_extension = 'WRI'
        filesig.f3_description = 'MS Write File_3'
        sig_list.append(filesig)
    #
    if bytesData[0:2] == b'\x32\xbe':
        filesig = FileSignature()
        filesig.f1_signature = b'\x32\xbe'
        filesig.f2_extension = 'WRI'
        filesig.f3_description = 'MS Write File_2'
        sig_list.append(filesig)
    #
    if bytesData[0:2] == b'\x31\xbe' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x31\xbe'
        filesig.f2_extension = 'WRI'
        filesig.f3_description = 'MS Write File_1'
        sig_list.append(filesig)
    #
    if bytesData[0:2] == b'\x1d\x7d' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x1d\x7d'
        filesig.f2_extension = 'WS'
        filesig.f3_description = 'WordStar Version 5.0/6.0 Document'
        sig_list.append(filesig)
    #
    if bytesData[0:6] == b'\x57\x53\x32\x30\x30\x30' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x57\x53\x32\x30\x30\x30'
        filesig.f2_extension = 'WS2'
        filesig.f3_description = 'WordStar For Windows File'
        sig_list.append(filesig)
    #
    if bytesData[0:1] == b'\x3c':
        filesig = FileSignature()
        filesig.f1_signature = b'\x3c'
        filesig.f2_extension = 'XDR'
        filesig.f3_description = 'BizTalk XML-Data Reduced Schema'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1' :
        filesig = FileSignature()
        filesig.f1_signature = b'\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1'
        filesig.f2_extension = 'XLA'
        filesig.f3_description = 'Microsoft Office Document'
        sig_list.append(filesig)
    #
    if bytesData[0:5] == b'\xfd\xff\xff\xff\x10' :
        filesig = FileSignature()
        filesig.f1_signature = b'\xfd\xff\xff\xff\x10'
        filesig.f2_extension = 'XLS'
        filesig.f3_description  ='Excel Spreadsheet Subheader_2'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\x09\x08\x10\x00\x00\x06\x05\x00' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x09\x08\x10\x00\x00\x06\x05\x00'
        filesig.f2_extension = 'XLS'
        filesig.f3_description = 'Excel Spreadsheet Subheader_1'
        sig_list.append(filesig)
    #
    if bytesData[0:5] == b'\xfd\xff\xff\xff\x29' :
        filesig = FileSignature()
        filesig.f1_signature = b'\xfd\xff\xff\xff\x29'
        filesig.f2_extension = 'XLS'
        filesig.f3_description = 'Excel Spreadsheet Subheader_7'
        sig_list.append(filesig)
    #
    if bytesData[0:5] == b'\xfd\xff\xff\xff\x28' :
        filesig = FileSignature()
        filesig.f1_signature = b'\xfd\xff\xff\xff\x28'
        filesig.f2_extension = 'XLS'
        filesig.f3_description = 'Excel Spreadsheet Subheader_6'
        sig_list.append(filesig)
    #
    if bytesData[0:5] == b'\xfd\xff\xff\xff\x23' :
        filesig = FileSignature()
        filesig.f1_signature = b'\xfd\xff\xff\xff\x23'
        filesig.f2_extension = 'XLS'
        filesig.f3_description = 'Excel Spreadsheet Subheader_5'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1' :
        filesig = FileSignature()
        filesig.f1_signature = b'\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1'
        filesig.f2_extension = 'XLS'
        filesig.f3_description = 'Microsoft Office Document'
        sig_list.append(filesig)
    #
    if bytesData[0:5] == b'\xfd\xff\xff\xff\x22' :
        filesig = FileSignature()
        filesig.f1_signature = b'\xfd\xff\xff\xff\x22'
        filesig.f2_extension = 'XLS'
        filesig.f3_description = 'Excel Spreadsheet Subheader_4'
        sig_list.append(filesig)
    #
    if bytesData[0:5] == b'\xfd\xff\xff\xff\x1f' :
        filesig = FileSignature()
        filesig.f1_signature = b'\xfd\xff\xff\xff\x1f'
        filesig.f2_extension = 'XLS'
        filesig.f3_description = 'Excel Spreadsheet Subheader_3'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x50\x4b\x03\x04' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x50\x4b\x03\x04'
        filesig.f2_extension = 'XLSX'
        filesig.f3_description = 'MS Office Open XML Format Document'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\x50\x4b\x03\x04\x14\x00\x06\x00' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x50\x4b\x03\x04\x14\x00\x06\x00'
        filesig.f2_extension = 'XLSX'
        filesig.f3_description = 'MS Office 2007 Documents'
        sig_list.append(filesig)
    #
    if bytesData[0:21] == b'\x3c\x3f\x78\x6d\x6c\x20\x76\65\x72\x73\x69' \
                            b'\x6f\x6e\x3d\x22\x31\x2e\x30\x22\x3f\x3e' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x3c\x3f\x78\x6d\x6c\x20\x76\65\x72\x73\x69' \
                            b'\x6f\x6e\x3d\x22\x31\x2e\x30\x22\x3f\x3e'
        filesig.f2_extension = 'XML'
        filesig.f3_description = 'User Interface Language'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x50\x4b\x03\x04' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x50\x4b\x03\x04'
        filesig.f2_extension = 'XPI\XPS\XPT'
        filesig.f3_description = 'Mozilla Browser Archive/XML Paper Specification File/eXact Packager Models'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\x58\x50\x43\x4f\x4d\x0a\x54\x79' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x58\x50\x43\x4f\x4d\x0a\x54\x79'
        filesig.f2_extension = 'XPT'
        filesig.f3_description = 'XPCOM Libraries'
        sig_list.append(filesig)
    #
    if bytesData[0:14] == b'\x4d\x5a\x90\x00\x03\x00\x00\x00\x04\x00\x00\x00\xff\xff' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x4d\x5a\x90\x00\x03\x00\x00\x00\x04\x00\x00\x00\xff\xff'
        filesig.f2_extension = 'ZAP'
        filesig.f3_description = 'ZoneAlam Data File'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\x50\x4b\x03\x04\x14\x00\x01\x00' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x50\x4b\x03\x04\x14\x00\x01\x00'
        filesig.f2_extension = 'ZIP'
        filesig.f3_description = 'ZLock Pro Encrypted ZIP'
        sig_list.append(filesig)
    #
    if bytesData[0:8] == b'\x50\x4b\x03\x04\x14\x00\x01\x00' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x50\x4b\x03\x04\x14\x00\x01\x00'
        filesig.f2_extension = 'ZIP'
        filesig.f3_description = 'ZLock Pro Encrypted ZIP'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x50\x4b\x07\x08' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x50\x4b\x07\x08'
        filesig.f2_extension = 'ZIP'
        filesig.f3_description = 'PKZIP Archive_3'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x50\x4b\x05\x06' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x50\x4b\x05\x06'
        filesig.f2_extension = 'ZIP'
        filesig.f3_description = 'PKZIP Archive_2'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x50\x4b\x03\x04' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x50\x4b\x03\x04'
        filesig.f2_extension = 'ZIP'
        filesig.f3_description = 'PKZIP Archive_1'
        sig_list.append(filesig)
    #
    if bytesData[0:5] == b'\x50\x4b\x53\x70\x58' :
        filesig = FileSignature()
        filesig.f1_signature =  b'\x50\x4b\x53\x70\x58'
        filesig.f2_extension = 'ZIP'
        filesig.f3_description = 'PKSFX Self-Extracting Archive'
        sig_list.append(filesig)
    #
    if bytesData[0:6] == b'\x50\x4b\x4c\x49\x54\x45' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x50\x4b\x4c\x49\x54\x45'
        filesig.f2_extension = 'ZIP'
        filesig.f3_description = 'PKLITE Archive'
        sig_list.append(filesig)
    #
    if bytesData[0:6] == b'\x57\x69\x6e\x5a\x69\x70' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x57\x69\x6e\x5a\x69\x70'
        filesig.f2_extension = 'ZIP'
        filesig.f3_description = 'WinZip Compressed Archive'
        sig_list.append(filesig)
    #
    if bytesData[0:4] == b'\x5a\x4f\x4f\x20' :
        filesig = FileSignature()
        filesig.f1_signature = b'\x5a\x4f\x4f\x20'
        filesig.f2_extension = 'ZOO'
        filesig.f3_description = 'ZOO Compressed Archive'
        sig_list.append(filesig)
    #
    #
    #

    sort_sig_list = sorted(sig_list, key=lambda x:len(x.f1_signature), reverse=True)
    return sort_sig_list
