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

start(1,2,3)
print(rotorA)
print(rotorB)
print(rotorC)
