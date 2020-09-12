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
from lib.pdf.PdfFile import PdfFile
from lib.hexlib.ShowHex import show2HexBytes as s2hex


#
#
#
class PdfShow:
    #
    def __init__(self, pdffile:PdfFile):
        self.o1_pdffile = pdffile
    #
    def objShow(self, index:int):
        if index -1 < index < len(self.o1_pdffile.p4_objs):
            tmp_obj = self.o1_pdffile.p4_objs[index]
            if tmp_obj.i3_stream_no != -1 and tmp_obj.i0_check :
                tmp_stream = self.o1_pdffile.p5_streams[ tmp_obj.i3_stream_no ]
                str_stream = '/*** STREAM (No:'+str(tmp_stream.i0_no)+') ***'
                tmp_bytes  = self.o1_pdffile.p2_pdf_bytes[ tmp_obj.i2_inner_start : tmp_stream.i1_out_start ] + str_stream.encode(encoding='utf-8',errors='strict') +\
                             self.o1_pdffile.p2_pdf_bytes[ tmp_stream.i1_out_end  : tmp_obj.i2_inner_end ]
            elif tmp_obj.i0_check :
                tmp_bytes = self.o1_pdffile.p2_pdf_bytes[ tmp_obj.i2_inner_start : tmp_obj.i2_inner_end ]
            else:
                return
            print()
            print( '\t<<Obj No : '+ str(tmp_obj.i0_no) + '>> \t-\t Obj header : "' + str(tmp_obj.i4_obj_first_no) + ' ' + str(tmp_obj.i5_obj_second_no) +' obj"')
            print( '\t'+('-'*60),end='')
            #
            tmp_string = tmp_bytes.decode(encoding='utf-8',errors='replace')
            len_tmp_str = len(tmp_string)
            char_shift = 0
            #
            check1_bool = True
            check2_bool = False
            #
            for ii in range( 0, len_tmp_str):
                #
                char1_ii = tmp_string[ii:ii+1]
                if ii + 1 < len_tmp_str:
                    char2_ii = tmp_string[ii+1:ii+2]
                else:
                    char2_ii = ''
                #
                if char1_ii != '\n' and char1_ii != '\r':
                    if char1_ii == '<' and char2_ii == '<':
                        char_shift += 1
                        txt_tmp = '\n\t{}<<'.format( char_shift*'\t' )
                        check2_bool = True
                    elif char1_ii == '>' and char2_ii == '>':
                        txt_tmp = '\n\t{}>>'.format( char_shift*'\t' )
                        char_shift -= 1
                        check2_bool = True
                    elif char1_ii == '/' :
                        if char2_ii != '/' and char2_ii != '':
                            txt_tmp = '\n\t{}{}'.format(  (char_shift*'\t') ,char1_ii)
                        else:
                            txt_tmp = char1_ii
                    elif ii == 0:
                        txt_tmp = '\n\t{}{}'.format(  (char_shift*'\t') ,char1_ii)
                    else:
                        txt_tmp = char1_ii
                    #
                    if  check1_bool:
                        print(txt_tmp, end='')
                    #
                    if check2_bool:
                        if  not check1_bool:
                            check1_bool = True
                            check2_bool = False
                        else:
                            check1_bool = False

            print('\n\t' + ('-' * 60))
            #
            if tmp_obj.i3_stream_no != -1:
                self.streamShow( index=tmp_obj.i3_stream_no )

    def objSummaryShow(self, index:int):
        if index -1 < index < len(self.o1_pdffile.p4_objs):
            tmp_obj = self.o1_pdffile.p4_objs[index]
            if tmp_obj.i3_stream_no != -1 and tmp_obj.i0_check :
                tmp_stream = self.o1_pdffile.p5_streams[ tmp_obj.i3_stream_no ]
                str_stream = '/*** STREAM (No:'+str(tmp_stream.i0_no)+') ***'
                tmp_bytes  = self.o1_pdffile.p2_pdf_bytes[ tmp_obj.i2_inner_start : tmp_stream.i1_out_start ] + str_stream.encode(encoding='utf-8',errors='strict') +\
                             self.o1_pdffile.p2_pdf_bytes[ tmp_stream.i1_out_end  : tmp_obj.i2_inner_end ]
            elif tmp_obj.i0_check :
                tmp_bytes = self.o1_pdffile.p2_pdf_bytes[ tmp_obj.i2_inner_start : tmp_obj.i2_inner_end ]
            else:
                return
            print()
            print( '\t<<Obj No : '+ str(tmp_obj.i0_no) + '>> \t-\t Obj header : "' + str(tmp_obj.i4_obj_first_no) + ' ' + str(tmp_obj.i5_obj_second_no) +' obj"')
            print( '\t'+('-'*60),end='')
            #
            tmp_string = tmp_bytes.decode(encoding='utf-8',errors='replace')
            len_tmp_str = len(tmp_string)
            char_shift = 0
            #
            check1_bool = True
            check2_bool = False
            #
            for ii in range( 0, len_tmp_str):
                #
                char1_ii = tmp_string[ii:ii+1]
                if ii + 1 < len_tmp_str:
                    char2_ii = tmp_string[ii+1:ii+2]
                else:
                    char2_ii = ''
                #
                if char1_ii != '\n' and char1_ii != '\r':
                    if char1_ii == '<' and char2_ii == '<':
                        char_shift += 1
                        txt_tmp = '\n\t{}<<'.format( char_shift*'\t' )
                        check2_bool = True
                    elif char1_ii == '>' and char2_ii == '>':
                        txt_tmp = '\n\t{}>>'.format( char_shift*'\t' )
                        char_shift -= 1
                        check2_bool = True
                    elif char1_ii == '/' :
                        if char2_ii != '/' and char2_ii != '':
                            txt_tmp = '\n\t{}{}'.format(  (char_shift*'\t') ,char1_ii)
                        else:
                            txt_tmp = char1_ii
                    elif ii == 0:
                        txt_tmp = '\n\t{}{}'.format(  (char_shift*'\t') ,char1_ii)
                    else:
                        txt_tmp = char1_ii
                    #
                    if  check1_bool:
                        print(txt_tmp, end='')
                    #
                    if check2_bool:
                        if  not check1_bool:
                            check1_bool = True
                            check2_bool = False
                        else:
                            check1_bool = False

            print('\n\t' + ('-' * 60))
            #
            if tmp_obj.i3_stream_no != -1:
                self.streamSummaryShow( index=tmp_obj.i3_stream_no )

    #
    def streamShow(self, index:int):
        if  -1 < index < len(self.o1_pdffile.p5_streams):
            result = self.detect_stream(index=index)
            print()
            print('\tStream No              : '+str(index) )
            print('\tStream Start-End Index : ' + str(self.o1_pdffile.p5_streams[index].i1_out_start) + '-' + str(self.o1_pdffile.p5_streams[index].i1_out_end) )
            print('\tStream Length          : ' + str(result['length']) +' bayts' )
            print('\tStream Data Type       : '+ result['type'] )
            if result['no'] == 1:
                print( '\tStream Start Marker    : "ff d8"' )
                print( '\tStream End Marker      : "ff d9"' )
            elif result['no'] == 2:
                print( '\tStream Start Marker    : "ff d8"')
            elif result['no'] == 5:
                print('\tZlib Stream Marker     : "' + self.o1_pdffile.p2_pdf_bytes[ self.o1_pdffile.p5_streams[index].i2_inner_start : self.o1_pdffile.p5_streams[index].i2_inner_start+4 ].hex(sep=' ') + '"'  )
            s2hex(dataName='Stream', dataBytes=result['bytes'], columnSize=20, linesHalt=1500)
    #
    #
    def streamSummaryShow(self, index:int):
        from  lib.hexlib.ShowHex import show3HexBytes as s3hex
        if  -1 < index < len(self.o1_pdffile.p5_streams):
            result = self.detect_stream(index=index)
            print()
            print('\tStream No              : '+str(index) )
            print('\tStream Start-End Index : ' + str(self.o1_pdffile.p5_streams[index].i1_out_start) + '-' + str(self.o1_pdffile.p5_streams[index].i1_out_end) )
            print('\tStream Length          : ' + str(result['length']) +' bayts' )
            print('\tStream Data Type       : '+ result['type'] )
            if result['no'] == 1:
                print( '\tStream Start Marker    : "ff d8"' )
                print( '\tStream End Marker      : "ff d9"' )
            elif result['no'] == 2:
                print( '\tStream Start Marker    : "ff d8"')
            elif result['no'] == 5:
                print('\tZlib Stream Marker     : "' + self.o1_pdffile.p2_pdf_bytes[ self.o1_pdffile.p5_streams[index].i2_inner_start : self.o1_pdffile.p5_streams[index].i2_inner_start+4 ].hex(sep=' ') + '"'  )
            print()
            if len( result['bytes'] ) < 21:
                print('\tStream Data (Only first {} bayts)'.format( len( result['bytes'] ) ) )
                s3hex( dataBytes=result['bytes'], columnSize=20, linesHalt=-1)
            else:
                print('\tStream Data (Only first 20 bayts)')
                s3hex( dataBytes=result['bytes'][0:20], columnSize=20, linesHalt=-1)

    #
    def xrefShow(self, index:int):
        if -1 < index < len(self.o1_pdffile.p6_xrefs):
            #
            tmp_list = []
            for ii in self.o1_pdffile.p6_xrefs:
                tmp_list.append(ii)
            for jj in self.o1_pdffile.p7_trailers:
                tmp_list.append(jj)
            for kk in  self.o1_pdffile.p8_startxrefs:
                tmp_list.append(kk)
            for ll in self.o1_pdffile.p9_eofs:
                tmp_list.append(ll)
            #
            sort_list = sorted(tmp_list)
            #
            index_start = self.o1_pdffile.p6_xrefs[index]
            index_end = -1
            #
            if len(sort_list) > 0:
                for rr in range( 0,len(sort_list) ):
                    if rr != len(tmp_list)-1:
                        if index_start == sort_list[rr]:
                            index_end = sort_list[ rr+1 ]
            #
            head = 'Xref (No:'+str(index)+')'
            s2hex(dataBytes=self.o1_pdffile.p2_pdf_bytes[index_start:index_end],index=index_start, dataName=head, columnSize=20, linesHalt=1500 )

    #
    def trailerShow(self, index:int):
        if -1 < index < len(self.o1_pdffile.p7_trailers):
            #
            tmp_list = []
            for ii in self.o1_pdffile.p6_xrefs:
                tmp_list.append(ii)
            for jj in self.o1_pdffile.p7_trailers:
                tmp_list.append(jj)
            for kk in  self.o1_pdffile.p8_startxrefs:
                tmp_list.append(kk)
            for ll in self.o1_pdffile.p9_eofs:
                tmp_list.append(ll)
            #
            sort_list = sorted(tmp_list)
            #
            index_start = self.o1_pdffile.p7_trailers[index]
            index_end = -1
            #
            if len(sort_list) > 0:
                for rr in range( 0,len(sort_list) ):
                    if rr != len(tmp_list)-1:
                        if index_start == sort_list[rr]:
                            index_end = sort_list[ rr+1 ]
            #
            head = 'Trailer (No:' + str(index) + ')'
            s2hex(dataBytes=self.o1_pdffile.p2_pdf_bytes[index_start:index_end],index=index_start, dataName=head, columnSize=20, linesHalt=1500 )

    #
    def startXrefShow(self, index:int):
        if -1 < index < len(self.o1_pdffile.p8_startxrefs):
            #
            tmp_list = []
            for ii in self.o1_pdffile.p6_xrefs:
                tmp_list.append(ii)
            for jj in self.o1_pdffile.p7_trailers:
                tmp_list.append(jj)
            for kk in  self.o1_pdffile.p8_startxrefs:
                tmp_list.append(kk)
            for ll in self.o1_pdffile.p9_eofs:
                tmp_list.append(ll)
            #
            sort_list = sorted(tmp_list)
            #
            index_start = self.o1_pdffile.p8_startxrefs[index]
            index_end = -1
            #
            if len(sort_list) > 0:
                for rr in range( 0,len(sort_list) ):
                    if rr != len(tmp_list)-1:
                        if index_start == sort_list[rr]:
                            index_end = sort_list[ rr+1 ]
            #
            head = 'StartXref (No:' + str(index) + ')'
            s2hex(dataBytes=self.o1_pdffile.p2_pdf_bytes[index_start:index_end], index=index_start, dataName=head, columnSize=20, linesHalt=1500 )

    #
    def __zlib(self, data:bytes) -> dict:
        import zlib
        try:
            zlibData = zlib.decompress(data)
            zlib_bool = True
        except zlib.error:
            zlibData = b''
            zlib_bool = False

        result = { 'zlib':zlib_bool , 'zlibData':zlibData }
        return result

    #
    def detect_stream(self, index:int) -> dict:
        tmp_stream = self.o1_pdffile.p5_streams[index]
        if tmp_stream.i0_check:
            tmp_stream_length = tmp_stream.i2_inner_end - tmp_stream.i2_inner_start
            if len(self.o1_pdffile.p2_pdf_bytes[ tmp_stream.i2_inner_start:tmp_stream.i2_inner_end ]) > 4:
                if self.o1_pdffile.p2_pdf_bytes[ tmp_stream.i2_inner_start:tmp_stream.i2_inner_start+2 ] == b'\xff\xd8':
                    if self.o1_pdffile.p2_pdf_bytes[ tmp_stream.i2_inner_end-2:tmp_stream.i2_inner_end ] == b'\xff\xd9':
                        return {
                                'result':True,
                                'no':1,
                                'type':'JPG/JPEG',
                                'length':tmp_stream_length,
                                'bytes': self.o1_pdffile.p2_pdf_bytes[ tmp_stream.i2_inner_start:tmp_stream.i2_inner_end ]
                        }
                    else:
                        return {
                                'result':True,
                                'no': 2,
                                'type':'JPG/JPEG (maybe)',
                                'length':tmp_stream_length,
                                'bytes': self.o1_pdffile.p2_pdf_bytes[ tmp_stream.i2_inner_start:tmp_stream.i2_inner_end ]
                        }
                else:
                    res = self.o1_pdffile.p2_pdf_bytes[tmp_stream.i2_inner_start:tmp_stream.i2_inner_end].find(b'xmpmeta')
                    if res != -1:
                        return {
                            'result': True,
                            'no': 3,
                            'type': 'XMP Meta',
                            'length': tmp_stream_length,
                            'bytes': self.o1_pdffile.p2_pdf_bytes[tmp_stream.i2_inner_start:tmp_stream.i2_inner_end]
                        }
                    else:
                        res = self.o1_pdffile.p2_pdf_bytes[tmp_stream.i2_inner_start:tmp_stream.i2_inner_end].find( b'?xpacket' )
                        if res != -1:
                            return {
                                'result': True,
                                'no': 4,
                                'type': '?Xpacket',
                                'length': tmp_stream_length,
                                'bytes': self.o1_pdffile.p2_pdf_bytes[tmp_stream.i2_inner_start:tmp_stream.i2_inner_end]
                            }
                        else:
                            res = self.__zlib(data=self.o1_pdffile.p2_pdf_bytes[tmp_stream.i2_inner_start:tmp_stream.i2_inner_end])
                            if res['zlib']:
                                return {
                                    'result': True,
                                    'no': 5,
                                    'type': 'Zlib',
                                    'length': len( res['zlibData'] ) ,
                                    'bytes': res['zlibData']
                                }
                            else:
                                return {
                                    'result': True,
                                    'no': 6,
                                    'type': 'Unknown',
                                    'length': tmp_stream_length ,
                                    'bytes': self.o1_pdffile.p2_pdf_bytes[tmp_stream.i2_inner_start:tmp_stream.i2_inner_end]
                                }
            else:
                return {
                    'result': True,
                    'no': 7,
                    'type': 'Unknown',
                    'length': tmp_stream_length,
                    'bytes': self.o1_pdffile.p2_pdf_bytes[tmp_stream.i2_inner_start:tmp_stream.i2_inner_end]
                }
        else:
            return { 'result':False , 'no':-1 ,'type':'Unknown', 'length': 0 , 'bytes':b'' }