# Only for Windows 10 / 64 bits
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
class dirData:
    #
    def __init__(self):
        self.r1_file = ''
        self.r2_ads_data = ''
        self.r3_type = ''
    #
#
#
#


#
def dir(path:str='') :
    #
    import subprocess, os
    files = []
    currentDirectory = ''
    #
    script = 'cmd /u /c dir /r {}'.format( path )
    cmd_connect = subprocess.Popen(script, stdout=subprocess.PIPE)
    cmd_bytes = cmd_connect.communicate()
    cmd_string = cmd_bytes[0].decode('u16')
    #
    for line_string in cmd_string.split('\r\n'):
        jj = line_string.find('Directory of')
        if jj != -1:
            currentDirectory = line_string[14:]

        ii = line_string.find('$DATA')
        if ii != -1:
            obj_file  = dirData()
            tmp_file  = line_string[36:].split(sep=':')
            obj_file.r1_file     = tmp_file[0]
            obj_file.r2_ads_data = tmp_file[1]
            #
            check_fd = currentDirectory + '\\' + obj_file.r1_file
            if os.path.isdir( check_fd ):
                obj_file.r3_type = 'Directory'
            elif os.path.isfile( check_fd ):
                obj_file.r3_type = 'File'
            else:
                obj_file.r3_type = 'Unknown'
            #
            files.append(obj_file)
        #
    #
    return files, currentDirectory
#

#
def currentDirectory(path:str='') :
    #
    import subprocess
    #
    script = 'cmd /u /c dir /r {}'.format(path)
    cmd_connect = subprocess.Popen(script, stdout=subprocess.PIPE)
    cmd_bytes = cmd_connect.communicate()
    cmd_string = cmd_bytes[0].decode('u16')
    #
    for line_string in cmd_string.split('\r\n'):
        jj = line_string.find('Directory of')
        if jj != -1:
            currentDirectory = line_string[14:]
            return True, currentDirectory
    #
    return False, ''
#