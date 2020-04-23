import pyaes, os, psutil, tracemalloc

#from statistics import mean

tracemalloc.start()
print ("Benchmark CPU: {}% ".format(psutil.cpu_percent(interval=1)))
current, peak = tracemalloc.get_traced_memory()
print ("Benchmark memory: {:10f}MB used\tPeaked at: {:10f}MB".format(current / 2**20, peak / 2**20))
tracemalloc.stop()

# 128 bit, 192 bit and 256 bit keys

key_128 = os.urandom(16)

key_192 = os.urandom(24)

key_256 = os.urandom(32)

keys = {"AES-128": key_128, "AES-192": key_192, "AES-256": key_256}

# For some modes of operation we need a random initialization vector
# of 16 bytes
iv = os.urandom(16)

#plaintext = "Text may be any length you wish, no padding is required"

plaintext = input("Enter message to be encrypted: ")
print()


for mode in pyaes.AESModesOfOperation.values():
    for key in keys:
        aes = mode(keys[key], iv) if mode == pyaes.AESModeOfOperationCFB else mode(keys[key])
        
        tracemalloc.start()
        encrypter = pyaes.Encrypter(aes)
        ciphertext = encrypter.feed(plaintext)
        ciphertext += encrypter.feed()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        
        # show the encrypted data
        print (key, mode.name[-5:])
        print ("Encrypted message CPU: {}% ".format(psutil.cpu_percent(interval=1)))
        print ("Encryption memory: {:10f}MB used\tPeaked at: {:10f}MB".format(current / 2**20, peak / 2**20))
        
        # DECRYPTION
        # CRT mode decryption requires a new instance be created
        aes = mode(keys[key], iv) if mode == pyaes.AESModeOfOperationCFB else mode(keys[key])
        
        # decrypted data is always binary, need to decode to plaintext
        tracemalloc.start()
        decrypter = pyaes.Decrypter(aes)
        decrypted = decrypter.feed(ciphertext)
        decrypted += decrypter.feed()
        decrypted = decrypted.decode("utf-8")
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        
        print ("Decryted message CPU: {}% ".format(psutil.cpu_percent(interval=1)))
        print ("Decryption memory: {:10f}MB used\tPeaked at: {:10f}MB".format(current / 2**20, peak / 2**20))
        print()
