import random
import time
#Этап 1

#1. Выбирает модуль n, равный произведению двух простых чисел

p = random.randint(3, 50)
q = random.randint(3, 50)

n = p * q
#2. Выбирает число v (открытый ключ), являющеейся квадратичным вычетом по модулю n и имеется обратное значение vl по модулю n

i = 0
while i == 0:
    x = random.randint(1, n)
    v = (x**2) % n
    if (v * x) % n == 1:
        i = 1
        vl = x
        print('Step 2 complete')
#3. Определяет закрытый ключ As, как наименьшее значение, удовлетворяющее следующему выражению s**2 % n = vl

i = 0
As = 0
while i == 0:

    for As in range(50):
        As += 1

        if (As**2) % n == vl:
            i = 1
            break

print('Step 3 complete')

#Этап 2
#1. A выбирает случайное число r{1,n-1}, вычисляет Az = (r**2) % n и посылает Bz

r = random.randint(1, n-1)
Az = (r**2) % n
Bz = Az

#2. Б посылает А случайный бит b

b = random.randint(0, 1)

#3 Ессли b=0, то А посылает Б r, иначе y = (r*s) % n

if b == 0:
    Br = r
    print('Br = {}'.format(Br))
else:
    y = (r * As) % n
    print('y = {}'.format(y))

#4 Ессли b=0, то Б проверяет, что Bz = (r**2) % n, иначе Bz = ((y**2) * v) % n

if b == 0:
    if Bz == (r**2) % n:
        print('{} == {}'.format(Bz, (r**2) % n))
        print('True')
    else:
        print('{} != {}'.format(Bz, (r**2) % n))
        print('False')
else:
    Bz = ((y**2) * v) % n
    print('Bz = {}'.format(Bz))