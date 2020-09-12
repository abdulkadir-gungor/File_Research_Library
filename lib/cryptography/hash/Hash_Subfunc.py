#!/usr/bin/python3
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
# Data Storage
class Hash:
    #
    def __init__(self):
        self.no   = -1
        self.name = ''

# CRC16
def CRC16(hash:str):
    if len(hash) == 4:
        if not hash.isalpha() and hash.isalnum():
            hash = Hash()
            hash.no = 101020
            hash.name = 'CRC-16'
            return hash
    return None

# CRC16CCITT
def CRC16CCITT(hash:str):
    if len(hash) == 4:
        if not hash.isdigit() and not hash.isalpha() and hash.isalnum():
            hash = Hash()
            hash.no = 101040
            hash.name = 'CRC-16-CCITT'
            return hash
    return None

# FCS16
def FCS16(hash:str):
    if len(hash) == 4:
        if not hash.isdigit() and not hash.isalpha() and hash.isalnum():
            hash = Hash()
            hash.no = 101060
            hash.name = 'FFCCS-16'
            return hash
    return None

# CRC32
def CRC32(hash:str):
    if len(hash) == 8:
        if not hash.isdigit() and not hash.isalpha() and hash.isalnum():
            hash = Hash()
            hash.no = 101100
            hash.name = 'CRC-32'
            return hash
    return None

# ADLER32
def ADLER32(hash:str):
    if len(hash) == 8:
        if not hash.isdigit() and not hash.isalpha() and hash.isalnum():
            hash = Hash()
            hash.no   = 101080
            hash.name = 'ADLER-32'
            return hash
    return None

# CRC32B
def CRC32B(hash:str):
    if len(hash) == 8:
        if not hash.isdigit() and not hash.isalpha() and hash.isalnum():
            hash = Hash()
            hash.no   = 101120
            hash.name = 'CRC-32B'
            return hash
    return None

# XOR32
def XOR32(hash:str):
    if len(hash) == 8:
        if not hash.isdigit() and not hash.isalpha() and hash.isalnum():
            hash = Hash()
            hash.no = 101140
            hash.name = 'XOR-32'
            return hash
    return None

# GHash323
def GHash323(hash:str):
    if len(hash) == 8:
        if hash.isdigit() and not hash.isalpha() and hash.isalnum():
            hash = Hash()
            hash.no   = 101180
            hash.name = 'GHash-32-3'
            return hash
    return None

# GHash325
def GHash325(hash:str):
    if len(hash) == 8:
        if hash.isdigit() and not hash.isalpha() and hash.isalnum():
            hash = Hash()
            hash.no  = 101160
            hash.name = 'GHash-32-5'
            return hash
    return None

# DESUnix
def DESUnix(hash:str):
    if len(hash) == 13:
        if not hash.isdigit() and not hash.isalpha():
            hash = Hash()
            hash.no   = 101200
            hash.name = 'DES(Unix)'
            return hash
    return None

# MD5Half
def MD5Half(hash:str):
    if len(hash) == 16:
        if not hash.isdigit() and not hash.isalpha() and hash.isalnum():
            hash = Hash()
            hash.no = 101260
            hash.name = 'MD5(Half)'
            return hash
    return None

# MD5Middle
def MD5Middle(hash:str):
    if len(hash) == 16:
        if not hash.isdigit() and not hash.isalpha() and hash.isalnum():
            hash = Hash()
            hash.no = 101240
            hash.name = 'MD5(Middle)'
            return hash
    return None

# MySQL
def MySQL(hash:str):
    if len(hash) == 16:
        if not hash.isdigit() and not hash.isalpha() and hash.isalnum():
            hash = Hash()
            hash.no = 101220
            hash.name = 'MySQL'
            return hash
    return None

# DomainCachedCredentials
def DomainCachedCredentials(hash:str):
    if len(hash) == 32:
        if not hash.isdigit() and not hash.isalpha() and hash.isalnum():
            hash = Hash()
            hash.no = 101300
            hash.name = 'Domain Cached Credentials - MD4(MD4(($pass)).(strtolower($username)))'
            return hash
    return None

# Haval128
def Haval128(hash:str):
    if len(hash) == 32:
        if not hash.isdigit() and not hash.isalpha()  and hash.isalnum():
            hash = Hash()
            hash.no = 101480
            hash.name = 'Haval-128'
            return hash
    return None

# Haval128HMAC
def Haval128HMAC(hash:str):
    if len(hash) == 32:
        if not hash.isdigit() and not hash.isalpha()  and hash.isalnum():
            hash = Hash()
            hash.no = 101500
            hash.name = 'Haval-128(HMAC)'
            return hash
    return None

# MD2
def MD2(hash:str):
    if len(hash) == 32:
        if not hash.isdigit() and not hash.isalpha() and  hash.isalnum():
            hash = Hash()
            hash.no = 101380
            hash.name = 'MD2'
            return hash
    return None

# MD2HMAC
def MD2HMAC(hash:str):
    if len(hash) == 32:
        if not hash.isdigit() and not hash.isalpha() and hash.isalnum():
            hash = Hash()
            hash.no = 101440
            hash.name = 'MD2(HMAC)'
            return hash
    return None

# MD4
def MD4(hash:str):
    if len(hash) == 32:
        if not hash.isdigit() and not hash.isalpha() and hash.isalnum():
            hash = Hash()
            hash.no   = 101360
            hash.name = 'MD4'
            return hash
    return None

# MD4HMAC
def MD4HMAC(hash:str):
    if len(hash) == 32:
        if not hash.isdigit() and not hash.isalpha() and hash.isalnum():
            hash = Hash()
            hash.no = 101420
            hash.name  = 'MD4(HMAC)'
            return hash
    return None

# MD5
def MD5(hash:str):
    if len(hash) == 32:
        if not  hash.isdigit() and not hash.isalpha() and hash.isalnum():
            hash = Hash()
            hash.no = 101280
            hash.name = 'MD5'
            return hash
    return None

# MD5HMAC
def MD5HMAC(hash:str):
    if len(hash) == 32:
        if not hash.isdigit() and not hash.isalpha() and hash.isalnum():
            hash = Hash()
            hash.no = 101400
            hash.name = 'MD5(HMAC)'
            return hash
    return None

# MD5HMACWordpress
def MD5HMACWordpress(hash:str):
    if len(hash) == 32:
        if not hash.isdigit() and not hash.isalpha() and hash.isalnum():
            hash = Hash()
            hash.no = 101460
            hash.name = 'MD5(HMAC(Wordpress))'
            return hash
    return None

# NTLM
def NTLM(hash:str):
    if len(hash) == 32:
        if not hash.isdigit() and not hash.isalpha() and hash.isalnum():
            hash = Hash()
            hash.no = 101340
            hash.name = 'NTLM'
            return hash
    return None

# RAdminv2x
def RAdminv2x(hash:str):
    if len(hash) == 32:
        if not hash.isdigit() and not hash.isalpha() and hash.isalnum():
            hash = Hash()
            hash.no = 101320
            hash.name = 'RAdmin v2.x'
            return hash
    return None

# RipeMD128
def RipeMD128(hash:str):
    if len(hash) == 32:
        if not hash.isdigit() and not hash.isalpha() and hash.isalnum():
            hash = Hash()
            hash.no = 101520
            hash.name = 'RipeMD-128'
            return hash
    return  None

# RipeMD128HMAC
def RipeMD128HMAC(hash:str):
    if len(hash) == 32:
        if not hash.isdigit() and not hash.isalpha() and hash.isalnum():
            hash = Hash()
            hash.no = 101540
            hash.name = 'RipeMD-128(HMAC)'
            return hash
    return None

# SNEFRU128
def SNEFRU128(hash:str):
    if len(hash) == 32:
        if not hash.isdigit() and not hash.isalpha() and hash.isalnum():
            hash = Hash()
            hash.no = 101560
            hash.name = 'SNEFRU-128'
            return hash
    return None

# SNEFRU128HMAC
def SNEFRU128HMAC(hash:str):
    if len(hash) == 32:
        if not hash.isdigit() and not hash.isalpha() and hash.isalnum():
            hash = Hash()
            hash.no = 101580
            hash.name = 'SNEFRU-128(HMAC)'
            return hash
    return None

# Tiger128
def Tiger128(hash:str):
    if len(hash) == 32:
        if not hash.isdigit() and not hash.isalpha() and hash.isalnum():
            hash = Hash()
            hash.no = 101600
            hash.name = 'Tiger-128'
            return hash
    return None

# Tiger128HMAC
def Tiger128HMAC(hash:str):
    if len(hash) == 32:
        if not hash.isdigit() and not hash.isalpha() and hash.isalnum():
            hash = Hash()
            hash.no = 101620
            hash.name = 'Tiger-128(HMAC)'
            return hash
    return None

# md5passsalt
def md5passsalt(hash:str):
    if len(hash) == 32:
        if not hash.isdigit() and not hash.isalpha() and hash.isalnum():
            hash = Hash()
            hash.no = 101640
            hash.name = 'md5($pass.$salt)'
            return hash
    return None

# md5saltmd5pass
def md5saltmd5pass(hash:str):
    if len(hash) == 32:
        if not hash.isdigit() and not hash.isalpha() and hash.isalnum():
            hash = Hash()
            hash.no = 101660
            hash.name = "md5($salt.'-'.md5($pass))"
            return hash
    return None

# md5saltpass
def md5saltpass(hash:str):
    if len(hash) == 32:
        if not hash.isdigit() and not hash.isalpha() and hash.isalnum():
            hash = Hash()
            hash.no = 101680
            hash.name = 'md5($salt.$pass)'
            return hash
    return None

#  md5saltpasssalt
def  md5saltpasssalt(hash:str) :
    if len(hash) == 32:
        if not hash.isdigit() and not hash.isalpha() and hash.isalnum():
            hash = Hash()
            hash.no = 101700
            hash.name = 'md5($salt.$pass.$salt)'
            return hash
    return None

# md5saltpassusername
def md5saltpassusername(hash:str):
    if len(hash) == 32:
        if not hash.isdigit() and not hash.isalpha() and hash.isalnum():
            hash = Hash()
            hash.no = 101720
            hash.name = 'md5($salt.$pass.$username)'
            return  hash
    return None

# md5saltmd5pass
def md5saltmd5pass2 (hash:str):
    if len(hash) == 32:
        if not hash.isdigit() and not hash.isalpha() and hash.isalnum():
            hash = Hash()
            hash.no = 101740
            hash.name = 'md5($salt.md5($pass))'
            return hash
    return  None

# md5saltmd5passsalt
def md5saltmd5passsalt(hash:str) :
    if len(hash) == 32:
        if not hash.isdigit() and not hash.isalpha() and hash.isalnum():
            hash = Hash()
            hash.no = 101760
            hash.name = 'md5($salt.md5($pass).$salt)'
            return hash
    return None

# md5saltmd5passsalt2
def md5saltmd5passsalt2(hash:str):
    if len(hash) == 32:
        if not hash.isdigit() and not hash.isalpha() and hash.isalnum():
            hash = Hash()
            hash.no = 101780
            hash.name = 'md5($salt.md5($pass.$salt))'
            return hash
    return None

# md5saltmd5saltpass
def md5saltmd5saltpass(hash:str):
    if len(hash) == 32:
        if not hash.isdigit() and not hash.isalpha() and hash.isalnum():
            hash = Hash()
            hash.no = 101800
            hash.name = 'md5($salt.md5($salt.$pass))'
            return hash
    return None

# md5saltmd5md5passsalt
def md5saltmd5md5passsalt(hash:str):
    if len(hash) == 32:
        if not hash.isdigit() and not hash.isalpha() and hash.isalnum():
            hash = Hash()
            hash.no = 101820
            hash.name = 'md5($salt.md5(md5($pass).$salt))'
            return hash
    return None

# md5username0pass
def md5username0pass(hash:str):
    if len(hash) == 32:
        if not hash.isdigit() and not hash.isalpha() and hash.isalnum():
            hash = Hash()
            hash.no = 101840
            hash.name = 'md5($username.0.$pass)'
            return hash
    return None

# md5usernameLFpass
def md5usernameLFpass(hash:str):
    if len(hash) == 32:
        if not hash.isdigit() and not hash.isalpha() and hash.isalnum():
            hash = Hash()
            hash.no = 101860
            hash.name = 'md5($username.LF.$pass)'
            return hash
    return None

# md5usernamemd5passsalt
def md5usernamemd5passsalt(hash:str):
    if len(hash) == 32:
        if not hash.isdigit() and not hash.isalpha() and hash.isalnum():
            hash = Hash()
            hash.no = 101880
            hash.name = 'md5($username.md5($pass).$salt)'
            return hash
    return None

#  md5md5pass
def  md5md5pass(hash:str):
    if len(hash) == 32:
        if not hash.isdigit() and not hash.isalpha() and hash.isalnum():
            hash = Hash()
            hash.no = 101900
            hash.name = 'md5(md5($pass))'
            return hash
    return None

# md5md5passsalt
def md5md5passsalt(hash:str):
    if len(hash) == 32:
        if not hash.isdigit() and not hash.isalpha() and hash.isalnum():
            hash = Hash()
            hash.no = 101920
            hash.name = 'md5(md5($pass).$salt)'
            return hash
    return None

# md5md5passmd5salt
def md5md5passmd5salt(hash:str):
    if len(hash) == 32:
        if not hash.isdigit() and not hash.isalpha() and hash.isalnum():
            hash = Hash()
            hash.no = 101940
            hash.name = 'md5(md5($pass).md5($salt))'
            return hash
    return None

# md5md5saltpass
def md5md5saltpass (hash:str):
    if len(hash) == 32:
        if not hash.isdigit() and not hash.isalpha() and hash.isalnum():
            hash = Hash()
            hash.no   = 101960
            hash.name = 'md5(md5($salt).$pass)'
            return hash
    return None

# md5md5saltmd5pass
def md5md5saltmd5pass(hash:str):
    if len(hash) == 32:
        if not hash.isdigit() and not hash.isalpha() and hash.isalnum():
            hash = Hash()
            hash.no = 101980
            hash.name = 'md5(md5($salt).md5($pass))'
            return hash
    return None

# md5md5usernamepasssalt
def md5md5usernamepasssalt(hash:str) :
    if len(hash) == 32:
        if not hash.isdigit() and not hash.isalpha() and hash.isalnum():
            hash = Hash()
            hash.no = 102000
            hash.name = 'md5(md5($username.$pass).$salt)'
            return hash
    return None

# md5md5md5pass
def md5md5md5pass(hash:str):
    if len(hash) == 32:
        if not hash.isdigit() and  not hash.isalpha() and hash.isalnum():
            hash = Hash()
            hash.no = 102020
            hash.name = 'md5(md5(md5($pass)))'
            return hash
    return None

# md5md5md5md5pass
def md5md5md5md5pass(hash:str):
    if len(hash) == 32:
        if not hash.isdigit() and not hash.isalpha() and  hash.isalnum():
            hash = Hash()
            hash.no = 102040
            hash.name = 'md5(md5(md5(md5($pass))))'
            return hash
    return None

# md5md5md5md5md5pass
def md5md5md5md5md5pass(hash:str):
    if len(hash) == 32:
        if not hash.isdigit() and not hash.isalpha() and hash.isalnum():
            hash = Hash()
            hash.no = 102060
            hash.name = 'md5(md5(md5(md5(md5($pass)))))'
            return hash
    return None

#  md5sha1pass
def  md5sha1pass(hash:str):
    if len(hash) == 32:
        if not hash.isdigit() and not hash.isalpha() and hash.isalnum():
            hash = Hash()
            hash.no = 102080
            hash.name = 'md5(sha1($pass))'
            return hash
    return None

# md5sha1md5pass
def md5sha1md5pass(hash:str):
    if len(hash) == 32:
        if not hash.isdigit() and not hash.isalpha() and hash.isalnum():
            hash = Hash()
            hash.no = 102100
            hash.name = 'md5(sha1(md5($pass)))'
            return hash
    return None

# md5sha1md5sha1pass
def md5sha1md5sha1pass(hash:str):
    if len(hash) == 32:
        if not hash.isdigit() and not hash.isalpha() and hash.isalnum():
            hash = Hash()
            hash.no = 102120
            hash.name = 'md5(sha1(md5(sha1($pass))))'
            return hash
    return None

# md5strtouppermd5pass
def md5strtouppermd5pass(hash:str):
    if len(hash) == 32:
        if not hash.isdigit() and not hash.isalpha() and hash.isalnum():
            hash = Hash()
            hash.no = 102140
            hash.name = 'md5(strtoupper(md5($pass)))'
            return hash
    return None

# LineageIIC4
def LineageIIC4(hash:str):
    if len(hash) == 34:
        if not hash.isdigit() and not hash.isalpha() and hash.isalnum():
            if hash[0:2].find('0x') == 0:
                hash = Hash()
                hash.no = 102220
                hash.name = 'Lineage II C4'
                return hash
    return None

# MD5phpBB3
def MD5phpBB3(hash:str):
    if len(hash) == 34:
        if not hash.isdigit() and not hash.isalpha() and not hash.isalnum():
            if hash[0:3].find('$H$') == 0:
                hash = Hash()
                hash.no = 102180
                hash.name = 'MD5(phpBB3)'
                return hash
    return None

# MD5Unix
def MD5Unix(hash:str):
    if len(hash) == 34:
        if not hash.isdigit() and not hash.isalpha() and not hash.isalnum():
            if hash[0:3].find('$1$') == 0:
                hash = Hash()
                hash.no = 102200
                hash.name = 'MD5(Unix)'
                return hash
    return None

# MD5Wordpress
def MD5Wordpress(hash:str):
    if len(hash) == 34:
        if not  hash.isdigit() and not hash.isalpha() and not hash.isalnum():
            if hash[0:3].find('$P$') == 0:
                hash = Hash()
                hash.no = 102160
                hash.name = 'MD5(Wordpress)'
                return hash
    return None

# MD5APR
def MD5APR(hash:str):
    if len(hash) == 37:
        if not hash.isdigit() and not hash.isalpha():
            if hash[0:4].find('$apr') == 0:
                hash = Hash()
                hash.no = 102240
                hash.name = 'MD5(APR)'
                return hash
    return None

# Haval160
def Haval160(hash:str):
    if len(hash) == 40:
        if not hash.isdigit() and not hash.isalpha() and hash.isalnum():
            hash = Hash()
            hash.no = 102340
            hash.name = 'Haval-160'
            return hash
    return None

# Haval160HMAC
def Haval160HMAC(hash:str):
    if len(hash) == 40:
        if not hash.isdigit() and not hash.isalpha() and hash.isalnum():
            hash = Hash()
            hash.no = 102440
            hash.name = 'Haval-160(HMAC)'
            return hash
    return None

# MySQL5
def MySQL5 (hash:str):
    if len(hash) == 40:
        if not hash.isdigit() and not hash.isalpha() and hash.isalnum():
            hash = Hash()
            hash.no = 102280
            hash.name = 'MySQL5 - SHA-1(SHA-1($pass))'
            return hash
    return None

# MySQL160bit
def MySQL160bit(hash:str):
    if len(hash) == 41:
        if not hash.isdigit() and not hash.isalpha() and not hash.isalnum():
            if hash[0:1].find('*') == 0:
                hash = Hash()
                hash.no = 102300
                hash.name = 'MySQL 160bit - SHA-1(SHA-1($pass))'
                return hash
    return None

# RipeMD160
def RipeMD160 (hash:str):
    if len(hash) == 40:
        if not hash.isdigit() and not hash.isalpha() and hash.isalnum():
            hash = Hash()
            hash.no = 102360
            hash.name = 'RipeMD-160'
            return hash
    return None

# RipeMD160HMAC
def RipeMD160HMAC (hash:str):
    if len(hash) == 40:
        if not hash.isdigit() and not hash.isalpha() and hash.isalnum():
            hash = Hash()
            hash.no = 102420
            hash.name = 'RipeMD-160(HMAC)'
            return hash
    return None

# SHA1
def SHA1 (hash:str):
    if len(hash) == 40:
        if not hash.isdigit() and not hash.isalpha() and hash.isalnum():
            hash = Hash()
            hash.no = 102260
            hash.name = 'SHA-1'
            return hash
    return None

# SHA1HMAC
def SHA1HMAC(hash:str):
    if len(hash) == 40:
        if not hash.isdigit() and not hash.isalpha() and hash.isalnum():
            hash = Hash()
            hash.no = 102380
            hash.name = 'SHA-1(HMAC)'
            return hash
    return hash

# SHA1MaNGOS
def SHA1MaNGOS(hash:str):
    if len(hash) == 40:
        if not hash.isdigit() and not hash.isalpha() and hash.isalnum():
            hash = Hash()
            hash.no = 102460
            hash.name = 'SHA-1(MaNGOS)'
            return hash
    return None

# SHA1MaNGOS2
def SHA1MaNGOS2(hash:str):
    if len(hash) == 40:
        if not hash.isdigit() and  not hash.isalpha() and hash.isalnum():
            hash = Hash()
            hash.no = 102480
            hash.name =  'SHA-1(MaNGOS2)'
            return hash
    return None

# Tiger160
def Tiger160(hash:str):
    if len(hash) == 40:
        if not hash.isdigit() and not hash.isalpha() and hash.isalnum():
            hash = Hash()
            hash.no = 102320
            hash.name = 'Tiger-160'
            return hash
    return None

# Tiger160HMAC
def Tiger160HMAC(hash:str):
    if len(hash) == 40:
        if not hash.isdigit() and not hash.isalpha() and hash.isalnum():
            hash = Hash()
            hash.no = 102400
            hash.name = 'Tiger-160(HMAC)'
            return hash
    return None

# sha1passsalt
def sha1passsalt (hash:str):
    if len(hash) == 40:
        if not  hash.isdigit() and not hash.isalpha() and hash.isalnum():
            hash = Hash()
            hash.no = 102500
            hash.name = 'sha1($pass.$salt)'
            return hash
    return None

# sha1saltpass
def sha1saltpass (hash:str):
    if len(hash) == 40:
        if not  hash.isdigit() and not hash.isalpha() and hash.isalnum():
            hash = Hash()
            hash.no = 102520
            hash.name = 'sha1($salt.$pass)'
            return hash
    return None

# sha1saltmd5pass
def sha1saltmd5pass(hash:str):
    if len(hash) == 40:
        if not hash.isdigit() and not hash.isalpha() and hash.isalnum():
            hash = Hash()
            hash.no = 102540
            hash.name = 'sha1($salt.md5($pass))'
            return hash
    return None

# sha1saltmd5passsalt
def sha1saltmd5passsalt(hash:str):
    if len(hash) == 40:
        if not hash.isdigit() and not hash.isalpha() and hash.isalnum():
            hash = Hash()
            hash.no = 102560
            hash.name = 'sha1($salt.md5($pass).$salt)'
            return hash
    return None

# sha1saltsha1pass
def sha1saltsha1pass(hash:str):
    if len(hash) == 40:
        if not hash.isdigit() and not hash.isalpha() and hash.isalnum():
            hash = Hash()
            hash.no = 102580
            hash.name = 'sha1($salt.sha1($pass))'
            return hash
    return None

# sha1saltsha1saltsha1pass
def sha1saltsha1saltsha1pass(hash:str):
    if len(hash) == 40:
        if not hash.isdigit() and not hash.isalpha() and hash.isalnum():
            hash = Hash()
            hash.no = 102600
            hash.name = 'sha1($salt.sha1($salt.sha1($pass)))'
            return hash
    return None

# sha1usernamepass
def sha1usernamepass(hash:str):
    if len(hash) == 40:
        if not hash.isdigit() and not hash.isalpha() and hash.isalnum():
            hash = Hash()
            hash.no = 102620
            hash.name = 'sha1($username.$pass)'
            return hash
    return None

# sha1usernamepasssalt
def sha1usernamepasssalt(hash:str):
    if len(hash) == 40:
        if not hash.isdigit() and not hash.isalpha() and hash.isalnum():
            hash = Hash()
            hash.no = 102640
            hash.name = 'sha1($username.$pass.$salt)'
            return hash
    return None

# sha1md5pass
def sha1md5pass(hash:str):
    if len(hash) == 40:
        if not hash.isdigit() and not hash.isalpha() and hash.isalnum():
            hash = Hash()
            hash.no = 103500
            hash.name = 'sha1(md5($pass))'
            return hash
    return None

# sha1md5passsalt
def sha1md5passsalt(hash:str):
    if len(hash) == 40:
        if not hash.isdigit() and not hash.isalpha() and hash.isalnum():
            hash = Hash()
            hash.no = 102660
            hash.name = 'sha1(md5($pass).$salt)'
            return hash
    return None

# sha1md5sha1pass
def sha1md5sha1pass(hash:str):
    if len(hash) == 40:
        if not hash.isdigit() and not hash.isalpha() and hash.isalnum():
            hash = Hash()
            hash.no = 102680
            hash.name = 'sha1(md5(sha1($pass)))'
            return hash
    return None


# sha1sha1pass
def sha1sha1pass(hash:str):
    if len(hash) == 40:
        if not hash.isdigit() and not hash.isalpha() and hash.isalnum():
            hash = Hash()
            hash.no = 102700
            hash.name = 'sha1(sha1($pass))'
            return hash
    return None


# sha1sha1passsalt
def sha1sha1passsalt(hash:str):
    if len(hash) == 40:
        if not hash.isdigit() and not hash.isalpha() and hash.isalnum():
            hash = Hash()
            hash.no = 102720
            hash.name = 'sha1(sha1($pass).$salt)'
            return hash
    return None

# sha1sha1passsubstrpass03
def sha1sha1passsubstrpass03(hash:str):
    if len(hash) == 40:
        if not hash.isdigit() and not hash.isalpha() and hash.isalnum():
            hash = Hash()
            hash.no = 102740
            hash.name = 'sha1(sha1($pass).substr($pass,0,3))'
            return hash
    return None

# sha1sha1saltpass
def sha1sha1saltpass(hash:str):
    if len(hash) == 40:
        if not hash.isdigit() and not hash.isalpha() and hash.isalnum():
            hash = Hash()
            hash.no = 102760
            hash.name = 'sha1(sha1($salt.$pass))'
            return hash
    return None

# sha1sha1sha1pass
def sha1sha1sha1pass(hash:str):
    if len(hash) == 40:
        if not hash.isdigit() and not hash.isalpha() and hash.isalnum():
            hash = Hash()
            hash.no = 102780
            hash.name = 'sha1(sha1(sha1($pass)))'
            return hash
    return None


# sha1strtolowerusernamepass
def sha1strtolowerusernamepass(hash:str):
    if len(hash) == 40:
        if not hash.isdigit() and not hash.isalpha() and hash.isalnum():
            hash = Hash()
            hash.no = 102800
            hash.name = 'sha1(strtolower($username).$pass)'
            return hash
    return None

# Haval192
def Haval192(hash:str):
    if len(hash) == 48:
        if not hash.isdigit() and not hash.isalpha() and hash.isalnum():
            hash = Hash()
            hash.no = 102840
            hash.name = 'Haval-192'
            return hash
    return None

# Haval192
def Haval192HMAC(hash:str):
    if len(hash) == 48:
        if not hash.isdigit() and not hash.isalpha() and hash.isalnum():
            hash = Hash()
            hash.no = 102880
            hash.name = 'Haval-192(HMAC)'
            return hash
    return None

#  Tiger192
def Tiger192(hash:str):
    if len(hash) == 48:
        if not hash.isdigit() and not hash.isalpha() and hash.isalnum():
            hash = Hash()
            hash.no = 102820
            hash.name = 'Tiger-192'
            return hash
    return None

#  Tiger192HMAC
def Tiger192HMAC(hash:str):
    if len(hash) == 48:
        if not hash.isdigit() and not hash.isalpha() and hash.isalnum():
            hash = Hash()
            hash.no = 102860
            hash.name = 'Tiger-192(HMAC)'
            return hash
    return None

# MD5passsaltjoomla1
def MD5passsaltjoomla1(hash:str):
    if len(hash) == 49:
        if not hash.isdigit() and not hash.isalpha() and not hash.isalnum():
            if hash[32:33].find(':') == 0:
                hash = Hash()
                hash.no = 102900
                hash.name = 'md5($pass.$salt) - Joomla'
                return hash
    return None

# SHA1Django
def SHA1Django(hash:str):
    if len(hash) == 52:
        if not hash.isdigit() and not hash.isalpha() and not hash.isalnum():
            if hash[0:5].find('sha1$') == 0:
                hash = Hash()
                hash.no = 102920
                hash.name = 'SHA-1(Django)'
                return hash
    return None

# Haval224
def Haval224(hash:str):
    if len(hash) == 56:
        if not hash.isdigit() and not hash.isalpha() and hash.isalnum():
            hash = Hash()
            hash.no = 102960
            hash.name = 'Haval-224'
            return hash
    return None

# Haval224HMAC
def Haval224HMAC(hash:str):
    if len(hash) == 56:
        if not hash.isdigit() and not hash.isalpha() and hash.isalnum():
            hash = Hash()
            hash.no = 103000
            hash.name = 'Haval-224(HMAC)'
            return hash
    return None

# SHA224
def SHA224(hash:str):
    if len(hash) == 56:
        if not hash.isdigit() and not hash.isalpha() and hash.isalnum():
            hash = Hash()
            hash.no = 102940
            hash.name = 'SHA-224'
            return hash
    return None

# SHA224HMAC
def SHA224HMAC(hash:str):
    if len(hash) == 56:
        if not hash.isdigit() and not hash.isalpha() and hash.isalnum():
            hash = Hash()
            hash.no = 102980
            hash.name = 'SHA-224(HMAC)'
            return hash
    return None

# SHA256
def SHA256(hash:str):
    if len(hash) == 64:
        if not hash.isdigit() and not hash.isalpha() and hash.isalnum():
            hash = Hash()
            hash.no = 103020
            hash.name = 'SHA-256'
            return hash
    return None

# SHA256HMAC
def SHA256HMAC(hash:str):
    if len(hash) == 64:
        if not hash.isdigit() and not hash.isalpha() and hash.isalnum():
            hash = Hash()
            hash.no = 103120
            hash.name = 'SHA-256(HMAC)'
            return hash
    return None

# Haval256
def Haval256(hash:str):
    if len(hash) == 64:
        if not hash.isdigit() and not hash.isalpha() and hash.isalnum():
            hash = Hash()
            hash.no = 103040
            hash.name = 'Haval-256'
            return hash
    return None

# Haval256HMAC
def Haval256HMAC(hash:str):
    if len(hash) == 64:
        if not hash.isdigit() and not hash.isalpha() and hash.isalnum():
            hash = Hash()
            hash.no = 103140
            hash.name = 'Haval-256(HMAC)'
            return hash
    return None

# GOSTR341194
def GOSTR341194(hash:str):
    if len(hash) == 64:
        if not hash.isdigit() and not hash.isalpha() and hash.isalnum():
            hash = Hash()
            hash.no  = 103060
            hash.name = 'GOST R 34.11-94'
            return hash
    return None

# RipeMD256
def RipeMD256(hash:str):
    if len(hash) == 64:
        if not hash.isdigit() and not hash.isalpha() and hash.isalnum():
            hash = Hash()
            hash.no = 103080
            hash.name = 'RipeMD-256'
            return hash
    return None

# RipeMD256HMAC
def RipeMD256HMAC(hash:str):
    if len(hash) == 64:
        if  not hash.isdigit() and not hash.isalpha() and hash.isalnum():
            hash = Hash()
            hash.no = 103160
            hash.name = 'RipeMD-256(HMAC)'
            return hash
    return None

# SNEFRU256
def SNEFRU256(hash:str):
    if len(hash) == 64:
        if  not hash.isdigit() and not hash.isalpha() and hash.isalnum():
            hash = Hash()
            hash.no = 103100
            hash.name = 'SNEFRU-256'
            return hash
    return None

# SNEFRU256HMAC
def SNEFRU256HMAC(hash:str):
    if len(hash) == 64:
        if not hash.isdigit() and not hash.isalpha() and hash.isalnum():
            hash = Hash()
            hash.no = 103180
            hash.name = 'SNEFRU-256(HMAC)'
            return hash
    return None

# SHA256md5pass
def SHA256md5pass(hash:str):
    if len(hash) == 64:
        if not hash.isdigit() and not hash.isalpha() and hash.isalnum():
            hash = Hash()
            hash.no = 103200
            hash.name = 'SHA-256(md5($pass))'
            return hash
    return None

#  SHA256sha1pass
def  SHA256sha1pass(hash:str):
    if len(hash) == 64:
        if not hash.isdigit() and not hash.isalpha() and hash.isalnum():
            hash = Hash()
            hash.no = 103220
            hash.name = 'SHA-256(sha1($pass))'
            return hash
    return None

# MD5passsaltjoomla2
def MD5passsaltjoomla2(hash:str):
    if len(hash) == 65:
        if not hash.isdigit() and not hash.isalpha() and not hash.isalnum():
            if hash[32:33].find(':') == 0:
                hash = Hash()
                hash.no = 103240
                hash.name = 'md5($pass.$salt) - Joomla'
                return hash
    return None

# SAM
def SAM(hash:str):
    if len(hash) == 65:
        if not hash.isdigit() and not hash.isalpha() and not hash.isalnum() and hash.isupper():
            if hash[32:33].find(':') == 0:
                hash = Hash()
                hash.no = 103260
                hash.name = 'SAM - (LM_hash:NT_hash)'
                return hash
    return None

# SHA256Django
def SHA256Django(hash:str):
    if len(hash) == 78:
        if not hash.isdigit() and not hash.isalpha() and not hash.isalnum():
            if hash[0:6].find('sha256') == 0:
                hash = Hash()
                hash.no = 103280
                hash.name = 'SHA-256(Django)'
                return hash
        return None

# RipeMD320
def RipeMD320(hash:str) :
    if len(hash) == 80:
        if not hash.isdigit() and not hash.isalpha() and hash.isalnum():
            hash = Hash()
            hash.no = 103300
            hash.name = 'RipeMD-320'
            return hash
    return None

# RipeMD320HMAC
def RipeMD320HMAC(hash:str):
    if len(hash) == 80:
        if not hash.isdigit() and not hash.isalpha() and hash.isalnum():
            hash = Hash()
            hash.no = 103320
            hash.name = 'RipeMD-320(HMAC)'
            return hash
    return None

# SHA384
def SHA384(hash:str):
    if len(hash) == 96:
        if not hash.isdigit() and not hash.isalpha() and hash.isalnum():
            hash = Hash()
            hash.no = 103340
            hash.name = 'SHA-384'
            return hash
    return None

# SHA384HMAC
def SHA384HMAC(hash:str):
    if len(hash) == 96:
        if not hash.isdigit() and not hash.isalpha() and hash.isalnum():
            hash = Hash()
            hash.no = 103360
            hash.name = 'SHA-384(HMAC)'
            return hash
    return None

# SHA256s
def SHA256s(hash:str):
    if len(hash) == 98:
        if not hash.isdigit() and not hash.isalpha() and not hash.isalnum():
            if hash[0:3].find('$6$') == 0:
                hash = Hash()
                hash.no = 103380
                hash.name = 'SHA-256'
                return hash
    return None

# SHA384Django
def SHA384Django(hash:str):
    if len(hash) == 110:
        if not hash.isdigit() and not hash.isalpha() and not hash.isalnum():
            if hash[0:6].find('sha384') == 0:
                hash = Hash()
                hash.no = 103400
                hash.name = 'SHA-384(Django)'
                return hash
    return None

# SHA512
def SHA512(hash:str):
    if len(hash) == 128:
        if not hash.isdigit() and not hash.isalpha() and hash.isalnum():
            hash = Hash()
            hash.no = 103420
            hash.name = 'SHA-512'
            return hash
    return None


# SHA512HMAC
def SHA512HMAC(hash:str):
    if len(hash) == 128:
        if not hash.isdigit() and not hash.isalpha() and hash.isalnum():
            hash = Hash()
            hash.no = 103460
            hash.name = 'SHA-512(HMAC)'
            return hash
    return None

# Whirlpool
def Whirlpool(hash:str):
    if len(hash) == 128:
        if not hash.isdigit() and not hash.isalpha() and hash.isalnum():
            hash = Hash()
            hash.no = 103440
            hash.name = 'Whirlpool'
            return hash
    return None

# WhirlpoolHMAC
def WhirlpoolHMAC(hash:str):
    if len(hash) == 128:
        if not hash.isdigit() and not hash.isalpha() and hash.isalnum():
            hash = Hash()
            hash.no = 103480
            hash.name = 'Whirlpool(HMAC)'
            return hash
    return None













































