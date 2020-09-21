svar = input('Antal sekunder: ') # läser in antalet sekunder från användaren
sek = int(svar) # konverterar svaret till ett heltal
print('Inmatningen:', sek)
tim = sek // 3600 # delar antalet sekunder med antalet sekunder på en timme, kapar till heltal med //
sek = sek % 3600 # använder modulo för att räkna ut antalet sekunder som blev över från timmarna
print('Rest från timmar:', sek)
min = sek // 60
sek = sek % 60
print('Rest från minuter:', sek)
print('Timmar:  ', tim)
print('Minuter: ', min)
print('Sekunder:', sek)