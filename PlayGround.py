import time

#def gen_keys():

def encrypt():
    message = raw_input("Please enter your message:")
    e = 131
    n = 21971
    start = time.time()
################################
    
    for x in message:
        nummes = ord(x)
        encrypted = pow(nummes, e, n)
        denumencry = unichr(encrypted)
        encrypted += denumencry
        print("Your message is know ready:")
        print 
    
    
################################
    end = time.time()
    
    print("The time taken was", end - start)
