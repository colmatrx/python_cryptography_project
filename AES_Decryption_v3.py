# -*- coding: utf-8 -*-
"""
AES CBC Decryption Mode
Created on Thu Jul 15 22:39:49 2021

@author: Idris Adeleke
"""

from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import unpad
import timeit

def decryptData(fileName, fileDirectory, keyPath):

    with open(fileDirectory + "\\" + fileName, 'rb') as f: 
        initializationVector = f.read(16)   #read the 16bytes initialization vector at the beginning of the cipherText file
        encryptedData = f.read()            #read the rest of the cipherText file
    
    with open(keyPath, 'rb') as f:  #open the encryption key file
        symmetricKey = f.read()         #read the key from file  
    
    cipher = AES.new(symmetricKey, AES.MODE_CBC, initializationVector)   #create the decryption cipher 

    plainText = cipher.decrypt(encryptedData)   #decrypt the ciphertext

    plainText = unpad(plainText, AES.block_size)    #remove the padding in the plaintext

    with open(fileDirectory + "\\" + fileName + "_PlainText", 'wb') as f: #open and write the decrypted data to file
        f.write(plainText)
    
    print ("\nDecryption Successful! \n\nThe decrypted file (PlainText) is located in the same directory as " + "'" + fileName + "'")
    return 0

fileName = input("Welcome to AES Decryption Demo. \n\nPlease provide the simple file name of the ciphertext eg encrypted_file.\n\n")

fileDirectory = input("Please provide the directory of the ciphertext file. Omit the ciphertext file name and do not include the back slash eg C:\\users\\docs\n\n")

keyPath = input("Please provide the full path of the secret key file including the file name eg C:\\users\\docs\\secretkeyfile\n\n")

print(timeit.repeat(stmt='decryptData(fileName, fileDirectory, keyPath)', setup='', repeat=5, number=1, globals=globals()))
