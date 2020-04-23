import pyaes, os, time
import binascii #makes print format a little more readable, but does not change actual byte value
from statistics import mean

# 128 bit, 192 bit and 256 bit keys

start = time.time()
key_128 = os.urandom(16)
end = time.time()
print("128 bit key generation time = {}ms".format((end-start)*1000))

start = time.time()
key_192 = os.urandom(24)
end = time.time()
print("192 bit key generation time = {}ms".format((end-start)*1000))

start = time.time()
key_256 = os.urandom(32)
end = time.time()
print("256 bit key generation time = {}ms".format((end-start)*1000))

keys = {"AES-128": key_128, "AES-192": key_192, "AES-256": key_256}

# For some modes of operation we need a random initialization vector
# of 16 bytes
iv = os.urandom(16)

#plaintext = "Text may be any length you wish, no padding is required"
plaintext = input("Enter message to be encrypted: ")

avgEncTime = []
avgDecTime = []


for mode in pyaes.AESModesOfOperation.values():
    avgModeEncTime = []
    avgModeDecTime = []
    for key in keys:
        """temp = plaintext
        if mode == pyaes.AESModeOfOperationCBC or mode == pyaes.AESModeOfOperationECB:
            print("Making plaintext 16 bytes...")
            if len(plaintext) >= 16:
                plaintext = plaintext[:16]
            else:
                while len(plaintext) < 16:
                    plaintext += "*"
            print("New plaintext: {}".format(plaintext))
        """
        aes = mode(keys[key], iv) if mode == pyaes.AESModeOfOperationCFB else mode(keys[key])
        
        start = time.time()
        encrypter = pyaes.Encrypter(aes)
        ciphertext = encrypter.feed(plaintext)
        ciphertext += encrypter.feed()
        end = time.time()
        print("{} {} encryprion time = {}ms".format(aes.name, key, (end-start)*1000))
        
        avgEncTime.append(end-start) # add to dictionary to compute average time
        avgModeEncTime.append(end-start)
        
        # show the encrypted data
        print ("Encrypted message = ", binascii.hexlify(ciphertext))
        
        # DECRYPTION
        # CRT mode decryption requires a new instance be created
        aes = mode(keys[key], iv) if mode == pyaes.AESModeOfOperationCFB else mode(keys[key])
        
        # decrypted data is always binary, need to decode to plaintext
        start = time.time()
        decrypter = pyaes.Decrypter(aes)
        decrypted = decrypter.feed(ciphertext)
        decrypted += decrypter.feed()
        end = time.time()
        print("{} {} decryption time = {}ms".format(aes.name, key, (end-start)*1000))
        decrypted = decrypted.decode("utf-8")
        
        avgDecTime.append(end-start) # add to dictionary to compute average time
        avgModeDecTime.append(end-start)

        print ("message = dec(enc(message))" if decrypted == plaintext else "message =/= dec(enc(message))")
        print("Decrypted message =", decrypted)
        print()
        
    print("{} Average Encryption Time = {} ms".format(mode.name, mean(avgModeEncTime)*1000))
    del avgModeEncTime
    print("{} Average Decryption Time = {} ms".format(mode.name, mean(avgModeDecTime)*1000))
    del avgModeDecTime
    print()

print("Overall Average Encryption Time = {} ms".format(mean(avgEncTime)*1000))
del avgEncTime
print("Overall Average Decryption Time = {} ms".format(mean(avgDecTime)*1000))
del avgDecTime
