# Input, assignment
name = input('What is your name?\n')
print('Heips! Käytä pistettä desimaalina, %s.' % name)


import decimal
try:
    raha=decimal.Decimal(input("Ensimmäinen rahamäärä: "))
    korko=decimal.Decimal(input("Ensimmäinen korko:"))
    # ottaa rahamäärän, jakaa sen sadalla, ja kertoo sen korolla.
    convert=(raha/100*korko)
    print(convert/12)
except decimal.InvalidOperation:
    print("Invalid input")
try:
    raha1=decimal.Decimal(input("Toinen rahamäärä:" ))
    korko1=decimal.Decimal(input("Toinen korko:" ))
    # ottaa rahamäärän, jakaa sen sadalla, ja kertoo sen korolla.
    convert1=((raha1/100)*korko1)
    print(convert1/12)
except decimal.InvalidOperation:
    print("Invalid input")
try:
    raha2=decimal.Decimal(input("Kolmas rahamäärä:" ))
    korko2=decimal.Decimal(input("Kolmas korko:" ))
    # ottaa rahamäärän, jakaa sen sadalla, ja kertoo sen korolla.
    convert2=((raha2/100)*korko2)
    print(convert2/12)
except decimal.InvalidOperation:
    print("Invalid input")
    # jakaa kaikki kolme summaa kahdellatoista
    # joka antaa kuukauden koron kertaa kolme
print(convert/12+convert1/12+convert2/12)
