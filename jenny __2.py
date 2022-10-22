#                        TASK № 1


import random
a = int(input('Введите номер вашего билета: от 1 до 10: '))
b = random.randint(0,10)
print(b)
if a==b:
    print('Поздравляем, вы выиграли!')
elif a!=b:
    print('Такого номера билета не существует')
else:
    print('Главное не победа, а участие :) ')




#                          TASK № 2



# a = int(input('Введите день вашего рождения: '))
# b = int(input('Введите номер месяца вашего рождения: '))
#
# if 21 <= a <= 31 and b == 3 or 1 <= a <= 20 and b == 4:
#     print('вы - овен')
# elif 21 <= a <= 30 and b == 4 or 1 <= a <= 21 and b == 5:
#     print('вы - телец')
# elif 22 <= a <= 31 and b == 5 or 1<= a <= 21 and b == 6:
#     print('вы - близнецы')
# elif 22 <= a <= 30 and b == 6 or 1 <= a <= 22 and b ==7:
#     print('вы - рак')
# elif 23 <= a <= 31 and b == 7 or 1 <= a <= 23 and b == 8:
#     print('вы - лев')
# elif 24 <= a <= 31 and b == 8 or 1 <= a <= 22 and b == 9:
#     print('вы - дева')
# elif 23 <= a <= 30 and b ==9 or 1 <= a <= 23 and b == 10:
#     print('вы - весы')
# elif 24 <= a <= 31 and b == 10 or 1 <= a <= 22 and b == 11:
#     print('вы - скорпион')
# elif 23 <= a <= 30 and b == 11 or 1 <= a <= 21 and b == 12:
#     print('вы - стрелец, самый лучший знак:)')
# elif 22 <= a <= 31 and b == 12 or 1 <= a <= 20 and b == 1:
#     print('вы - козерог')
# elif 21 <= a <= 31 and b == 1 or 1 <= a <= 18 and b == 2:
#     print('вы - водолей')
# elif 19 <= a <= 29 and b == 2 or 1 <= a <= 20 and b == 3:
#     print("вы - рыбы")
# else:
#     print('такой даты не существует')



#                          TASK № 3


# Пользователь вводит свой возраст ( до 50),
# просклонять слово "год/ года / лет"


#                       SOLUTION



# a = int(input('Введите свой возраст'))
#
# if a==1 or a==21 or a==31 or a==41:
#     print('Вам', int(a), 'год')
# elif 2<=a<=4 or 22<=a<=24 or 32<=a<=34 or 42<=a<=44:
#     print('Вам', int(a), 'года')
# elif 5<=a<=20 or 25<=a<=30 or 35<=a<=40 or 45<=a<=50:
#     print('Вам', int(a), 'лет')
#
# else:
#     print('Вау, вы перешагнули полувековой рубеж')


