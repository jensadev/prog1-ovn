inmatning = int(input('Skriv in antalet sekunder: '))

tim = inmatning % 3600
min = inmatning % 60
sek = inmatning % 1

print(f'Timmar: {tim} \nMinuter: {min} \nSekunder: {sek}')
