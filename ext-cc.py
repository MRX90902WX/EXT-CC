from time   import sleep
from bs4    import BeautifulSoup
import re, time, os, sys, datetime

class extrapola:
  def __init__(self,bin1,bin2):
    self.bin1=bin1
    self.bin2=bin2
    self.ccout=''

  #Extrapolacion por similitud
  def simpleE(self):
    if(len(self.bin1)!=16 or len(self.bin2)!=16):
      return 'FORMATO INCORRECTO P SimpleE'
    if(self.bin1[:1] != "3" or self.bin2[:1] != "3"):                                                                
      if(self.bin1[:6] != self.bin2[:6]):
        return 'FORMATO INCORRECTO P SimpleE'
      for letter in range(len(self.bin1)):
        if(self.bin1[letter] == self.bin2[letter]):
          self.ccout += self.bin1[letter]
        else:
          self.ccout +='x'
    else:
      self.ccout = False
    return self.ccout
    self.ccout = ''
  #Extrapolacion por lugar Banco
  def compleE(self):
    if(not len(self.bin1)==16 or not len(self.bin2)==16):
      return 'FORMATO INCORRECTO P CompleE'
    if(self.bin1[:1] != "3" or self.bin2[:1] != "3"):
      if(self.bin1[:6] != self.bin2[:6]):
        return 'FORMATO INCORRECTO P CompleE'
      cuerpo1 = self.bin1[:8]
      cuerpo2 = self.bin2[8:]
      #multiplica
      ccmult=''
      for num in range(len(cuerpo1)):
        ccmult = ccmult + str(int(cuerpo1[num])*int(cuerpo2[num]))
      #extragenerado
      cuerpo1+=ccmult[:8]
      #comparacion
      for letter in range(len(self.bin1)):
        if(self.bin1[letter] == cuerpo1[letter]):
          self.ccout += self.bin1[letter]
        else:
          self.ccout +='x'
      if(self.ccout[15:]=='x'):
        self.ccout = self.ccout[:15]+'1'
      return(self.ccout)
      self.ccout = ''
  #Extrapolacion Avanzada
  def avanE(self):
    if(not len(self.bin1)==16 or not len(self.bin2)==16):
      return 'FORMATO INCORRECTO P AvanE'
    if(self.bin1[:1] != "3" or self.bin2[:1] != "3"):
      if(self.bin1[6:8] != self.bin2[6:8]):
        return 'FORMATO INCORRECTO P AvanE'
      elif(self.bin1[:6] != self.bin2[:6]):
        return 'FORMATO INCORRECTO P AvanE'
      cuerpo1 = self.bin1[:8]
      mul1 = self.bin1[9:11]
      mul2 = self.bin2[9:11]
      #se suman
      mul1= str(int(mul1[0:1]) + int(mul1[1:]))
      mul2= str(int(mul2[0:1]) + int(mul2[1:]))
      #Re suman dobles
      while True:
        if(len(mul1) >= 2):
          mul1= str(int(mul1[0:1]) + int(mul1[1:]))
          continue
        elif(len(mul2) >= 2):
          mul2= str(int(mul2[0:1]) + int(mul2[1:]))
        else:
          break
      #Division
      mul1 = str(int(mul1) / 2)
      mul2 = str(int(mul2) / 2)
      #Multiplicacion
      mul1 = str(round(float(mul1)*5,))
      mul2 = str(round(float(mul2)*5,))
      #suma
      cuerpo1+=str(int(mul1)+int(mul2))
      self.ccout= cuerpo1
      for i in range(6):
        self.ccout+='x'
      return(self.ccout)
      self.ccout = ''

    else:
      return 'Invalid Format'
  #Extrapolacion 343
  def grupE(self):
    if(not len(self.bin1)==16):                                                                                                                                                        
      return 'Invalid Format grupE'
    if(self.bin1[:1] != "3" or self.bin2[:1] != "3"):
      self.ccout = self.bin1[:6]+self.bin1[6:7]+'x'+self.bin1[8:9]+self.bin1[9:10]+'xx'+self.bin1[12:13]+self.bin1[13:14]+'x'+self.bin1[15:]
      value=self.ccout
      return value


    else:
      return 'Invalid Format'
  #Extrapolacion 5
  def fivE(self):
    if(not len(self.bin1)==16):
      return 'Invalid Format grupE'
    if(self.bin1[:1] != "3" or self.bin2[:1] != "3"):
      self.ccout=self.bin1[:11]
      for i in range(5):
        self.ccout= self.ccout +"x"
      return(self.ccout)
    else:
      return "Invalid Format"
  #Extrap X
  def xiE(self):
    if(not len(self.bin1)==16):
      return 'Invalid Format grupE'
    if(self.bin1[:1] != "3" or self.bin2[:1] != "3"):
      self.ccout=self.bin1[:6]+'xxxx'+self.bin1[10:14]+'xx'
      return(self.ccout)
    else:
      return "Invalid Format"
  #Extrapolacion X
  def xiiE(self):
    if(not len(self.bin1)==16):
      return 'Invalid Format grupE'
    if(self.bin1[:1] != "3" or self.bin2[:1] != "3"):
      self.ccout=self.bin1[:10]
      for i in range(6):
        self.ccout= self.ccout +"x"
      return(self.ccout)
    else:
      return "Invalid Format"
  #Extrapolacion X
  def xiiiE(self):
    if(not len(self.bin1)==16):
      return 'Invalid Format grupE'
    if(self.bin1[:1] != "3" or self.bin2[:1] != "3"):
      self.ccout=self.bin1[:7]+'x'+self.bin1[8:9]+'xxx'+self.bin1[12:14]+'xx'
      return(self.ccout)
    else:
      return "Invalid Format"
  #Extrapolacion X
  def xiiiiE(self):
    if(not len(self.bin1)==16):
      return 'Invalid Format grupE'
    if(self.bin1[:1] != "3" or self.bin2[:1] != "3"):
      self.ccout=self.bin1[:7]+'xx'+self.bin1[10:11]+'x'+self.bin1[12:13]+'xxxx'
      return(self.ccout)
    else:
      return "Invalid Format"
def extrapolar(bin1,bin2=' '):
    try:
      message='\n'
      if(bin2!= ' ' and bin2!='' and bin2!=False):
        message+= 'Similitud -->' + extrapola(bin1,bin2).simpleE() +'\n'
        message+= 'Banco     -->' + extrapola(bin1,bin2).compleE() +'\n'
      message+= 'XB1       -->' + extrapola(bin1,bin2).grupE() +'\n'
      message+= 'XB2       -->' + extrapola(bin1,bin2).fivE() +'\n'
      message+= 'XB3       -->' + extrapola(bin1,bin2).xiiiiE() + "\n"
      message+= 'XB4       -->' + extrapola(bin1,bin2).xiiiE() + "\n"
      message+= 'XB5       -->' + extrapola(bin1,bin2).xiE() + '\n'
      message+= 'XB6       -->' + extrapola(bin1,bin2).xiiE() + "\n"
      return(message)
    except:                                                                                                                                                                            
      return('Error: BAD FORMAT')


def extrapolatodoB():
  os.system('clear')
  print("\033[1;32m    ______     __")
  print("\033[1;32m   / ____/  __/ /_      __________")
  print("\033[1;37m  / __/ | |/_/ __/_____/ ___/ ___/")
  print("\033[1;37m / /____>  </ /_/_____/ /__/ /__")  
  print("\033[1;32m/_____/_/|_|\__/      \___/\___/")                                  
  print("")
  print("\033[1;31m              𝑽.\033[1;37m 1.3")
  print("\033[1;31m             By:\033[1;37m Lanniscaf")       
  os.system("sleep 1")
  print("")
  print("\033[1;36m---------------------------------------")
  print("\033[1;31mUPS: \033[1;37mESTE PROCESO REQUIERE DOS TARJETAS!")
  print("\033[1;36m---------------------------------------") 
  print("")
  os.system("sleep 1")
  tarjeta1=input('\033[1;35m'+'TARJETA 1 --> '+'\033[0m')
  tarjeta2=input('\033[1;35m'+'TARJETA 2 (OPCIONAL) --> '+'\033[0m')
  if(tarjeta2=='' or tarjeta2==' '):
    tarjeta2=False
  print('\033[1;32m',"\t",extrapolar(tarjeta1,tarjeta2),end='\n')
extrapolatodoB()
