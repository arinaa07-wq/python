#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# есть список животных в зоопарке

zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ]

# посадите медведя (bear) между львом и кенгуру
#  и выведите список на консоль
# TODO здесь ваш код
zoo=zoo[:1]+['bear'] +zoo[1:]
print(zoo)

# добавьте птиц из списка birds в последние клетки зоопарка
birds = ['rooster', 'ostrich', 'lark', ]
print(zoo)
#  и выведите список на консоль
# TODO здесь ваш код
zoo=zoo+birds
print(zoo)
# уберите слона
#  и выведите список на консоль
# TODO здесь ваш код
zoo=zoo[:3]+zoo[4:]
print(zoo)
# выведите на консоль в какой клетке сидит лев (lion) и жаворонок (lark).
# Номера при выводе должны быть понятны простому человеку, не программисту.
# TODO здесь ваш код
leonp=zoo[:1]
leonpr=len(leonp)
larkp=len(zoo)
print("лев сидит в клетке номер "+str(leonpr))
print("жаворонок сидит в клетке "+str(larkp))
