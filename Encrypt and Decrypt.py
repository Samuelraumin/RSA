import random

title = """
·▄▄▄▄  .▄▄ ·     ▄▄▄ . ▐ ▄  ▄▄· ▄▄▄   ▄· ▄▌ ▄▄▄·▄▄▄▄▄▪         ▐ ▄ 
██▪ ██ ▐█ ▀.     ▀▄.▀·•█▌▐█▐█ ▌▪▀▄ █·▐█▪██▌▐█ ▄█•██  ██ ▪     •█▌▐█
▐█· ▐█▌▄▀▀▀█▄    ▐▀▀▪▄▐█▐▐▌██ ▄▄▐▀▀▄ ▐█▌▐█▪ ██▀· ▐█.▪▐█· ▄█▀▄ ▐█▐▐▌
██. ██ ▐█▄▪▐█    ▐█▄▄▌██▐█▌▐███▌▐█•█▌ ▐█▀·.▐█▪·• ▐█▌·▐█▌▐█▌.▐▌██▐█▌
▀▀▀▀▀•  ▀▀▀▀      ▀▀▀ ▀▀ █▪·▀▀▀ .▀  ▀  ▀ • .▀    ▀▀▀ ▀▀▀ ▀█▄▀▪▀▀ █▪
                        Cryption At Best
"""

######## Prime Number Tester #########
def primetest(number, randomprimetest):
  # print (randomprimetest)  // use to check what primetest is being used for, hash out later
  if (int(number) == 1 or 0):
    print (int(number), "is not a prime number!")
    return False
  n_square = (int(number)**(1/2.0))
  m = round(n_square)
  m_2 = m
  sizelist = []
  passlist = []
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
      print (int(number), "is not a prime number!")
    return False
  if (len(passlist) == 1):
    e = int(float(passlist[0]))
    if (randomprimetest == True):
      print ("\n'e' is: ", e)
    return True

######### Range Test ##########
def inrange(low, test, high):
  if low < test < high:
    return True
  else:
    return False
    
######### Public Key ##########
def publicgen(p, q, e_fail=None):
  public_n = int(p)*int(q)
  userchoice = input("\n[1] Choose Prime (e)\n[2] Randomly choose Prime (e)\nChoice: ")
  while True:
    if (userchoice == "1"):
      print ("\nAcceptable range: (2 - ", public_n-1, ")", sep="")
      e = input("Enter your desired Prime 'e' value: ")
      while True:
        if inrange(1, int(e), public_n) == True:
          while True:
            if primetest(int(e), False) == False:
              e = input("Corrected Prime Value within range: ")
              break
            elif primetest(int(e), False) == True:
              if e_fail == True:
                print ("Your new Public Key is (", e, ", ", public_n, ")", sep="")
              elif e_fail != True:
                print ("Your Public Key is (", e, ", ", public_n, ")", sep="")
              privategen(p, q, e, e_fail, public_n)
              return
        elif inrange(1, int(e), public_n) != True:
          e = input("Input not within acceptable range: ")
    elif (userchoice == "2"):
      e = random.randint(2, (public_n))
      if e % 2 == 0:
        while True:
          e = random.randint(2, (public_n))
          if (primetest(e, True)) == True:
            if e_fail == True:
              print ("Your new Public Key is (", e, ", ", public_n, ")", sep="")
            elif e_fail != True:
              print ("Your Public Key is (", e, ", ", public_n, ")", sep="")
            privategen(p, q, e, e_fail, public_n)
            return
      elif (primetest(e, True)) == True:
        if e_fail == True:
          print ("Your new Public Key is (", e, ", ", public_n, ")", sep="")
        elif e_fail != True:
          print ("Your Public Key is (", e, ", ", public_n, ")", sep="")
        privategen(p, q, e, e_fail, public_n)
        return
    else:
      userchoice = input("Invalid Input: ")
  return


########## Private Key ############
def privategen(p, q, e, e_fail, public_n):
  
  # (d * x) % y = 1
  
  phi_n = (int(p)-1) * (int(q)-1)
  print ("\n  Private Key Generation")
  if e_fail != True:
    print ("\nΦ(n) is:", phi_n)
  print ("\nYour current Equation:\n((", e,")*d) = 1(mod(", phi_n, "))", sep='')
  attempts=input("\nHow many attempts do you want to try to find 'd'? (Recommended: minimum: 10,000,000)\nAttempts: ")
  d=0
  twop = True
  fourp = True
  sixp = True
  eightp = True
  while (d <= int(attempts)):
      calculation = ((int(d)*(int(e))) % (int(phi_n)))
      if int(calculation) == 1:
        print ("\n'd' is: ", d, "\nYour Private Key is (", d, ", ", phi_n, ")", sep="")
        mainmenu(False, p, q, public_n, e, d)
        return
      elif d == int(attempts):
        fail_ans = input("■■■■■■■■■■ 100% of Allotted attempts tried...\n\nUh oh! It's either unsolvable or I wasn't given enough possible attempts! Want to start over?\n[1] Change 'e' value\n[2] Enter more attempts\n[3] Return to Main Menu\nChoice:")
        while True:
          if (fail_ans == '1'):
            publicgen(p, q, True)
          elif (fail_ans == '2'):
            twop = True
            fourp = True
            sixp = True
            eightp = True
            attempts=input("Enter a number bigger than your last attempt: ")
            break
          elif (fail_ans == "3"):
            d=0
            mainmenu(False, p, q, public_n, e, d)
            return
          else:
            print ("Invalid input!")
            fail_ans = input("Choice: ")
      else:
        d+=1
        if (d == (int(attempts)*.2)):
          if (twop == True):
            print("\n■■□□□□□□□□ 20% of Allotted attempts tried...")
            twop = False
        elif (d == (int(attempts)*.4)):
          if (fourp == True):
            print("■■■■□□□□□□ 40% of Allotted attempts tried...")
            fourp = False
        elif (d == (int(attempts)*.6)):
          if (sixp == True):
            print("■■■■■■□□□□ 60% of Allotted attempts tried...")
            sixp = False
        elif (d == (int(attempts)*.8)):
          if (eightp == True):
            print("■■■■■■■■□□ 80% of Allotted attempts tried...")
            eightp = False
  return

######### Encryption ############
def encrypt(e, public_n, p, q, d):
  message = ''
  encrypted_message = ''
  message = input('\nPlease type the message you wish to encrypt:')
  for letter in message:
      numerated_letter = ord(letter)
      encrypted_message += chr(pow(numerated_letter, e, public_n))
  print("Encrypted message:", encrypted_message)
  mainmenu(False, p, q, public_n, e, d)
  return

########## Decryption ##########
def decrypt(d, p, q, public_n, e):
  decrypted_message = ''    
  encrypted_message= input("\nInput the encrypted message:")

  for letter in encrypted_message:
      numerated_letter = ord(letter)
      decrypted_message += chr(pow(numerated_letter, d, public_n))
  print("Here is the decrypted message:", decrypted_message)
  mainmenu(False, p, q, public_n, e, d)
  return

############ Startup ###########
def mainmenu(startup, p=0, q=0, public_n=0, e=0, d=0):
  if (startup == True):
    print (title)
    firstcom = input("\nWhat do you wish to do?\n[1] Generate a Public and Private Key\n[2] Encrypt\n[3] Decrypt\n[4] Check stored variables\n[5] Exit\nChoice:")
  elif (startup == False):
    firstcom = input("\nWhat do you wish to do now?\n[1] Generate another Public and Private Key\n[2] Encrypt\n[3] Decrypt\n[4] Check stored variables\n[5] Exit\nChoice:")
  while firstcom != "5":
    if firstcom == "1":
      print ("\n  Public Key Generation")
      p = input("\nEnter your Prime 'p' value:")
      while not primetest(p, False):
        p = input("Enter your Prime 'p' value:")
      q = input("Enter your Prime 'q' value:")
      while not primetest(q, False):
        q = input("Enter your Prime 'q' value:")
      print ("\n'n' is ", int(p)*int(q))
      publicgen(p, q)
      mainmenu(False)
      return
    elif (firstcom == "2"):
      print ("\nLet's Encrypt!")
      encryptcom = input("[1] Encrypt using a Public Key\n[2] Encrypt using stored variables\n[3] Return\nChoice: ")
      while True:
        if (encryptcom == "1"):
          e = int(input("\nExample Public Key: (e, n)\nEnter your 'e' value: "))
          public_n = int(input("Enter your 'n' value: "))
          encrypt(e, public_n, p, q, d)
          return
        elif (encryptcom == "2"):
          if (p == 0):
            print ("\nYou currently have no stored variables! Want to generate some now?")
            thirdcom = input("[1] Generate a Public and Private Key now\n[2] Return to Main Menu\nChoice: ")
            while True:
              if (thirdcom == "1"):
                print ("\n  Public Key Generation")
                p = input("\nEnter your Prime 'p' value:")
                while not primetest(p, False):
                  p = input("Enter your Prime 'p' value:")
                q = input("Enter your Prime 'q' value:")
                while not primetest(q, False):
                  q = input("Enter your Prime 'q' value:")
                print ("\nn is ", int(p)*int(q))
                publicgen(p, q)
                return
              elif (thirdcom == "2"):
                mainmenu(False, p, q, public_n, e, d)
                return
              else:
                thirdcom = input("Choice:")
          else:
            print ("\nCurrent Public Key: (", e, ", ", public_n, ")", sep="")
            encrypt(e, public_n, p, q, d)
            return
        elif (encryptcom == "3"):
          mainmenu(False, p, q, public_n, e, d)
          return
        else:
          encryptcom = input("Choice:")
    elif (firstcom == "3"):
      print ("\nLet's Decrypt!")
      decryptcom = input("[1] Decrypt using personal Private Key\n[2] Decrypt using stored variables\n[3] Return\nChoice: ")
      while True:
        if (decryptcom == "1"):
          d = int(input("\nExample Private Key: (d, Φ(n))\nEnter your 'd' value: "))
          public_n = int(input("Enter your 'n' value: "))
          decrypt(e, public_n, p, q, d)
          return
        elif (decryptcom == "2"):
          if (p == 0):
            print ("\nYou currently have no stored variables! Want to generate some now?")
            thirdcom = input("[1] Generate a Public and Private Key now\n[2] Return to Main Menu\nChoice: ")
            while True:
              if (thirdcom == "1"):
                print ("\n  Public Key Generation")
                p = input("\nEnter your Prime 'p' value:")
                while not primetest(p, False):
                  p = input("Enter your Prime 'p' value:")
                q = input("Enter your Prime 'q' value:")
                while not primetest(q, False):
                  q = input("Enter your Prime 'q' value:")
                print ("\nn is ", int(p)*int(q))
                publicgen(p, q)
                return
              elif (thirdcom == "2"):
                mainmenu(False, p, q, public_n, e, d)
                return
              else:
                thirdcom = input("Choice:")
          else:
            print ("\nCurrent Private Key: (", d, ", ", public_n, ")", sep="")
            decrypt(d, p, q, public_n, e)
            return
        elif (decryptcom == "3"):
          mainmenu(False, p, q, public_n, e, d)
          return
    elif (firstcom == "4"):
      print ("\n'p' is:", p, "\n'q' is:", q, "\n'n' is:", public_n, "\n'e' is:", e, "\n'd' is:", d)
      mainmenu(False, p, q, public_n, e, d)
      return
    else:
      firstcom = input("Choice:")
  print ("\nThanks for using our encryption table. - Sam and Dane [DS Encryption]")
  return
mainmenu(True)