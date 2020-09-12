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
from lib.cryptography.hash.Hash_Subfunc import *

def detectHash(hashStr:str) -> list:
    #
    tmp_result = []
    nullitem = Hash()
    #
    item = CRC16(hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = CRC16CCITT(hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = FCS16(hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = CRC32(hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = ADLER32(hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = CRC32B(hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = XOR32(hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = GHash323(hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = GHash325(hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = DESUnix(hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = MD5Half(hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = MD5Middle(hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = MySQL(hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = DomainCachedCredentials(hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = Haval128(hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = Haval128HMAC(hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = MD2(hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = MD2HMAC(hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = MD4(hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = MD4HMAC(hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = MD5(hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = MD5HMAC(hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = MD5HMACWordpress(hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = NTLM(hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = RAdminv2x(hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = RipeMD128(hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = RipeMD128HMAC(hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = SNEFRU128(hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = SNEFRU128HMAC(hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = Tiger128(hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = Tiger128HMAC(hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = md5passsalt(hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = md5saltmd5pass(hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = md5saltpass(hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = md5saltpasssalt(hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = md5saltpassusername(hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = md5saltmd5pass2 (hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = md5saltmd5passsalt  (hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = md5saltmd5passsalt2 (hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = md5saltmd5saltpass (hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = md5saltmd5md5passsalt (hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = md5username0pass (hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = md5usernameLFpass (hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = md5usernamemd5passsalt (hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = md5md5pass (hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = md5md5passsalt (hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = md5md5passmd5salt (hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = md5md5saltpass (hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = md5md5saltmd5pass (hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = md5md5usernamepasssalt (hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = md5md5md5pass (hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = md5md5md5md5pass (hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = md5md5md5md5md5pass (hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = md5sha1pass (hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = md5sha1md5pass (hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = md5sha1md5sha1pass (hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = md5strtouppermd5pass (hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = LineageIIC4 (hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = MD5phpBB3 (hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = MD5Unix (hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = MD5Wordpress (hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = MD5APR (hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = Haval160 (hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = Haval160HMAC (hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = MySQL5 (hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = MySQL160bit (hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = RipeMD160 (hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = RipeMD160HMAC (hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = SHA1 (hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = SHA1HMAC (hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = SHA1MaNGOS (hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = SHA1MaNGOS2 (hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = Tiger160 (hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = Tiger160HMAC (hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = sha1passsalt  (hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = sha1saltpass (hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = sha1saltmd5pass (hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = sha1saltmd5passsalt (hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = sha1saltsha1pass (hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = sha1saltsha1saltsha1pass (hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = sha1usernamepass (hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = sha1usernamepasssalt (hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = sha1md5pass (hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = sha1md5passsalt (hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = sha1md5sha1pass (hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = sha1sha1pass (hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = sha1sha1passsalt (hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = sha1sha1passsubstrpass03 (hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = sha1sha1saltpass (hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = sha1sha1sha1pass (hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = sha1strtolowerusernamepass (hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = Haval192 (hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = Haval192HMAC (hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = Tiger192 (hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = Tiger192HMAC (hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = MD5passsaltjoomla1 (hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = SHA1Django (hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = Haval224 (hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = Haval224HMAC (hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = SHA224 (hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = SHA224HMAC (hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = SHA256 (hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = SHA256HMAC (hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = Haval256  (hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = Haval256HMAC (hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = GOSTR341194 (hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = RipeMD256 (hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = RipeMD256HMAC (hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = SNEFRU256 (hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = SNEFRU256HMAC (hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = SHA256md5pass (hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = SHA256sha1pass (hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = MD5passsaltjoomla2 (hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = SAM (hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = SHA256Django (hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = RipeMD320 (hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = RipeMD320HMAC (hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = SHA384 (hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = SHA384HMAC (hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = SHA256s (hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = SHA384Django (hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = SHA512 (hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = SHA512HMAC (hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = Whirlpool (hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    item = WhirlpoolHMAC (hashStr)
    if type(item) == type(nullitem):
        tmp_result.append(item)
    #
    result = sorted(tmp_result, key=lambda jj: jj.no)
    return result
