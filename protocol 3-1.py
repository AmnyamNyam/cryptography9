import random

#Открытые и закрытые ключи А
Ae = random.randint(1,20)
An = random.randint(1,20)
Ad = random.randint(1,20)



#А передает открытый ключ Б
Be = Ae

#1. Б выбирает случайное число Bk, вычисляется Br = Bk**Ae % An и посылает Ar A

Bk = random.randint(1,An-1)
Br = Bk ** Ae % An
Ar = Br

#2. А вычисляет Ak = Ar ** Ad и посылает Ak в Bk. Здесь мы не пишем Bk = Ak чтобы сравнить в 3 этапе.

Ak = Ar ** Ad

#3. Б проверяет соотношение Ak = Bk и если оно истинно, принимает доказательство, в противном случае - отвергает.

if Ak == Bk:
    print('{} == {}'.format(Ak,Bk))
    print('True')
else:
    print('{} != {}'.format(Ak, Bk))
    print('False')