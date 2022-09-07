# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 17:23:25 2018

@author: bhara
"""

import hashlib
import rsa

msg="Hello, How are you?"

#generate message digest
msgdigest=hashlib.sha1(msg.encode('utf8')).hexdigest()
print("Message Digest=",msgdigest)

#generating public and private key
(pubkey, privkey) = rsa.newkeys(512)

#encrypting the message digest with public key
encmsg=rsa.encrypt(msgdigest.encode('utf8'),pubkey)

print("Encrypted message digest=",encmsg)

decmsg=rsa.decrypt(encmsg,privkey).decode('utf8')
print("Decrypted message digest=",decmsg)
