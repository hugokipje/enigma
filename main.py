alfabet = "abcdefghijklmnopqrstuvwxyz"
rotorA = alfabet
rotorB = alfabet
rotorC = alfabet


def shift(tekst, amount):
  amount = amount % 26  
  eersteDeel = tekst[amount:26]
  tweedeDeel = tekst[0:amount]
  return eersteDeel + tweedeDeel

def start(a,b,c):  
  global alfabet
  global rotorA
  global rotorB
  global rotorC
  rotorA = shift(alfabet,a)
  rotorB = shift(alfabet,b)
  rotorC = shift(alfabet,c)

def encrypt(tekst):  
  global rotorA
  global rotorB
  global rotorC

  encryptedtekst = ""
  tekst = tekst.lower()  

  for letter in tekst:
    if not(letter in alfabet):
      encryptedtekst = encryptedtekst + letter
      continue

    rotorA = shift(rotorA,1)
    idx = alfabet.index(letter)
    encryptedletter = rotorA[idx]
    print(encryptedletter)
    
    idx = alfabet.index(encryptedletter)
    encryptedletter = rotorB[idx]
    print(encryptedletter)
    
    idx = alfabet.index(encryptedletter)
    encryptedletter = rotorC[idx]
    print(encryptedletter)

    encryptedtekst = encryptedtekst + encryptedletter
  
  return encryptedtekst

start(10,14,16)
tekst = input("Type your message:")
print(encrypt(tekst))
