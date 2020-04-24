import DES
import Random
import Counter
from timeit import default_timer as timer

print('')
#Keys fixed at 8 bytes = 64 bits
#Electronic Codebook Mode
print('Electronic Codebook Mode')
start = timer()
key = 'Eight ky'
iv =  Random.new().read(DES.block_size)
cipher = DES.new(key, DES.MODE_ECB , iv)
plaintext = 'aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbb'
msg = cipher.encrypt(plaintext)
print('Ciphertext:')
print(msg)

cipher1 = DES.new(key, DES.MODE_ECB, iv)
decryptedtext = cipher1.decrypt(msg)
print('Plaintext:')
print(decryptedtext)
end = timer()
print('Elapsed time:')
print(end - start)
print('')
print('---------------------------------------------')
print('---------------------------------------------')

#Cipher-Block Chaining Mode
print('')
print('Cipher-Block Chaining Mode')
start1 = timer()
key = 'Eight ky'
iv1 =  Random.new().read(DES.block_size)
cipher2 = DES.new(key, DES.MODE_CBC , iv1)
plaintext = 'aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbb'
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
print('---------------------------------------------')
print('---------------------------------------------')


#Cipher-Feedback Mode
print('')
print('Cipher-Feedback Mode')
start2 = timer()
key = 'Eight ky'
iv2 =  Random.new().read(DES.block_size)
cipher4 = DES.new(key, DES.MODE_CFB , iv2)
plaintext = 'aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbb'
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
print('---------------------------------------------')
print('---------------------------------------------')

#Output-Feedback Mode
print('')
print('Output-Feedback Mode')
start3 = timer()
key = 'Eight ky'
iv3 =  Random.new().read(DES.block_size)
cipher6 = DES.new(key, DES.MODE_OFB , iv3)
plaintext = 'aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbb'
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
print('---------------------------------------------')
print('---------------------------------------------')

#Counter Mode
print('')
print('Counter Mode')
start4 = timer()
key = 'Eight ky'
ctr = Counter.new(64)
cipher8 = DES.new(key, DES.MODE_CTR , counter = ctr)
pt = 'aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbb'
ct = cipher8.encrypt(pt)
print('Ciphertext:')
print(ct)

ctr1 = Counter.new(64)
cipher9 = DES.new(key, DES.MODE_CTR, counter = ctr1)
decryptedtext4 = cipher9.decrypt(ct)
print('Plaintext:')
print(decryptedtext4)
end4 = timer()
print('Elapsed time:')
print(end4 - start4)