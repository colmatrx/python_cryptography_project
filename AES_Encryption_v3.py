# -*- coding: utf-8 -*-
"""

AES CBC Encryption Mode
Created on Thu Jul 15 19:22:44 2021

@author: Idris Adeleke
"""
from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes
from Cryptodome.Util.Padding import pad
import timeit

def encryptData(fileName, fileDirectory, keyLength):
    
    with open(fileDirectory + "\\" + fileName, 'rb') as f: 
        plainText = f.read() 
    
    plainText = pad(plainText, AES.block_size)  #pad plaintext data to 16 byte block
    
    keyLength = int(keyLength) / 8

    symmetricKey = get_random_bytes(int(keyLength))   #generate secret key of keyLength bytes -> keyLength x 8bits 

    with open(fileDirectory + "\\" + fileName + "_SecretKey_" + str(int(keyLength)*8) + "bits", 'wb') as f:
        f.write(symmetricKey)   #save the encryption key to file
    
    cipher = AES.new(symmetricKey,AES.MODE_CBC)  #Initialization Vector is automatically generated here 

    cipherText = cipher.encrypt(plainText)   #encrypt the palintext

    with open(fileDirectory + "\\" + fileName + "_CipherText",'wb') as f:
        f.write(cipher.iv)    #write 16bytes (128 bits) initialization vector at the beginning of the cipherText
        f.write(cipherText)   #write the cipher text to file
    
    print ("\nEncryption Successful! \n\nThe encrypted file (CipherText) and the secret key file (SecretKey) are located in the same directory as " + "'" + fileName + "'")
    return 0


fileName = input("Welcome to AES Encryption Demo \nPlease provide the plaintext file name and extension eg crypto.txt\n\n")

fileDirectory = input("Please provide the directory of the file. Omit the file name and do not include the backslash eg C:\\users\\docs\n\n")

keyLength = input("\nChoose the encryption key length in integer -->  128 or 256\n")

print(timeit.repeat(stmt='encryptData(fileName, fileDirectory, keyLength)', setup='', repeat = 5, number=1, globals=globals()))
 
     
 
