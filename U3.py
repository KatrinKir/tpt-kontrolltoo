# 3
print('\n ===== ÜLESANNE 3 =====')
num1list = '11 15 6 13 13 25 32 11 20 5 31 16 32 29 11 13 3 29 28 24'
num2list = '5 19 16 4 12 7 2 28 34 29 29 36 6 8 24 18 31 7 1 7'
# (1
list1 = num1list.split()
list2 = num2list.split()
list3 = set(list1).intersection(set(list1))

print("Ühisosa:")
print("\n".join(list3))


# (4
def printAvg(num1list):
    summa = sum(num1list)
    arv = float(len(num1list))
    print(summa / arv)
    print('Keskmine')


def printAvg(num2list):
    summa = sum(num2list)
    arv = float(len(num2list))
    print(summa / arv)
