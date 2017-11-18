# 2. Laadige alla kttekst.txt
#   1) Kirjutage Programm mis loeb kokku mitu sõna on tekstis
#   2) Lugege kokku mitu sõna on väiksemad kui 5 tähte
print('\n ===== ÜLESANNE 2 =====')
fin = open('kttekst.txt')

lines = fin.readlines()

wordsCount = 0
words5Count = 0

for line in lines:
    line = line.lower().replace(',', '').replace('.', '')
    words = line.split()
    wordsCount += len(words)
    for word in words:
        if (len(word) < 5):
            words5Count += 1

fin.close()

print('Tulemused:')
print('\tLeiti sõnu: ' + str(wordsCount))
print('\tLeiti 5 sümbolist lühemaid sõnu: ' + str(words5Count))

