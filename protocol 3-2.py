import random
import time

#Этап 1. Генерация ключей (Выполняет А)
#1. Выбирается два простых числа p и q такие, что (p-1) % q == 0

i = 0
while i == 0:
    p = random.randint(3, 50)
    q = random.randint(3, 50)
    if (p - 1) % q == 0:
        i = 1
        print('Step 1 complete')
    time.sleep(0.5)

#2. Выбирается секретный ключ х(1,q-1)

x = random.randint(1,q-1)

#3. Выбирается g, что (g ** q) % p == 1

i = 0
while i == 0:
    g = random.randint(1, 50)
    if (g ** q) % p == 1:
        i = 1
        print('Step 3 complete')
    time.sleep(0.5)

#4. Выбирается открытый ключ (y) такой, что ((g**y) * y) % p == 1

i = 0
while i == 0:
    y = random.randint(1, 50)
    if ((g**y) * y) % p == 1:
        i = 1
        print('Step 4 complete')
    time.sleep(0.5)
#5 Публикация открытого ключа y
print(y)

#Этап 2. Аутентификация.
#1. A выбирает случайное число k (1,q-1), вычисляет Ar = (g**k) % p и посылает Br

k = random.randint(1, q-1)
Ar = (g**k) % p
Br = Ar

#2. Б выбирает случайное число Be(0,(2**t)-1), где t - некоторый параметр, и посылает Ae

t = 52
Be = random.randint(1, (2**t)-1)
Ae = Be

#3. А вычисляет As = (k + x * Ae) % q и посылает Bs

As = (k + x * Ae) % q
Bs = As

#4. Б проверяет соотношение Br = ((g**Bs) * (y**Be)) % p и, если оно выполняется, принимает доказательство, в противном случае - отвергает
print (Br)
l = (((g**Bs) * (y**Be)) % p)
print (Br)
print (l)
if Br == ((g**Bs) * (y**Be)) % p:
    print('{} == {}'.format(Br, ((g**Bs) * (y**Be)) % p))
    print('True')
else:
    print('{} == {}'.format(Br, ((g**Bs) * (y**Be)) % p))
    print('False')