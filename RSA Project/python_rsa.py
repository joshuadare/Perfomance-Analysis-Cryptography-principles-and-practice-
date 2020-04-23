import Crypto
from PyRsa.pyrsa import RsaKey
from PyRsa.pyb64 import Base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto import Random
import ast
import timeit
import psutil

#Before Key Generation
print ("\nCPU USAGE BEFORE KEY Generation is ", psutil.cpu_percent(),"%") #CPU percentage during before generation
print ("\nMemory USAGE BEFORE KEY Generation is ", psutil.virtual_memory())#gives memory useage bytes only

memoryused = psutil.virtual_memory().used / (1000.0 ** 3) #calculates memory used before key generation in GB
print('\nTotal Memory Used before Key Generation in GB:')
print(memoryused)#memory used before key generation in GB

memorytotal = psutil.virtual_memory().total/ (1000.0 ** 3)#calculates total memory before key generation in GB
print('\nTotal Memory in GB:')
print(memorytotal)#total memory before key generation in GB


start = timeit.default_timer() #starts timing

random_generator = Random.new().read #defines random_generator
key = RSA.generate(1024, random_generator) #defines key

#During Key Generation
print ("\nCPU USAGE during KEY Generation is ", psutil.cpu_percent(),"%") #CPU percentage during key generation
print ("\nMemory USAGE during KEY Generation is ", psutil.virtual_memory())#gives memory useage bytes only

memoryused = psutil.virtual_memory().used / (1000.0 ** 3) #calculates memory used during key generation in GB
print('\nTotal Memory Used during Key Generation in GB:')
print(memoryused)#memory used during key generation in GB

memorytotal = psutil.virtual_memory().total/ (1000.0 ** 3)#calculates total memory  key generation in GB
print('\nTotal Memory in GB:')
print(memorytotal)#total memory during key generation in GB


stop = timeit.default_timer() #stop timing

#Key Geration Final time 
print('\nTime of Key generation is:', stop - start,' ms') #gives key generation time in milliseconds

#Before Encryption
print ("\nCPU USAGE BEFORE Encryption is ", psutil.cpu_percent(),"%") #CPU percentage before Encryption
print ("\nMemory USAGE BEFORE Encryption is ", psutil.virtual_memory())#gives memory useage bytes only

memoryused = psutil.virtual_memory().used / (1000.0 ** 3)#calculates memory used before Encryption in GB
print('\nTotal Memory Used before Encryption in GB:')
print(memoryused)#memory used before encryption in GB

memorytotal = psutil.virtual_memory().total/ (1000.0 ** 3)#calculates total memory before Encryption in GB
print('\nTotal Memory in GB:')
print(memorytotal)#total memory before encryption in GB

start = timeit.default_timer() #starts timing
publickey = key.publickey() #defines public key


#During Encryption
encryptor = PKCS1_OAEP.new(publickey) #declares encryptor
encrypted = encryptor.encrypt(b'barsoum') #messge to be encrypted

print ("\nCPU USAGE During Encryption is ", psutil.cpu_percent(),"%") #CPU percentage during Encryption
print ("\nMemory USAGE During Encryption is ", psutil.virtual_memory())

memoryused = psutil.virtual_memory().used / (1000.0 ** 3)#calculates memory used during Encryption in GB
print('\nTotal Memory Used during Encryption in GB:')
print(memoryused)#memory used during encryption in GB

memorytotal = psutil.virtual_memory().total/ (1000.0 ** 3)#calculates total memory during Encryption in GB
print('\nTotal Memory in GB:')
print(memorytotal)#total memory during encryption in GB

stop = timeit.default_timer() #stops timer

#Encrypted message and time of Encryption
print ('\nencrypted message:') 
print (encrypted) #encrpyted message
print('\n\nTime of Encryption of the text is: ', stop - start,' ms') #gives time of encrytion in milliseconds

#Before Decryption
print ("\nCPU USAGE BEFORE Decryption is ", psutil.cpu_percent(),"%") #CPU percentage before decryption
print ("\nMemory USAGE BEFORE Decryption is ", psutil.virtual_memory())#gives memory useage bytes only

memoryused = psutil.virtual_memory().used / (1000.0 ** 3)#calculates memory used before Decryption in GB
print('\nTotal Memory Used before Decrytption in GB:')
print(memoryused) #memory used before decrpytion in GB

memorytotal = psutil.virtual_memory().total/ (1000.0 ** 3) #calculates total memory before Decryption in GB
print('\nTotal Memory Before Decryption in GB:') 
print(memorytotal) #total memory before decrpytion in GB

start = timeit.default_timer() #starts timing


#During Decryption
decryptor = PKCS1_OAEP.new(key) #defines dcryptor
decrypted = decryptor.decrypt(ast.literal_eval(str(encrypted))) #message to be decrypted

print ("\nCPU USAGE During Decryption is ", psutil.cpu_percent(),"%") #calculates GPU usage during decryption
print ("\nMemory USAGE During Decryption is ", psutil.virtual_memory()) #gives memory useage bytes only

memoryused = psutil.virtual_memory().used / (1000.0 ** 3) #calculates memory used during Decryptionin in GB
print('\nTotal Memory Used during Decryption in GB:')
print(memoryused) #memory used during decryption in GB

memorytotal = psutil.virtual_memory().total/ (1000.0 ** 3) #calculates total memory during Decryption in GB
print('\nTotal Memory During in GB:')
print(memorytotal) #total memory during decrpytion in GB

stop = timeit.default_timer() #stops timing


#Gives Decrypted Message and Time of Decryption
print ('\ndecrypted message:') 
print (decrypted) #ciphertext/decrypted message
print('\nTime of Decryption of the text is: ', stop - start,' ms') #gives decryption time in milliseconds




