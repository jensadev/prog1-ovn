# Uppgift 2.5
pris = float(input('Skriv varans pris: ')) #inmatning, konvertera till float
moms = float(input('Skriv in varans moms i procent: ')) #inmatning, konvertera till float

# räkna ut priset exklusive moms, pris delat i momsen omvandlat till .decimal +1
emoms = pris / (moms / 100 + 1)

# skriv ut resultatet
print(f'Priset exklusive moms: {emoms}')
print(f'Momsen är: {pris - emoms} ')