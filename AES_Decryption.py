# -*- coding: utf-8 -*-
"""

AES CBC Decryption Mode
Created on Thu Jul 15 20:17:52 2021

@author: Idris Adeleke
"""

from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import unpad

with open(r"C:\Users\acdc\Python Project\cipherText", 'rb') as f:
    initializationVector = f.read(16)   #read the 16bytes initialization vector at the beginning of the cipherText file
    encryptedData = f.read()            #read the rest of the cipherText file
    
with open(r"C:\Users\acdc\Python Project\secret_key", 'rb') as f:  #open the encryption key file
    symmetricKey = f.read()         #read the key from file
    
cipher = AES.new(symmetricKey, AES.MODE_CBC, initializationVector)   #create the decryption cipher

plainText = cipher.decrypt(encryptedData)   #decrypt the ciphertext

plainText = unpad(plainText, AES.block_size)    #remove the padding in the plaintext


with open(r"C:\Users\acdc\Python Project\my_file.txt", 'wb') as f: #open and write the decrypted data to file
    f.write(plainText)
    
