############################################################################
#
#   © 2020 ABDULKADİR GÜNGÖR All Rights Reserved
#   Contact email address: abdulkadir_gungor@outlook.com
#
#	Developper:	Abdulkadir GÜNGÖR (abdulkadir_gungor@outlook.com)
#	Date:	09/2020
#	All Rights Reserved (Tüm Hakları Saklıdır)
#
############################################################################
class FileStorage:
    #
    def __init__(self):
        self.f1_name = ''
        self.f2_relativepath = ''
        self.f3_fullpath = ''

#
###
class File:
    #
    def __init__(self, path:str=''):
        self.__path_input = path
        self.current_directory = ''
        self.checkFile = False
        self.checkDirectory  = False
        self.file = FileStorage()
        self.update()
    #
    def __reset(self):
        self.checkDirectory = False
        self.checkFile = False
        self.file  = FileStorage()
    #
    def update(self):
        #
        import subprocess
        self.__reset()
        #
        script = 'cmd /u /c dir {}'.format(self.__path_input)
        cmd_connect = subprocess.Popen(script, stdout=subprocess.PIPE, stderr=False)
        cmd_bytes = cmd_connect.communicate()
        cmd_string = cmd_bytes[0].decode('u16')
        #
        line_list = cmd_string.split(sep='\r\n')
        isCurrentDirectory = line_list[3]
        isFile = line_list[5]
        #
        valDir = isCurrentDirectory.find('Directory of')
        valFile = isFile.find('<DIR>')
        #
        if valDir != -1 and len(isCurrentDirectory[14:]) > 0 :
            self.current_directory = isCurrentDirectory[14:]
        #
        if valFile == -1  and len(isFile[36:]) > 0 :
            file_obj = FileStorage()
            file_obj.f1_name = isFile[36:]
            file_obj.f2_relativepath = file_obj.f1_name
            file_obj.f3_fullpath = self.current_directory + '\\' +  file_obj.f1_name
            self.file = file_obj
            self.checkFile = True
            self.checkDirectory = False
        elif valFile != -1:
            file_obj = FileStorage()
            file_obj.f1_name = 'filename.nothing'
            file_obj.f2_relativepath = 'filename.nothing'
            file_obj.f3_fullpath = self.current_directory + '\\' + file_obj.f1_name
            self.file = file_obj
            self.checkFile = False
            self.checkDirectory = True
        else:
            check_name = self.__path_input.find('\\')
            if check_name != -1:
                filename_list =  self.__path_input.split(sep='\\')
                filename_str = filename_list[-1]
            else:
                filename_str = self.__path_input
            file_obj = FileStorage()
            file_obj.f1_name = filename_str
            file_obj.f2_relativepath = filename_str
            file_obj.f3_fullpath = self.current_directory + '\\' + file_obj.f1_name
            self.file = file_obj
            self.checkFile = False
            self.checkDirectory = False


#
class Directory:
    #
    def __init__(self, path:str=''):
        self.__path_input = path
        self.current_directory = ''
        self.files = []
        self.update()

    def update(self):
        #
        import subprocess
        self.__reset()
        #
        script = 'cmd /u /c dir /s {}'.format(self.__path_input)
        cmd_connect = subprocess.Popen(script, stdout=subprocess.PIPE, stderr=False)
        cmd_bytes = cmd_connect.communicate()
        cmd_string = cmd_bytes[0].decode('u16')
        #
        cmd_string_list = cmd_string.split(sep='\r\n\r\n')
        if len(cmd_string_list) > 3:
            dir_and_files_list = cmd_string_list[1:-1]
            if len(dir_and_files_list)%2 == 0:
                count = 1
                sub_directory = ''
                for str_tmp in dir_and_files_list:
                    if count == 1:
                        result, directory = self.__directory(data=str_tmp)
                        if result:
                            self.current_directory = directory
                        else:
                            self.__reset()
                    elif count == 2:
                        self.__firstFiles(data=str_tmp)
                    elif count%2 == 1:
                        result, directory = self.__directory(data=str_tmp)
                        if result:
                            sub_directory = directory
                        else:
                            self.__reset()
                    elif count%2 == 0:
                        self.__files(directory=sub_directory, data=str_tmp)
                    #
                    count += 1
            else:
                self.__reset()
                return
    #
    def showDebug(self):
        print('\tMain Directory     : "' + self.current_directory + '"' )
        print('\tSum Of The File(s) : ' + str( len(self.files) ) )
        print()
        count  = 0
        txt_head1 = '\tNo  \t***FILE(S)***'
        txt_head2 = '\t--- \t-------------'
        txt_format = '\t{:<3} \tName : "{}" \t Relative Path : "{}"  \t Full Path : "{}"'
        for file in self.files:
            if count == 0:
                print(txt_head1)
                print(txt_head2)
            print( txt_format.format(count, file.f1_name, file.f2_relativepath , file.f3_fullpath )   )
            count += 1

    #
    def show(self):
        print('\tMain Directory     : "' + self.current_directory + '"' )
        print('\tSum Of The File(s) : ' + str( len(self.files) ) )
        print()
        count  = 1
        txt_head1 = '\t***FILE(S)***'
        txt_head2 = '\t' + ('-'*25)
        txt_format = '\t"{}"'
        for file in self.files:
            if count == 1:
                print(txt_head1)
                print(txt_head2)
            print( txt_format.format(file.f2_relativepath)   )
            count += 1
    #
    def __reset(self):
        self.current_directory = ''
        self.files = []

    #
    def __directory(self, data:str):
        val = data.find('Directory of')
        if val != -1 and len(data[14:]) > 0:
            return True, data[14:]
        else:
            return False, ''

    #
    def __firstFiles(self, data:str):
        data_list = data.split(sep='\r\n')
        if len(data_list) > 1:
            for line in data_list[0:-1]:
                val= line.find('<DIR>')
                if val == -1 and len(line[36:]) > 0:
                    file_name = line[36:]
                    file_obj = FileStorage()
                    file_obj.f1_name = file_name
                    file_obj.f2_relativepath = file_name
                    file_obj.f3_fullpath = self.current_directory + '\\' + file_name
                    self.files.append(file_obj)

    #
    def __files(self, directory:str, data:str):
        data_list = data.split(sep='\r\n')
        if len(data_list) > 1:
            for line in data_list[0:-1]:
                val= line.find('<DIR>')
                if val == -1 and len(line[36:]) > 0:
                    file_name = line[36:]
                    file_obj = FileStorage()
                    file_obj.f1_name = file_name
                    cd_length = len(self.current_directory)
                    file_obj.f2_relativepath = directory[cd_length+1:] + '\\' + file_name
                    file_obj.f3_fullpath = directory + '\\' + file_name
                    self.files.append(file_obj)


