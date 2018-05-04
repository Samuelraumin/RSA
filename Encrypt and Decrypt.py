import random

startup = """

·▄▄▄▄  .▄▄ ·     ▄▄▄ . ▐ ▄  ▄▄· ▄▄▄   ▄· ▄▌ ▄▄▄·▄▄▄▄▄▪         ▐ ▄ 
██▪ ██ ▐█ ▀.     ▀▄.▀·•█▌▐█▐█ ▌▪▀▄ █·▐█▪██▌▐█ ▄█•██  ██ ▪     •█▌▐█
▐█· ▐█▌▄▀▀▀█▄    ▐▀▀▪▄▐█▐▐▌██ ▄▄▐▀▀▄ ▐█▌▐█▪ ██▀· ▐█.▪▐█· ▄█▀▄ ▐█▐▐▌
██. ██ ▐█▄▪▐█    ▐█▄▄▌██▐█▌▐███▌▐█•█▌ ▐█▀·.▐█▪·• ▐█▌·▐█▌▐█▌.▐▌██▐█▌
▀▀▀▀▀•  ▀▀▀▀      ▀▀▀ ▀▀ █▪·▀▀▀ .▀  ▀  ▀ • .▀    ▀▀▀ ▀▀▀ ▀█▄▀▪▀▀ █▪

                        Cryption At Best
"""

######## Prime Number Tester #########
def primetest(number, randomprimetest, n=0):
  # print (randomprimetest)  // use to check what primetest is being used for, hash out later
  n_square = (int(number)**(1/2.0))
  m = round(n_square)
  m_2 = m
  sizelist = []
  passlist = []
  if (int(number) == 1):
    print (int(number), "is not a prime number! :(")
    return False
  while (m_2 >= 1):
    sizelist.append(str(m_2))
    m_2 -= 1
  for x in sizelist:
    if ((int(number)/m).is_integer() == True):
      passlist.append(str(int(number)/m))
    if (m > 1):
      m -= 1
  if (len(passlist) >= 2):
    if (randomprimetest == False):
      print (int(number), "is not a prime number! :(")
    return False
  if (len(passlist) == 1):
    e = int(float(passlist[0]))
    if (randomprimetest == True):
      print ("\nYour randomly generated prime number (e) is: ", e)
      find_d(e, n)
      if (command == 'encrypt'):
        encrypt(e,n)
    return True


########## Phi of n finder #########
def find_phin():
  print ("\n", "Φ(n) = (p-1)(q-1)\n")
  p = input("Enter your Prime 'p' value: ")
  # while True:
  #   try:
  #     p = input("Enter your Prime 'p' value: ")
  #   except ValueError:
  #     print ("Invalid")
  #   p = input("Enter your Prime 'p' value: ")
  while not primetest(p, False):
    p = input("Enter your Prime 'p' value: ")
  q = input("Enter your Prime 'q' value: ")
  while not primetest(q, False):
    q = input("Enter your Prime 'q' value: ")
  n = (int(p)-1) * (int(q)-1)
  print ("\n", "Φ(n) =", (int(p)-1) * (int(q)-1))
  userchoice = input("\n[1] Manually choose Prime (e)\n[2] Randomly choose Prime (e)\nChoice: ")
  n_choicepass = True
  while (n_choicepass != False):
    if (userchoice == "1"):
      manualchoice = input("Enter your desired Prime 'e' value: ")
      if (primetest(int(manualchoice), False, n) == True):
        break
      n_choicepass = True
    elif (userchoice == "2"):
      random_number = random.randint(2, (n-1))
      if random_number % 2 == 0:
        random_number = random.randint(2, (n-1))
      if (primetest(random_number, True, n)) == True:
        break
    else:
      userchoice = input("Invalid Input: ")
       
########## D Finder ############
def find_d(e, n):
    
    # (d * x) % y = 1

    print ("Your 'e' value is:", e)
    print ("Your 'Φ(n)' value is:", n)
    print ("\n((", e,")*d) = 1(mod(", n, "))", sep='')
    attempts=input("\nHow many attempts do you want to try to find 'd'?\nAttempts: ")
    d=0
    while (d <= int(attempts)):
        calculation = ((int(d)*(int(e))) % (int(n)))
        if int(calculation) == 1:
            print ("\nI found it!\nThe multiplier(d) is: ", d, "\nYour Private Key is (", d, ", ", n, ")\n", sep="")
            encrypt(e, n)
        elif d == int(attempts):
            print ("Sorry! It's either unsolvable or I wasn't given enough possible attempts!\nWant to start over?\n[1] Start over\n[2] Enter more attempts")
            fail_ans = input("Choice: ")
            while True:
              if (fail_ans == '1'):
                print ("\n-------------------")
                find_phin()
              elif (fail_ans == '2'):
                attempts=input("Enter a number bigger than your last attempt: ")
                break
              else:
                print ("Invalid input!")
                fail_ans = input("Choice: ")
        else:
            d+=1

######### Cryption Unit ##########

######### Encryption ############

def encrypt(e,n):
    message = ''
    encrypted_message = ''
    message = input('Please type the message you wish to encrypt:')
    for letter in message:
        nummes = ord(letter)
        encrypt = ((nummes**e) % n)
        encrypted_message += chr(encrypt)

    print("Encrypted message:", encrypted_message)

########## Decryption ##########

def decrypt(d,n):
    decrypted_message = ''    
    encrypted_message= input("Input the encrypted message:")
    for t in encrypted_message:
        nummes = ord(t)
        decrypt = ((nummes**d) % n)
        denumerize = chr(decrypt)
        decrypted_message += denumerize
        
    print("Here is the decrypted message:", decrypted_message)

############ Startup ###########
def mainmenu():
    print (startup)
    firstcom = input("\nDo you wish to generate your Private Key now or use an existing one?\n[1] Generate now\n[2] Use existing Private Key\n[3] Exit\nChoice:")
    while firstcom != "3":
      if firstcom == "1" or firstcom == "2" or firstcom == "3":
        if firstcom == "1":
          find_phin()
        elif firstcom == "2":
          command = input("[1] Encrypt\n[2] Decrypt\n[3] Return\nChoice:") 
          while command != "3":
            if command == "1":
              e = int(input("What is your e value?"))
              n = int(input("What is your n value?"))
              encrypt(e,n)
            elif command == "2":
              decrypt(d,n)
              command = input("\nWould you like to encrypt or decrypt again? Or exit?")
            else:
              command = input("[1] Encrypt\n[2] Decrypt\n[3] Return\nChoice:")
          mainmenu()
    command = "3"
    print("Thanks for using our encryption table. - Sam and Dane [DS Encryption]")

print ("To start the main options menu system, run mainmenu(). Encrypt and Decrypt are optional.")