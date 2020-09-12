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
#
#
#
from  lib.hexlib.ReadBinaryFile import readBytes as rfile
from  lib.pdf.pdfdata.PdfHeaderData import PdfHeaderData as header
from  lib.pdf.pdfdata.PdfObjData import PdfObjData as obj
from  lib.pdf.pdfdata.PdfStreamData import PdfStreamData as stream


#
class PdfFile:
    #
    def __init__(self, filename:str):
        self.p1_filename    = filename
        self.p2_pdf_bytes   = b''
        self.p3_header      = header()
        self.p4_objs        = []
        self.p5_streams     = []
        self.p6_xrefs       = []
        self.p7_trailers    = []
        self.p8_startxrefs  = []
        self.p9_eofs        = []
        self.c1_checkNormal = True
        self.c2_error       = ''


    # Process -> Class değişkenlerini atar
    def process(self):
        print()
        print('\tFile name : {}'.format(self.p1_filename)  )
        print()
        print("\t1) Dosya yükleniyor !...")
        self.p2_pdf_bytes = self.fileImport()
        print("\t1) Dosya yüklendi.")
        if self.c1_checkNormal :
            # 2) pdf header
            print("\t2) Pdf <<header>> işleniyor !... ")
            self.findPdfHeader()
            print("\t2) Pdf <<header>> işlendi. ")
            # 3) pdf objs
            print("\t3) Pdf <<obj-endobj>> işleniyor !...")
            self.findPdfObjs()
            print("\t3) Pdf <<obj-endobj>> işlendi. {} adet bulundu.".format( len(self.p4_objs) ) )
            # 4) pdf streams
            print("\t4) Pdf <<stream-endstream>> işleniyor !...")
            self.findPdfStreams()
            print("\t4) Pdf <<stream-endstream>> işlendi. {} adet bulundu.".format( len(self.p5_streams) ))
            # 5) pdf Xrefs
            print("\t5) Pdf <<xref>> işleniyor !...")
            self.findPdfXrefs()
            print("\t5) Pdf <<xref>> işlendi. {} adet bulundu.".format(len(self.p6_xrefs)) )
            # 6) pdf Trailers
            print("\t6) Pdf <<trailer>> işleniyor !...")
            self.findPdfTrailers()
            print("\t6) Pdf <<trailer>> işlendi. {} adet bulundu.".format(len(self.p7_trailers)) )
            # 7) pdf StartXrefs
            print("\t7) Pdf <<startxref>> işleniyor !...")
            self.findPdfStartXrefs()
            print("\t7) Pdf <<startxref>> işlendi. {} adet bulundu.".format(len(self.p8_startxrefs)))
            # 8) pdf %%EOF
            print("\t8) Pdf <<%%EOF>> işleniyor !...")
            self.findPdfEOFs()
            print("\t8) Pdf <<%%EOF>> işlendi. {} adet bulundu.".format(len(self.p9_eofs)))
            print("\t9) Pdf <<obj-stream>> kontrolleri yapılıyor !...")
            self.findChildRoot()
            print("\t9) Pdf <<obj-stream>> kontrolleri yapıldı.")
        else:
            print( '\tHata Meydana Geldi! (Error Occurred!)' )
            print( "\t<<{}>>".format(self.c2_error) )


    # Karakter kontrol
    def checkByte(self, char:bytes ) -> bool:
        if char == b'\r' or char == b'\n' or char == b'\x20' :
            return  True
        else:
            return  False

    # Pdf Bytes import
    def fileImport(self) -> bytes:
        try:
            result = rfile(filename=self.p1_filename)
            if result[0:4] == b'%PDF':
                return result
            else:
                self.c1_checkNormal = False
                self.c2_error = 'PDF dosyası değil. (Not a pdf file)'
        except:
            self.c1_checkNormal = False
            self.c2_error = "Dosya bulunamadı. (File not found)"
        return b''

    # Find Pdf Header
    def findPdfHeader(self):
        #
        self.p3_header.i1_out_start = 0
        self.p3_header.b1_marker = b'%'
        self.p3_header.b2_tag = self.p2_pdf_bytes[1:8]

        checkheader = self.p2_pdf_bytes[0:30]
        tmp_percent = checkheader[1:].find(b'%')
        #
        if tmp_percent > -1:
            second_percent = tmp_percent + 1
            ii_end = second_percent + 5
            self.p3_header.b5_tag = self.p2_pdf_bytes[second_percent + 1:ii_end]
            self.p3_header.b4_marker = b'%'
            self.p3_header.b3_split = self.p2_pdf_bytes[8:second_percent]
            for jj in range(ii_end, ii_end + 4):
                if self.checkByte(char=self.p2_pdf_bytes[jj:jj + 1]):
                    continue
                else:
                    self.p3_header.i1_out_end = jj
                    break
            self.p3_header.b6_split = self.p2_pdf_bytes[ii_end:self.p3_header.i1_out_end]
        else:
            self.p3_header.b4_marker = b''
            self.p3_header.b5_tag = b''
            self.p3_header.b6_split = b''
            ii_end = 8
            for jj in range(ii_end, ii_end + 4):
                if self.checkByte(char=self.p2_pdf_bytes[jj:jj + 1]):
                    continue
                else:
                    self.p3_header.i1_out_end = jj
                    break
            self.p3_header.b3_split = self.p2_pdf_bytes[ii_end:self.p3_header.i1_out_end]
        #

    # Find Pdf Obj
    def findPdfObjs(self):
        counter = 0
        ii_index = 0
        #
        while True:
            find_relative_index = self.p2_pdf_bytes[ii_index:].find(b'obj')
            if find_relative_index != -1:
                find_index = find_relative_index + ii_index
                char1 = self.p2_pdf_bytes[find_index-1:find_index]
                if char1 == b' ':
                    char2 = self.p2_pdf_bytes[find_index-2:find_index-1]
                    if char2.isdigit():
                        char3 = self.p2_pdf_bytes[find_index-3:find_index-2]
                        if char3 == b' ':
                            turn_index = find_index-4
                            chars4 = b''
                            start_obj= -1
                            for jj in  range(turn_index,turn_index-9, -1):
                                if self.p2_pdf_bytes[jj:jj+1].isdigit():
                                    continue
                                else:
                                    chars4 = self.p2_pdf_bytes[jj+1:find_index-3]
                                    start_obj = jj+1
                                    break
                            #
                            tmp_obj = obj()
                            tmp_obj.i0_no = counter
                            counter += 1
                            #
                            tmp_obj.i1_out_start = start_obj
                            tmp_obj.i4_obj_first_no  =  int(chars4.decode(encoding='ascii',errors='strict') )
                            tmp_obj.i5_obj_second_no =  int(char2.decode(encoding='ascii', errors='strict') )
                            del_relative_index1 = self.p2_pdf_bytes[find_index:].find(b' obj')
                            del_relative_index2 = self.p2_pdf_bytes[find_index:].find(b'endobj')
                            if del_relative_index2 != -1:
                                if (del_relative_index1 == -1 or del_relative_index2 < del_relative_index1) and del_relative_index2 != -1:
                                    tmp_obj.i1_out_end = find_index + del_relative_index2 + 6
                                    ii_index = tmp_obj.i1_out_end
                                    tmp_obj.i0_check = True
                                else:
                                    tmp_obj.i0_check = False
                                    tmp_obj.i1_out_end = find_index + 3
                                    ii_index = tmp_obj.i1_out_end
                            else:
                                tmp_obj.i0_check = False
                                tmp_obj.i1_out_end = find_index + 3
                                ii_index = tmp_obj.i1_out_end
                            #
                            if tmp_obj.i0_check == True:
                                for jj in range(1,4):
                                    start_jj = (find_index+2)+jj
                                    if self.checkByte(self.p2_pdf_bytes[start_jj:start_jj+1]):
                                        continue
                                    else:
                                        tmp_obj.i2_inner_start = start_jj
                                        break
                                for ll in range(-1,-4,-1):
                                    start_ll = (tmp_obj.i1_out_end-6)+ll
                                    if self.checkByte(self.p2_pdf_bytes[start_ll:start_ll+1]):
                                        continue
                                    else:
                                        tmp_obj.i2_inner_end = start_ll+1
                                        break
                                #
                                if tmp_obj.i2_inner_start == -1:
                                    tmp_obj.i2_inner_start = find_index+3
                                if tmp_obj.i2_inner_end == -1:
                                    tmp_obj.i2_inner_end = tmp_obj.i1_out_end - 6
                            #
                            self.p4_objs.append(tmp_obj)
                            #
                        else:
                            ii_index += 3
                    else:
                        ii_index += 3
                else:
                    ii_index += 3
            else:
                break


    # Find Pdf Streams
    def findPdfStreams(self):
        counter = 0
        ii_index = 0
        #
        while True:
            find_relative_index = self.p2_pdf_bytes[ii_index:].find(b'stream')
            if find_relative_index != -1:
                find_index = find_relative_index + ii_index
                if  self.p2_pdf_bytes[find_index-1:find_index] != b'd' :
                    #
                    tmp_stream = stream()
                    tmp_stream.i0_no = counter
                    counter += 1
                    tmp_stream.i1_out_start = find_index
                    #
                    find2_relative_index = self.p2_pdf_bytes[find_index+6:].find(b'endstream')
                    if find2_relative_index != -1:
                        find2_index = find2_relative_index + (find_index+6)
                        tmp_stream.i1_out_end = find2_index + 9
                        #
                        for pp in range(1,4):
                            ii_start = tmp_stream.i1_out_start + 5 + pp
                            char_pp = self.p2_pdf_bytes[ii_start:ii_start+1]
                            if self.checkByte(char=char_pp):
                                continue
                            else:
                                tmp_stream.i2_inner_start = ii_start
                                break
                        for rr in  range(-1,-4, -1):
                            rr_start = find2_index + rr
                            char_rr = self.p2_pdf_bytes[rr_start:rr_start+1]
                            if self.checkByte(char=char_rr):
                                continue
                            else:
                                tmp_stream.i2_inner_end = rr_start+1
                                break
                        if tmp_stream.i2_inner_start == -1:
                            tmp_stream.i2_inner_start = tmp_stream.i1_out_start + 6
                        if tmp_stream.i2_inner_end == -1:
                            tmp_stream.i2_inner_end = tmp_stream.i1_out_end - 9
                        #
                    else:
                        tmp_stream.i1_out_end = tmp_stream.i1_out_start + 6
                        tmp_stream.i2_inner_start = tmp_stream.i1_out_end
                        tmp_stream.i2_inner_end = tmp_stream.i1_out_end
                        tmp_stream.i0_check = False
                    #
                    self.p5_streams.append(tmp_stream)
                    ii_index = tmp_stream.i1_out_end
                    #
                else:
                    ii_index = find_index + 6
            else:
                break
    #
    def findPdfXrefs(self):
        ii_index = 0
        #
        while True:
            ii = self.p2_pdf_bytes[ii_index:].find(b'xref')
            if ii != -1:
                jj = ii + ii_index
                if self.checkByte(self.p2_pdf_bytes[jj-1:jj]):
                    self.p6_xrefs.append(jj)
                ii_index = jj + 4
            else:
                break
    #
    def findPdfTrailers(self):
        ii_index = 0
        #
        while True:
            ii = self.p2_pdf_bytes[ii_index:].find(b'trailer')
            if ii != -1:
                jj = ii + ii_index
                self.p7_trailers.append(jj)
                ii_index = jj + 4
            else:
                break
    #
    def findPdfStartXrefs(self):
        ii_index = 0
        #
        while True:
            ii = self.p2_pdf_bytes[ii_index:].find(b'startxref')
            if ii != -1:
                jj = ii + ii_index
                self.p8_startxrefs.append(jj)
                ii_index = jj + 4
            else:
                break

    #
    def findPdfEOFs(self):
        ii_index = 0
        #
        while True:
            ii = self.p2_pdf_bytes[ii_index:].find(b'%%EOF')
            if ii != -1:
                jj = ii + ii_index
                self.p9_eofs.append(jj)
                ii_index = jj + 4
            else:
                break

    #
    def findChildRoot(self):
        count_stream = len( self.p5_streams )
        index_stream  = 0
        if count_stream > 0:
            for ii_obj in  self.p4_objs:
                tmp_stream = self.p5_streams[index_stream]
                if ii_obj.i1_out_end < tmp_stream.i1_out_start:
                    continue
                elif ii_obj.i1_out_start < tmp_stream.i1_out_start < ii_obj.i1_out_end :
                    ii_obj.i3_stream_no = tmp_stream.i0_no
                    tmp_stream.i3_obj_no = ii_obj.i0_no
                    index_stream += 1
                    if index_stream < count_stream:
                        continue
                    else:
                        break
                else:
                    break
    #
    def objNo(self, index:int) -> obj:
        return self.p4_objs[index]
    #
    def streamNo(self, index:int) -> stream:
        return self.p5_streams[index]
    #
    def objFirstNo(self, index:int) -> obj:
        for tmp_obj in self.p4_objs:
            if tmp_obj.i4_obj_first_no == index:
                return tmp_obj
        return obj()
    #
    def show(self):
        print()
        print( '\tFile Name : ' + self.p1_filename )
        print( '\tFile Size : ' + str(len(self.p2_pdf_bytes)) + ' bayts' )
        print()
        print( '\tPdf Header (1. Marker)     : '  + self.p3_header.b1_marker.decode( encoding='ascii', errors='strict' )  )
        print( '\tPdf Header (Version)       : '  + self.p3_header.b2_tag.decode( encoding='ascii', errors='strict'    )  )
        print( '\tPdf Header (1. Split) Hex  : "' + self.p3_header.b3_split.hex(' ') + '"'  )
        print( '\tPdf Header (2. Marker)     : '  + self.p3_header.b4_marker.decode( encoding='ascii', errors='strict') )
        print( '\tPdf Header (Signature) Hex : "' + self.p3_header.b5_tag.hex(sep=' ') + '"' )
        print( '\tPdf Header (2. Split) Hex  : "' + self.p3_header.b3_split.hex(' ') + '"')
        print()
        print('\tPdf <<obj-endobj>> count       : ' + str(len(self.p4_objs))    )
        print('\tPdf <<stream-endstream>> count : ' + str(len(self.p5_streams)) )
        print()
        print('\tPdf <<xref>> count      : ' + str(len(self.p6_xrefs)) )
        print('\tPdf <<trailer>> count   : ' + str(len(self.p7_trailers)) )
        print('\tPdf <<startxref>> count : ' + str(len(self.p8_startxrefs)) )
        print('\tPdf <<%%EOF>> count     : ' + str(len(self.p9_eofs)) )

