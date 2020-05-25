alfabet = "abcdefghijklmnopqrstuvwxyz"
rotorA = alfabet
rotorB = alfabet
rotorC = alfabet


def shift(tekst, amount):
  amount = amount % 26  
  eersteDeel = tekst[amount:26]
  tweedeDeel = tekst[0:amount]
  return eersteDeel + tweedeDeel

print(shift(alfabet,9))
print(shift(alfabet,20))
print(shift(alfabet,23))
