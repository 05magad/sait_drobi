"""
План работы над сайтом:

Часть 1, алгоритмы.
1. Пишем функцию, которая считает общий знаменатель для 2 дробей;
2. Пишем функцию, которая складывает или вычитает 2 дроби;
3. Пишем функцию, которая умножает 2 дроби;
4. Пишем функцию, которая вычитает 2 дроби.

Часть 2, внешний вид.
Верстаем основную страничку. Там должны быть:
1. 2 поля для ввода чисел;
2. Выбор операции (+, -, *, /)
3. Кнопка "Посчитать".

Часть 3, связка внешнего вида с алгоритмами.
1. Пишем веб-приложение на Python, которое будет принимать числа и операцию и возвращать результат.

Часть 4, деплой (публикация во внешнем мире).
1. Берём в аренду недорогой сервер (170 руб./месяц);
2. Берём в аренду на год недорогое доменное имя типа 05.NLO.ru;
3. Настраиваем сервер (пишем команды для Linux);
4. Публикуем туда наше веб-приложение.
"""


def ob_znam(x, y):
    """Находит общий знаменатель двух дробей: x и y.
    Например:
    # x = (0, 3, 2)
    # y = (5, 4, 4)
    """

    s = x[2] * y[2]
    return s


def sokrati(drob):
    for i in range(min(abs(drob[1]), abs(drob[2])), 1, -1):
        if drob[1] % i == 0 and drob[2] % i == 0:
            return (drob[0], drob[1] // i, drob[2] // i)
    return drob


def celoe(drob):
    # (1, 2, 7) => (1, 2, 7)
    # (1, 7, 2) => (4, 1, 2)
    # (1, 4, 2) => (3, 1, 1)

    # Если числитель уже меньше знаменателя, то просто возвращаем исходную дробь
    if abs(drob[1]) < abs(drob[2]):
        return sokrati(drob)

    is_negative = drob[0] < 0 or drob[1] < 0
    new_drob = (abs(drob[0]) + abs(drob[1]) // drob[2], abs(drob[1]) % abs(drob[2]), drob[2])
    if is_negative:
        if new_drob[0] > 0:
            new_drob = (-new_drob[0], new_drob[1], new_drob[2])
        else:
            new_drob = (0, -new_drob[1], new_drob[2])
    # Если числитель стал равен 0, то дробь превратилась в целое число, поэтому дробную часть делаем 1/1
    if new_drob[1] == 0:
        return (new_drob[0], 1, 1)

    # Если в числителе минус, то нужно проверить, надо ли уменьшать целую часть
    # (1, 5, 9) - (0, 6, 9) => (1, -1, 9) => (0, 8, 9)
    return sokrati(new_drob)



def plus(drob1, drob2):
    """Складывает 2 дроби"""
    # Узнаём общий знаменатель
    znam = ob_znam(drob1, drob2)

    # Приводим обе дроби к этому общему знаменателю
    drob1 = (drob1[0], int(drob1[1] * znam / drob1[2]), znam)
    drob2 = (drob2[0], int(drob2[1] * znam / drob2[2]), znam)

    # Складываем дроби
    vmeste = (drob1[0] + drob2[0], drob1[1] + drob2[1], znam)
    return celoe(vmeste)


def minus(drob1, drob2):
    """Вычитает 2 дроби"""
    znam = ob_znam(drob1, drob2)
    #  1ДРОБЬ
    drob1 = (drob1[0], int(drob1[1] * znam / drob1[2]), znam)
    drob1 = (0 , drob1[0] * drob1[2] + drob1[1], drob1[2])
    # 2 ДРОБЬ
    drob2 = (drob2[0], int(drob2[1] * znam / drob2[2]), znam)
    drob2 = (0, drob2[0] * drob2[2] + drob2[1], drob2[2])

    return celoe((0, drob1[1] - drob2[1], znam))



def umnozh(drob1, drob2):
    """Умножает 2 дроби"""

    drob1 = (0, drob1[0] * drob1[2] + drob1[1], drob1[2])
    drob2 = (0, drob2[0] * drob2[2] + drob2[1], drob2[2])

    umnoth = (0, drob1[1] * drob2[1],drob1[2] * drob2[2])
    return celoe(umnoth)


def deli(drob1, drob2):
    """Делит 2 дроби"""
    drob2 = (0, drob2[0] * drob2[2] + drob2[1], drob2[2])
    drob2 = (drob2[0], drob2[2], drob2[1])
    return umnozh(drob1, drob2)


# drob1 = (1, 2, 9)
# drob2 = (0, 5, 3)
#
# assert sokrati((2, 4, 8)) == (2, 1, 2)
# assert sokrati((2, 3, 9)) == (2, 1, 3)
# assert sokrati((0, 15, 5)) == (0, 3, 1)
# print('Сокращение работает правильно')
#
# assert plus(drob1, drob2) == (2, 8, 9), f'Неправильно работает сложение: выдаёт {plus(drob1, drob2)} вместо {(2, 8, 9)}'
# assert umnozh(drob1, drob2) == (2, 1, 27), f'Неправильно работает умножение: выдаёт {umnozh(drob1, drob2)} вместо {(2, 1, 27)}'
# assert deli(drob1, drob2) == (0, 11, 15), f'Неправильно работает деление: выдаёт {deli(drob1, drob2)} вместо {(0, 11, 15)}'
# print('Всё, кроме отрицания, работает правильно!')
#
# assert minus((1, 4, 5), (1, 3, 5)) == (0, 1, 5), minus((1, 4, 5), (1, 3, 5))
# assert minus((1, 3, 5), (1, 4, 5)) == (0, -1, 5), minus((1, 3, 5), (1, 4, 5))
# assert minus((0, 4, 5), (2, 4, 5)) == (-2, 1, 1), minus((0, 4, 5), (2, 4, 5))
# assert minus((0, 4, 5), (2, 3, 5)) == (-1, 4, 5), minus((0, 4, 5), (2, 3, 5))
# print('Всё огонь')
