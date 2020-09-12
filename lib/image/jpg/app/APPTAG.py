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
from lib.image.jpg.app.tags.JFIF import JFIF as jfif
from lib.image.jpg.app.tags.JFXX import JFXX as jfxx
from lib.image.jpg.app.tags.ICC_PROFILE import ICC_PROFILE as icc_profile
from lib.image.jpg.app.tags.EXIF import EXIF as exif
from lib.image.jpg.app.tags.XMP import XMP as xmp
from lib.image.jpg.app.tags.PHOTOSHOP import PHOTOSHOP as photoshop
from lib.image.jpg.app.tags.MPF import MPF as mpf
from lib.image.jpg.app.tags.ADOBE import ADOBE as adobe
from lib.image.jpg.app.tags.ADOBE_CM import ADOBE_CM as adobe_cm
from lib.image.jpg.app.APPHEX import APPHEX as apphex
from lib.image.jpg.sector import Sector

class APPTAG:
    #
    #
    def __init__(self, sector:Sector, bytesData:bytes ):
        #
        self.a0_sector = sector
        #
        # (1) check jfif
        if jfif.check(bytesData):
            self.a1_tag_no = 1
            self.a2_tag_name = 'JFIF'
            self.a3_tag_obj = jfif(bytesData=bytesData)
        # (2) check jfxx
        elif jfxx.check(bytesData):
            self.a1_tag_no = 2
            self.a2_tag_name = 'JFXX'
            self.a3_tag_obj  = jfxx(bytesData=bytesData)
        # (3) check exif
        elif exif.check(bytesData):
            self.a1_tag_no = 3
            self.a2_tag_name = 'Exif'
            self.a3_tag_obj  = exif(bytesData=bytesData)
        # (4) check icc_profile
        elif icc_profile.check(bytesData):
            self.a1_tag_no = 4
            self.a2_tag_name = 'ICC_PROFILE'
            self.a3_tag_obj = icc_profile(bytesData=bytesData)
        # (5) check xmp
        elif xmp.check(bytesData):
            self.a1_tag_no = 5
            self.a2_tag_name = 'XMP'
            self.a3_tag_obj  = xmp(bytesData=bytesData)
        # (6) check mpf
        elif mpf.check(bytesData):
            self.a1_tag_no = 6
            self.a2_tag_name = 'MPF'
            self.a3_tag_obj  = mpf(bytesData=bytesData)
        # (7) check photoshop
        elif photoshop.check(bytesData):
            self.a1_tag_no = 7
            self.a2_tag_name = 'Photoshop'
            self.a3_tag_obj = photoshop(bytesData=bytesData)
        # (8) check adobe
        elif adobe.check(bytesData):
            self.a1_tag_no = 8
            self.a2_tag_name = 'Adobe'
            self.a3_tag_obj = adobe(bytesData=bytesData)
        # (9) check adobe_cm
        elif adobe_cm.check(bytesData):
            self.a1_tag_no = 9
            self.a2_tag_name = 'Adobe CM'
            self.a3_tag_obj = adobe_cm(bytesData=bytesData)
        else:
            self.a1_tag_no = -1
            self.a2_tag_name = 'UNKNOWN'
            self.a3_tag_obj = apphex(bytesData=bytesData)

    def showHeader(self):
        if self.a1_tag_no == 1:   # 1 JFIF
            self.a3_tag_obj.show()
        elif self.a1_tag_no == 2: # 2 JFXX
            self.a3_tag_obj.show()
        elif self.a1_tag_no == 3: # 3 Exif
            self.a3_tag_obj.showHeader()
        elif self.a1_tag_no == 4: # 4 ICC_PROFILE
            self.a3_tag_obj.showHeader()
        elif self.a1_tag_no == 5: # 5 XMP
            self.a3_tag_obj.showHeader()
        elif self.a1_tag_no == 6: # 6 MPF
            self.a3_tag_obj.showHeader()
        elif self.a1_tag_no == 7: # 7 Photoshop
            self.a3_tag_obj.showHeader()
        elif self.a1_tag_no == 8: # 8 Adobe
            self.a3_tag_obj.showHeader()
        elif self.a1_tag_no == 9: # 9 Adobe_CM
            self.a3_tag_obj.showHeader()

    def show(self):
        if self.a1_tag_no == 1:   # 1 JFIF
            self.a3_tag_obj.showAll()
        elif self.a1_tag_no == 2: # 2 JFXX
            self.a3_tag_obj.showAll()
        elif self.a1_tag_no == 3: # 3 Exif
            self.a3_tag_obj.showHeader()
        elif self.a1_tag_no == 4: # 4 ICC_PROFILE
            self.a3_tag_obj.showHeader()
        elif self.a1_tag_no == 5: # 5 XMP
            self.a3_tag_obj.show()
        elif self.a1_tag_no == 6: # 6 MPF
            self.a3_tag_obj.showHeader()
        elif self.a1_tag_no == 7: # 7 Photoshop
            self.a3_tag_obj.showHeader()
        elif self.a1_tag_no == 8: # 8 Adobe
            self.a3_tag_obj.show()
        elif self.a1_tag_no == 9: # 9 Adobe_CM
            self.a3_tag_obj.show()
        elif self.a1_tag_no == 10: # Unknown
            self.a3_tag_obj.show()
    #
    def version(self) -> str:
        if self.a1_tag_no == 1:   # 1 JFIF
            return self.a3_tag_obj.version()
        elif self.a1_tag_no == 2: # 2 JFXX
            return  self.a3_tag_obj.version()
        elif self.a1_tag_no == 3: # 3 Exif
            return self.a2_tag_name
        elif self.a1_tag_no == 4: # 4 ICC_PROFILE
            return self.a2_tag_name
        elif self.a1_tag_no == 5: # 5 XMP
            return self.a2_tag_name
        elif self.a1_tag_no == 6: # 6 MPF
            return self.a3_tag_obj.version()
        elif self.a1_tag_no == 7: # 7 Photoshop
            return self.a2_tag_name
        elif self.a1_tag_no == 8: # 8 Adobe
            return self.a2_tag_name
        elif self.a1_tag_no == 9: # 9 Adobe_CM
            return self.a2_tag_name
        else:
            return self.a2_tag_name

    #
    def showVersion(self) :
        print('\t'+self.version())
    #

    #
    def no3_exif_showAllTagsNames(self):
        if self.a1_tag_no == 3:
            self.a3_tag_obj.showAllTagNames()
    #

    #
    def no3_exif_show0IFDTagsNames(self):
        if self.a1_tag_no == 3:
            self.a3_tag_obj.show0IFDTagNames()
    #

    #
    def no3_exif_show0IFDTag(self, index:int):
        if self.a1_tag_no == 3:
            try:
                self.a3_tag_obj. show0IFDTag(index)
            except:
                pass
    #

    #
    def no3_exif_showExifIFDTagsNames(self):
        if self.a1_tag_no == 3:
            self.a3_tag_obj.showExifIFDTagNames()
    #

    #
    def no3_exif_showExifIFDTag(self, index:int):
        if self.a1_tag_no == 3:
            try:
                self.a3_tag_obj.showExifIFDTag(index)
            except:
                pass
    #

    #
    def no3_exif_showInteroperabilityIFDTagsNames(self):
        if self.a1_tag_no == 3:
            self.a3_tag_obj.showInteroperabilityIFDTagNames()
    #

    #
    def no3_exif_showInterOperabilityIFDTag(self, index:int):
        if self.a1_tag_no == 3:
            try:
                self.a3_tag_obj.showInterOperabilityIFDTag(index)
            except:
                pass
    #


    #
    def no3_exif_showGpsIFDTagsNames(self):
        if self.a1_tag_no == 3:
            self.a3_tag_obj.showGpsIFDTagNames()
    #

    #
    def no3_exif_showGpsIFDTag(self, index:int):
        if self.a1_tag_no == 3:
            try:
                self.a3_tag_obj.showGpsIFDTag(index)
            except:
                pass
    #

    #
    def no3_exif_show1IFDTagNames(self):
        if self.a1_tag_no == 3:
            self.a3_tag_obj.show1IFDTagNames()
    #

    #
    def no3_exif_show1IFDTag(self, index:int):
        if self.a1_tag_no == 3:
            try:
                self.a3_tag_obj.show1IFDTag(index)
            except:
                pass
    #

    #
    def no6_mpf_showHex(self):
        if self.a1_tag_no == 6:
            self.a3_tag_obj.showHex()
    #

    #  4-icc_profile 6-mpf 7-photoshop
    def showBodyTagsNames(self):
        if self.a1_tag_no == 4: # icc_profile
            self.a3_tag_obj.showBodyTags()
        elif self.a1_tag_no == 6: # mpf
            self.a3_tag_obj.showTagsNames()
        elif self.a1_tag_no == 7: # photoshop
            self.a3_tag_obj.showTagsNames()
    #

    # 4-icc_profile 6-mpf 7-photoshop
    def showBodyTag(self, index:int):
        if self.a1_tag_no == 4:
            try:
                self.a3_tag_obj. showBodyTag(index)
            except:
                pass
        elif self.a1_tag_no == 6:
            try:
                self.a3_tag_obj.showTag(index)
            except:
                pass
        elif self.a1_tag_no == 7:
            try:
                self.a3_tag_obj.showTag(index)
            except:
                pass
    #
