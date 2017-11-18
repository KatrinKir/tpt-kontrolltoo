def keskmine(num1list):
    summa = sum(num1list)
    arv = float(len(num1list))
    return summa / arv


# 3
print(' ===== ÜLESANNE 3 =====')
num1list = '11 15 6 13 13 25 32 11 20 5 31 16 32 29 11 13 3 29 28 24'
num2list = '5 19 16 4 12 7 2 28 34 29 29 36 6 8 24 18 31 7 1 7'
# (1
list1 = num1list.split()
list1 = list(map(int, list1))
list2 = num2list.split()
list2 = list(map(int, list2))
list3 = [x for x in list1 if x in list2]

list1.sort()
list2.sort()

print('Kahe all oleva listi: ')
print(list1)
print(list2)
print("\n 1) Ühisosa on:")
print(list3)

# (2
print("\n 2) Mõlemalisti suurim väärtus :")
print(max([max(list1), max(list2)]))

# (3
print("\n 3)Mõlema listi väikseim väärtus :")
print(min([min(list1), min(list2)]))
# (4
print("\n 4) Listi keskimine on :")

print("\tEsimese listi keskmine on :")
print(keskmine(list1))

print("\tTeise listi keskmine on :")
print(keskmine(list2))

#(5
print("\n5)Listide keskmine on : ")
print(keskmine([keskmine(list1), keskmine(list2)]))
