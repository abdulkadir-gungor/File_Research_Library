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
from lib.hexlib.ReadBinaryFile import readBytes as rfile
from lib.hexlib.ShowHex import show3HexBytes as s3hex
from lib.image.jpg.app.APPTAG import APPTAG as App
from lib.image.jpg.JPGSectors import findSectors
from lib.image.jpg.sector import Sector


class JPGFile:
    #
    def __init__(self, filename:str):
        self.filename = filename
        self.bytes   = rfile(filename=filename)
        self.sectors = []
        self.apps    = []
        tmp_sectors =  findSectors(jpgBytes=self.bytes)
        count = 0
        for ii_sector in tmp_sectors:
            if 1 < ii_sector.type.no < 19 :
                ii_sector.applistno = count
                tmp_app = App( sector=ii_sector ,bytesData=self.bytes[ii_sector.start:ii_sector.end] )
                self.apps.append( tmp_app )
                count += 1
            self.sectors.append(ii_sector)

    # (Func 1) Find Sector Using Element Index
    def findSectorUsingElementIndex(self, index:int) -> Sector:
        for ii_sector in self.sectors:
            if ii_sector.no == index:
               return ii_sector
        return Sector()
    #

    # (Func 2) Find App Using Element Index
    def findAppUsingElementIndex(self, index:int) -> App:
        for ii_app in self.apps:
            if ii_app.a0_sector.no == index:
                return ii_app
        return App(sector=Sector(), bytesData=b'')
    #

    # (Func 3) Application and comment Details
    def func3_showAllAppsDetails(self):
        txt1 = "\t{}){} {:5>} {:15} \t<<{} bayt>> \tStart/End Hex Index:{} - {} \t\t#Element Index:{} # Root Index:{}#"
        count = 1
        for app in self.apps:
            if count == 1 :
                txtheader = "\t{:^115}"
                print( '\t<<File Name:"'+self.filename+'">>' )
                print()
                print(txtheader.format(" JPG/JPEG APPLICATION AND COMMENT SEGMENTS " ))
                print( '\t' + '-'*115 )
            #
            if app.a0_sector.root == 0:
                print(txt1.format( count ,'', app.a0_sector.type.shortname ,"('"+app.version()+"')" , (app.a0_sector.end-app.a0_sector.start) ,app.a0_sector.start, app.a0_sector.end ,app.a0_sector.no, app.a0_sector.root) )
            else:
                print(txt1.format( '(*',' '+str(count)+')',  app.a0_sector.type.shortname, "('"+app.version()+"')" , (app.a0_sector.end-app.a0_sector.start) , app.a0_sector.start, app.a0_sector.end , app.a0_sector.no, app.a0_sector.root) )
            #
            print('\t'+"~HEX~")
            if app.a0_sector.start+20 < app.a0_sector.end:
                s3hex(dataBytes=self.bytes[app.a0_sector.start:app.a0_sector.start+20], index=app.a0_sector.start+1, columnSize=20 )
            else:
                s3hex(dataBytes=self.bytes[app.a0_sector.start:app.a0_sector.end], index=app.a0_sector.start+1, columnSize=20)
            print('\t' + '-' * 115)
            count += 1

    # (Func 3) Application and Comment
    def func3_showAllApps(self):
        txt1 = "\t{}{}) {} {:5>} {:15} \t<<{} bayt>> \tStart/End Hex Index:{} - {} \t\t#Element Index:{} # Root Index:{}#"
        count = 1
        for app in self.apps:
            if count == 1 :
                txtheader = "\t{:^115}"
                print( '\t<<File Name:"'+self.filename+'">>' )
                print()
                print(txtheader.format(" JPG/JPEG APPLICATION AND COMMENT SEGMENTS " ))
                print( '\t' + '-'*115 )
            #
            if app.a0_sector.root == 0:
                print(txt1.format( '' ,count, '' ,app.a0_sector.type.shortname ,"('"+app.version()+"')" , (app.a0_sector.end-app.a0_sector.start) ,app.a0_sector.start, app.a0_sector.end ,app.a0_sector.no, app.a0_sector.root) )
            else:
                print(txt1.format( '\t',count, '*' ,app.a0_sector.type.shortname, "('"+app.version()+"')" , (app.a0_sector.end-app.a0_sector.start) , app.a0_sector.start, app.a0_sector.end , app.a0_sector.no, app.a0_sector.root) )
            if len(self.apps) == count:
                print('\t' + '-' * 115)
            count += 1

    # (Func 3) Application and Comment
    def func3_showAllAppsSummary(self):
        txt1 = "\t{}{}) {} {:5>} {:15} \t<<{} bayt>>"
        count = 1
        for app in self.apps:
            if count == 1 :
                txtheader = "\t{:^70}"
                print( '\t<<File Name:"'+self.filename+'">>' )
                print()
                print(txtheader.format(" JPG/JPEG APPLICATION AND COMMENT SEGMENTS " ))
                print( '\t' + '-'*70 )
            #
            if app.a0_sector.root == 0:
                print(txt1.format( '',count,'', app.a0_sector.type.shortname ,"('"+app.version()+"')" , (app.a0_sector.end-app.a0_sector.start) ))
            else:
                print(txt1.format('\t',count, '*', app.a0_sector.type.shortname, "('" + app.version() + "')",
                                  (app.a0_sector.end - app.a0_sector.start)))
            #
            if len(self.apps) == count:
                print('\t' + '-' * 70)
            count += 1

    # (Func 3) Application and comment
    def func3_findAllApp(self, index:int) -> App:
        if  len(self.apps) >= index > 0:
            return self.apps[(index-1)]
        else:
            return App( Sector(), bytesData=b'' )
        #

    # (Func 4)
    def func4_showSegmentsDetails(self):
        txt1 = "\t{}{}) {} {:<10} {:<15} \t<<{} bayt>> \tStart/End Hex Index:{} - {} \t\t#Element Index:{} # Root Index:{}#"
        count = 1
        for segment in self.sectors:
            if 24 < segment.type.no < 33:
                pass
            else:
                if count == 1 :
                    txtheader = "\t{:^115}"
                    print( '\t<<File Name:"'+self.filename+'">>' )
                    print()
                    print(txtheader.format(" JPG/JPEG ALL SEGMENTS (EXCEPT RST) " ))
                    print( '\t' + '-'*115 )
                #
                if segment.root == 0:
                    if segment.applistno != -1:
                        tmp_txt = txt1.format('',count, '' , segment.type.shortname ,"('"+self.apps[segment.applistno].version()+"')"
                                              , (segment.end - segment.start) , segment.start, segment.end, segment.no
                                              , segment.root )
                    else:
                        tmp_txt = txt1.format('',count, '' ,segment.type.shortname ,''
                                              , (segment.end - segment.start) , segment.start, segment.end, segment.no
                                              , segment.root )
                else:
                    if segment.applistno != -1:
                        tmp_txt = txt1.format('(*) ', count ,'', segment.type.shortname ,"('"+self.apps[segment.applistno].version()+"')"
                                              , (segment.end - segment.start) , segment.start, segment.end, segment.no
                                              , segment.root )
                    else:
                        tmp_txt = txt1.format('(*) ',  count , '' ,segment.type.shortname ,''
                                              , (segment.end - segment.start) , segment.start, segment.end, segment.no
                                              , segment.root )
                print(tmp_txt)
                print('\t' + "~HEX~")
                if segment.start + 20 < segment.end:
                    s3hex(dataBytes=self.bytes[segment.start:segment.start + 20], index=segment.start+1,
                          columnSize=20)
                else:
                    s3hex(dataBytes=self.bytes[segment.start:segment.end], index=segment.start+1,
                          columnSize=20)
                print('\t' + '-' * 115)
                count += 1

    # (Func 4)
    def func4_showSegments(self):
        txt1 = "\t{}{}) {} {:<10} {:<15} \t<<{} bayt>> \tStart/End Hex Index:{} - {} \t\t#Element Index:{} # Root Index:{}#"
        count = 1
        for segment in self.sectors:
            if 24 < segment.type.no < 33:
                pass
            else:
                if count == 1 :
                    txtheader = "\t{:^115}"
                    print( '\t<<File Name:"'+self.filename+'">>' )
                    print()
                    print(txtheader.format("JPG/JPEG ALL SEGMENTS (EXCEPT RST)" ))
                    print( '\t' + '-'*115 )
                #
                if segment.root == 0:
                    if segment.applistno != -1:
                        tmp_txt = txt1.format('',count, '' , segment.type.shortname ,"('"+self.apps[segment.applistno].version()+"')"
                                              , (segment.end - segment.start) , segment.start, segment.end, segment.no
                                              , segment.root )
                    else:
                        tmp_txt = txt1.format('',count, '' ,segment.type.shortname ,''
                                              , (segment.end - segment.start) , segment.start, segment.end, segment.no
                                              , segment.root )
                else:
                    if segment.applistno != -1:
                        tmp_txt = txt1.format('\t',count ,'*', segment.type.shortname ,"('"+self.apps[segment.applistno].version()+"')"
                                              , (segment.end - segment.start) , segment.start, segment.end, segment.no
                                              , segment.root )
                    else:
                        tmp_txt = txt1.format('\t',count, '*' ,segment.type.shortname ,''
                                              , (segment.end - segment.start) , segment.start, segment.end, segment.no
                                              , segment.root )
                print(tmp_txt)
                count += 1
        print('\t' + '-' * 115)

    # (Func 4)
    def func4_showSegmentsSummary(self):
        txt1 = "\t{}{}) {} {:<10} {:<15} \t<<{} bayt>>"
        count = 1
        for segment in self.sectors:
            if 24 < segment.type.no < 33:
                pass
            else:
                if count == 1 :
                    txtheader = "\t{:^70}"
                    print( '\t<<File Name:"'+self.filename+'">>' )
                    print()
                    print(txtheader.format(" JPG/JPEG ALL SEGMENTS (EXCEPT RST) " ))
                    print( '\t' + '-'*70 )
                #
                if segment.root == 0:
                    if segment.applistno != -1:
                        tmp_txt = txt1.format('',count, '' , segment.type.shortname ,"('"+self.apps[segment.applistno].version()+"')"
                                              , (segment.end - segment.start) )
                    else:
                        tmp_txt = txt1.format('',count, '' ,segment.type.shortname ,''
                                              , (segment.end - segment.start) )
                else:
                    if segment.applistno != -1:
                        tmp_txt = txt1.format('\t',count ,'*', segment.type.shortname ,"('"+self.apps[segment.applistno].version()+"')"
                                              , (segment.end - segment.start) )
                    else:
                        tmp_txt = txt1.format('\t',count, '*' ,segment.type.shortname ,''
                                              , (segment.end - segment.start))
                print(tmp_txt)
                count += 1
        print('\t' + '-' * 70)

    # (Func 4)
    def func4_findSegment(self, index:int) -> Sector:
        count = 1
        for segment in self.sectors:
            if 24 < segment.type.no < 33:
                pass
            else:
                if index == count:
                    return segment
                count += 1
        return Sector()

    # (Func 5)
    def func5_showAllSegmentsDetails(self):
        txt1 = "\t{}{}) {} {:<10} {:<15} \t<<{} bayt>> \tStart/End Hex Index:{} - {} \t\t#Element Index:{} # Root Index:{}#"
        count = 1
        for segment in self.sectors:
            if count == 1:
                txtheader = "\t{:^115}"
                print('\t<<File Name:"' + self.filename + '">>')
                print()
                print(txtheader.format(" JPG/JPEG ALL SEGMENTS "))
                print('\t' + '-' * 115)
            #
            if segment.root == 0:
                if segment.applistno != -1:
                    tmp_txt = txt1.format('', count, '', segment.type.shortname,
                                          "('" + self.apps[segment.applistno].version() + "')"
                                          , (segment.end - segment.start), segment.start, segment.end, segment.no
                                          , segment.root)
                else:
                    tmp_txt = txt1.format('', count, '', segment.type.shortname, ''
                                          , (segment.end - segment.start), segment.start, segment.end, segment.no
                                          , segment.root)
            else:
                if segment.applistno != -1:
                    tmp_txt = txt1.format('\t', count, '*', segment.type.shortname,
                                          "('" + self.apps[segment.applistno].version() + "')"
                                          , (segment.end - segment.start), segment.start, segment.end, segment.no
                                          , segment.root)
                else:
                    tmp_txt = txt1.format('\t', count, '*', segment.type.shortname, ''
                                          , (segment.end - segment.start), segment.start, segment.end, segment.no
                                          , segment.root)
            print(tmp_txt)
            count += 1
            print('\t' + "~HEX~")
            if segment.start + 20 < segment.end:
                s3hex(dataBytes=self.bytes[segment.start:segment.start + 20], index=segment.start+1,
                      columnSize=20)
            else:
                s3hex(dataBytes=self.bytes[segment.start:segment.end], index=segment.start+1,
                      columnSize=20)
            print('\t' + '-' * 115)

    # (Func 5)
    def func5_showAllSegments(self):
        txt1 = "\t{}{}) {} {:<10} {:<15} \t<<{} bayt>> \tStart/End Hex Index:{} - {} \t\t#Element Index:{} # Root Index:{}#"
        count = 1
        for segment in self.sectors:
            if count == 1:
                txtheader = "\t{:^115}"
                print('\t<<File Name:"' + self.filename + '">>')
                print()
                print(txtheader.format(" JPG/JPEG ALL SEGMENTS "))
                print('\t' + '-' * 115)
            #
            if segment.root == 0:
                if segment.applistno != -1:
                    tmp_txt = txt1.format('', count, '', segment.type.shortname,
                                          "('" + self.apps[segment.applistno].version() + "')"
                                          , (segment.end - segment.start), segment.start, segment.end, segment.no
                                          , segment.root)
                else:
                    tmp_txt = txt1.format('', count, '', segment.type.shortname, ''
                                          , (segment.end - segment.start), segment.start, segment.end, segment.no
                                          , segment.root)
            else:
                if segment.applistno != -1:
                    tmp_txt = txt1.format('\t', count, '*', segment.type.shortname,
                                          "('" + self.apps[segment.applistno].version() + "')"
                                          , (segment.end - segment.start), segment.start, segment.end, segment.no
                                          , segment.root)
                else:
                    tmp_txt = txt1.format('\t', count, '*', segment.type.shortname, ''
                                          , (segment.end - segment.start), segment.start, segment.end, segment.no
                                          , segment.root)
            print(tmp_txt)
            count += 1
        print('\t' + '-' * 115)

    # (Func 5)
    def func5_showAllSegmentsSummary(self):
        txt1 = "\t{}{}) {} {:<10} {:<15} \t<<{} bayt>>"
        count = 1
        for segment in self.sectors:
            if count == 1:
                txtheader = "\t{:^70}"
                print('\t<<File Name:"' + self.filename + '">>')
                print()
                print(txtheader.format(" JPG/JPEG ALL SEGMENTS "))
                print('\t' + '-' * 70)
            #
            if segment.root == 0:
                if segment.applistno != -1:
                    tmp_txt = txt1.format('', count, '', segment.type.shortname,
                                          "('" + self.apps[segment.applistno].version() + "')"
                                          , (segment.end - segment.start) )
                else:
                    tmp_txt = txt1.format('', count, '', segment.type.shortname, ''
                                          , (segment.end - segment.start) )
            else:
                if segment.applistno != -1:
                    tmp_txt = txt1.format('\t', count, '*', segment.type.shortname,
                                          "('" + self.apps[segment.applistno].version() + "')"
                                          , (segment.end - segment.start) )
                else:
                    tmp_txt = txt1.format('\t', count, '*', segment.type.shortname, ''
                                          , (segment.end - segment.start) )
            print(tmp_txt)
            count += 1
        print('\t' + '-' * 70)

    # (Func 5)
    def func5_findAllSegment(self, index:int) -> Sector:
        if  0 < index <= len(self.sectors):
            return self.sectors[index-1]
        else:
            return Sector()
    #

    # graph
    def graph_apps(self):
        count = 1
        txt_tmp = '{} Element index :{:<4d} | root :{:<4d} | {:>5} | {:^15} | Length :{:<9d} (bayt) --> Start Index :{} - End Index :{}'
        txt1    = '\t|--->'
        txt2    = '\t|------>'
        for app in self.apps:
            if count == 1:
                print('\t<<File Name:"' + self.filename + '">>')
                print()
                print( '\t{:^80}'.format(' JPG/JPEG APPLICATION AND COMMENT SEGMENTS ') )
                print( '\t'+('#'*80) )
            #
            if app.a0_sector.root == 0:
                txtscreen = txt_tmp.format(txt1, app.a0_sector.no, app.a0_sector.root ,app.a0_sector.type.shortname ,"'"+app.version()+"'", (app.a0_sector.end-app.a0_sector.start), app.a0_sector.start, app.a0_sector.end )
            else:
                txtscreen = txt_tmp.format(txt2, app.a0_sector.no, app.a0_sector.root , app.a0_sector.type.shortname ,"'"+app.version()+"'", (app.a0_sector.end-app.a0_sector.start), app.a0_sector.start, app.a0_sector.end )
            #
            print(txtscreen)
            count += 1
    #

    # graph
    def graph_segments(self):
        count = 1
        txt_tmp = '{} Element index :{:<4d} | root :{:<4d} | {:>5} | {:^15} | Length :{:<9d} (bayt) --> Start Index :{} - End Index :{}'
        txt1 = '\t|--->'
        txt2 = '\t|------>'
        for sector in self.sectors:
            if  24 < sector.type.no < 33:
                pass
            else:
                if count == 1:
                    print('\t<<File Name:"' + self.filename + '">>')
                    print()
                    print('\t{:^80}'.format(' JPG/JPEG ALL SEGMENTS (EXCEPT RST) ') )
                    print('\t' + ('#' * 80))
                #
                if sector.applistno == -1:
                    app_txt = " * "
                else:
                    app_txt = self.apps[sector.applistno].version()
                #
                if sector.root == 0:
                    txtscreen = txt_tmp.format(txt1, sector.no , sector.root , sector.type.shortname ,
                                               "'" + app_txt + "'", (sector.end - sector.start),
                                               sector.start, sector.end)
                else:
                    txtscreen = txt_tmp.format(txt2, sector.no , sector.root , sector.type.shortname ,
                                               "'" + app_txt + "'", (sector.end - sector.start),
                                               sector.start, sector.end)
                #
                print(txtscreen)
                count += 1
    #

    # graph
    def graph_allsegments(self):
        count = 1
        txt_tmp = '{} Element index :{:<4d} | root :{:<4d} | {:>5} | {:^15} | Length :{:<9d} (bayt) --> Start Index :{} - End Index :{}'
        txt1 = '\t|--->'
        txt2 = '\t|------>'
        for sector in self.sectors:
            if count == 1:
                print('\t<<File Name:"' + self.filename + '">>')
                print()
                print('\t{:^80}'.format(' JPG/JPEG ALL SEGMENTS '))
                print('\t' + ('#' * 80))
            #
            if sector.applistno == -1:
                app_txt = " * "
            else:
                app_txt = self.apps[sector.applistno].version()
            #
            if sector.root == 0:
                txtscreen = txt_tmp.format(txt1, sector.no, sector.root, sector.type.shortname,
                                           "'" + app_txt + "'", (sector.end - sector.start),
                                           sector.start, sector.end)
            else:
                txtscreen = txt_tmp.format(txt2, sector.no, sector.root, sector.type.shortname,
                                           "'" + app_txt + "'", (sector.end - sector.start),
                                           sector.start, sector.end)
            #
            print(txtscreen)
            count += 1
    #