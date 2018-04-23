import sys, time
global n

def startup():
    end = 0
    while end != 1:
        print "Welcome to CryptTables, the simple solution do a big problem."
        unicodelist = list()
        encryptedlist = list()
        x = 0
        while x != 1:
            print "Loading Unicode Information... Please Wait"
            numlist = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127]
            for x in numlist:
                unicodelist += chr(x)
            x = 1 #Set to Finish the Unicode assignment
        mainmenu()
def mainmenu():
    print "Would you like to encrypt, decrypt, or exit? Note: You can call for the seperate functions if you aready ran startup() by calling encrypt() or decrypt()."
    x = 0
    while x != 1:
        command = str(raw_input("Command:"))
        if command == "Encrypt" or command == "encrypt":
            encrypt()
        elif command == "Decrypt" or command == "decrypt":
            decrypt()
        elif command  == "Exit" or command == "exit":
            print "Thank you for using CryptTables! - Sam and Dane"
            x = 1
            end = 1
        else:
            print "This is not a recongizable command. Please type encrypt, decrypt, or exit."


def decrypt(e, n):
    x = 1
    if e > 0 and n > 0:
        for a in unicodelist:
            holder = ord(a)
            holder += encryptedlist
    else:
        print "It looks like you id not run startup(). Please restart the program and run startup()."
        end = 1 
    
def encrypt():
    x = 1
    print "encrypt"