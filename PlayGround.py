import time

#def gen_keys():

e = 131
n = 21971
d = 17867
encryptedmessage = ""
decrypted_message = ""
encryptedmessage2 = ""
decrypted_message2 = ""
LUT_encryption = dict()

encryptedmessage2 = ""


def encryptanddecrypt():
    message = raw_input("Please enter your message:")
    start = time.time()
#######Encryption#########
    
    for x in message:
        nummes = ord(x)
        encrypted = pow(nummes, e, n)
        denumerize = unichr(encrypted)
        encryptedmessage += denumerize
    print encryptedmessage

    
#######Decryption########    
    for t in encryptedmessage:
        nummes = ord(t)
        decrypt = pow(nummes, d, n)
        denumerize = chr(decrypt)
        decrypted_message += denumerize
    print decrypted_message
    
    
######Encryption V2########

    print "V2 Encrypt"
    for x in message:
        if x in LUT_encryption:
            encryptedmessage2 += LUT_encryption[x]
        else:
            nummes = ord(x)
            encrypted = pow(nummes, e, n)
            denumerize = unichr(encrypted)
            encryptedmessage2 += denumerize
            LUT_encryption[x] = denumerize
    
#Also called LUT (Look Up Tables, Hash Tables, Dictionaries)
    

#######Decryption V2########
    print "V2 Decrypt"
    for t in encryptedmessage2:
        if t in LUT_decryption:
            decryptedmessage2 += LUT_decryption[t]
        else:
            nummes = ord(t)
            decrypt = pow(nummes, d, n)
            denumerize = chr(decrypt)
            LUT_decryption[t] += denumerize
    print decrypted_message2






    end = time.time()
    
    print("Time", end - start)

#####Loading Animation####

import time
import sys

done = 'false'
#here is the animation
def animate():
    while done == 'false':
        sys.stdout.write('\rloading |')
        time.sleep(0.1)
        sys.stdout.write('\rloading /')
        time.sleep(0.1)
        sys.stdout.write('\rloading -')
        time.sleep(0.1)
        sys.stdout.write('\rloading \\')
        time.sleep(0.1)
    sys.stdout.write('\rDone!     ')

#long process here
done = 'true' #fix later


######Cryption Table########
