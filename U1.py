def kysiNumber(sonum):
    while True:
        try:
            userInput = int(input(sonum))
        except ValueError:
            print("See pole number! Proovi uuesti...")
            continue
        else:
            break
    return userInput


print('\n ===== ÜLESANNE 1 =====')
# 1. Küsige kasutajalt 2 arvu. Printige kõik paarisarvud mis jäävad nende kahe arvu vahele.
esimene = kysiNumber("Sisesta palun esimene number : ")
teine = kysiNumber("Sisesta palun teine number : ")
# Kui esimene on suurem, kui teine vahetame väärtused
if (esimene > teine):
    teine = esimene + teine
    esimene = teine - esimene
    teine = teine - esimene


print([esimene, teine])

for i in range(esimene, teine):
    if(i%2==0):
        print(i)
