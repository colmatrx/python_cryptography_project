# -*- coding: utf-8 -*-
"""

AES CBC Encryption Mode
Created on Thu Jul 15 19:22:44 2021

@author: Idris Adeleke
"""
from Cryptodome.Cipher import AES
from Crypto.Random import get_random_bytes
from Cryptodome.Util.Padding import pad

with open(r"C:\Users\acdc\Python Project\my_file.txt", 'rb') as f:
    plainText = f.read()
    
plainText = pad(plainText, AES.block_size)  #pad plaintext data to 16 byte block

symmetricKey = get_random_bytes(16)   #generate secret key of 16 bytes -> 128 bits

with open(r'C:\Users\acdc\Python Project\secret_key','wb') as f:
    f.write(symmetricKey)   #save the encryption key to file

cipher = AES.new(symmetricKey,AES.MODE_CBC)  #Initialization Vector is automatically generated here

cipherText = cipher.encrypt(plainText)   #encrypt the palintext

with open(r'C:\Users\acdc\Python Project\cipherText','wb') as f:
    f.write(cipher.iv)    #write 16bytes (128 bits) initialization vector at the beginning of the cipherText
    f.write(cipherText)




