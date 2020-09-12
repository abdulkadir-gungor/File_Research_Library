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

from lib.pdf.PdfFile import PdfFile as pdfFile
#
#
#
class checkList:
    #
    def __init__(self):
        self.b1_page            = b'/Page'
        self.b2_encrypt         = b'/Encrypt'
        self.b3_authevent       = b'/AuthEvent'
        self.b4_objstm          = b'/ObjStm'
        self.b5_js              = b'/JS'
        self.b6_javascript      = b'/JavaScript'
        self.b7_aa              = b'/AA'
        self.b8_xml             = b'/XML'
        self.b9_action          = b'/Action'
        self.b10_openaction     = b'/OpenAction'
        self.b11_acroform       = b'/AcroForm'
        self.b12_acrofield      = b'/AcroField'
        self.b13_fdf            = b'/FDF'
        self.b14_xform          = b'/XForm'
        self.b15_form           = b'/Form'
        self.b16_xfa            = b'/XFA'
        self.b17_launch         = b'/Launch'
        self.b18_jbig2decode    = b'/JBIG2Decode'
        self.b19_asciihexdecode = b'/ASCIIHexDecode'
        self.b20_richmedia      = b'/RichMedia'
        self.b21_fileattachment = b'/FileAttachment'
        self.b22_type           = b'/Type'
        self.b23_filespec       = b'/FileSpec'
        self.b24_embeddedfile   = b'/EmbeddedFile'
        self.b25_xobject        = b'/XObject'
        self.b26_f              = b'/F '
        self.b27_ef             = b'/EF'
        self.b28_image          = b'/Image'
        self.b29_font           = b'/Font '
        self.b30_fontname       = b'/FontName'
        self.b31_metadata       = b'/Metadata'
        self.b32_link           = b'/Link'
        self.b33_uri            = b'URI'
        self.b34_http           = b'http://'
        self.b35_https          = b'https://'
        self.b36_ftp            = b'ftp://'
        self.b37_ftps           = b'ftps://'
        self.b38_goto           = b'/GoTo '
        self.b39_gotor          = b'/GoToR'
        self.b40_gotoe          = b'/GoToE'
        self.b41_thread         = b'/Thread'
        self.b42_sound          = b'/Sound'
        self.b43_movie          = b'/Movie'
        self.b44_hide           = b'/Hide'
        self.b45_named          = b'/Named'
        self.b46_submitform     = b'/SubmitForm'
        self.b47_resetform      = b'/ResetForm'
        self.b48_importdata     = b'/ImportData'
        self.b49_setocgstate    = b'/SetOCGState'
        self.b50_rendition      = b'/Rendition'
        self.b51_trans          = b'/Trans'
        self.b52_goto3dview     = b'/GoTo3DView'
        self.b53_checksum       = b'/CheckSum'

#
#
class checkObjBetik:
    #
    def __init__(self, pdffile:pdfFile ):
        self.o1_pdffile = pdffile
        #
        self.p1_page_objs = []
        self.p1_page_obj_total = 0
        self.p1_page_pdf_total = 0
        self.p2_encrypt_objs = []
        self.p2_encrypt_obj_total = 0
        self.p2_encrypt_pdf_total = 0
        self.p3_authevent_objs = []
        self.p3_authevent_obj_total = 0
        self.p3_authevent_pdf_total = 0
        self.p4_objstm_objs = []
        self.p4_objstm_obj_total = 0
        self.p4_objstm_pdf_total = 0
        self.p5_js_objs = []
        self.p5_js_obj_total = 0
        self.p5_js_pdf_total = 0
        self.p6_javascript_objs = []
        self.p6_javascript_obj_total = 0
        self.p6_javascript_pdf_total = 0
        self.p7_aa_objs = []
        self.p7_aa_obj_total = 0
        self.p7_aa_pdf_total = 0
        self.p8_xml_objs = []
        self.p8_xml_obj_total = 0
        self.p8_xml_pdf_total = 0
        self.p9_action_objs = []
        self.p9_action_obj_total = 0
        self.p9_action_pdf_total = 0
        self.p10_openaction_objs = []
        self.p10_openaction_obj_total = 0
        self.p10_openaction_pdf_total = 0
        self.p11_acroform_objs = []
        self.p11_acroform_obj_total = 0
        self.p11_acroform_pdf_total = 0
        self.p12_acrofield_objs = []
        self.p12_acrofield_obj_total = 0
        self.p12_acrofield_pdf_total = 0
        self.p13_fdf_objs = []
        self.p13_fdf_obj_total = 0
        self.p13_fdf_pdf_total = 0
        self.p14_xform_objs = []
        self.p14_xform_obj_total = 0
        self.p14_xform_pdf_total = 0
        self.p15_form_objs = []
        self.p15_form_obj_total = 0
        self.p15_form_pdf_total = 0
        self.p16_xfa_objs = []
        self.p16_xfa_obj_total = 0
        self.p16_xfa_pdf_total = 0
        self.p17_launch_objs = []
        self.p17_launch_obj_total = 0
        self.p17_launch_pdf_total = 0
        self.p18_jbig2decode_objs = []
        self.p18_jbig2decode_obj_total = 0
        self.p18_jbig2decode_pdf_total = 0
        self.p19_asciihexdecode_objs = []
        self.p19_asciihexdecode_obj_total = 0
        self.p19_asciihexdecode_pdf_total = 0
        self.p20_richmedia_objs = []
        self.p20_richmedia_obj_total = 0
        self.p20_richmedia_pdf_total = 0
        self.p21_fileattachment_objs = []
        self.p21_fileattachment_obj_total = 0
        self.p21_fileattachment_pdf_total = 0
        self.p22_type_objs = []
        self.p22_type_obj_total = 0
        self.p22_type_pdf_total = 0
        self.p23_filespec_objs = []
        self.p23_filespec_obj_total = 0
        self.p23_filespec_pdf_total = 0
        self.p24_embeddedfile_objs = []
        self.p24_embeddedfile_obj_total = 0
        self.p24_embeddedfile_pdf_total = 0
        self.p25_xobject_objs = []
        self.p25_xobject_obj_total = 0
        self.p25_xobject_pdf_total = 0
        self.p26_f_objs = []
        self.p26_f_obj_total = 0
        self.p26_f_pdf_total = 0
        self.p27_ef_objs = []
        self.p27_ef_obj_total = 0
        self.p27_ef_pdf_total = 0
        self.p28_image_objs = []
        self.p28_image_obj_total = 0
        self.p28_image_pdf_total = 0
        self.p29_font_objs = []
        self.p29_font_obj_total = 0
        self.p29_font_pdf_total = 0
        self.p30_fontname_objs = []
        self.p30_fontname_obj_total = 0
        self.p30_fontname_pdf_total = 0
        self.p31_metadata_objs = []
        self.p31_metadata_obj_total = 0
        self.p31_metadata_pdf_total = 0
        self.p32_link_objs = []
        self.p32_link_obj_total = 0
        self.p32_link_pdf_total = 0
        self.p33_uri_objs = []
        self.p33_uri_obj_total = 0
        self.p33_uri_pdf_total = 0
        self.p34_http_objs = []
        self.p34_http_obj_total = 0
        self.p34_http_pdf_total = 0
        self.p35_https_objs = []
        self.p35_https_obj_total = 0
        self.p35_https_pdf_total = 0
        self.p36_ftp_objs = []
        self.p36_ftp_obj_total = 0
        self.p36_ftp_pdf_total = 0
        self.p37_ftps_objs = []
        self.p37_ftps_obj_total = 0
        self.p37_ftps_pdf_total = 0
        self.p38_goto_objs = []
        self.p38_goto_obj_total = 0
        self.p38_goto_pdf_total = 0
        self.p39_gotor_objs = []
        self.p39_gotor_obj_total = 0
        self.p39_gotor_pdf_total = 0
        self.p40_gotoe_objs = []
        self.p40_gotoe_obj_total = 0
        self.p40_gotoe_pdf_total = 0
        self.p41_thread_objs = []
        self.p41_thread_obj_total = 0
        self.p41_thread_pdf_total = 0
        self.p42_sound_objs = []
        self.p42_sound_obj_total = 0
        self.p42_sound_pdf_total = 0
        self.p43_movie_objs = []
        self.p43_movie_obj_total = 0
        self.p43_movie_pdf_total = 0
        self.p44_hide_objs = []
        self.p44_hide_obj_total = 0
        self.p44_hide_pdf_total = 0
        self.p45_named_objs = []
        self.p45_named_obj_total = 0
        self.p45_named_pdf_total = 0
        self.p46_submitform_objs = []
        self.p46_submitform_obj_total = 0
        self.p46_submitform_pdf_total = 0
        self.p47_resetform_objs = []
        self.p47_resetform_obj_total = 0
        self.p47_resetform_pdf_total = 0
        self.p48_importdata_objs = []
        self.p48_importdata_obj_total = 0
        self.p48_importdata_pdf_total = 0
        self.p49_setocgstate_objs = []
        self.p49_setocgstate_obj_total = 0
        self.p49_setocgstate_pdf_total = 0
        self.p50_rendition_objs = []
        self.p50_rendition_obj_total = 0
        self.p50_rendition_pdf_total = 0
        self.p51_trans_objs = []
        self.p51_trans_obj_total = 0
        self.p51_trans_pdf_total = 0
        self.p52_goto3dview_objs = []
        self.p52_goto3dview_obj_total = 0
        self.p52_goto3dview_pdf_total = 0
        self.p53_checksum_objs = []
        self.p53_checksum_obj_total = 0
        self.p53_checksum_pdf_total = 0
        #

    #
    def findPdfBetik(self):
        oo = checkList()
        #
        self.p1_page_pdf_total = self.o1_pdffile.p2_pdf_bytes.count( oo.b1_page )
        self.p2_encrypt_pdf_total = self.o1_pdffile.p2_pdf_bytes.count( oo.b2_encrypt )
        self.p3_authevent_pdf_total = self.o1_pdffile.p2_pdf_bytes.count(  oo.b3_authevent )
        self.p4_objstm_pdf_total = self.o1_pdffile.p2_pdf_bytes.count( oo.b4_objstm )
        self.p5_js_pdf_total = self.o1_pdffile.p2_pdf_bytes.count( oo.b5_js )
        self.p6_javascript_pdf_total =  self.o1_pdffile.p2_pdf_bytes.count( oo.b6_javascript )
        self.p7_aa_pdf_total = self.o1_pdffile.p2_pdf_bytes.count( oo.b7_aa )
        self.p8_xml_pdf_total = self.o1_pdffile.p2_pdf_bytes.count( oo.b8_xml )
        self.p9_action_pdf_total = self.o1_pdffile.p2_pdf_bytes.count(oo.b9_action)
        self.p10_openaction_pdf_total = self.o1_pdffile.p2_pdf_bytes.count( oo.b10_openaction )
        self.p11_acroform_pdf_total = self.o1_pdffile.p2_pdf_bytes.count( oo.b11_acroform )
        self.p12_acrofield_pdf_total = self.o1_pdffile.p2_pdf_bytes.count( oo.b12_acrofield )
        self.p13_fdf_pdf_total = self.o1_pdffile.p2_pdf_bytes.count( oo.b13_fdf )
        self.p14_xform_pdf_total = self.o1_pdffile.p2_pdf_bytes.count( oo.b14_xform )
        self.p15_form_pdf_total = self.o1_pdffile.p2_pdf_bytes.count( oo.b15_form )
        self.p16_xfa_pdf_total = self.o1_pdffile.p2_pdf_bytes.count( oo.b16_xfa )
        self.p17_launch_pdf_total = self.o1_pdffile.p2_pdf_bytes.count( oo.b17_launch )
        self.p18_jbig2decode_pdf_total = self.o1_pdffile.p2_pdf_bytes.count( oo.b18_jbig2decode )
        self.p19_asciihexdecode_pdf_total = self.o1_pdffile.p2_pdf_bytes.count( oo.b19_asciihexdecode )
        self.p20_richmedia_pdf_total = self.o1_pdffile.p2_pdf_bytes.count( oo.b20_richmedia )
        self.p21_fileattachment_pdf_total = self.o1_pdffile.p2_pdf_bytes.count( oo.b21_fileattachment )
        self.p22_type_pdf_total = self.o1_pdffile.p2_pdf_bytes.count( oo.b22_type )
        self.p23_filespec_pdf_total = self.o1_pdffile.p2_pdf_bytes.count( oo.b23_filespec )
        self.p24_embeddedfile_pdf_total = self.o1_pdffile.p2_pdf_bytes.count( oo.b24_embeddedfile )
        self.p25_xobject_pdf_total = self.o1_pdffile.p2_pdf_bytes.count( oo.b25_xobject )
        self.p26_f_pdf_total = self.o1_pdffile.p2_pdf_bytes.count( oo.b26_f )
        self.p27_ef_pdf_total = self.o1_pdffile.p2_pdf_bytes.count( oo.b27_ef )
        self.p28_image_pdf_total = self.o1_pdffile.p2_pdf_bytes.count( oo.b28_image )
        self.p29_font_pdf_total = self.o1_pdffile.p2_pdf_bytes.count( oo.b29_font )
        self.p30_fontname_pdf_total = self.o1_pdffile.p2_pdf_bytes.count( oo.b30_fontname )
        self.p31_metadata_pdf_total = self.o1_pdffile.p2_pdf_bytes.count( oo.b31_metadata )
        self.p32_link_pdf_total = self.o1_pdffile.p2_pdf_bytes.count( oo.b32_link )
        self.p33_uri_pdf_total = self.o1_pdffile.p2_pdf_bytes.count( oo.b33_uri )
        self.p34_http_pdf_total = self.o1_pdffile.p2_pdf_bytes.count( oo.b34_http )
        self.p35_https_pdf_total = self.o1_pdffile.p2_pdf_bytes.count( oo.b35_https )
        self.p36_ftp_pdf_total = self.o1_pdffile.p2_pdf_bytes.count( oo.b36_ftp )
        self.p37_ftps_pdf_total = self.o1_pdffile.p2_pdf_bytes.count( oo.b37_ftps )
        self.p38_goto_pdf_total = self.o1_pdffile.p2_pdf_bytes.count( oo.b38_goto )
        self.p39_gotor_pdf_total = self.o1_pdffile.p2_pdf_bytes.count( oo.b39_gotor )
        self.p40_gotoe_pdf_total = self.o1_pdffile.p2_pdf_bytes.count( oo.b40_gotoe )
        self.p41_thread_pdf_total = self.o1_pdffile.p2_pdf_bytes.count( oo.b41_thread )
        self.p42_sound_pdf_total = self.o1_pdffile.p2_pdf_bytes.count( oo.b42_sound )
        self.p43_movie_pdf_total = self.o1_pdffile.p2_pdf_bytes.count( oo.b43_movie )
        self.p44_hide_pdf_total = self.o1_pdffile.p2_pdf_bytes.count( oo.b44_hide )
        self.p45_named_pdf_total = self.o1_pdffile.p2_pdf_bytes.count( oo.b45_named )
        self.p46_submitform_pdf_total = self.o1_pdffile.p2_pdf_bytes.count( oo.b46_submitform )
        self.p47_resetform_pdf_total = self.o1_pdffile.p2_pdf_bytes.count( oo.b47_resetform )
        self.p48_importdata_pdf_total = self.o1_pdffile.p2_pdf_bytes.count( oo.b48_importdata )
        self.p49_setocgstate_pdf_total = self.o1_pdffile.p2_pdf_bytes.count( oo.b49_setocgstate )
        self.p50_rendition_pdf_total = self.o1_pdffile.p2_pdf_bytes.count( oo.b50_rendition )
        self.p51_trans_pdf_total = self.o1_pdffile.p2_pdf_bytes.count( oo.b51_trans )
        self.p52_goto3dview_pdf_total = self.o1_pdffile.p2_pdf_bytes.count( oo.b52_goto3dview )
        self.p53_checksum_pdf_total = self.o1_pdffile.p2_pdf_bytes.count( oo.b53_checksum )
        #

    #
    def findObjBetik(self):
        oo = checkList()
        #
        for obj in self.o1_pdffile.p4_objs:
            if obj.i0_check:
                #
                tmp = self.o1_pdffile.p2_pdf_bytes[obj.i1_out_start:obj.i1_out_end].count( oo.b1_page )
                if  0 < tmp:
                    self.p1_page_objs.append( obj.i0_no )
                    self.p1_page_obj_total += tmp
                #
                tmp = self.o1_pdffile.p2_pdf_bytes[obj.i1_out_start:obj.i1_out_end].count( oo.b2_encrypt )
                if  0 < tmp:
                    self.p2_encrypt_objs.append( obj.i0_no )
                    self.p2_encrypt_obj_total += tmp
                #
                tmp = self.o1_pdffile.p2_pdf_bytes[obj.i1_out_start:obj.i1_out_end].count( oo.b3_authevent )
                if  0 < tmp:
                    self.p3_authevent_objs.append( obj.i0_no )
                    self.p3_authevent_obj_total += tmp
                #
                tmp = self.o1_pdffile.p2_pdf_bytes[obj.i1_out_start:obj.i1_out_end].count( oo.b4_objstm )
                if  0 < tmp:
                    self.p4_objstm_objs.append( obj.i0_no )
                    self.p4_objstm_obj_total += tmp
                #
                tmp = self.o1_pdffile.p2_pdf_bytes[obj.i1_out_start:obj.i1_out_end].count( oo.b5_js )
                if  0 < tmp:
                    self.p5_js_objs.append( obj.i0_no )
                    self.p5_js_obj_total += tmp
                #
                tmp = self.o1_pdffile.p2_pdf_bytes[obj.i1_out_start:obj.i1_out_end].count( oo.b6_javascript )
                if  0 < tmp:
                    self.p6_javascript_objs.append( obj.i0_no )
                    self.p6_javascript_obj_total += tmp
                #
                tmp = self.o1_pdffile.p2_pdf_bytes[obj.i1_out_start:obj.i1_out_end].count( oo.b7_aa )
                if  0 < tmp:
                    self.p7_aa_objs.append( obj.i0_no )
                    self.p7_aa_obj_total += tmp
                #
                tmp = self.o1_pdffile.p2_pdf_bytes[obj.i1_out_start:obj.i1_out_end].count( oo.b8_xml)
                if  0 < tmp:
                    self.p8_xml_objs.append( obj.i0_no )
                    self.p8_xml_obj_total += tmp
                #
                tmp = self.o1_pdffile.p2_pdf_bytes[obj.i1_out_start:obj.i1_out_end].count( oo.b9_action )
                if  0 < tmp:
                    self.p9_action_objs.append( obj.i0_no )
                    self.p9_action_obj_total += tmp
                #
                tmp = self.o1_pdffile.p2_pdf_bytes[obj.i1_out_start:obj.i1_out_end].count( oo.b10_openaction )
                if  0 < tmp:
                    self.p10_openaction_objs.append( obj.i0_no )
                    self.p10_openaction_obj_total += tmp
                #
                tmp = self.o1_pdffile.p2_pdf_bytes[obj.i1_out_start:obj.i1_out_end].count( oo.b11_acroform )
                if  0 < tmp:
                    self.p11_acroform_objs.append( obj.i0_no )
                    self.p11_acroform_obj_total += tmp
                #
                tmp = self.o1_pdffile.p2_pdf_bytes[obj.i1_out_start:obj.i1_out_end].count( oo.b12_acrofield )
                if  0 < tmp:
                    self.p12_acrofield_objs.append( obj.i0_no )
                    self.p12_acrofield_obj_total += tmp
                #
                tmp = self.o1_pdffile.p2_pdf_bytes[obj.i1_out_start:obj.i1_out_end].count( oo.b13_fdf )
                if  0 < tmp:
                    self.p13_fdf_objs.append( obj.i0_no )
                    self.p13_fdf_obj_total += tmp
                #
                tmp = self.o1_pdffile.p2_pdf_bytes[obj.i1_out_start:obj.i1_out_end].count( oo.b14_xform )
                if  0 < tmp:
                    self.p14_xform_objs.append( obj.i0_no )
                    self.p14_xform_obj_total += tmp
                #
                tmp = self.o1_pdffile.p2_pdf_bytes[obj.i1_out_start:obj.i1_out_end].count( oo.b15_form )
                if  0 < tmp:
                    self.p15_form_objs.append( obj.i0_no )
                    self.p15_form_obj_total += tmp
                #
                tmp = self.o1_pdffile.p2_pdf_bytes[obj.i1_out_start:obj.i1_out_end].count( oo.b16_xfa )
                if  0 < tmp:
                    self.p16_xfa_objs.append( obj.i0_no )
                    self.p16_xfa_obj_total += tmp
                #
                tmp = self.o1_pdffile.p2_pdf_bytes[obj.i1_out_start:obj.i1_out_end].count( oo.b17_launch )
                if  0 < tmp:
                    self.p17_launch_objs.append( obj.i0_no )
                    self.p17_launch_obj_total += tmp
                #
                #
                tmp = self.o1_pdffile.p2_pdf_bytes[obj.i1_out_start:obj.i1_out_end].count( oo.b18_jbig2decode )
                if  0 < tmp:
                    self.p18_jbig2decode_objs.append( obj.i0_no )
                    self.p18_jbig2decode_obj_total += tmp
                #
                tmp = self.o1_pdffile.p2_pdf_bytes[obj.i1_out_start:obj.i1_out_end].count( oo.b19_asciihexdecode )
                if  0 < tmp:
                    self.p19_asciihexdecode_objs.append( obj.i0_no )
                    self.p19_asciihexdecode_obj_total += tmp
                #
                tmp = self.o1_pdffile.p2_pdf_bytes[obj.i1_out_start:obj.i1_out_end].count( oo.b20_richmedia )
                if  0 < tmp:
                    self.p20_richmedia_objs.append( obj.i0_no )
                    self.p20_richmedia_obj_total += tmp
                #
                tmp = self.o1_pdffile.p2_pdf_bytes[obj.i1_out_start:obj.i1_out_end].count( oo.b21_fileattachment )
                if  0 < tmp:
                    self.p21_fileattachment_objs.append( obj.i0_no )
                    self.p21_fileattachment_obj_total += tmp
                #
                tmp = self.o1_pdffile.p2_pdf_bytes[obj.i1_out_start:obj.i1_out_end].count( oo.b22_type )
                if  0 < tmp:
                    self.p22_type_objs.append( obj.i0_no )
                    self.p22_type_obj_total += tmp
                #
                tmp = self.o1_pdffile.p2_pdf_bytes[obj.i1_out_start:obj.i1_out_end].count( oo.b23_filespec )
                if  0 < tmp:
                    self.p23_filespec_objs.append( obj.i0_no )
                    self.p23_filespec_obj_total += tmp
                #
                tmp = self.o1_pdffile.p2_pdf_bytes[obj.i1_out_start:obj.i1_out_end].count( oo.b24_embeddedfile )
                if  0 < tmp:
                    self.p24_embeddedfile_objs.append( obj.i0_no )
                    self.p24_embeddedfile_obj_total += tmp
                #
                tmp = self.o1_pdffile.p2_pdf_bytes[obj.i1_out_start:obj.i1_out_end].count( oo.b25_xobject )
                if  0 < tmp:
                    self.p25_xobject_objs.append( obj.i0_no )
                    self.p25_xobject_obj_total += tmp
                #
                tmp = self.o1_pdffile.p2_pdf_bytes[obj.i1_out_start:obj.i1_out_end].count( oo.b26_f )
                if  0 < tmp:
                    self.p26_f_objs.append( obj.i0_no )
                    self.p26_f_obj_total += tmp
                #
                tmp = self.o1_pdffile.p2_pdf_bytes[obj.i1_out_start:obj.i1_out_end].count( oo.b27_ef )
                if  0 < tmp:
                    self.p27_ef_objs.append( obj.i0_no )
                    self.p27_ef_obj_total += tmp
                #
                tmp = self.o1_pdffile.p2_pdf_bytes[obj.i1_out_start:obj.i1_out_end].count( oo.b28_image)
                if  0 < tmp:
                    self.p28_image_objs.append( obj.i0_no )
                    self.p28_image_obj_total += tmp
                #
                tmp = self.o1_pdffile.p2_pdf_bytes[obj.i1_out_start:obj.i1_out_end].count( oo.b29_font )
                if  0 < tmp:
                    self.p29_font_objs.append( obj.i0_no )
                    self.p29_font_obj_total += tmp
                #
                tmp = self.o1_pdffile.p2_pdf_bytes[obj.i1_out_start:obj.i1_out_end].count( oo.b30_fontname )
                if  0 < tmp:
                    self.p30_fontname_objs.append( obj.i0_no )
                    self.p30_fontname_obj_total += tmp
                #
                tmp = self.o1_pdffile.p2_pdf_bytes[obj.i1_out_start:obj.i1_out_end].count( oo.b31_metadata )
                if  0 < tmp:
                    self.p31_metadata_objs.append( obj.i0_no )
                    self.p31_metadata_obj_total += tmp
                #
                tmp = self.o1_pdffile.p2_pdf_bytes[obj.i1_out_start:obj.i1_out_end].count( oo.b32_link )
                if  0 < tmp:
                    self.p32_link_objs.append( obj.i0_no )
                    self.p32_link_obj_total += tmp
                #
                tmp = self.o1_pdffile.p2_pdf_bytes[obj.i1_out_start:obj.i1_out_end].count( oo.b33_uri )
                if  0 < tmp:
                    self.p33_uri_objs.append( obj.i0_no )
                    self.p33_uri_obj_total += tmp
                #
                tmp = self.o1_pdffile.p2_pdf_bytes[obj.i1_out_start:obj.i1_out_end].count( oo.b34_http )
                if  0 < tmp:
                    self.p34_http_objs.append( obj.i0_no )
                    self.p34_http_obj_total += tmp
                #
                tmp = self.o1_pdffile.p2_pdf_bytes[obj.i1_out_start:obj.i1_out_end].count( oo.b35_https )
                if  0 < tmp:
                    self.p35_https_objs.append( obj.i0_no )
                    self.p35_https_obj_total += tmp
                #
                tmp = self.o1_pdffile.p2_pdf_bytes[obj.i1_out_start:obj.i1_out_end].count( oo.b36_ftp )
                if  0 < tmp:
                    self.p36_ftp_objs.append( obj.i0_no )
                    self.p36_ftp_obj_total += tmp
                #
                tmp = self.o1_pdffile.p2_pdf_bytes[obj.i1_out_start:obj.i1_out_end].count( oo.b37_ftps )
                if  0 < tmp:
                    self.p37_ftps_objs.append( obj.i0_no )
                    self.p37_ftps_obj_total += tmp
                #
                tmp = self.o1_pdffile.p2_pdf_bytes[obj.i1_out_start:obj.i1_out_end].count( oo.b38_goto )
                if  0 < tmp:
                    self.p38_goto_objs.append( obj.i0_no )
                    self.p38_goto_obj_total += tmp
                #
                tmp = self.o1_pdffile.p2_pdf_bytes[obj.i1_out_start:obj.i1_out_end].count( oo.b39_gotor )
                if  0 < tmp:
                    self.p39_gotor_objs.append( obj.i0_no )
                    self.p39_gotor_obj_total += tmp
                #
                tmp = self.o1_pdffile.p2_pdf_bytes[obj.i1_out_start:obj.i1_out_end].count( oo.b40_gotoe )
                if  0 < tmp:
                    self.p40_gotoe_objs.append( obj.i0_no )
                    self.p40_gotoe_obj_total += tmp
                #
                tmp = self.o1_pdffile.p2_pdf_bytes[obj.i1_out_start:obj.i1_out_end].count( oo.b41_thread )
                if  0 < tmp:
                    self.p41_thread_objs.append( obj.i0_no )
                    self.p41_thread_obj_total += tmp
                #
                tmp = self.o1_pdffile.p2_pdf_bytes[obj.i1_out_start:obj.i1_out_end].count( oo.b42_sound )
                if  0 < tmp:
                    self.p42_sound_objs.append( obj.i0_no )
                    self.p42_sound_obj_total += tmp
                #
                tmp = self.o1_pdffile.p2_pdf_bytes[obj.i1_out_start:obj.i1_out_end].count( oo.b43_movie )
                if  0 < tmp:
                    self.p43_movie_objs.append( obj.i0_no )
                    self.p43_movie_obj_total += tmp
                #
                tmp = self.o1_pdffile.p2_pdf_bytes[obj.i1_out_start:obj.i1_out_end].count( oo.b44_hide )
                if  0 < tmp:
                    self.p44_hide_objs.append( obj.i0_no )
                    self.p44_hide_obj_total += tmp
                #
                tmp = self.o1_pdffile.p2_pdf_bytes[obj.i1_out_start:obj.i1_out_end].count( oo.b45_named )
                if  0 < tmp:
                    self.p45_named_objs.append( obj.i0_no )
                    self.p45_named_obj_total += tmp
                #
                tmp = self.o1_pdffile.p2_pdf_bytes[obj.i1_out_start:obj.i1_out_end].count( oo.b46_submitform )
                if  0 < tmp:
                    self.p46_submitform_objs.append( obj.i0_no )
                    self.p46_submitform_obj_total += tmp
                #
                tmp = self.o1_pdffile.p2_pdf_bytes[obj.i1_out_start:obj.i1_out_end].count( oo.b47_resetform )
                if  0 < tmp:
                    self.p47_resetform_objs.append( obj.i0_no )
                    self.p47_resetform_obj_total += tmp
                #
                tmp = self.o1_pdffile.p2_pdf_bytes[obj.i1_out_start:obj.i1_out_end].count( oo.b48_importdata )
                if  0 < tmp:
                    self.p48_importdata_objs.append( obj.i0_no )
                    self.p48_importdata_obj_total += tmp
                #
                tmp = self.o1_pdffile.p2_pdf_bytes[obj.i1_out_start:obj.i1_out_end].count( oo.b49_setocgstate )
                if  0 < tmp:
                    self.p49_setocgstate_objs.append( obj.i0_no )
                    self.p49_setocgstate_obj_total += tmp
                #
                tmp = self.o1_pdffile.p2_pdf_bytes[obj.i1_out_start:obj.i1_out_end].count( oo.b50_rendition )
                if  0 < tmp:
                    self.p50_rendition_objs.append( obj.i0_no )
                    self.p50_rendition_obj_total += tmp
                #
                tmp = self.o1_pdffile.p2_pdf_bytes[obj.i1_out_start:obj.i1_out_end].count( oo.b51_trans )
                if  0 < tmp:
                    self.p51_trans_objs.append( obj.i0_no )
                    self.p51_trans_obj_total += tmp
                #
                tmp = self.o1_pdffile.p2_pdf_bytes[obj.i1_out_start:obj.i1_out_end].count( oo.b52_goto3dview )
                if  0 < tmp:
                    self.p52_goto3dview_objs.append( obj.i0_no )
                    self.p52_goto3dview_obj_total += tmp
                #
                tmp = self.o1_pdffile.p2_pdf_bytes[obj.i1_out_start:obj.i1_out_end].count( oo.b53_checksum )
                if  0 < tmp:
                    self.p53_checksum_objs.append( obj.i0_no )
                    self.p53_checksum_obj_total += tmp


    #
    def show(self):
        txt_format = '\t{:<2} \t{:^20} \t{:^7} \t{:^7} \t{:^7}'
        #
        print(txt_format.format('', '', 'Obj', 'Obj Tag', 'Pdf Tag'))
        print(txt_format.format('No', 'Tag', 'Count', 'Count', 'Count') )
        print( txt_format.format( 2*'-', 20*'-', 7*'-', 7*'-', 7*'-') )
        #
        print( txt_format.format(1,'"/Page"',  len(self.p1_page_objs), self.p1_page_obj_total, self.p1_page_pdf_total) )
        print( txt_format.format(2, '"/Encrypt"',  len(self.p2_encrypt_objs), self.p2_encrypt_obj_total, self.p2_encrypt_pdf_total) )
        print( txt_format.format(3, '"/AuthEvent"', len(self.p3_authevent_objs), self.p3_authevent_obj_total, self.p3_authevent_pdf_total ) )
        print( txt_format.format(4, '"/ObjStm"',  len(self.p4_objstm_objs), self.p4_objstm_obj_total, self.p4_objstm_pdf_total ) )
        print( txt_format.format(5, '"/JS"',  len(self.p5_js_objs), self.p5_js_obj_total, self.p5_js_pdf_total ) )
        print( txt_format.format(6, '"/JavaScript"', len(self.p6_javascript_objs), self.p6_javascript_obj_total, self.p6_javascript_pdf_total ) )
        print( txt_format.format(7, '"/AA"', len(self.p7_aa_objs), self.p7_aa_obj_total, self.p7_aa_pdf_total ) )
        print( txt_format.format(8, '"/XML"',  len(self.p8_xml_objs), self.p8_xml_obj_total, self.p8_xml_pdf_total ) )
        print( txt_format.format(9, '"/Action"',  len(self.p9_action_objs), self.p9_action_obj_total, self.p9_action_pdf_total ) )
        print( txt_format.format(10, '"/OpenAction"',  len(self.p10_openaction_objs), self.p10_openaction_obj_total, self.p10_openaction_pdf_total ) )
        print( txt_format.format(11, '"/AcroForm"',  len(self.p11_acroform_objs), self.p11_acroform_obj_total, self.p11_acroform_pdf_total ) )
        print( txt_format.format(12, '"/AcroField"',  len(self.p12_acrofield_objs), self.p12_acrofield_obj_total, self.p12_acrofield_pdf_total ) )
        print( txt_format.format(13, '"/FDF"',  len(self.p13_fdf_objs), self.p13_fdf_obj_total, self.p13_fdf_pdf_total ) )
        print( txt_format.format(14, '"/XForm"',  len(self.p14_xform_objs), self.p14_xform_obj_total, self.p14_xform_pdf_total ) )
        print( txt_format.format(15, '"/Form"',  len(self.p15_form_objs), self.p15_form_obj_total, self.p15_form_pdf_total ) )
        print( txt_format.format(16, '"/XFA"',  len(self.p16_xfa_objs), self.p16_xfa_obj_total, self.p16_xfa_pdf_total ) )
        print( txt_format.format(17, '"/Launch"',  len(self.p17_launch_objs), self.p17_launch_obj_total, self.p17_launch_pdf_total  ) )
        print( txt_format.format(18, '"/JBIG2Decode"',  len(self.p18_jbig2decode_objs), self.p18_jbig2decode_obj_total, self.p18_jbig2decode_pdf_total ) )
        print( txt_format.format(19, '"/ASCIIHexDecode"',  len(self.p19_asciihexdecode_objs), self.p19_asciihexdecode_obj_total, self.p19_asciihexdecode_pdf_total ) )
        print( txt_format.format(20, '"/RichMedia"',  len(self.p20_richmedia_objs), self.p20_richmedia_obj_total, self.p20_richmedia_pdf_total ) )
        print( txt_format.format(21, '"/FileAttachment"',  len(self.p21_fileattachment_objs), self.p21_fileattachment_obj_total, self.p21_fileattachment_pdf_total ) )
        print( txt_format.format(22, '"/Type"',  len(self.p22_type_objs), self.p22_type_obj_total, self.p22_type_pdf_total ))
        print( txt_format.format(23, '"/FileSpec"', len(self.p23_filespec_objs), self.p23_filespec_obj_total, self.p23_filespec_pdf_total ) )
        print( txt_format.format(24, '"/EmbeddedFile"',  len(self.p24_embeddedfile_objs), self.p24_embeddedfile_obj_total, self.p24_embeddedfile_pdf_total ) )
        print( txt_format.format(25, '"/XObject"',  len(self.p25_xobject_objs), self.p25_xobject_obj_total, self.p25_xobject_pdf_total) )
        print( txt_format.format(26, '"/F "',  len(self.p26_f_objs), self.p26_f_obj_total, self.p26_f_pdf_total) )
        print( txt_format.format(27, '"/EF"',  len(self.p27_ef_objs), self.p27_ef_obj_total, self.p27_ef_pdf_total ) )
        print( txt_format.format(28, '"/Image"',  len(self.p28_image_objs), self.p28_image_obj_total, self.p28_image_pdf_total) )
        print( txt_format.format(29, '"/Font "',  len(self.p29_font_objs), self.p29_font_obj_total, self.p29_font_pdf_total ) )
        print( txt_format.format(30, '"/FontName"',  len(self.p30_fontname_objs), self.p30_fontname_obj_total, self.p30_fontname_pdf_total ) )
        print( txt_format.format(31, '"/Metadata"',  len(self.p31_metadata_objs), self.p31_metadata_obj_total, self.p31_metadata_pdf_total ) )
        print( txt_format.format(32, '"/Link"',  len(self.p32_link_objs), self.p32_link_obj_total, self.p32_link_pdf_total ) )
        print( txt_format.format(33, '"URI"',  len(self.p33_uri_objs), self.p33_uri_obj_total, self.p33_uri_pdf_total ) )
        print( txt_format.format(34, '"http://"',  len(self.p34_http_objs), self.p34_http_obj_total, self.p34_http_pdf_total ) )
        print( txt_format.format(35, '"https://"', len(self.p35_https_objs), self.p35_https_obj_total, self.p35_https_pdf_total ) )
        print( txt_format.format(36, '"ftp://"',  len(self.p36_ftp_objs), self.p36_ftp_obj_total, self.p36_ftp_pdf_total ) )
        print( txt_format.format(37, '"ftps://"',  len(self.p37_ftps_objs), self.p37_ftps_obj_total, self.p37_ftps_pdf_total ) )
        print( txt_format.format(38, '"/GoTo "',  len(self.p38_goto_objs), self.p38_goto_obj_total, self.p38_goto_pdf_total ) )
        print( txt_format.format(39, '"/GoToR"',  len(self.p39_gotor_objs), self.p39_gotor_obj_total, self.p39_gotor_pdf_total ) )
        print( txt_format.format(40, '"/GoToE"',  len(self.p40_gotoe_objs), self.p40_gotoe_obj_total, self.p40_gotoe_pdf_total ) )
        print( txt_format.format(41, '"/Thread"', len(self.p41_thread_objs), self.p41_thread_obj_total, self.p41_thread_pdf_total ) )
        print( txt_format.format(42, '"/Sound"',  len(self.p42_sound_objs), self.p42_sound_obj_total, self.p42_sound_pdf_total ) )
        print( txt_format.format(43, '"/Movie"',  len(self.p43_movie_objs), self.p43_movie_obj_total, self.p43_movie_pdf_total ) )
        print( txt_format.format(44, '"/Hide"',   len(self.p44_hide_objs), self.p44_hide_obj_total, self.p44_hide_pdf_total ) )
        print( txt_format.format(45, '"/Named"',  len(self.p45_named_objs), self.p45_named_obj_total, self.p45_named_pdf_total  ) )
        print( txt_format.format(46, '"/SubmitForm"',  len(self.p46_submitform_objs), self.p46_submitform_obj_total, self.p46_submitform_pdf_total ) )
        print( txt_format.format(47, '"/ResetForm"',  len(self.p47_resetform_objs), self.p47_resetform_obj_total, self.p47_resetform_pdf_total ) )
        print( txt_format.format(48, '"/ImportData"',  len(self.p48_importdata_objs), self.p48_importdata_obj_total, self.p48_importdata_pdf_total ) )
        print( txt_format.format(49, '"/SetOCGState"', len(self.p49_setocgstate_objs), self.p49_setocgstate_obj_total, self.p49_setocgstate_pdf_total ) )
        print( txt_format.format(50, '"/Rendition"',  len(self.p50_rendition_objs), self.p50_rendition_obj_total, self.p50_rendition_pdf_total ) )
        print( txt_format.format(51, '"/Trans"' ,  len(self.p51_trans_objs), self.p51_trans_obj_total, self.p51_trans_pdf_total ) )
        print( txt_format.format(52, '"/GoTo3DView"',  len(self.p52_goto3dview_objs), self.p52_goto3dview_obj_total, self.p52_goto3dview_pdf_total ) )
        print( txt_format.format(53, '"/CheckSum"', len(self.p53_checksum_objs), self.p53_checksum_obj_total, self.p53_checksum_pdf_total))
        #

    #
    def selection(self, index:int) -> list:
        if index == 1:
            return self.p1_page_objs
        elif index == 2:
            return self.p2_encrypt_objs
        elif index == 3:
            return  self.p3_authevent_objs
        elif index == 4:
            return  self.p4_objstm_objs
        elif index == 5:
            return self.p5_js_objs
        elif index == 6:
            return self.p6_javascript_objs
        elif index == 7:
            return self.p7_aa_objs
        elif index == 8:
            return self.p8_xml_objs
        elif index == 9:
            return self.p9_action_objs
        elif index == 10:
            return self.p10_openaction_objs
        elif index == 11:
            return self.p11_acroform_objs
        elif index == 12:
            return self.p12_acrofield_objs
        elif index == 13:
            return  self.p13_fdf_objs
        elif index == 14:
            return  self.p14_xform_objs
        elif index == 15:
            return  self.p15_form_objs
        elif index == 16:
            return self.p16_xfa_objs
        elif index == 17:
            return  self.p17_launch_objs
        elif index == 18:
            return self.p18_jbig2decode_objs
        elif index == 19:
            return self.p19_asciihexdecode_objs
        elif index == 20:
            return self.p20_richmedia_objs
        elif index == 21:
            return  self.p21_fileattachment_objs
        elif index == 22:
            return  self.p22_type_objs
        elif index == 23:
            return self.p23_filespec_objs
        elif index == 24:
            return  self.p24_embeddedfile_objs
        elif index == 25:
            return  self.p25_xobject_objs
        elif index == 26:
            return  self.p26_f_objs
        elif index == 27:
            return self.p27_ef_objs
        elif index == 28:
            return  self.p28_image_objs
        elif index == 29:
            return  self.p29_font_objs
        elif index == 30:
            return  self.p30_fontname_objs
        elif index == 31:
            return self.p31_metadata_objs
        elif index == 32:
            return self.p32_link_objs
        elif index == 33:
            return self.p33_uri_objs
        elif index == 34:
            return self.p34_http_objs
        elif index == 35:
            return self.p35_https_objs
        elif index == 36:
            return  self.p36_ftp_objs
        elif index == 37:
            return  self.p37_ftps_objs
        elif index == 38:
            return self.p38_goto_objs
        elif index == 39:
            return self.p39_gotor_objs
        elif index == 40:
            return  self.p40_gotoe_objs
        elif index == 41:
            return  self.p41_thread_objs
        elif index == 42:
            return  self.p42_sound_objs
        elif index == 43:
            return  self.p43_movie_objs
        elif index == 44:
            return self.p44_hide_objs
        elif index == 45:
            return self.p45_named_objs
        elif index == 46:
            return  self.p46_submitform_objs
        elif index == 47:
            return  self.p47_resetform_objs
        elif index == 48:
            return  self.p48_importdata_objs
        elif index == 49:
            return  self.p49_setocgstate_objs
        elif index == 50:
            return self.p50_rendition_objs
        elif index == 51:
            return self.p51_trans_objs
        elif index == 52:
            return  self.p52_goto3dview_objs
        elif index == 53:
            return  self.p53_checksum_objs
        else:
            return list()


