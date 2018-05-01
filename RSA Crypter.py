def encrypt(e,n):
    message = ''
    encrypted_message = ''
    message = input('Please type your message:')
    for x in message:
        nummes = ord(x)
        encrypt = pow(nummes, e, n)
        denumerize = chr(encrypt)
        encrypted_message += denumerize

    print("Encrypted message:", encrypted_message)
    

def decrypt(d,n):
    decrypted_message = ''    
    encrypted_message= input("Input the encrypted message:")
    for t in encrypted_message:
        numerize = ord(t)
        decrypt = pow(numerize,d,n)
        denumerize = chr(decrypt)
        decrypted_message += denumerize
        
    print("Here is the decrypted message:", decrypted_message)


def mainmenu():
    command = input("Hello, would you like to encrypt, decrypt, or exit?") 
    while command!= "exit" and command!= "Exit":
        if command != "encrypt" and command!= "decrypt" and command!= "exit":
          command = input("Hello, would you like to encrypt, decrypt, or exit?")
        else:
          if command == "encrypt":
              e = int(input("What is your e value?"))
              n = int(input("What is your n value?"))
              encrypt(e,n)
              command = input("Hello, would you like to encrypt, decrypt, or exit?") 
          
          elif command == "decrypt":
              d = int(input("What is your d value?"))
              n = int(input("What is your n value?")) 
              decrypt(d,n)
              command = input("Hello, would you like to encrypt, decrypt, or exit?")
    print("Thanks for using our encryption table. - Sam and Dane")
mainmenu()