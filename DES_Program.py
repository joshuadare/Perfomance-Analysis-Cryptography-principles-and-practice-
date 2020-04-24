from Crypto.Cipher import DES
from Crypto import Random
from Crypto.Util import Counter
from timeit import default_timer as timer

print('')
#Using 8 bytes keys
#Electronic Codebook Mode (ECB)
print('Electronic Codebook Mode')
start = timer()
key = 'Eight ky'
iv =  Random.new().read(DES.block_size)
cipher = DES.new(key, DES.MODE_ECB)
plaintext = 'aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbccccccccccccccccdddddddddddddddd'
msg = cipher.encrypt(plaintext)
print('Ciphertext:')
print(msg)

cipher1 = DES.new(key, DES.MODE_ECB)
decryptedtext = cipher1.decrypt(msg)
print('Plaintext:')
print(decryptedtext)
end = timer()
print('Elapsed time:')
print(end - start)
print('')
print('-------------------------------------------------------')

#CipherBlock Chain Mode (CBC)
print('')
print('Cipher-Block Chain Mode')
start1 = timer()
key = 'Eight ky'
iv1 =  Random.new().read(DES.block_size)
cipher2 = DES.new(key, DES.MODE_CBC , iv1)
plaintext = 'aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbccccccccccccccccdddddddddddddddd'
msg2 = cipher2.encrypt(plaintext)
print('Ciphertext:')
print(msg2)

cipher3 = DES.new(key, DES.MODE_CBC, iv1)
decryptedtext1 = cipher3.decrypt(msg2)
print('Plaintext:')
print(decryptedtext1)
end1 = timer()
print('Elapsed time:')
print(end1 - start1)
print('')
print('-------------------------------------------------------')


#Cipher-Feedback Mode
print('')
print('Cipher-Feedback Mode')
start2 = timer()
key = 'Eight ky'
iv2 =  Random.new().read(DES.block_size)
cipher4 = DES.new(key, DES.MODE_CFB , iv2)
plaintext = 'aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbccccccccccccccccdddddddddddddddd'
msg3 = cipher4.encrypt(plaintext)
print('Ciphertext:')
print(msg3)

cipher5 = DES.new(key, DES.MODE_CFB, iv2)
decryptedtext2 = cipher5.decrypt(msg3)
print('Plaintext:')
print(decryptedtext2)
end2 = timer()
print('Elapsed time:')
print(end2 - start2)
print('')
print('-------------------------------------------------------')

#Output-Feedback Mode (OFB)
print('')
print('Output-Feedback Mode')
start3 = timer()
key = 'Eight ky'
iv3 =  Random.new().read(DES.block_size)
cipher6 = DES.new(key, DES.MODE_OFB , iv3)
plaintext = 'aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbccccccccccccccccdddddddddddddddd'
msg4 = cipher6.encrypt(plaintext)
print('Ciphertext:')
print(msg4)

cipher7 = DES.new(key, DES.MODE_OFB, iv3)
decryptedtext3 = cipher7.decrypt(msg4)
print('Plaintext:')
print(decryptedtext3)
end3 = timer()
print('Elapsed time:')
print(end3 - start3)
print('')
print('-------------------------------------------------------')

#Counter Mode (ctr)
print('')
print('Counter Mode')
start4 = timer()
key = 'Eight ky'
ctr = Counter.new(64)
cipher8 = DES.new(key, DES.MODE_CTR , counter = ctr)
plaintext = 'aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbccccccccccccccccdddddddddddddddd'
ciphertxt = cipher8.encrypt(plaintext)
print('Ciphertext:')
print(ciphertxt)

ctr1 = Counter.new(64)
cipher9 = DES.new(key, DES.MODE_CTR, counter = ctr1)
decryptedtext4 = cipher9.decrypt(ciphertxt)
print('Plaintext:')
print(decryptedtext4)
end4 = timer()
print('Elapsed time:')
print(end4 - start4)
